from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.switch_to.frame("login_frame_qq")

# 4) 回到默认的html页面当中 - 第一代
driver.switch_to.default_content()

# 5) 回到上一级的iframe - 上一代
driver.switch_to.parent_frame()