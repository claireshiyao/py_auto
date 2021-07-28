"""
Alert类
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Pychram-Workspace/py25-web-base/web_0307/myHtml.html")

# 点击动作触发 弹框出现
driver.find_element_by_id("press").click()


# 等等弹框出现
time.sleep(1)
# 切换
alert = driver.switch_to.alert

# 我要把这个弹框关掉，进行下一步的页面处理
print(alert.text)
# alert.send_keys("")
alert.accept()


# 关闭会话
time.sleep(7)
driver.quit()




