# author by clairet

import unittest

from selenium import webdriver
from PO.PageObjects.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        LoginPage(self.driver).login('13760246701', 'python')
