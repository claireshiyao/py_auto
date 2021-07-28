#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/12 21:43
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""
异常：程序无法按照预计结果开始走，
一但程序报错了，程序将停止运行。

try:
    我要执行的可能出现错误的代码
    当没有出现错误，那么try 就会执行完
    一单出现错误，立即跳到 except 里面
except:
    出现异常以后要运行的代码

"""

num1 = input("请输入数字1：")
num2 = input("请输入数字2")

try:
    print("hello")
    print(num1 * num2)
    print("world")
except:
    # 异常捕获 catch, 如果你出现错误，那么你就按我说的做
    print("这里有一个 bug")
    try:
        1 / 0
    except:
        print("1 不能 / 0")
    print("finish")

print("程序还在执行吗？？？？")