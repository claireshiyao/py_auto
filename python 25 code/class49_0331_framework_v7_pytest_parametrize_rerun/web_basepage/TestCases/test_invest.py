#!/usr/bin/python3
"""
@File    : test_invest.py
@Time    : 2019/12/2 21:30
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
"""
前置(准备条件)：
1、登陆网站 
2、有可投资的标(没有就会去创建标)
3、可投金额，大于你投资的金额
4、用户得有足够的余额去投资(功能：一次充它一个亿)

代码：接口(创建标、审核标)、接口(每次充5000，或者，先查询有没钱，没有就充XXXX)

步骤+断言(web页面，期望结果除外)：
1、(前置)登陆页面登陆;
2、首页选标；
3、标页面获取用户余额；
4、标页面获取 标的余额；
5、标页面：投标动作；
6、个人页面：获取用户余额
7、回退到标页面：再次获取标的余额
"""

import unittest
from selenium import webdriver
import logging
from web_basepage.Common import logger
import ddt

from web_basepage.PageObjects.login_page import LoginPage
from web_basepage.PageObjects.home_page import HomePage
from web_basepage.PageObjects.bid_page import BidPage
from web_basepage.PageObjects.user_page import UserPage

from web_basepage.TestDatas import Common_Datas as CD
from web_basepage.TestDatas import invest_datas as ID

@ddt.ddt
class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 1、(前置)登陆页面登陆;
        self.driver = webdriver.Chrome()
        self.driver.get(CD.login_url)
        LoginPage(self.driver).login(CD.user,CD.passwd)
        # 标页面选第一标   # 2、首页选标；
        HomePage(self.driver).click_first_bid()
        self.bp = BidPage(self.driver)


    def tearDown(self) -> None:
        self.driver.quit()

    # 正常场景 - 投资成功
    def test_invest_success(self):
        logging.info("******* 投资功能 - 正常场景用例：投资1000元成功。用户可用余额减少1000，标余额减少1000 *******")
        # 3、标页面获取用户余额；
        user_money_before_invest = self.bp.get_user_money()
        # 4、标页面获取 标的余额；
        bid_money_before_invest = self.bp.get_bid_left_money()
        # 5、标页面：投标动作；
        self.bp.invest(ID.success["money"])
        # 6、点击投标成功提示框当中：查看并激活按钮
        self.bp.click_activeButton_on_success_popup()
        # 7、个人页面：获取用户余额
        user_money_after_invest = UserPage(self.driver).get_user_left_money()
        # 8、回退到标页面、刷新后：再次获取标的余额
        self.driver.back()
        self.driver.refresh()
        bid_money_after_invest = self.bp.get_bid_left_money()
        # 9、断言
        # print(float(user_money_before_invest) - float(user_money_after_invest))
        # print(float(bid_money_before_invest) - float(bid_money_after_invest))
        # print((float(bid_money_before_invest) - float(bid_money_after_invest))*10000)
        self.assertEqual(ID.success["money"],int(float(user_money_before_invest) - float(user_money_after_invest)))
        self.assertEqual(ID.success["money"],int((float(bid_money_before_invest) - float(bid_money_after_invest))*10000))


    # 异常场景: 数据字段 格式校验 - 弹框提示金额格式不对。
    @ddt.data(*ID.invalid_data_format)
    def test_invest_failed_invalid_money(self,invalid_data):
        logging.info("******* 投资功能 - 异常场景用例：投资金额有效性校验 - 投资金额为非100的整数倍、错误的格式等 *******")
        # 3、标页面获取用户余额；
        user_money_before_invest = self.bp.get_user_money()
        # 4、标页面获取 标的余额；
        bid_money_before_invest = self.bp.get_bid_left_money()
        # 5、标页面：投标动作；
        self.bp.invest(invalid_data["money"])
        # 6、获取页面提示信息
        error_msg = self.bp.get_errorMsg_from_pageCenter()
        # 7、刷新当前页面，获取用户余额、标余额。
        self.driver.refresh()
        user_money_after_invest = self.bp.get_user_money()
        bid_money_after_invest = self.bp.get_bid_left_money()
        # 8、断言 - 提示信息是否正确。标的金额不变，用户的余额也不变。
        self.assertEqual(error_msg,invalid_data["check"])
        self.assertEqual(user_money_before_invest,user_money_after_invest)
        self.assertEqual(bid_money_before_invest,bid_money_after_invest)

