# ----------------------------------------------------------------------------
# File: AddProduct.feature
# Autor: Kosalram
# Date: 16-9-2016
# ----------------------------------------------------------------------------

from behave import given, when, then
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Login with valid credientials')
def step_impl(context):
    # context.browser.get('http://demo.cs-cart.com/admin.php?dispatch=auth.login_form&return_url=admin.php')
    # assert_that(context.browser.title, 'Administration panel')
     context.browser.maximize_window()
    # u_name = context.browser.find_element_by_id('username')
    # u_name.clear()
    # u_name.send_keys('admin@example.com')
    # u_psw = context.browser.find_element_by_id('password')
    # u_psw.clear()
    # u_psw.send_keys('admin')
    # submit_btn = context.browser.find_element_by_xpath('/html/body/div[5]/div/form/div[3]/input')
    # submit_btn.click()
    # assert_text = context.browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[1]/h2').text
    # assert_that(assert_text, equal_to('Dashboard'))
    #pass

@when('Adding valid product')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)

    product = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]/div/div[2]/ul/li[3]/a')))
    ActionChains(context.browser).move_to_element(product).perform()

    prod = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]/div/div[2]/ul/li[3]/ul/li[2]/a/span[1]')))
    ActionChains(context.browser).move_to_element(prod).click().perform()

    add_prod = wait.until((EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div[1]/div[3]/div[1]/div/a/i'))))
    ActionChains(context.browser).move_to_element(add_prod).click().perform()

    prod_name = context.browser.find_element_by_id('product_description_product')
    prod_name.send_keys('LEXINGTON CARDIGAN SWEATER')

    add_cat = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div[2]/div/a')))
    ActionChains(context.browser).move_to_element(add_cat).click().perform()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[13]/div[1]/span')))
    add_cat_win_txt = context.browser.find_element_by_xpath('/html/body/div[13]/div[1]/span').text
    #print add_cat_win_txt
    add_cat_win_dsk = context.browser.find_element_by_id('input_cat_168')
    add_cat_win_dsk.click()
    add_cat_win_add = context.browser.find_element_by_xpath('/html/body/div[13]/div[2]/div/form/div[2]/input[1]')
    add_cat_win_add.click()

    wait.until(EC.visibility_of_element_located((By.ID, 'elm_price_price')))
    prod_pri = context.browser.find_element_by_id('elm_price_price')
    prod_pri.send_keys('80.00')

    prod_create_btn = context.browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[3]/a[2]')
    prod_create_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]')))
    #context.browser.get_screenshot_as_file("asdf.png")

@then('Sucessfully added into the system')
def step_impl(context):
    #pass
    wait = WebDriverWait(context.browser, 10)
    src_prod = context.browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[3]/div/div/form/div[1]/div/div[1]/input')
    src_prod.send_keys('LEXINGTON')
    src_prod_btn = context.browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[3]/div/div/form/div[2]/input')
    src_prod_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[3]/a')))
    res_src_prod = context.browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div[2]/form/div/table/tbody/tr/td[3]/a').get_attribute('innerHTML')
    #print res_src_prod
    assert_that(res_src_prod, 'LEXINGTON CARDIGAN SWEATER')
    context.browser.get_screenshot_as_file("Screenshots/%s.png" % "prodct_added_result")
