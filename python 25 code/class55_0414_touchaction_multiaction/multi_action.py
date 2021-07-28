# -*- coding:utf8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    "platformName": "Android",
    "platformVersion": '7.1.2',
    "deviceName": "emulator-5554",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "noReset": True
}

# 连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

loc = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()  # 点击题库

size = driver.get_window_size()

# 多点触控，放大屏幕
a = TouchAction(driver)
a.press(x=size["width"]*0.5, y=size["height"]*0.5).wait(200)\
    .move_to(x=size["width"]*0.2, y=size["height"]*0.8)\
    .release()
b = TouchAction(driver)
b.press(x=size["width"]*0.5, y=size["height"]*0.5).wait(200)\
    .move_to(x=size["width"]*0.8, y=size["height"]*0.2)\
    .release()

ma = MultiAction(driver)
ma.add(a, b)
ma.perform()
