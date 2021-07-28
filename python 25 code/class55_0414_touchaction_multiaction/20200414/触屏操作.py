"""
模拟触屏操作：TouchAction    --- ActionChains
1、有很多行为
   tap  屏幕点击
   press 按住屏幕
   long_press
   release  释放
   move_to  从上一个点移动到这个点

   wait: 等待


2、perform()

滑屏操作：
"""

from appium.webdriver.common.touch_action import TouchAction
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
time.sleep(6)
# 等待所有题库都出来了，再滑动


# 1、获取整屏的大小
size = driver.get_window_size()

# 1）实例化TouchAction类
tc = TouchAction(driver)

tc.press(x=size["width"]*0.5,y=size["height"]*0.9).wait(200).\
   move_to(x=size["width"]*0.5,y=size["height"]*0.3).\
   release()
tc.perform()


