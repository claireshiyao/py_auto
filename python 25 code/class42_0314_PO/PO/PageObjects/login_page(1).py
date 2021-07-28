# author by claire
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button = (By.TAG_NAME, 'button')
    # 请输入手机号
    phone_hint = (By.XPATH, '// div[text() = "请输入手机号"]')


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, username, passwd):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.login_button))
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.passwd_input).send_keys(passwd)
        self.driver.find_element(*self.login_button).click()

    def get_error_msg(self):
        self.driver.find_element(*self.phone_hint)

