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
from libs.utility import readIni


class Pages():

    html_path = None
    conf = None  # conf obj
    grabber = None

    def __init__(self):
        self.conf = readIni()
        self.grabber = Grabber()
        self.html_path = os.path.dirname(
            os.path.realpath(__file__)) + "/../html/"

 

    def dashboard(self):

        page = self.grabber.getInfoPage()
        head_info = None
        if page:
            head_info = self.grabber.getHeadInfo()
        head = {
            "head_mac":head_info["otherPartyMac"],
            "head_ip":head_info["otherParty"]
        }
        return self.get_page("dashboard",head)

    def get_page(self, page, vars):
        main = self.__merge_page("main.html", page, vars)
        return main

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


grabber = None


def init():
    grabber = Grabber()
    
