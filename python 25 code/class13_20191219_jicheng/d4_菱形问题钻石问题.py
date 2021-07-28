#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/19 21:03
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""
广度优先：
深度优先：

c3算法。

"""

class A:
    def play(self):
        print("a is playing")

class B(A):
    # def play(self):
    #     print("b is playing")
    pass

class C():
    def play(self):
        print("C is playing")

class D(B, C):
    # def play(self):
    #     print("d is playing")
    pass

d = D()

d.play()
# 查找顺序
print(D.__mro__)
