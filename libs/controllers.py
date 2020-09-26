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
from twisted.python.filepath import FilePath
from twisted.web.template import Element, XMLFile, XMLString, renderer, tags

import libs.grabber
from libs.utility import readIni


class Pages():

    html_path = None
    conf = None  # conf obj

    def __init__(self):
        self.conf = readIni()
        self.html_path = os.path.dirname(
            os.path.realpath(__file__)) + "/../html/"

    def get_page(self, page):
        main = self.__merge_page("main.html", page)
        return main

    def __merge_page(self, main_page, page_name):

        page = self.__get_page(main_page)
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
        return page

    def __get_page(self, page_name):
        page = None
        with open('{}{}'.format(self.html_path, page_name)) as f:
            page = f.read()
        return page


class HomeController(Element):
    title = "Dashboard"
    loader = XMLFile(FilePath('./html/main.xml'))
    dashboard_xml = XMLFile(FilePath('./html/dashboard.xml'))
    menu_content_xml = XMLFile(FilePath('./html/menu.xml'))
    foot_xml = XMLFile(FilePath('./html/footer.xml'))

    @renderer
    def menu(self, request, tag):
        return self. menu_content_xml.load()

    @renderer
    def dashboard(self, request, tag):
        return self.dashboard_xml.load()

    @renderer
    def footer(self, request, tag):
        return self.foot_xml.load()


class AboutController(Element):
    title = "About"
    loader = XMLFile(FilePath('./html/main.xml'))
    dashboard_xml = XMLFile(FilePath('./html/about.xml'))
    menu_content_xml = XMLFile(FilePath('./html/menu.xml'))
    foot_xml = XMLFile(FilePath('./html/footer.xml'))

    @renderer
    def menu(self, request, tag):
        return self. menu_content_xml.load()

    @renderer
    def dashboard(self, request, tag):
        return self.dashboard_xml.load()

    @renderer
    def footer(self, request, tag):
        return self.foot_xml.load()
