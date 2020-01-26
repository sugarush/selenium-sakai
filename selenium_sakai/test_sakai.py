import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumSakai(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get('https://qa1-us.nightly.sakaiproject.org/portal')

        username = self.driver.find_element_by_id('eid')
        password = self.driver.find_element_by_id('pw')
        submit = self.driver.find_element_by_id('submit')

        username.send_keys('admin')
        password.send_keys('admin')
        submit.click()

        self.assertIn('Overview', self.driver.page_source)
