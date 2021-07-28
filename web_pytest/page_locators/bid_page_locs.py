# author by claire
from selenium.webdriver.common.by import By


class BidPageLocs:

    # 投标金额输入框
    money_input = (By.XPATH, '//input[@class="form-control invest-unit-investinput"]')
    # 标的可投余额
    bid_left_money = (By.XPATH, '//div[contains(@class,"money_overplus")]//span[text()="剩余："]/following-sibling::span')
    # 投标按钮
    invest_button = (By.XPATH, '//button[text()="投标"]')
    # 投资成功-激活按钮
    active_button = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败错误弹出框-页面中间
    bid_failed_popup = (By.XPATH, '//div[@class="text-center"]')
    # 投资失败-确定按钮-关闭弹框
    bid_failed_close_popup = (By.XPATH, '//a[@class="layui-layer-btn0"]')

