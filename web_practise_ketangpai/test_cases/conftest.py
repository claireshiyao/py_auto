# author by claire

import pytest
import logging
from selenium import webdriver
from common import logger
from page_objects.login_page import LoginPage
from test_datas import global_datas as gds

@pytest.fixture
def init_driver():
    logging.info("*****conftest.py共享的init_driver的前置*****")
    # option = webdriver.ChromeOptions()
    # option.add_argument("--disable-infobars")
    driver = webdriver.Chrome()
    driver.get(gds.login_url)
    driver.maximize_window()
    yield driver
    driver.quit()
    logging.info("*****conftest.py共享的init_driver的后置*****")


@pytest.fixture
def init_login(init_driver):
    logging.info("init_login前置")
    LoginPage(init_driver).login(gds.user, gds.passwd)
    yield init_driver
    logging.info("init_login后置")



