# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo", "Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"

import logging
import os
import re

import requests
from libs.grabber import Grabber
from libs.database import Database
from libs.utility import readIni


class Pages():

    html_path = None
    conf = None  # conf obj
    grabber = None
    db = None

    def __init__(self):
        self.conf = readIni()
        self.grabber = Grabber()
        self.db = Database()
        self.html_path = os.path.dirname(
            os.path.realpath(__file__)) + "/../html/"

    def dashboard(self):
        other_heads_table = None
        
        error_head = {
            "head_mac": "ERROR",
            "head_ip": "ERROR",
            "head_name": "ERROR",
            "other_heads_table":other_heads_table
        }

        page = self.grabber.getInfoPage()
        head_info = None

        
        if page:
            head_info = self.grabber.getHeadInfo()
            self.grabber.update_heads(
                head_info["otherPartyMac"], head_info["otherParty"])
            head_on_db = self.grabber.get_head_from_db(
                head_info["otherPartyMac"])
            if head_on_db:
                other_heads_table = self.grabber.gen_head_table(head_on_db[2])
                head = {
                    "head_mac": head_on_db[1],
                    "head_ip": head_on_db[2],
                    "head_name": head_on_db[3],
                    "other_heads_table":other_heads_table
                }
            else:
                head = error_head
        else:
            head = error_head

        return self.get_page("dashboard", head)

    def get_page(self, page, vars):
        main = self.__merge_page("main.html", page, vars)
        return main


    def delete_head(self,id):
        return self.db.deleteHeadById(id)

    def update_head(self,id,new_name):
        return self.db.updateHeadById(id,new_name)
    
    def __merge_page(self, main_page, page_name, vars):

        page = self.__get_page(main_page)
        new_page = None
        for line in page.splitlines():
            if "{{" in line:
                m = re.search('{{(.+?)}}', line)
                if m:
                    found = m.group(1)
                    if found == "content":
                        insert_page = self.__get_page(page_name+".html")
                        new_page = page.replace("{{content}}", insert_page)
                    elif found == "customjs":
                        new_page = page.replace(
                            "{{customjs}}", "js/"+page_name+".js")
                    else:
                        to_be_replaced = "{{" + found + "}}"
                        insert_page = self.__get_page(found)
                        new_page = page.replace(to_be_replaced, insert_page)

                    page = new_page

        if vars:
            for line in page.splitlines():
                if "{{" in line:
                    for var in vars:
                        new_page = page.replace("{{"+var+"}}", vars[var])
                        page = new_page

        del new_page
        return page

    def __get_page(self, page_name):
        page = None
        with open('{}{}'.format(self.html_path, page_name)) as f:
            page = f.read()
        return page
