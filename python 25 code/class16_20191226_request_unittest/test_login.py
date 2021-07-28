#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
1, 模块名以test开头
2， 类以 Test 开头
3, 方法test 开头


运行：右击：出现 unittest
如果没有出现，那么要配置
"""
import unittest

from class_16_requests.d3_unittest import visit


url = 'http://120.78.128.25:8766/futureloan/member/login'
headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}


class TestLogin(unittest.TestCase):

    def test_login_success(self):
        # res = visit(url, data, headers)
        # print(res)
        self.assertEqual(1, 3-3)

