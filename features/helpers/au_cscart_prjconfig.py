import configparser
import os
from .au_cscart_browsers import Browsers
import platform
import sys

#au_cscart_prjRoot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#au_cscart_prjRoot = os.path.dirname(os.path.dirname(__file__))
au_cscart_prjRoot =os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#print au_cscart_prjRoot

def is_64bit():
    return sys.maxsize > 2**32

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

#def get_chromedriver():
    #return "chromedriver.exe"

def read_ie_location():
    return os.path.join(au_cscart_prjRoot,"tools",get_iedriver())

def get_iedriver():
    return "IEDriverServer"

def get_url():
    return (get_setting("tests","url"))

#print("Test URL =" + " "+ get_setting("tests", "url"))

def is_windows():
    return platform.system().lower() == "windows"
    
def is_linux():
    return platform.system().lower() == "linux"
    
def get_chromedriver():
    return "chromedriver.exe" if is_windows() else "chromedriver_l64" if is_64bit() else "chromedriver_l32"

