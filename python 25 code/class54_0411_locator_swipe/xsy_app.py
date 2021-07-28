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

# android_uiautomator -  利用自动化框架提供的定位方法
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Python自动化")')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()   # 点击python自动化

# driver.tap([(38, 89)])

# 返回
os.system("adb shell input tap 38 89")

time.sleep(3)
# 等待所有题库都出来了，再滑动

# 滑屏
size = driver.get_window_size()
driver.swipe(size["width"]*0.5, size["height"]*0.8, size["width"]*0.5, size["height"]*0.2, 300)


