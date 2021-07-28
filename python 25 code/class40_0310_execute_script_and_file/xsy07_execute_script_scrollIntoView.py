# author by claire

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")
element.send_keys("selenium webdriver")
driver.find_element_by_id('su').click()

loc = (By.XPATH, '//a[text()=" 常用API - Ethon - 博客园"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
a = driver.find_element(*loc)

# 移动滚动条至元素在可见区域下方
driver.execute_script('arguments[0].scrollIntoView(false);', a)

# 滚动至底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

# 滚动至顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
time.sleep(2)