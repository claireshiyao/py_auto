#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/9/4 10:10
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


"""
1. 将用户输入的所有数字相乘之后对20取余数

用户输入的数字个数不确定
"""
# num = input("请输入数字，")
# num1 = input('请输入数字2：')

# 用 , 或者其他符号 *
import random

# nums = input("请输入数数字：用逗号隔开")
# # 保存多个数据，用列表存储
# # 字符串转化成列表， 用， 分割， split
# # change_nums_to_list()
# nums_list = nums.split(',')

# 取余数，逻辑稍微复杂一点的，封装成函数。 get_mod()
# 参数：1， 列表作为，2，不定长参数 *args

"""
# 什么时候封装函数？？
# 过程比较复杂，函数
# 多个地方会同时使用某一段程序，ctrL + c
# 1, 要不要参数？？有参数， 
# 2，函数封装返回值一般是确定的，根据参数确定的。
"""

def get_mod(args):
    """
    当你不知道有多少个参数的时候。

    获取输入值的乘积对20的余数

    :param args: 输入的所有值
    :return: 乘积对20的余数
    """
    # input
    product = 1
    for arg in args:
        # 1 * 第一个参数 * 第二个参数
        product *= float(arg)
    return product % 20

# input 放到函数里去
# get_mod() == get_mod()


# a = input("请输入数字，用逗号隔开")

# nums = a.split(',')  # 字符切割，得到的是一个列表
#
# print(get_remainder(*nums))

# print(get_mod(nums_list))

# 传入的参数类型是：： 列表

"""
2，编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回

阅读全文。。。三元表达式，三目运算。
"""

def remain_two(mlist):
    if len(mlist) > 2:
        return mlist[:2]
    return mlist
#
# print(remain_two([3,3,4]))
# 新知识： 三目运算，三元表达式。
def remain_two(mlist):
    return mlist[:2] if len(mlist) > 2 else mlist


"""

3， 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典

加入默认参数的情况， values()

# key 保持不可变类型，并且是唯一的。
"""

def add_element(e, mdict={}):
    # TODO: 不要 把 mdict={} 成默认参数
    if e not in mdict.values():
        # e 作为 key
        while True:
            key = random.randint(1, 90000000)
        # 判断 key 是否在 mdict.keys()
            if key not in mdict.keys():
                mdict[key] = e
                break
    return mdict

# key 永远都不可能重复， 时间点作为 key
# import time
# int(time.time())

#
# print(add_element.__defaults__)
# #
# print(add_element('hello'))
# print(add_element('hello1'))
# print(add_element('hello2'))

# 可变类型不要作为默认参数。 列表，字典

"""

4， 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
"""


methods = {'1':'+', '2': '-', '3': '*', '4': '/'}

def calc(x, y, method):
    # methods['1']  + - * /
    method_f = methods[method] #
    # 字符串转化成可以运行的 python 代码
    # 3 + 4
    return eval("{} {} {}".format(x,method_f,y))

method = input("运算符：")
print(calc(3.1, 4, method))

#
# print(calc(2,3, '1'))
# 代码好不好：逻辑清楚，容易理解。 扩展性强，通用性。
# python原理

"""

5， 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""

def join_team(age):
    """shifou 可以加入足球"""
    if 15 <= age <= 22:
        return True
    return False
#
def main():
    """主程序"""
    num = 0
    for i in range(3):
        age = input('输入年龄：')
        # 做
        if not age.isdigit():
            print("输入不合法。")
            continue
        joined = join_team(int(age))
        if joined:
            num += 1
    print(num)


