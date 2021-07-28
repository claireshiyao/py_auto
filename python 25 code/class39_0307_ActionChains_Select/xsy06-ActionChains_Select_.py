# author by claire

# ActionChains 动作链
"""
1. 悬浮 move_to_element
2. 点击 click
3. 双击 double_click
4. 右击 context_click
5. 拖拽  drag_and_drop
6. 暂停 pause
7. 输入 send_keys

将要执行的所有鼠标动作，先放到列表当中
perform(), 执行鼠标动作

"""
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 会自动等待页面加载完成，不需要等待

# 悬浮到设置元素
ele = driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_settingicon"]')

# 实例化Actionchains类
ac = ActionChains(driver)
ac.move_to_element(ele)
ac.perform()

# 也可以一步到位，方法返回的是self对象
# ActionChains(driver).move_to_element(ele).perform()
loc = (By.XPATH, '//a[text()="高级搜索"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
# 高级搜索点击
driver.find_element(*loc).click()

# select类处理，下拉列表
from selenium.webdriver.support.select import Select
loc = (By.XPATH, '//select[@name="ft"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
select_element = driver.find_element(*loc)

s = Select(select_element)
s.select_by_index(6)
time.sleep(3)
s.select_by_value("doc")
time.sleep(3)
s.select_by_visible_text("微软 Powerpoint (.ppt)")

time.sleep(7)
driver.quit()
