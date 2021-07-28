from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

ele = driver.find_element_by_id("s_usersetting_top")
ele.click()

import time

time.sleep(3)
driver.quit()