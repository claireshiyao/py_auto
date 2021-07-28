#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import json

# 字典：""
data = '{"mobile_phone":"13595271250","pwd":null}'

# a = eval(data)
# print(a)

# json 和 字典的转化尽量不要用 eval

# 使用 json 模块完成转化
# loads 表示把 json 字符串转化成字典
data_dict = json.loads(data)
print(data_dict)
# {'mobile_phone': '13595271250', 'pwd': None}

# 字典转化成 json
data_dict = {'name': 'yuz', 'pwd': None}
json_data = json.dumps(data_dict)
print(json_data)
# {"name": "yuz", "pwd": null}