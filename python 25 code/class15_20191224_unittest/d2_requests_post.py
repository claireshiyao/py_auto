#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

import requests

# 发送 post请求
url = 'http://localhost:5000/login'


# 如何发送 header 请求头
headers = {"dalao": "y", "sing_dog": "yuz"}

# 如何传递参数， params, query_string 的形式传递的。
data = {"username": "flybird", "admin": "bawa"}


# 传递参数2： 表单形式
# form_data = {"form_admin": "benben"}

json_data = {"json_data": "shenhai"}
# 传递参数3， json

res = requests.post(url, data, json=json_data, headers=headers, params=data)

# 获取相应文本，得到的数据类型， string
# print(res.text)

# 获取二进制形式
# print(res.content)

# json, 不是 json 的相应数据，就会报错， try: except
# json 得到的是 字典 数据类型。
print(type(res.json()))