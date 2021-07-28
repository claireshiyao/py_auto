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
    一旦出现错误，立即跳到 except 里面
except 异常类型（默认就是所有的类型， 语法错误除外） as e:
    出现异常以后要运行的代码
    e: 错误信息

有哪一些异常类型：
1，NameError, 名字错误，没有定义
2， IndexError

为什么不直接使用默认的捕获：
1， 不方便定位问题，
2， 不确定是什么原因造成的异常。
3， 一般不是使用默认的。而是会加入异常类型。

"""
num1 = 'a'
num2 = 'b'

try:
    print("hello")
    print(num1 * num2)
    print("world")
# except IndexError:
#     print("index error")
except Exception as e:
    # 异常捕获 catch, 如果你出现错误，那么你就按我说的做
    print("这里有一个 bug", e)
    print("finish")

# NameError
# print(abc)

# IndexError
# print(['a', 'b'][100])

# KeyError
# print({"a": "yuze"}['xianren'])


""""
os 模块， 记住用法。 os.path.abspath,  os.path.dirname()
os.mkdir
os.path.exists()

f = open(filename, mode='w', encoding="utf-8") 
f.close()
f.read()
f.readlines()
f.write()

异常处理：
try:
    ..
except 类型 as e:
    ...

print("其他的代码")
gbk,编码格式

"""