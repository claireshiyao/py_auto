# 什么是函数
# 小学4年级， y= x + 1  ==> f（x）= x + 1
# python f（x）= x + 1
# x, 自变量，

# python: x 叫做参数，  x + 1, 返回值。
# x : 输入，，， x+1，return 返回值

# f(x) = x + 1
# f(4)

# python 定义函数
def add(x):
    # x 是参数，输入， 吃东西
    y = x + 1
    # return 返回。
    # return 拉东西
    return y


# y = add(2)  # x=2
# # result = y = 3
# print(y)

print(add(2))


# print: 讲某一个值打印（输出）到屏幕上面
# return： 函数定义体力拉出来的东西，使用变量去接收函数的返回值。

# 函数的表示：
"""
def 函数名称(参数1, 参数2, 参数3):
    （缩进）函数体
     函数体里面的内容函数外面看得到吗？？  看不到
     外面能看到的。（函数名，参数值（输入）， 返回值（输出） ） 
     return 返回值
"""


def swap(x, y):
    """
    交换值。
    :param x:
    :param y:
    :return:
    """
    c = y + 1
    return  {"a": c, "b": x}




# 打印名片

name = 'yuz'
age = 12
gender = '女'

# print("""**************""")
# print("""名字：{}""".format(name))
# print("""年龄：{}""".format(age))
# print("""性别：{}""".format(gender))
# print("""**************""")
#
#
# # 十万行代码
# print("""**************""")
# print("""名字：{}""".format(name))
# print("""年龄：{}""".format(age))
# print("""性别：{}""".format(gender))
# print("""**************""")
#
#
# # 二十五万行代码
# print("""**************""")
# print("""名字：{}""".format(name))
# print("""年龄：{}""".format(age))
# print("""性别：{}""".format(gender))
# print("copyright")
# print("""**************""")
#
#
# name = '拼命姑娘'
# print("""**************""")
# print("""名字：{}""".format(name))
# print("""年龄：{}""".format(age))
# print("""性别：{}""".format(gender))
# print("copyright")
# print("""**************""")


# 函数的作用：存储一段可以重复执行的程序， 逻辑
# 1， 程序的使用更加简洁。
# 2, 可以重复使用
# 3， 代码具有可读性。一读函数名称和注释我就知道这段代码的作用。

# 变量的作用： 存储数据
def user_info(name, age, gender):
    """名片"""
    print("""**************""")
    print("""名字：{}""".format(name))
    print("""年龄：{}""".format(age))
    print("""性别：{}""".format(gender))
    print(""""copyright""")
    print("""**************""")
    return None # 省略

# fact_name = 'yuz'
# fact_age = 12
# fact_gender = '女'
# #
# yuz = user_info(fact_name, fact_age, fact_gender)
# print(yuz)


my_list = [12,3]
b = my_list.append('hello')

c = my_list.pop(1)
print(b)
print(c)

print(c + 1)

# 函数的定义的参数和 实际传入的参数个数要相等，而且顺序要相等。
# 函数定义的参数： 形式参数， x, y, z
# 函数调用，使用的参数， 实际参数， 实际的值， 1， 2， 3，

# 1, 什么是函数， 函数的定义和调用。  TODO: 函数体里面的内容只有当函数被调用的时候才会执行。
# 2， 函数的作用
# return