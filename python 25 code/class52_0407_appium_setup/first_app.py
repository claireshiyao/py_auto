from appium import webdriver

# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
desired_caps = {
    "platformName":"Android",
    "platformVersion":'7.1.2',
    "deviceName":"emulator-5554",
    "appPackage":"com.lemon.lemonban",
    "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
    "noReset":True
}

# 3、连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 准备工作
# 1、启动appium server程序
# 2、至少有一个设备是能够识别到的。
# 代码 -- appium server --- 模拟器/真机
# appium server有哪些模拟器/真机？  --- 识别/电脑需要识别连接的设备。
# adb命令(安卓调试桥-pc端发命令操作手机)：adb devices



# 安装 5大件：appium desktop，appium-python库，模拟器/真机，ADT工具包，JDK

# 在windows写python代码，操控另外的移动设备去执行命令。
#  python代码 === appium desktop服务  ===  安卓手机

# appium desktop服务同时支持  android 和 ios
# android 和 ios有自带的自动化框架
# android 和 ios有很多的版本，且版本之间存在自动化框架上的差异

# 代码当中，必须 告诉appium，你是要在 哪个平台的哪个版本上，对哪个app进行操作。
# 启动参数获取地址：http://appium.io/docs/en/writing-running-appium/caps/#general-capabilities

# 1）系统/andorid,IOS
# 2）系统版本号
# 3）设备名称 - 需要这个参数但是没有实际使用
# 4）包名
# 5）入口页面-activity

# apk包获取包名和入口页面
# aapt dump badging apk路径   获取app的包名和launchable-activity



# appium日志分析？？？
# selenium之间的关系 -- appium用到了selenium --Command

