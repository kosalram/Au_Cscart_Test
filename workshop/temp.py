
# ----------------------------------------------------------------------------
# File: temp.py
# Autor: Kosalram
# Date: 8-9-2016
# ----------------------------------------------------------------------------

import unittest
from selenium import webdriver
from hamcrest import assert_that, equal_to

class BenchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_Sucessfully_logged_in_and_displaying_the_dashboard_page(self):

        self.browser.get('http://demo.cs-cart.com/admin.php?dispatch=auth.login_form&return_url=admin.php')
        self.assertEqual(self.browser.title, 'Administration panel')
        u_name = self.browser.find_element_by_id('username')
        u_name.clear()
        u_name.send_keys('admin@example.com')
        u_psw = self.browser.find_element_by_id('password')
        u_psw.clear()
        u_psw.send_keys('admin')
        submit_btn = self.browser.find_element_by_xpath('//*[@id="main_column_login"]/div/form/div[3]/input')
        submit_btn.click()
        assert_text = self.browser.find_element_by_xpath('//*[@id="actions_panel"]/div[1]/h2').text
        assert_that(assert_text, equal_to('Dashboard'))


    @ classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == "__main__":
   unittest.main()