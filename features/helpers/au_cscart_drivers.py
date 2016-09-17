from au_cscart_browsers import Browsers
from helpers import au_cscart_prjconfig
import os
from selenium import webdriver

def get_chrome():
    chromedriver = au_cscart_prjconfig.read_chromedriver_location()
    os.environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(chromedriver)

def get_ie():
    iedriver = au_cscart_prjconfig.read_ie_location()
    os.environ["webdriver.ie.driver"] = iedriver
    return webdriver.Ie(iedriver)

def switch_browser(browser):
    return {Browsers.chrome: get_chrome, Browsers.internetexplorer: get_ie}.get(browser, lambda: webdriver.Firefox())()
