

# 不定长参数
# 我不知道需要定义多少个参数。

def sum(a, b):
    total = 0
    c = total + a + b
    return c


def sum_total(a, b, *args, name='yuz', **kwargs):
    """**kwargs 表示接收多余的关键字参数"""
    # 函数体力 kwargs 是字典的形式接收多余的关键字参数
    print(args)
    print(kwargs)

other_info = {"hobby": "girl", "food": "辣条"}

# *
# 化妆
# hobby='girl', food='辣条'
# 函数外面可以用
sum_total(3, 4, name="feixu")


# 总结
# 函数的返回值 return,  return 后面是返回值，   return 语句之后的不生效，遇到 return 就终止
# 函数的参数。 位置参数： 一个萝卜一个坑
# 关键字参数： 好记，有标记； 2， 可以换顺序
# 默认参数：  可以少传参数。
# 注意： 顺序， 位置参数最前面，  关键字参数和默认参数是在后面

# 不定长参数。动态参数。 1， 位置参数， *args, *c, *随意   函数体和函数外面
#  2， 关键字，  **kwargs.   keyworld-arguments,   **kw


# 预告：函数的作用域， 导包 import

# qtranslate




