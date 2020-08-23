# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo","Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"

from lib.utility import readIni
from BeautifulSoup import BeautifulSoup
import requests


class Grabber:

    conf = None  # conf obj
    infoPageUrl = None

    def __init__(self):
        self.conf = readIni()

        if self.conf:
            self.infoPageUrl = "{}{}".format(
                self.conf.get('remoterig','remoterigUrl'),
                self.conf.get('remoterig','infoPage')
                )            
            

    def getInfoPage(self):
        page = self.getPage(self.infoPageUrl)
        return page    


    def getPage(self, url):        
        response = requests.get(url)
        if response.status_code == 200:        
            return response.content
        else:
            print("Page not available: {}".format(url))
            return False



