#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/12 21:34
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os

dir_name = os.path.dirname(os.path.abspath(__file__))
xianren = os.path.join(dir_name, 'xianren.txt')


f = open(xianren, encoding='utf-8')

# 只会读取一行
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# readlines() 得到的是一个列表
a = f.readlines()
print(a)
# for i in a:
#     print(i, end='')

"""读取机制：根据光标移动的。
seek()
"""

# 1 * 2
