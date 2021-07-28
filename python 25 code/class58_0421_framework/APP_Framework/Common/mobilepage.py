"""
======================
Author: 柠檬班-小简
Time: 2020/4/18 11:31
Project: py25-app
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver import Remote

import logging
import time
import datetime


class MobilePage:

    def __init__(self,driver:Remote):
        self.driver = driver

    # 获取设备大小
    def get_device_size(self):
        size = self.driver.get_window_size()
        return size

    # 滑屏操作 - 上下左右
    def swipe_by_direction(self, direction):
        """
        :param direction: up,down,left,right  向哪个方向滑动
        :return: None
        """
        size = self.get_device_size()
        if direction == "up":
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.3, 200)
        # elif

    # 列表滑动 - 找文本/找元素/向上/向下
    # toast获取
    # 混合应用 - 获取所有的，然后切换一下。webview的名称
    # 微信小程序