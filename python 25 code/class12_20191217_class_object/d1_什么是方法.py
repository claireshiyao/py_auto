#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/17 21:11
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

print("学习类和对象")

"""
方法：类里面的函数就叫方法
函数和方法

方法和属性的关系：
属性：特征，名词
方法：行为，动作，动词

方法和方法之间的相互调用。

带有 self 参数的方法叫做实例方法。
self 可以修改，站位子的。但是强烈不建议修改.

没有self 的方法：
1, 静态方法：self,
就是表示刚刚好放在类下面的普通的函数
只是为了方便管理我们的代码。
静态方法的调用： self.方法，    obj.方法
类名.方法

类方法：
cls， ===> 类本身， 类自己
类方法的调用：  类.方法名，   实例.方法名


类方法：主要用来做备用的构造函数。
实例方法：用得最多。
静态方法：有提示的时候, 

"""


class Dalao:
    favor = 'python'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(food):
        print("大佬喜欢吃 {}".format(food))
        return "大佬喜欢吃 {}".format(food)

    def offer(self, money, food):
        print("恭喜{}拿到 {} 的 offer".format(self.name, money))
        food = self.eat(food)
        Dalao.code()

    @classmethod
    def code(cls):
        dalao = Dalao('四叶草')
        print("我喜欢的编程语言是 {}".format(cls.favor))

    @classmethod
    def make_instance(cls, name):
        # Dalao(name)
        return cls(name)


dalao = Dalao("克拉美学")
dalao.offer('40k', '辣条')
# Dalao.eat('辣条')

dalao.code()
"""
总计：
什么是方法：类下面的函数，表示类或者对象的行为；

方法和方法之间如何调用？？和普通函数差不多：前面要加前缀， 

静态， 实例， 类方法
"""