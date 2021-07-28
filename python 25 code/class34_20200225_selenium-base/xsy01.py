# author by claire
from selenium import webdriver

# 启动chromedriver, 建立连接，会话ID
driver = webdriver.Chrome()

# get是函数名称
driver.get("http://www.baidu.com")
