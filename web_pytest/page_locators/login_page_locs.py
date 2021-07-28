# author by claire
from selenium.webdriver.common.by import By


class LoginPageLocs:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button = (By.TAG_NAME, 'button')
    # 登录页面提示框
    login_hint = (By.XPATH, '//div[@class= "form-error-info"]')
    # 账号或密码错误提示弹出框
    wrong_account_alert = (By.XPATH, '//div[@class ="layui-layer-content"]')
