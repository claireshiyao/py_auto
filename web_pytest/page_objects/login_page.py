# author by claire
from selenium.webdriver.remote.webdriver import WebDriver

from common.basepage import BasePage
from page_locators.login_page_locs import LoginPageLocs as locs


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, passwd):
        self.input_text(locs.user_input, username, "登录页面-输入用户名")
        self.input_text(locs.passwd_input, passwd,  "登录页面-输入密码")
        self.click_element(locs.login_button, "登录页面-点击登录按钮")


    def get_error_msg(self):
        self.wait_element_visible(locs.login_hint, "登录页面-等待登录表单的错误提示元素")
        eles = self.get_elements(locs.login_hint, "登录页面-获取登录表单的错误提示元素")
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            eles_list = []
            for i in eles:
                eles_list.append(i.text)
            return eles_list

    def get_error_hint(self):
        self.wait_element_visible(locs.wrong_account_alert, "登录页面-等待登录表单的错误弹框文本")
        eles = self.get_elements(locs.wrong_account_alert, "登录页面-获取登录表单的错误弹框文本")
        print(eles)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            eles_list = []
            for i in eles:
                eles_list.append(i.text)
            return eles_list




