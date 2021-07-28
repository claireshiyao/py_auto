#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/5 17:36
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""函数。

def func_name(params1, params2):   # 形式参数
    # 函数体，
    # 函数体里的内容在外部无法查看
    return value   #
"""


def dalao(name):
    new_name = 'DALAO' + name
    return new_name

    # 函数体里面程序遇到 return 就终止，不会在往下面运行。
    print("吴孟是一个真的大佬")
    print("大家要向他学习")

# 函数定义以后需要调用才能执行里面的逻辑哦
new = dalao('吴孟')
print(new)


# return 注意
def get_bmi(height):
    if height > 185:
        return '高富帅'
    else:
        pass

    print("不是高富帅")
    if height < 34:
        return '矮矬穷'
    else:
        pass

    print('也不是爱从穷')
    return '普通人'
    print("做普通的人的感觉真好。")


# get_bmi(190)  # 没有输出到屏幕上。
# get_bmi(173)  # 没有输出到屏幕上。

a = 4
if a < 3:
    print("hello")

print("正常")