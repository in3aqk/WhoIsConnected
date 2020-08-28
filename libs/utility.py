# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo"
__credits__ = ["Paolo Mattiolo","Edmondo Conetta"]
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "mattiolo@gmail.com"
__status__ = "Development"



import os
import configparser



def readIni():
    """ Read the ini file and return a config object

        return: config obj or False on failure
    """
    
    
    cfgPath = os.path.join('./','config','config.ini')

    if os.path.isfile(cfgPath): 
        config = configparser.ConfigParser()
        config.read(cfgPath)           
        return config
        
    else:
        print ("No config file")
        return False