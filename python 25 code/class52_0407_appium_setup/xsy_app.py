# author by claire

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": '7.1.2',
    "deviceName": "emulator-5554",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# app  -工具定位
