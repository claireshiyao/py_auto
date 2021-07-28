"""
ActionChains   动作链

鼠标操作： 参数都是元素对象，除了与坐标有关的函数外。
悬浮  move_to_element
点击  click
双击  double_click
右键   context_click
拖拽  drag_and_drop
暂停  pause
输入  send_keys

1、将你要执行所有鼠标的动作，先放到一个列表当中。
2、perform() : 执行鼠标动作。


1、悬浮  2、点击  3、双击

"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 1) 找到鼠标要操作的元素
loc = (By.XPATH,'//div[@id="u1"]//a[@name="tj_settingicon"]')
ele = driver.find_element(*loc)
ele.click()
# # 2) 实例化Actionchains类
# ac = ActionChains(driver)
#
# # 3)调用鼠标行为
# ac.move_to_element(ele).click(ele)
#
# # 4)调用perform()来执行鼠标动作。
# ac.perform()

# # 2）3）4）
# ActionChains(driver).move_to_element(ele).perform()
# 1)等待 下拉列表当中的元素可见
loc = (By.XPATH,'//a[text()="高级搜索"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
# 2）选你想的元素
driver.find_element(*loc).click()  # 触发了高级搜索内容出现


#*********************************Select类处理****************************
from selenium.webdriver.support.select import Select
# 1)初始化，传select对象
loc = (By.XPATH,'//select[@name="ft"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
select_element = driver.find_element(*loc)

s = Select(select_element)

# 2) 根据下标、value属性、文本内容来选择值
s.select_by_index(6)  # 下标选值
time.sleep(3)
s.select_by_value("doc")
time.sleep(3)
s.select_by_visible_text('RTF 文件 （.rtf)')
time.sleep(3)



# 关闭会话
time.sleep(7)
driver.quit()



