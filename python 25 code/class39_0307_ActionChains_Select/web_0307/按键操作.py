from selenium.webdriver.common.keys import Keys


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
# driver.implicitly_wait(10)   # 隐性等待
driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")   # WebElement对象 - 1个对象对应1个元素
# driver.find_elements_by_id("kw")
element.send_keys("selenium webdriver",Keys.ENTER)
# element.send_keys(Keys.CONTROL,"c")

"""
WebdriverWait类

switch_to: 切换

Alert: 处理alert弹框。

ActionChains：鼠标操作

Select： select下拉列表操作。

Keys：特殊键。


#  js操作、上传操作。
"""