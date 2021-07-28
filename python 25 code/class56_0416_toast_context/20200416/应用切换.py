from appium import webdriver

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
desired_caps = {
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "platformVersion":'7.1.2',
    "deviceName":"emulator-5554",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True
}

# 3、连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


loc = (MobileBy.ID,"com.lemon.lemonban:id/navigation_my")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

driver.start_activity("com.baidu.BaiduMap","com.baidu.baidumaps.WelcomeScreen")