# author by claire
import time

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")
element.send_keys("柠檬班", Keys.ENTER)
element.send_keys(Keys.CONTROL, "c")

time.sleep(6)

driver.quit()
