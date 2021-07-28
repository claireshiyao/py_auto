# 测试用例级别

import pytest
from selenium import webdriver
from web_basepage.TestDatas import Common_Datas as CD
from web_basepage.PageObjects.login_page import LoginPage
import logging
from web_basepage.Common import logger

@pytest.fixture
def init_driver():
    """
    前置：打开浏览器，访问系统网址
    后置：退出浏览器。
    """
    logging.info("***** conftest.py共享的 init_driver 的前置  *****")
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    yield driver
    driver.quit()
    logging.info("***** conftest.py共享的 init_driver 的后置  *****")

"""
前置：打开浏览器，访问系统网址 + 登陆系统
后置：退出浏览器。
"""
@pytest.fixture
def init_login(init_driver): # init_driver代表的是它的返回值：driver
    LoginPage(init_driver).login(CD.user, CD.passwd)
    yield init_driver  # 返回driver对象。
    print("1111111111111")
"""
init_driver的前置
init_login的前置
init_login的后置
init_driver的后置

假设：init_driver是class级，init_login是function级别？
      可以"继承"。
      init_driver是function级，init_login是function级别?
      可以调用。
      init_driver是function级，init_login是class级别?
      不可以。

一个fixture，可以使用比它高的/与它同级的 fixture作为它的参数。 

   function，可以调用class,function,module,session.
   function最小单位。最后执行。其它的级别一定是比它先执行。


进去：校门 -> 楼大门 -> 教室门
出来：教室门 -> 楼大门 -> 校门
"""

@pytest.fixture(scope="session",autouse=True)
def mySs():
    print("**** 我是session级别的fixture 前置 ****")
    yield
    print("**** 我是session级别的fixture 后置 ****")


@pytest.fixture(scope="module")
def myMo():
    print("**** 我是module级别的fixture 前置 ****")
    yield
    print("**** 我是module级别的fixture 后置 ****")
