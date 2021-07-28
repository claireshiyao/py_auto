#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
1， 单元测试框架： unittest
2, 什么是单元测试：函数， 类
3, 单元测试是谁去测试的， 开发测试，
4， 单元测试框架和我们的接口测试有什么关系，


如何判断结果: 断言， 判断预期结果和实际结果是否相等。
assert
"""

# 访问接口
import requests

url = 'http://120.78.128.25:8766/futureloan/member/login'
headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}

def visit(url, data, headers):
    res = requests.post(url, json=data, headers=headers)
    return res.json()


# 断言 1 + 1 == 2
# 断言，如果断言失败，抛出异常 AssertionError
# 如果成功， 继续运行
# assert 1 + 2 == 2
# print("assert finished")




