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

运行2，使用 python 去运行


断言结果：
1， . 表示通过 或者 pass
2， F False, 表示断言没有通过
3， E Error, 表示程序内部发生了错误。


执行顺序：
1， 根据 ascii 编码排序
2， 如果我们想手工调整测试用例的执行顺序，不同的字母前面加 数字。


pycharm 运行的注意事项：
1， 在空行处右击，执行整个模块
2， 在类名上， 执行单个测试类
3， 在方法明上， 执行单个测试用例
tips: 注意在指定的位置运行，空行的地方去运行。


setUp: 每次测试用例方法执行之前都会执行的方法。 前置条件
可以把测试数据放到 setUp 当中，

tearDown: 每次用例方法执行之后都会自动执行的方法。 后置条件。
过程：先执行 setUp, 然后执行 test_.... 测试用例方法， 最后执行 tearDown.

"""
import unittest

# from class_17_unittest.d3_unittest import visit
import requests


def visit(url, data, headers):
    res = requests.post(url, json=data, headers=headers)
    return res.json()


url = 'http://120.78.128.25:8766/futureloan/member/login'
headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}
expected = 'hello world'

# data = {"url": "http://120.78.128.25:8766/futureloan/member/login",
#         "headers" : {"X-Lemonban-Media-Type": "lemonban.v2"},
#         "data":{"mobile_phone": "18111111111", "pwd": "12345678"},
#         "expected": "hello world"
#         }



class TestLogin(unittest.TestCase):

    # 前置条件当中
    # 每一个测试用例方法执行之前都会运行的代码
    def setUp(self):
        print("正在准备测试数据")
        self.data = {"url": "http://120.78.128.25:8766/futureloan/member/login",
            "headers" : {"X-Lemonban-Media-Type": "lemonban.v2"},
            "data":{"mobile_phone": "18111111111", "pwd": "12345678"},
            "expected": "hello world"
        }

    def tearDown(self):
        print("测试用例执行完毕。")

    def test_login_2_success(self):
        # ?? 结果
        res = visit(self.data['url'], self.data['headers'], self.data['data'])
        # 预期结果
        self.assertEqual(self.data['expected'], res)

    def test_demo(self):
        pass

if __name__ == '__main__':
    unittest.main()