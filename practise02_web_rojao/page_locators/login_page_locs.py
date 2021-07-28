# author by claire
from selenium.webdriver.common.by import By


class LoginPageLocs:
    # 用户名输入框
    account_input = (By.ID, "username")
    # 密码输入框
    passwd_input = (By.ID, 'password')
    # 登录按钮
    login_button = (By.ID, 'to-recover')