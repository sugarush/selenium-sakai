import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

class SeleniumSakai(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        self.driver.get('https://qa1-us.nightly.sakaiproject.org/portal')

        username = self.driver.find_element_by_id('eid')
        password = self.driver.find_element_by_id('pw')
        submit = self.driver.find_element_by_id('submit')

        username.send_keys('admin')
        password.send_keys('admin')
        submit.click()

        self.assertIn('Overview', self.driver.page_source)
