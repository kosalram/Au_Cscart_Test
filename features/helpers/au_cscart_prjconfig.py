import configparser
import os
from .au_cscart_browsers import Browsers

#au_cscart_prjRoot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
au_cscart_prjRoot = os.path.dirname(os.path.dirname(__file__))
#print au_cscart_prjRoot

def getConfig():
    confFilePath = os.path.join(au_cscart_prjRoot,"features","au_cscart_config.ini")
    configParse = configparser.RawConfigParser()
    configParse.read(confFilePath)
    return configParse

config = getConfig()

def get_setting(partent,key):
    return config.get(partent,key)

def get_browser():
    return Browsers.get_browser(get_setting("selenium","driver"))
   

#print("Driver Assigned =" + " "+ get_setting("selenium", "driver"))

def read_chromedriver_location():
    return os.path.join(au_cscart_prjRoot,"tools",get_chromedriver())

def get_chromedriver():
    return "chromedriver"

def read_ie_location():
    return os.path.join(au_cscart_prjRoot,"tools",get_iedriver())

def get_iedriver():
    return "IEDriverServer"

def get_url():
    return (get_setting("tests","url"))

#print("Test URL =" + " "+ get_setting("tests", "url"))

