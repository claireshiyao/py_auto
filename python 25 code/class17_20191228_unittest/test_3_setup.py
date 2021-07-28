#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽







import unittest

# from class_17_unittest.d3_unittest import visit


url = 'http://120.78.128.25:8766/futureloan/member/login'
headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}


class TestLogin(unittest.TestCase):

    def test_login_2_success(self):
        try:
            print("测试用例1")
            self.assertEqual(1 , 1)  # AssersionError
        except AssertionError as e:
            # 如果你想断言失败，那么一定要抛出一个 AssertionError
            print("断言失败", e)
            raise AssertionError

    def test_login_3_error(self):
        print("测试用例2")
        self.assertEqual(1, 2)
