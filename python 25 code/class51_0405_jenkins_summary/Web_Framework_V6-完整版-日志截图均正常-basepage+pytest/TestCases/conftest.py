#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/7/23
import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_datas as ld
from TestDatas import Comm_Datas as CD
import logging

# 定义一个函数级别的fixtures  1个函数=前置+后置
# 函数名称前面  @pytest.fixture

@pytest.fixture
def access_web():
    # 前置 - 打开浏览器访问网址
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    yield driver   # 分界线+返回值
    # 后置 - 关闭浏览器
    driver.quit()

@pytest.fixture
def login_web(access_web):
    LoginPage(access_web).login(CD.user, CD.passwd)
    yield access_web
    logging.info("=====每一个用例后置：关闭浏览器会话========")

"""
access_web的前置
login_web的前置
。。。测试用例。。。。
login_web的后置
access_web的后置
"""




# 在测试用例当中使用fixture,
# 在测试类或者用例前面加上@pytest.mark.usefixtures("fixture的函数名称")
# 如果fixture有返回值，
# 如果测试用例当中，要用到返回值，那么fixture的函数名称=返回值，
# 作为测试用例的参数传给测试用例使用。

# @pytest.fixture
# def refresh(access_web):  # 如果access_web没执行，那么执行了access_web，再执行refresh
#     yield access_web
#     access_web.refresh()


