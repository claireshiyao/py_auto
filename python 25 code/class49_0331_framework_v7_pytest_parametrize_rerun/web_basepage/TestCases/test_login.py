#!/usr/bin/python3
"""
@File    : test_login.py
@Time    : 2019/11/29 21:53
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium import webdriver
import ddt
import logging
from web_basepage.Common import logger

from web_basepage.PageObjects.login_page import LoginPage
from web_basepage.PageObjects.home_page import HomePage

from web_basepage.TestDatas import Common_Datas as CD
from web_basepage.TestDatas import login_datas as LD
import pytest


@pytest.fixture
def init(init_driver):
    logging.info("***** login用例自己的 init 的前置  *****")
    lp = LoginPage(init_driver)
    yield init_driver,lp   #(driver对象，lp页面对象)
    logging.info("***** login用例自己的 init 的后置  *****")


@pytest.mark.usefixtures("init")
class TestLogin:

    # 正常场景 - 登陆成功。
    def test_login_success(self,init):
        logging.info("******* 登陆功能 - 正常场景用例：登陆成功 *******")
        # 调用登陆页面的。登陆行为。
        init[1].login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言 - 首页当中，应该存在 退出元素。
        assert HomePage(init[0]).check_user_exist()
        # 断言2 - url地址  应当为 http://120.78.128.25:8765/Index/index
        assert init[0].current_url == LD.success_data["check_url"]


    # 异常用例 - 用户名为空/密码为空/用户名格式不正确
    # @ddt.data(*LD.wrong_datas)
    @pytest.mark.parametrize("case",LD.wrong_datas)
    def test_login_failed_by_wrongData(self,case,init):
        logging.info("******* 登陆功能 - 异常场景用例：数据格式校验 - 用户名为空/密码为空/用户名格式不正确 *******")
        # 调用登陆页面的。登陆行为。
        init[1].login(case["user"], case["passwd"])
        # 断言 - 登陆页面 - 应当现提示信息：请输入手机号
        self.assertEqual(case["check"], init[1].get_error_msg())


    # # 错误的密码
    # def test_login_failed_by_wrong_passwd(self):
    #     logging.info("******* 登陆功能 - 异常场景用例：数据后台有效性校验 - 密码错误 *******")
    #     # 调用登陆页面的。登陆行为。
    #     self.lp.login("18684720553", "python11")
    #     # 断言 - 登陆页面 - 应当现提示信息：帐号或密码错误!
    #     self.assertEqual("帐号或密码错误!", self.lp.get_error_msg_from_dialog())

