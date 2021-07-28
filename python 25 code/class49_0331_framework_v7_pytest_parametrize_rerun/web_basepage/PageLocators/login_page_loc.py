#!/usr/bin/python3
"""
@File    : login_page_loc.py
@Time    : 2019/12/2 22:00
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium.webdriver.common.by import By

class LoginPageLoc:

    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (By.TAG_NAME, "button")
    # 错误提示框
    form_error_loc = (By.XPATH, '//div[@class="form-error-info"]')
    # 页面中dialog的提示
    dialog_error_loc = (By.XPATH, '//div[@class="layui-layer-content"]')