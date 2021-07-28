# author by claire

# 多个属性组合来找元素或通过其它的关系来找元素
"""
1. xpath -语法
绝对路径
相对路径--靠自己的特征来定位

2. css_selector
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw") # WebElement对象
element.is_selected()

driver.find_element_by_class_name("s_ipt")
driver.find_elements_by_class_name("s_ipt") # 匹配多个元素-列表

driver.find_element_by_name("wd")

driver.find_element_by_tag_name("input")

driver.find_element_by_link_text("地图")

driver.find_element_by_partial_link_text("hao")

driver.find_element_by_xpath("")

driver.find_element_by_css_selector('input#kw.s_ipt')

driver.find_element(By.XPATH, '//p[@title="写忆"]/preceding-sibling::p[@class="stuno"]')

# 元素操作：
# 输入：send_keys
# 点击: click
# 智能等待：最多等待多久
# 隐形等待：implicitly_wait(10)
#     2种场景：元素存在/上一个命令执行完成
#         每一个会话当中，只需要被调用一次
# 显性等待：等待上限、轮询周期

loc = ("xpath", '//a[text()=" - SeleniumHQ Browser Automation"]')
WebDriverWait(driver,15,0.5).until(EC.visibility_of_element_located(loc))
# 获取文本和获取属性

