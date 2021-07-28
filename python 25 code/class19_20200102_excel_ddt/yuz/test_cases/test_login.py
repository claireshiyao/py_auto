#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""
ddt: 数据驱动思想：data driven testing
你会 data driven testing 数据驱动思想。

现在所说的是一个叫做 ddt 的 python 库
ddt 库是和 unittest 搭配起来使用的， 是 unittest 的一个插件。
python / unittest / ddt 自动化测试框架


@ddt.ddt   没有括号
class TestDemo:

    @ddt.data()   右括号
    def test_demo(self):
        pass

"""
import unittest
import ddt

from class_19_excel.common.excel_handler import ExcelHandler
from class_19_excel.common.requests_handler import RequestsHandler



test_data = [
        {"url": "http://120.78.128.25:8766/futureloan/member/login",
         "method": "post",
         "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
         "data": {"mobile_phone": "18111111111", "pwd": "12345678"},
         "expected": {"msg":"", "code":""}},

        {"url": "http://120.78.128.25:8766/futureloan/member/login",
         "method": "post",
         "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
         "data": {"mobile_phone": "1811", "pwd": "123"},
         "expected": "hello world"},
    ]


test_data = ExcelHandler(r"d:\cases.xlsx").read('Sheet1')
print(test_data)


@ddt.ddt
class TestLogin(unittest.TestCase):

    # def setUp(self) -> None:

    # 前置条件当中
    # 每一个测试用例方法执行之前都会运行的代码
    def setUp(self):
        pass

    def tearDown(self):
        print("测试用例执行完毕。")

    @ddt.data(*test_data)
    # 将 *test_data 当中的一组测试数据 赋值到 data_info 这个参数
    def test_login(self, data_info):
        res = RequestsHandler().visit(data_info['url'],
                                      data_info['method'],
                                      json=data_info['data'],
                                      headers=data_info['headers'])

        self.assertEqual(res, data_info['expected'])


if __name__ == '__main__':
    unittest.main()
    # test_login()

