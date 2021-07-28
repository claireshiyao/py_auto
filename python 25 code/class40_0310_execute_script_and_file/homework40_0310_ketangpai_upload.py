
# 完成课堂派，上传作业的操作；使用已封装的upload方法；
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from class40_0310_execute_script_and_file.upload import upload
option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars")

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.ketangpai.com/")

# 课堂派首页登录
driver.find_element_by_class_name('login').click()

# 输入手机号
loc = (By.NAME, 'account')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys('13711743452')

# 输入密码
driver.find_element_by_name("pass").send_keys('******')

# 点击登录按钮
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]').click()

# 课堂页面：Python全栈第25期
loc = (By.XPATH, '//a[@class="jumptoclass" and @title="Python全栈第25期"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 选择作业页面
loc = (By.XPATH, '//a[text()="作业"]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击作业链接
loc = (By.XPATH, '//a[contains(text(), "js操作体验和上传")]')
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 添加作业文件
loc = (By.XPATH, '//a[@class="sc-btn webuploader-container"]')
WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# ele = driver.find_element(*loc)
# ActionChains(driver).click(ele).perform()

# 调用upload函数上传文件
time.sleep(4)
filepath = 'D:\python\PycharmProjects\python25\class40_0310_execute_script_and_file\homework40_0310_ketangpai_upload.py'
upload(filepath)

# 提交
loc = (By.XPATH, '//a[text()="提交"]')
WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(loc))
driver.find_element(*loc).click()


