# author by claire

from selenium import webdriver
import time
# 启动chromedriver, 建立连接，会话ID
driver = webdriver.Chrome()  # 打开一个第一次使用的浏览器

# get是函数名称
driver.get("http://www.baidu.com")

# 窗口最大化
driver.maximize_window()

driver.get("http://www.taobao.com")

# 返回到上一个页面
driver.back()
time.sleep(2)

driver.forward()

driver.refresh()

# 退出会话-关闭浏览器-关闭chromedriver进程
driver.quit()

# driver.close()  关闭当前操作的窗口

