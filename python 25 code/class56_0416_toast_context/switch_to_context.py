#  -*-coding:utf8 -*-
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
    "chromedriverExecutable": "D:\\soft\\chromedriver.exe",
    "noReset": True
}

# 连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

loc = (MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"全程班\")")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (MobileBy.CLASS_NAME,"android.webkit.WebView")
time.sleep(2)

cons = driver.contexts
driver.switch_to.context(cons[-1])

loc = (MobileBy.XPATH,"//span[text()=\"加群\"]")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
