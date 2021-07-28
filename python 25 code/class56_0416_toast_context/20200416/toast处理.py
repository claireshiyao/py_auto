"""
toast:
UiAutomator2

xpath定位：//*[contains(@text,"手机号码")]

不能够用元素可见  ，只能用元素存在

"""

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

loc = (MobileBy.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (MobileBy.ID,"com.lemon.lemonban:id/btn_login")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# xpath表达式
loc = (MobileBy.XPATH,'//*[contains(@text,"手机号码或密码")]')
try:
    # 等待元素存在
    WebDriverWait(driver,6,0.01).until(EC.presence_of_element_located(loc))
    text = driver.find_element(*loc).text
    print(text)
except:
    print("我没有获取到toast的提示信息！！")


