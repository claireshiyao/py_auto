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
time.sleep(3)
# 等待所有题库都出来了，再滑动


# 1、获取整屏的大小
size = driver.get_window_size()

# 循环/滑动
# 什么时候滑？滑几次？滑到什么时候终止？滑到底部了如何不再滑动？
# 滑动以前的内容  != 滑动以后的内容 => 继续滑
# 滑动以前的内容  == 滑动以后的内容 => 已经到底部
"""
old = None
new = driver.page_source
while 滑动以前的内容  != 滑动以后的内容:
    如果元素找着了(driver.find_element()/page_source.find())：
        break
    如果没找着：
        滑动操作 - 
        sleep(3)
        old = new
        new = driver.page_source   
"""
old = None
new = driver.page_source

while old != new:
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("安全测试")')
    except:
        driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"]*0.5,size["height"]*0.3,200)
        time.sleep(3)
        old = new
        new = driver.page_source
    else:
        print("找到了安全测试")
        break



