
# 12306查票操作，请用javascript实现出发地和目的地的选择,日期处理，并提交查询操作；

from selenium import webdriver
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars")

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.12306.cn/index/")

# 点击出发地地理位置图标
loc = ('xpath', '//i[@class="icon icon-place" and @data-click="fromStationText"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# 选择广州
loc = ('xpath', '//li[@title="广州"]')
ele = driver.find_element(*loc).click()
# 修改出发地value属性
loc = ('xpath', '//input[@id="fromStation"]')
ele = driver.find_element(*loc)
driver.execute_script('var a = arguments[0]; a.value = "GZQ";', ele)

# 点击到达地地理位置图标
loc = ('xpath', '//i[@class="icon icon-place" and @data-click="toStationText"]')
driver.find_element(*loc).click()
# 选择上海
loc = ('xpath', '//li[@title="上海"]')
ele = driver.find_element(*loc).click()
# 修改到达地value属性
loc = ('xpath', '//input[@id="toStation"]')
ele = driver.find_element(*loc)
driver.execute_script('var a = arguments[0]; a.value = "SHH";', ele)

# 日期
loc = ("xpath", "//*[@id='train_date']")
date_ele = driver.find_element(*loc)
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# 修改日期属性，并选择今天日期
driver.execute_script('var a = arguments[0]; a.readOnly=false; a.value=arguments[1];', date_ele, today)

# 查询
loc = ('xpath', '//a[@id="search_one"]')
driver.find_element(*loc).click()

time.sleep(3)


