#!/usr/bin/python3
"""
@File    : login_page.py
@Time    : 2019/11/29 21:38
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_basepage.PageLocators.login_page_loc import LoginPageLoc as loc
from web_basepage.Common.basepage import BasePage


class LoginPage(BasePage):
    # 元素操作 # 登陆操作
    def login(self,username,passwd):
        self.input_text(loc.user_loc,username,"登陆页面_用户名输入")
        self.input_text(loc.passwd_loc,passwd,"登陆页面_密码输入")
        self.click_element(loc.login_button_loc,"登陆页面_点击登陆按钮")

    # 获取提示信息
    def get_error_msg(self):
        return self.get_element_text(loc.form_error_loc,"登陆页面_表单区域错误提示")

    # 获取页面中的错误提示信息
    def get_error_msg_from_dialog(self):
        return self.get_element_text(loc.dialog_error_loc,"登陆页面_页面中间toast错误提示")
