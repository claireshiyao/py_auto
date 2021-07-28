#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/19 19:57
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
"""
1.编写如下程序
编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。

getattr, setattr
"""
# class JiSuan
class Calculation(object):
    pass


class Calculation:
    def __init__(self, a, b):
        """"""
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def mulit(self):
        return self.a * self.b

    def division(self):
        # 特殊情况
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("b 不能为 0")

# 实例化
cal = Calculation(2, 0)
cal.division()

"""
2， 定义一个手机类， 具有打电话和录音的功能，打电话的时候可以录音，也可以不录音。
"""

# 可不可以不写 __init__
class Phone:
    # 如果你不自己定义一个 __init__
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def call(self,  record=True):
        if record == True:
            self.record()
        print("正在打电话")

    def record(self):
        print(" {} 正在进行录音".format(self))

    def __repr__(self):
        """返回对象打印出来的效果。名字固定用法"""
        return self.model


iphone = Phone('iphone8', '黄色')
# iphone.record()
iphone.call(False)

