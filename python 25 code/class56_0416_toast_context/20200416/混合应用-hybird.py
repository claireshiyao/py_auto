
""""""
"""
混合应用：html页面和原生控件都在app里边儿
混合应用自动化测试：web自动化+app自动化的组合。

1、如何识别混合应用？怎么知道当前这个页面含有html??
android.webkit.WebView   网页视图
开发者模式当中，打开显示布局边界

1.2、开启调试模式  
   开启调试模式。http://www.lemfix.com/topics/317

1.3、获取到目前的conTexts   driver.contexts 

2、从页面的原生控件，切换到了html页面。  在启动参数当中指定了chromdriver
   switch_to.context(名字?)
   context:上下文。

======================= Web自动化 ==========================
驱动要跟浏览器匹配 ---  安卓系统的webview的版本
找html元素 --- ？？？ 得到页面的html，然后去通过F12
1、uc-devtool  - 查看元素定位
2、chrome://inspect/#devices   --- 科学上网
3、driver.page_source --- 获取当前的html，
4、找开发 - 谁写的页面找谁


"""

from appium import webdriver

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# *******************   App自动化    **********************

# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
desired_caps = {
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "platformVersion":'7.1.2',
    "deviceName":"emulator-5554",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True,
    "chromedriverExecutable":"D:\\ChromeDrivers\\chrome67-69\\chromedriver.exe",
    # "chromedriverExecutableDir":"D:\\ChromeDrivers"
}

# 3、连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

loc = (MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"全程班\")")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (MobileBy.CLASS_NAME,"android.webkit.WebView")
time.sleep(2)

# 获取当前所有的contexts
cons = driver.contexts
print(cons)

# 切换到webview - html页面去
driver.switch_to.context('WEBVIEW_com.lemon.lemonban')

# //span[text()="加群"]

# *******************   web自动化  -- 操作html页面了   **********************
loc = (MobileBy.XPATH,"//span[text()=\"加群\"]")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()