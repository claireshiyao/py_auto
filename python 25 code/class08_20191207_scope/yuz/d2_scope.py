#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/7 10:19
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# name = '小马哥'
# offer = '30k'
#
#
# def main():
#     # name, offer 定义在函数体里面？？还是在函数外面。
#     dalao_name = '深海的鱼'
#     dalao_offer = '40k'
#     # 预支详情，请你到这个目录去找
#     print(name, offer)
#
# # 没有
# print(name)
# print(offer)
# main()
#
# #
# print(name)
# print(offer)


# 函数体内定义的变量，局部变量。 局部变量只能在函数体里面生效。
# 函数体外面的变量，叫全局变量。 我能不能在函数体里面去使用？？？ 可以。

# name = '闲人'
#
#
# def dalao():
#     # 函数体里没有 name??
#     # name
#     print("{} is dalao".format(name))
#
#
# dalao() # 报错，你犯了很严重的错误。


# 变量的使用，局部，全局
# 不知要要，我还要改。

# name = '闲人'
# def dalao(name):
#     # name = 'andy'
#     print("{} is dalao".format(name))
#
# dalao() #
# print(name)

# 函数的参数是局部变量还是全局变量， 是局部变量。
# id() 查看某个值或者变量在内存到中的地址。




# 全局变量和局部变量的修改
# 局部变量能在函数提当中被修改吗？？？
# 局部变量能在函数体外面被修改吗？？？ 不能够
# 全局变量讷讷个在函数题里面被修改吗？？

name = '晓峰'


# 高能部分。
# local variable 'name' referenced before assignment
def dalao():
    # 此 name 非 彼 name
    # 找不找得到？？？ 局部变量有没有 name???
    # name 是全局变量？？？ 但是如果你要去修改，
    # 如果你想修改全局变量，告诉别人，静的别人的同意。
    global name
    name = name + '彼'

    print("{} is dalao".format(name))

# 不能获取局部变量， 更不用说修改了。
print(dalao())
print(name)

def lao_1():
    pass

def dalao_100():
    pass

# global 全局变量声明， 但是现阶段强烈不建议大家使用 global 这个关键
# global 造成数据紊乱

# 闲人大佬是我偶像
# range()

# 内置函数：python 自己内部放置的函数，python 自己定义，不需要我们去定义的函数。
# print(), input() len(), max(), type() , range(), min() , id(), sorted(), enumerate()
# eval(),
# sum()
# round()
# zip()
#  range() : 你喜欢看源码啊。
# 'str'.join() 不是内置函数

# 获取帮助信息
# min()
# print(help(range))


#
# for index, i in enumerate([1,7, 9, 5]):
#     print(index, i)


# eval() 脱字符串的衣服
print("1 + 5")
print(1 + 5)
print(eval("1 + 5"))

