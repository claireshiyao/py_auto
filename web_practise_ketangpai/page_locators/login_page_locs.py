# author by claire
from selenium.webdriver.common.by import By


class LoginPageLocs:
    # 用户名输入框
    account_input = (By.NAME, 'account')
    # 密码输入框
    passwd_input = (By.NAME, 'pass')
    # 登录按钮
    login_button = (By.XPATH, '//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')