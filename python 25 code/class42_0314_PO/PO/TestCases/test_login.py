import unittest
from selenium import webdriver

from PO.PageObjects.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 访问登陆页面
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")

    def tearDown(self) -> None:
        self.driver.quit()


    def test_login_success(self):
        # 步骤 # 1、登陆页面 - 登陆操作
        LoginPage(self.driver).login("18684720553","python")
        # 断言  # 2、首页 - 获取元素是否存在
        pass


    def test_login_failed_no_userName(self):
        # 步骤
        # 1、登陆页面 - 登陆操作
        # 断言
        # 2、登陆页面  - 获取错误的提示信息
        pass