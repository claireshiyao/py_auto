# author by claire
import os
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
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

old = None
new = driver.page_source

while old != new:
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("安全测试")')
    except:
        driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.3, 300)
        time.sleep(5)
        old = new
        new = driver.page_source
    else:
        print("找到安全测试")
        driver.find_element_by_android_uiautomator('new UiSelector().text("安全测试")').click()
        break




