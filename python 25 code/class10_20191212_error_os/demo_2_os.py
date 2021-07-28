#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/12 20:16
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""如果你想是直接用别人已经写好的模块或者是包。


如果不是 python 内置的：
1， 放到项目下面，作为一个包或者模块；
2， lib / site-packages

os 模块是别人写好的，python 内置的。
主要处理系统相关的。

os.path 处理系统路径相关的


"""

import os

# pwd 显示当前文件路径
# 你在哪里运行的 python 指令，这个路径就是当前文件路径
# 每次会变，取决于你在哪里运行的 python
print(os.getcwd())

# 如果我们想每次得到的都一行，要用绝对路径
print(os.path.abspath(__file__))

# 获取文件的文件夹名称，dirname
a = os.path.dirname(os.path.abspath(__file__))

# 路径拼接， os.path.join()
print(os.path.join(a, 'yuze.txt'))
# cases.xlsx

# 创建文件夹 先得到 data 目录的绝对路径
# 创建文件一次建立一级
data_path = os.path.join(a, 'data')
# os.mkdir(data_path)

# 是否是一个文件夹
print(os.path.isdir(data_path))
print(os.path.isdir(a))

# 是否是一个文件
print(os.path.isfile(a))

# 路径是否真的存在
print(os.path.exists(data_path))

xianren_path = os.path.join(a, 'xianren')
print(os.path.exists(xianren_path))

# 判断 data 是否存在, 如果存在：pass, 如果不存在：创建一个

if not os.path.exists(xianren_path):
    os.mkdir(xianren_path)





