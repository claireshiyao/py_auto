# author by claire
from selenium.webdriver.remote.webdriver import WebDriver

from common.basepage import BasePage
from page_locators.login_page_locs import LoginPageLocs as locs

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, passwd):
        self.input_text(locs.account_input, username, "登录页面-输入用户名")
        self.input_text(locs.passwd_input, passwd, "登录页面-输入密码")
        self.click_element(locs.login_button, "登录页面-点击登录按钮")




