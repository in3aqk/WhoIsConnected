# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo", "Edmondo Conetta"]
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
    example_path = None
    is_local = None

    def __init__(self):
        self.conf = readIni()

        if self.conf:
            self.infoPageUrl = "{}{}".format(
                self.conf.get('remoterig', 'remoterigUrl'),
                self.conf.get('remoterig', 'infoPage')
            )
            self.is_local = self.conf.getboolean('general', 'is_local')
            self.example_path = "./{}/status.htm".format(
                self.conf.get('general', 'local_path'))

    def getInfoPage(self):
        """Get the Remote rig info page

            returns: the page in success or false on failure
        """
        if not self.is_local:
            page = self.__get_page(self.infoPageUrl)
        else:
            page = self.__get_static_page()
        return page

    def getHeadInfo(self):
        """Get remote rig head info grabbing the info page

           returns tuple with usel info
        """
        infos = {}
        otherParty = None
        otherPartyMac = None
        page = self.getInfoPage()
        if not self.is_local:
            soup = BeautifulSoup(page.content, 'html.parser')
        else:
            soup = BeautifulSoup("".join(page), 'html.parser')

        infos['otherPartyMac'] = ''

        ipFound = False
        macFound = False
        for tr in soup.find_all('tr'):
            if b"Other party" in tr.renderContents() and not ipFound:
                tds = tr.find_all('td')
                ipFound = True
                if len(tds) == 2:
                    otherParty = tds[1].renderContents()
                    infos['otherParty'] = otherParty.decode()
                    # TODO LOG Entry Duplicate
                    logging.info("Head ip %s", otherParty.decode())
                else:
                    otherParty = None
            if b"Other party(mac)" in tr.renderContents() and not macFound:
                tds = tr.find_all('td')
                if len(tds) == 2:
                    macFound = True
                    otherPartyMac = tds[1].renderContents()
                    infos['otherPartyMac'] = otherPartyMac.decode()
                    logging.info("Head %s", otherPartyMac)
                else:
                    otherPartyMac = None
                    infos['otherPartyMac'] = ''

        if otherPartyMac == None:
            logging.info("Head not found")

        return infos

    def __get_page(self, url):
        """Get a page content

           param: url: the page url\n
           returns: the page in success or false on failure 
        """
        response = False
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
            else:
                print("Page not available: {}".format(url))
                return False
        except requests.exceptions.Timeout:
            print("Timeout")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects")
        except requests.exceptions.RequestException as e:
            print(e)
            raise SystemExit(e)
        finally:
            logging.info("Retrieved URL: {}".format(url))
            return response

    def __get_static_page(self):
        """ Get the page from the filesystem for debugging pourpouses
        """
        with open(self.example_path) as f:
            content = f.readlines()
            return content
