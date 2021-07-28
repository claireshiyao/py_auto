# author by claire

# 多个属性组合来找元素或通过其它的关系来找元素
"""
1. xpath -语法
绝对路径
相对路径--靠自己的特征来定位

2. css_selector
"""


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw") # WebElement对象
element.is_selected()

driver.find_element_by_class_name("s_ipt")
driver.find_elements_by_class_name("s_ipt") # 匹配多个元素-列表

driver.find_element_by_name("wd")

driver.find_element_by_tag_name("input")

driver.find_element_by_link_text("地图")


driver.find_element_by_partial_link_text("hao")

