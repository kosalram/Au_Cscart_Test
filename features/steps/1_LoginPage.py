# ----------------------------------------------------------------------------
# File: LoginPage.py
# Autor: Kosalram
# Date: 8-9-2016
# ----------------------------------------------------------------------------

from behave import given, when, then
from hamcrest import assert_that, equal_to
from helpers import au_cscart_prjconfig


@given ('Open the url')
def step_impl(context):
    url=au_cscart_prjconfig.get_url()
    context.browser.get(url)
    title = context.browser.title
    assert_that(title, equal_to('Administration panel'))

@when ('Valid username and password entered')
def step_impl(context):
    u_name=context.browser.find_element_by_id('username')
    u_name.clear()
    u_name.send_keys('admin@example.com')
    u_psw=context.browser.find_element_by_id('password')
    u_psw.clear()
    u_psw.send_keys('admin')
    submit_btn = context.browser.find_element_by_xpath('//*[@id="main_column_login"]/div/form/div[3]/input')
    submit_btn.click()

@then('Sucessfully logged in and displaying the dashboard page')
def setp_impl(context):
    assert_text = context.browser.find_element_by_xpath('//*[@id="actions_panel"]/div[1]/h2').text
    assert_that(assert_text,equal_to('Dashboard'))

