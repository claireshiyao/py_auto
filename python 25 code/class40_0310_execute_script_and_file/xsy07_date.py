import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.12306.cn/index/")

loc = ("xpath", "//*[@id='train_date']")
ele = driver.find_element(*loc)

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# 修改日期属性，并选择今天日期
driver.execute_script('var a = arguments[0]; a.readOnly=false; a.value=arguments[1]', ele, today)

