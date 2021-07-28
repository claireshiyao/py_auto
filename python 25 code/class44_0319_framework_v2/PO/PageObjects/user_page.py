from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BidPage:

    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 11、获取用户余额
    def get_user_money(self):
        pass

