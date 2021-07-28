import pytest
from selenium import webdriver

# 定义fixture
@pytest.fixture()   # pytest就能识别它为一个前置后置
def init():
    # 前置
    print("****我是函数别的前置！！，开始****")
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    # yield driver,True   # 银河 # 返回driver对象
    yield driver
    # 后置
    print("****我是函数别的后置！！，结束****")
    driver.quit()