from appium import webdriver

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# WebElement  click  send_keys  get_attribute   .text
driver.find_element(*loc).click()

# 2、-- android_uiautomator -  利用自动化框架提供的定位方法 - java
# 第三方库：1、元素定位  2、元素操作  3、。。。。。。
# xpath - 组合
# new UiSelector().text("Python自动化").resourceId("com.lemon.lemonban:id/fragment_category_type")
# new UiSelector().方法名称(值).方法名称(值).方法名称(值)
# 选择python自动化的题 库类型
loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Python自动化")')
# driver.find_element_by_android_uiautomator('new UiSelector().text("Python自动化")')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 3、xpath
loc = (MobileBy.XPATH,'//*[@resource-id="com.lemon.lemonban:id/second_level"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 4、description - content-desc
# driver.find_element_by_accessibility_id()

# 5、class属性定位
# driver.find_element_by_class_name('android.widget.ImageView')

# 6、坐标
# os.system("adb shell tap x y")

# driver.lock()
# driver.unlock()
# driver.is_locked()

# driver.open_notifications()

