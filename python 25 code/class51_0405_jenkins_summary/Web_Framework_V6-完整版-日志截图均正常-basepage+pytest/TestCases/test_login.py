#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: 简
# Time: 2019/6/6

# import unittest
from selenium import webdriver


from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_datas as ld
from TestDatas import Comm_Datas as cd
import pytest

# @pytest.fixture
# def myDemo():
#     print("====独有前置====")
#
#
# # @pytest.mark.usefixtures("login_web")
# def test_demo(myDemo):
#     print("111111111111111111")


# 用例三步曲：前置 、步骤 、 断言
@pytest.mark.usefixtures("access_web")  # 使用了access_web函数的前置和后置
class TestLogin:


    # 正常用例 - 登陆+首页
    def test_login_2_success(self,access_web): # fixture的函数名称=返回值
        # logging.info("用例1-正常场景-登陆成功-使用到测试数据-")
        # 步骤 - 登陆操作 - 登陆页面 - 18684720553、python
        LoginPage(access_web).login(ld.success_data["user"],ld.success_data["passwd"])  # 测试对象+测试数据
        # 断言 - 页面是否存在   我的帐户   元素   元素定位+元素操作
        assert IndexPage(access_web).check_nick_name_exists() # 测试对象+测试数据
        # url跳转
        # self.assertEqual(access_web.current_url,ld.success_data["check"]) # 测试对象+测试数据 # # 正常用例 - 登陆+首页
        # self.assertEqual(access_web.current_url,ld.success_data["check"]) # 测试对象+测试数据 # # 正常用例 - 登陆+首页

    # 异常用例 -....
    # @ddt.data(*ld.wrong_datas)
    @pytest.mark.parametrize("data",ld.wrong_datas)
    def test_login_0_failed_by_wrong_datas(self,data,access_web):
        # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
        LoginPage(access_web).login(data["user"], data["passwd"])
        # 断言 - 页面的提示内容为：请输入密码
        assert data["check"] == LoginPage(access_web).get_error_msg_from_loginForm()

    # @ddt.data(*ld.fail_datas)
    @pytest.mark.parametrize("data", ld.fail_datas)
    def test_login_1_failed_by_fail_datas(self,data,access_web):
        # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
        LoginPage(access_web).login(data["user"], data["passwd"])
        # 断言 - 页面的提示内容为：请输入密码
        assert data["check"] == LoginPage(access_web).get_error_msg_from_pageCenter()




    # def test_login_failed_by_no_user(self):
    #     # 步骤 - 登陆操作 - 登陆页面 - 用户名为空 python
    #     LoginPage(self.driver).login("", "python")
    #     self.assertEqual("请输入手机号码", LoginPage(self.driver).get_error_msg_from_loginForm())
    #
    # def test_login_failed_by_wrong_user_formater(self):
    #     # 步骤 - 登陆操作 - 登陆页面 - 用户名为空 python
    #     LoginPage(self.driver).login("1867744", "python")
    #     self.assertEqual("请输入正确的手机号", LoginPage(self.driver).get_error_msg_from_loginForm())



