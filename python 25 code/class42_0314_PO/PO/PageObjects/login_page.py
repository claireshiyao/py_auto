# from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # 用户名输入框
    user_input = (By.XPATH,'//input[@name="phone"]')
    # 密码输入框
    passwd_input = (By.XPATH,'//input[@name="password"]')
    # 登陆按钮
    login_button = (By.TAG_NAME,'button')


    def __init__(self,driver:WebDriver):
        # 初始化driver
        self.driver = driver
        # self.driver = webdriver.Chrome() # 打开了一个浏览器，开始了一个新会话

    # 登陆  - 元素操作 - 不知道用例在什么情况下会调用我？？
    def login(self,username,passwd):
        # 等待？？
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.login_button))
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.passwd_input).send_keys(passwd)
        self.driver.find_element(*self.login_button).click()


    # 获取登陆区域的提示信息
    def get_error_msg(self):
        pass