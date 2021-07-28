# author by claire
from selenium.webdriver.common.by import By


class UserPageLocs:
    # 用户可用余额
    user_left_money = (By.XPATH, '//li[@class="color_sub"]')