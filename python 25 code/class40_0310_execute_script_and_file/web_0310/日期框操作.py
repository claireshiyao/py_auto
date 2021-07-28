
from selenium import webdriver

driver  = webdriver.Chrome()

# pha_js = "var a = arguments[0];a.readOnly=false;a.value= arguments[1];"

loc = ("xpath","//*[@id='train_date']")
ele = driver.find_element(*loc)

now_10 = "1111"  # datetime获取当前时间

driver.execute_script("var a = arguments[0];a.readOnly=false;a.value= arguments[1];",ele,now_10)