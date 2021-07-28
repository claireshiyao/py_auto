#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
print('setattr')
"""
setattr : 设置属性 （动态获取某个属性的函数）

setattr(对象或者类名， 属性名称， 赋值的新值)
不管属性存不存在，都会赋值给新的值
"""

class Phone:
    recharge = True
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        self.xianren = '男'
        print("正在打电话")

    def send_msg(self):
        print("发送短信")


phone = Phone("apple")
phone.brand = 'xiaomi'

print(phone.brand)

# 获取属性，获取属性如果不存在，会报错。
# 修改 字典
phone.color = 'red'
print(phone.color)

setattr(phone, 'food', '辣条')
print(phone.food)

setattr(phone, 'brand', 'oppo')
print(phone.brand)

# 有时候我们提前不知道属性名称是什么，是从别的地方拿过来的
# 测试用例：Excel ， method:get,   url: ‘http://’

# class Visit:
#


