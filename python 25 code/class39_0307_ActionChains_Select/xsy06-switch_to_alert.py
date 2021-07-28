# author by claire

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///E:/PycharmProjects/python25/class39_0307_ActionChains_Select/xsyHtml3.html")

# 触发弹出框
driver.find_element_by_id("press").click()

time.sleep(1)

# 切换
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(6)

driver.quit()

