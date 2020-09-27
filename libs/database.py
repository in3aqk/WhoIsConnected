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
import sqlite3
from sqlite3 import Error

class Database:

    conf = None  # conf obj
    dbName = None
    dbFolder = None
    

    def __init__(self):
        self.conf = readIni()

        if self.conf:
            self.dbName = self.conf.get('database','dbName')
            self.dbFolder = self.conf.get('database','dbFolder')

    def connect(self):
        conn = False
        try:
            a = '../{}/{}'.format(self.dbFolder,self.dbName)
            conn = sqlite3.connect('./{}/{}'.format(self.dbFolder,self.dbName))
        except sqlite3.OperationalError as e:
            logging.error(e)
            raise
        else:
            logging.info("Db Connection with %s ok",self.dbName)
        finally:
            return conn


    def insertHead(self, ip, mac, name="unknown"):
        """ Save a new remote rig head\n
            param:ip  : Head Ip \n
            param:mac : Head Mac address\n
            param:name: Head name\n
        """
        result = False
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("insert into heads (mac, ip, name) values (?, ?, ?)", (mac, ip, name))
            con.commit()
        except Error as err:
            logging.error(err)
        else:
            logging.info("Inserted new head %s %s",ip,mac)
            result = True
        finally:
            cur.close()
            con.close()
            return result


    def getHead(self, mac):
        """ Get from db head by his mac\n
            param:mac : Head Mac address            
        """
        result = False
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("select * from heads where mac = ?", (mac,))
            row = cur.fetchone()
        except Error as err:
            logging.error(err)
        else:            
            result = row
        finally:
            cur.close()
            con.close()
            return result

    def get_all_heads(self):
        """ Get from db all heads\n            
        """
        result = False
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("select * from heads order by name asc")
            rows = cur.fetchall()
        except Error as err:
            logging.error(err)
        else:            
            result = rows
        finally:
            cur.close()
            con.close()
            return result



    def updateHeadByMac(self, ip, mac, name="unknown"):
        """ Save a new remote rig head\n
            param:ip  : Head Ip \n
            param:mac : Head Mac address\n
            param:name: Head name\n
        """
        result = False
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("update heads set ip=?, name=? where mac = ?", (ip, name, mac))
            con.commit()
        except Error as err:
            logging.error(err)
        else:
            logging.info("Updated head %s",mac)
            result = True
        finally:
            cur.close()
            con.close()
            return result

    def deleteHeadByMac(self, mac):
        """ Delete a remoterig head searching by mac\n
            
            param:mac : Head Mac address\n
        """
        result = False
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("delete from heads where mac=?", (mac,))
            con.commit()
        except Error as err:
            logging.error(err)
        else:
            logging.info("Deleted head %s",mac)
            result = True
        finally:
            cur.close()
            con.close()
            return result

    def deleteHeadById(self, id):
        """ Delete a remoterig head searching by id\n
            
            param:mac : Head id\n
        """
        result = False
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("delete from heads where id=?", (id,))
            con.commit()
        except Error as err:
            logging.error(err)
        else:
            logging.info("Deleted head %s",id)
            result = True
        finally:
            cur.close()
            con.close()
            return result


