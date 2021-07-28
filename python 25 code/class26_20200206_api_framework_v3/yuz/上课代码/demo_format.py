#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


print(" a + b = {}".format('c'))

print("xiaofeng is {}".format({"name": "xiaofeng"}))


class DemoA:

    def __str__(self):
        return "demo aaaaaa"


print("demo a: {}".format(DemoA()))

# print("demo a", DemoA())