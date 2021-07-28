#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
print('getattr')
"""
getattr : 获取属性 （动态获取某个属性的函数）

getattr(对象或者类名， 属性名称，当没有次属性的时候，需要提供的默认值)
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

iphone = Phone("apple")
# print(iphone.brand)

# 如果获取没有存在的属性，会报错。
# print(iphone.color)
# iphone.call()
# print(iphone.xianren)

# print(getattr(iphone, 'brand',  '华为'))

# iphone.xianren
# print(getattr(iphone, 'xianren', '大佬'))

# 类名.类属性      类名.实例属性 是错误的。
print(getattr(Phone, 'brand', 'huawei'))

print(getattr(Phone, 'recharge', '充电很强'))


