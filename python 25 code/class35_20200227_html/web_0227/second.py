from selenium import webdriver
import time

# 打开一个浏览器，与浏览器建立会话
# 启动了chromedriver.exe    并且还建立了连接，会话ID
driver = webdriver.Chrome()  # 打开一个第一次使用浏览器

driver.get("http://www.baidu.com")

# 窗口最大化
driver.maximize_window()

driver.get("http://www.taobao.com")

# # 回到上一个页面
# driver.back()
# time.sleep(2)
#
# # 前进到下一个页面
# driver.forward()
# time.sleep(2)
#
# #刷新
# driver.refresh()
# time.sleep(2)


#
# # 关闭当前操作的窗口
# driver.close()
# # 退出会话 - 关闭浏览器，关闭chroemdriver这个进程
# driver.quit()