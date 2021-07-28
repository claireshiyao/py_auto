# author by claire
from selenium.webdriver.common.by import By


class HomePageLocs:
    # 退出链接
    exit_link = (By.XPATH, '//a[text()="退出"]')
    # 抢投标按钮
    bid_button = (By.XPATH, '//a[@class="btn btn-special"]')
    # 我的帐户链接
    user_link = (By.XPATH, '//a[@href="/Member/index.html"]')

