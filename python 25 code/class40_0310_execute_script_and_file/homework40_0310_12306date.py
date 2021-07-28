
# 12306查票操作，请用javascript实现出发地和目的地的选择,日期处理，并提交查询操作；

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars")

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.12306.cn/index/")

# 出发地输入广州
loc = ('xpath', '//input[@id="fromStationText"]')
ele = driver.find_element(*loc)
ele.clear()
ele.send_keys("广州")

# 选择广州南
loc = ('xpath', '//div[@id="citem_0"]')
ele = driver.find_element(*loc).click()

# 修改出发地value属性
loc = ('xpath', '//input[@id="fromStation"]')
ele = driver.find_element(*loc)
driver.execute_script('var a = arguments[0]; a.value = "IZQ"', ele)

# 到达地输入衡阳
loc = ('xpath', '//input[@id="toStationText"]')
ele = driver.find_element(*loc)
ele.clear()
ele.send_keys("衡阳")

# 选择衡阳东
loc = ('xpath', '//div[@id="citem_1"]')
ele = driver.find_element(*loc).click()

# 修改到达地value属性
loc = ('xpath', '//input[@id="toStation"]')
ele = driver.find_element(*loc)
driver.execute_script('var a = arguments[0]; a.value = "HVQ"', ele)

# 日期
loc = ("xpath", "//*[@id='train_date']")
date_ele = driver.find_element(*loc)
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# 修改日期属性，并选择今天日期
driver.execute_script('var a = arguments[0]; a.readOnly=false; a.value=arguments[1]', date_ele, today)

# 查询
loc = ('xpath', '//a[@id="search_one"]')
driver.find_element(*loc).click()

time.sleep(3)

# 报错，无法运行


