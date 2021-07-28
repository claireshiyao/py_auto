from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BidPage:

    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 11、标页面 - 获取用户余额
    def get_user_money(self):
        pass

    # 111、标页面 - 获取标的余额
    def get_bid_money(self):
        pass

    # 2、标页面 - 输入金额2000，点投标
    def invest(self,money):
        pass

    # 3、标页面 - 在投标成功的弹出框里，点击查看并激活按钮
    def click_active_button_in_success_popup(self):
        pass