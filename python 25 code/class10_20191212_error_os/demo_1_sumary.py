#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/12 19:59
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""模块导入

模块如何导入
1， from 包.包.模块 import 函数名，类名，变量名
第一个包是项目目录下开始的，

2, from 包.包.模块 import 函数名，类名，变量名 as 别名
别名的作用：
1， 避免和其他名称重复
2， 名称过长

3, from 包.包 import 模块名
3.5, from 包.模块 import * (通配符，所有的)

4， import 包.模块 as
"""

# from class_10_file_handler.module_1 import run
# run()

# from class_10_file_handler import module_1
# module_1.run()

# * 用法
# 为什么不建议用 *， 导入非常混乱，很容易造成名称冲突，所以强烈不建议使用。
# from class_10_file_handler.module_1 import *
# run()


# if __..... 作用：自己定义好的函数或者类使用的。
# 如果你想直接执行某个 python 文件，那么就写一个 if ....
# main()

def demo_1():
    pass


def demo_2():
    pass


if __name__ == '__main__':
    pass