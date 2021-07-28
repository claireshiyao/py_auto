# author by claire

"""
1. return, 函数遇到return终止，return 后面的值为函数返回值
2. 函数种类：
位置参数：一个萝卜一个坑
关键字参数：对换顺序
默认参数：节省所传的参数，少传参
3. 不定长参数：*args, **kwargs

函数：1. 作用
2. 对于学习python非常重要，不需要每次去百度
"""

import os

os.path.exists()  # ctrl + enter可以点击函数查看详情


# 函数的相互调用
# 函数的作用域

def main():
    # name, offer定义在函数体里面
    name = "xsy"
    offer = '40k'
    dalao(name, offer)


def eat(dalaoname, food):
    print("{}最喜欢吃{}".format(dalaoname, food))
    return


def dalao(name, money, food='榴莲'):
    print("恭喜{}拿到了一个{}的offer".format(name, money))
    eat(name, food)
    return


main()


# 1. 当所有的函数没有被调用之前，函数的定义顺序没关系
# 2. 一旦某个函数被调用，那么函数体如果调用了其他函数，那么这个其他的函数必须要在调用之前。
