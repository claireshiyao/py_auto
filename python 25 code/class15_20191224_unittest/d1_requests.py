#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
模块导入：
内置模块： python 自己内部写好的模块
自己写的模块：
别人写的模块：第三方


requests 仓库, 安装。
pip install requests
"""

# 导入 requests
import requests

# 访问一个 url 接口 地址, 发送一个 get 请求
# url = 'http://api.github.com'
# res = requests.get(url)
#
# print(res.text)    # <Response [200]>

# 如何传递参数，如何修改请求头，token
headers = {"token": "123", "username": "yuze"}
url = 'http://localhost:5000/login'


# 如何传递参数 ， 位置参数，或者关键字参数 params，  通过？ 也就是 querystring, 查询字符串的形式传递。
data = {"username": "xianren", "pwd": "123456"}

#
res = requests.get(url, params=data, headers=headers)