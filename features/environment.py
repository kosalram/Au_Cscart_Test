# from selenium import webdriver
#
# def before_all(context):
#     context.browser = webdriver.Chrome()
#
#
# def after_all(context):
#     context.browser.quit()

from helpers import au_cscart_prjconfig
from helpers import au_cscart_drivers

def before_all(context):
    browsertype = au_cscart_prjconfig.get_browser()
    context.browser= au_cscart_drivers.switch_browser(browsertype)

def after_all(context):
    context.browser.quit()

