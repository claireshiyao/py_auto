from appium.webdriver.common.multi_action import MultiAction
# 实现了多个单点触控，同时执行
# add   添加单点触控的行为
# perfrom 执行

# 放大
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction


# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
desired_caps = {
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "platformVersion":'7.1.2',
    "deviceName":"emulator-5554",
    "appPackage": "com.baidu.BaiduMap",
    "appActivity": "com.baidu.baidumaps.WelcomeScreen",
    "noReset":True
}

# 3、连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(15)

# 1、获取整屏的大小
size = driver.get_window_size()

# 放大
# 从中心向左下角滑动
a = TouchAction(driver)
a.press(x=size["width"]*0.5,y=size["height"]*0.5).wait(200).move_to(x=size["width"]*0.1,y=size["height"]*0.9).release()
# 从中心，向右上角滑动
b = TouchAction(driver)
b.press(x=size["width"]*0.5,y=size["height"]*0.5).wait(200).move_to(x=size["width"]*0.9,y=size["height"]*0.1).release()

# 加入Multiaction
ma = MultiAction(driver)
ma.add(a,b)
ma.perform()