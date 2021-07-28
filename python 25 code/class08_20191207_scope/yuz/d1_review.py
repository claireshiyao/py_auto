#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/12/7 9:36
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


"""
1, return 1, 函数遇到 return 终止， return 后面紧跟着的值是函数的返回值
2，参数的种类： 1，位置参数，一个萝卜一个坑， 2， 关键字参数，对换顺序；3， 默认参数，节省所传的参数。少传参
3，不定长参数， *args, **kwargs.

函数：1，作用。  2， 对于学习 python 非常重要。不需要每次bd, cainiao

"""

import os


# os.path.exists()


# 函数的相互调用
# 函数的作用域

def main():
    # name, offer 定义在函数体里面？？还是在函数外面。
    name = '深海的鱼'
    offer = '40k'
    # 预支详情，请你到这个目录去找
    dalao(name, offer)



def dalao(name, money, food='榴莲'):
    print("恭喜 {} 拿到了一个 {} 的 offer.".format(name, money))
    eat(name, food)
    return


main()

def eat(dalaoname, food):
    print("{} 最喜欢吃 {}".format(dalaoname, food))
    return


# 1, 当所有的函数没有被调用之前，函数的定义顺序有关系？？
# 2， 一单某一个函数被调用，那么函数体体如果调用了其他的函数,那么这个其他的函数必须要在调用之前。

