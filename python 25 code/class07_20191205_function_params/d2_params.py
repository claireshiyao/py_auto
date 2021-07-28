# author by claire

def dalao(name, money, food):
    print("恭喜{}拿到了一个{}的offer".format(name, money))
    return

dalao('xsy', '20k', 'fruit')
# 函数的定义和函数的调用，参数要一一对应。
# 形式参数要赋值 = 实际参数
# 位置参数：形式参数和实际参数要根据位置（顺序）一一赋值。

# 位置：position

# 关键字参数
# 默认参数
# 位置参数的问题，要求严格，一旦参数多了，

# 标记，关键字参数，给实际参数赋值给形式参数
# 关键字参数：1. 换顺序 2. 可以部分作为关键字参数，部分作为位置参数。
dalao(name='xsy', money='40k', food='海鲜')
dalao(money='40k', name='xsy', food='海鲜')
dalao('xsy', money='40k', food='海鲜')
# 不可以：dalao( money='40k', food='海鲜，'xsy')
# TODO:关键字参数必须放到位置参数的后面

# 默认参数：可以少传参数
def dalao(name, money, food='榴莲'):
    print("恭喜{}拿到了一个{}的offer".format(name, money))
    print("{}最喜欢吃{}".format(name, food))
    return
# food重新赋值了
dalao('xsy', '20k', food='雪糕')
# 当函数定义的时候有默认参数，在调用的时候，这个具有默认参数可以不传实际参数，使用默认参数作为实际参数。
# 可以少传参数。
# 函数在定义的时候可以复杂，在调用的时候要简单。（好记，少传参数）
# 默认参数也必须要放到位置参数的后面
dalao('xsy','20k')

# 默认参数：对于形参
# 关键字参数：函数调用
