from selenium import webdriver

# 打开一个浏览器，与浏览器建立会话
# 启动了chromedriver.exe    并且还建立了连接，会话ID
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

"""
人 --  浏览器

代码(selenium webdriver)  --  驱动程序(XXXdriver) -- 浏览器(ie、firefox\chrome)


代码(selenium webdriver)    --http通信--   驱动程序(XXXdriver)
java/python/C#.../postman

把每一个对网页(api)的操作，都是一个接口。json格式，url、请求类型、请求数据。
协议名称：jsonWireProtocol

"""