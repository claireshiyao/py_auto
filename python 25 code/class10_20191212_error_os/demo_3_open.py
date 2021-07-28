#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/12 20:51
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""
os, open 的作用：
自动生成测试报告

如何读取文件：
1, 打开文件。 内置函数 open()
open(path/文件名称，mode='r', encoding='编码')
2， 读取
3，(一定要) 关闭文件。  数据不对，或者写入内容不生效，文件无法再次被打开

mode:
1, 'r', 读取
2， ‘w’, 写入,  当已经存在这个文件的时候，原来文件的内容会被覆盖
3，‘a’ , 追加。


1, 'b', binary, 二进制。 图片，视频
2，‘t’,与b相对。




根据指定的编码格式读取。
编码是根据一定的规则讲计算机内容的机器字节码转化成人能看懂的字符喘 \x23\x23\x43\
编码，
解码,
"""
import os

# dir_name = os.path.dirname(os.path.abspath(__file__))
# xianren = os.path.join(dir_name, 'xianren.txt')
# #
# # # 编码n(xianren, en
# f = open(xianren , mode='rt', encoding='utf-8')
# print(f.read())
# # # 关闭
# # f.close()
#
#
# # 读取文件
# # 写入
# f = open(xianren, mode='at', encoding='utf-8')
# f.write('小马哥')
# f.close()
#
# f = open(xianren, mode='wt', encoding='utf-8')
# f.write('胡哥哥')
# f.close()
#
#
# # b
dir_name = os.path.dirname(os.path.abspath(__file__))
png_pic = os.path.join(dir_name, '1.png')

f = open(png_pic, mode='rb')
print(f.read())
f.close()







