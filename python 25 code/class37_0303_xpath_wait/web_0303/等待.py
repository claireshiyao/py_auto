from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
# driver.implicitly_wait(10)   # 隐性等待
driver.get("http://www.baidu.com")

# 1、输入操作  send_keys
# 2、点击操作  click
# 获取文本和获取属性

"""
1、sleep - 强制
2、智能等待：最多愿意等待15秒。但是呢，如果在15内，任何一个时候元素出现了，那就继续下一行代码。
             超时了，报超时异常  TimeoutException、 NosuchElementExption

   隐性等待：2种场景  1个元素被找到-元素存在/1条命令执行完成-api的执行
             每一个会话当中，只需要被调用一次。
             会话：从你打开浏览器，到quit关闭整个过程。 --- sessionId

   显性等待：等待元素可见？等待url变更为XXX?? 等待新的窗口出现？？等待元素可用？？
   在你需要的地方，直接用显性等待。  条件+等待
   等待：等待上限 - 15秒   轮询周期 - 多少秒去确认一下条件是否成立。默认是0.5.  WebDriverWait类
   WebDriverWait(driver,15,0.5).until/not_until(条件)
   条件：有一个专门的条件模块。Expected_condition
   
   

"""

# id
element = driver.find_element_by_id("kw")   # WebElement对象 - 1个对象对应1个元素
# driver.find_elements_by_id("kw")
element.send_keys("selenium webdriver")
driver.find_element_by_id('su').click()  # 带来了内容上的变化
# time.sleep(5)
# 条件： '//a[text()=" - SeleniumHQ Browser Automation"]'这个元素要是可见或者存在的
loc = ("xpath",'//a[text()=" - SeleniumHQ Browser Automation"]')
# EC.visibility_of_element_located(loc)  # loc元素可见的条件
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element_by_xpath('//a[text()=" - SeleniumHQ Browser Automation"]').click()


# 退出会话
time.sleep(7)
driver.quit()