#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/5 20:55
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


def dalao(name, money, food):
    print("恭喜 {} 拿到了一个 {} 的 offer.".format(name, money))
    return


dalao('李七七', '30k', '辣条')
# 函数的定义和函数的调用，参数要一一对应
# 形式参数要赋值 = 实际参数
# 形式参数和实际参数是 一个萝卜一个坑，
# 位置参数：形式参数和实际参数要根据位置（顺序）一一赋值。

# 位置，postion
# 编程，函数的参数传递位置要保持一致。
dalao('30k', '李七七', '辣条')


# 关键字参数
# 默认参数
# 位置参数的问题，要求严格，一旦参数多了，

# 帖个标记，关键字参数. 给实际参数赋值给形式参数
# 关键字参数的好处：1，换顺序， 2， 可以部分作为关键字参数，部分做位置参数
dalao(name='小马哥', money='50k', food='海鲜')
dalao(money='50k', name='小马哥', food='鸡腿')

dalao('小马哥', food='鸡腿', money='50k')

# 不可以。 位置参数跟在关键字参数的后面，所以报错了。
# 关键字参数必须放到位置参数的后面
# dalao(food='鸡腿', money='50k', '小马哥')

dalao('小马哥', '40k', food='海鲜')


# 默认参数： 作用在于：可以少传参数

def dalao(name, money, food='榴莲'):
    print("恭喜 {} 拿到了一个 {} 的 offer.".format(name, money))
    print("{} 最喜欢吃 {}".format(name, food) )
    return

# food = '榴莲',  food = '哈根达斯'
dalao('阿花', '25k', food='哈根达斯')

# 当函数定义的时候有默认参数，那么在调用的时候，这个具有默认参数可以不传实际参数，使用默认参数作为实际参数。
# 可以少传参数了，

# 函数在定义的时候可以复杂，在调用的时候要简单，（好记，少传参数）
# 默认参数也必须要放到位置参数的后面
dalao('阿花', '25k')

# 默认参数和关键字参数的区别。
# 默认参数是对于形参，函数定义的时候， 关键字参数对函数调用



