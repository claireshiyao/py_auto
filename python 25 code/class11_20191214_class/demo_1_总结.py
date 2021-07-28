#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/14 9:31
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
print("yuz@")
"""
1, os
查找现在文件的绝对路径。

绝对路径：每次都要从最开始的地方查找。C:\data\jianguoyun\projects\python25\class_11_类和对象\demo_1_总结.py
相对路径：依据现有的路径进行查找，e.g.: C:\data\jianguoyun\projects\python25， 
demo_1_总结.py 相对于 C:\data\jianguoyun\projects\python25， 为：class_11_类和对象\demo_1_总结.py

# demo_1_总结.py 文件相对于 demo 这个文件夹，
. 表示当前层级，当前目录

liux, mac  /home/yuz/

2, 文件读写
f = open(file_path, mode='r', encoding='utf-8')
f.read()  # 读取文件， 根据光标读取内容。 seek()
f.readlines()   # 列表。
f.close() 

既想读取又想写入。
w+


3， 异常处理
try:
    执行
except Exception as e:  # Exception 通用， 具体： TypeError, NameError.
    print(e)
except TypeError as type_e:
    print()

"""

# 现在项目的名称：python25
# 根据现在的文件路径获取项目根目录路径

# import os
# dir_name = os.path.dirname(os.path.abspath(__file__))
# print(dir_name)
#
# # 找到dir_name 的文件夹
# root_path = os.path.dirname(dir_name)
# print(root_path)
#
# # 判断文件是否存在，如果存在你就创建
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
#
# file_path = os.path.join(dir_name, 'xiaofeng.txt')
# f = open(file_path, 'w+', encoding='utf-8')
# f.write('xiaofeng is big dalao')
#
# # 移动光标
# f.seek(0)
#
# print("读取", f.read())
# f.close()


try:  # 我试一下
    print(['1'][100])
    print({"name": "yuz"}["bala"])
    print("想喝小马哥玩游戏")
except (IndexError, KeyError):
    print("hello")
    # 下面抛出一个异常：我要告诉程序，报一个错误，终止这个程序
    raise NameError

# except KeyError:
#     print("key")
finally:
    # 无论你有没有报错，程序是否正常执行，都会执行的语句
    # 1 / 0
    print("本本生气了，大家来哄她")


# def add(a, b):
#     if not isinstance(a, int):
#         raise ValueError
#     return a + b
#
# print(add('a', 4))


# 文件操作：不管文件有没有正常打开，我都执行
import os
dir_name = os.path.dirname(os.path.abspath(__file__))
print(dir_name)

# 找到dir_name 的文件夹
root_path = os.path.dirname(dir_name)

file_path = os.path.join(dir_name, 'xiaofeng.txt')
# print(root_path)

try:
    file_path = os.path.join(dir_name, 'xiaofeng.txt')
    f = open(file_path, 'w+', encoding='utf-8')
    f.write('xiaofeng is big dalao')
except Exception as e:
    print(e)
finally:
    f.close()


# with f = open()
with open(file_path, 'w+', encoding='utf-8') as f:
    f.write('langlang')

