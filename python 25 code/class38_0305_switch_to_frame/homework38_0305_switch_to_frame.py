
# 1）同步上课的元素操作场景 代码。
#
# 2)  实现腾讯课堂 - QQ用户名密码登陆的自动化脚本 。
#
# 注意：有iframe.  另，如果公司项目有iframe，可用公司项目的。
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://ke.qq.com/")

driver.maximize_window()

# 等待登录按钮可见
loc = (By.XPATH, '//a[@id="js_login"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))

# 点击登录按钮
driver.find_element_by_xpath('//a[@id="js_login"]').click()

# 等待QQ登录可见并点击
loc_qq = (By.XPATH, '//a[@class="js-btns-enter btns-enter btns-enter-qq"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc_qq))
driver.find_element_by_xpath('//a[@class="js-btns-enter btns-enter btns-enter-qq"]').click()

# 切换到qq登录内嵌页面
driver.switch_to.frame("login_frame_qq")

# 选择用户名密码登录
loc_user = (By.XPATH, '//a[@id="switcher_plogin"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc_user))
driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()

driver.find_element_by_id("u").send_keys("3270466428")
driver.find_element_by_id("p").send_keys("xsy123456")
driver.find_element_by_xpath('//input[@id="login_button"]').click()

time.sleep(10)
driver.quit()

