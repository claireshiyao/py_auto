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
# 1、
loc = (MobileBy.ID,'com.lemon.lemonban:id/navigation_tiku')
# 等待 - 3大等待方式
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))

driver.find_element(*loc).click()  # 进入题库界面
time.sleep(3)
# 等待所有题库都出来了，再滑动


# 1、获取整屏的大小
size = driver.get_window_size()
# 2、通过百分比去滑动
driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"]*0.5,size["height"]*0.3,200)