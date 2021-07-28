# author by claire

# 代码怎么知道哪个窗口是新的？
# 1. 得到目前打开的所有窗口。句柄。每一个窗口都有句柄。
# 列表。最新窗口在列表最后
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

loc = (By.XPATH,'//a[text()=" - SeleniumHQ Browser Automation"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element_by_xpath('//a[text()=" - SeleniumHQ Browser Automation"]').click()  # 触发新的窗口出现

time.sleep(1)

# 所有的窗口句柄
wins = driver.window_handlers
# 当前窗口句柄
print(driver.current_window_handle)

# 切换到新窗口
driver.switch_to.window(wins[-1])

loc = (By.XPATH,'//div[@class="download-button-container"]//a')
WebDriverWait(driver,15).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()




