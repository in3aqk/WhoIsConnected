# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo","Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"

from libs.utility import readIni
import libs.grabber
from bs4 import BeautifulSoup
import requests
import logging


class Grabber:

    conf = None  # conf obj
    infoPageUrl = None


    def __init__(self):
        self.conf = readIni()
                
        logging.info("Test")

        if self.conf:
            self.infoPageUrl = "{}{}".format(
                self.conf.get('remoterig','remoterigUrl'),
                self.conf.get('remoterig','infoPage')
                )            


    def getInfoPage(self):
        """Get the Remote rig info page

            returns: the page in success or false on failure
        """

        page = self.__getPage(self.infoPageUrl)
        return page    


    def __getPage(self, url):
        """Get a page content

           param: url: the page url\n
           returns: the page in success or false on failure 
        """
        response =  False
        try:
            response = requests.get(url)
            if response.status_code == 200:        
                return response.content
            else:
                print("Page not available: {}".format(url))
                return False
        except requests.exceptions.Timeout:
            print ("Timeout")            
        except requests.exceptions.TooManyRedirects:
            print ("Too many redirects")            
        except requests.exceptions.RequestException as e:
            print(e)            
            raise SystemExit(e)                  
        finally:
            logging.info("Retrieved URL: {}".format(url))
            return response        
        



