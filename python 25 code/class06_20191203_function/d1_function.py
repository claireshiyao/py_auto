# author by claire

# python定义函数
def add(x):
    y = x + 1
    return y
result = add(2)
print(result)
# 也可以print(add(2))

# print：将某一个值打印到屏幕上面
# return: 函数定义输出的值，使用变量接收函数的返回值。

# 函数的表示：
"""
def 函数名称(参数1，参数2，参数3)
    函数体
    函数体里面的内容函数外面看不到。
    外面能看到的：函数名，参数值（输入），返回值（输出）
    返回值可以有多个
"""

def swap(x, y):
    """文档字符串"""
    c = y + 1
    return c, x
print(swap(6, 9))  # (10, 6)

# 打印名片
# name = 'xsy'
# age = 12
# gender = '女'
# print("""********""")
# print("""名字：{}""".format(name))
# print("""姓名：{}""".format(age))
# print("""性别：{}""".format(gender))
# print("""********""")

# 函数的作用：存储一段可以重复执行的程序
# 1. 程序的使用更加简洁，可以重复使用
# 2. 代码具有可读性，一读函数名称和注释我就知道这段代码的作用。。

# 变量：存储数据

def user_info(name, age, gender):
    """名片"""
    print("""********""")
    print("""名字：{}""".format(name))
    print("""姓名：{}""".format(age))
    print("""性别：{}""".format(gender))
    print("""********""")
    # return None #省略

fact_name = 'yuz'
fact_age = 12
fact_gender = '女'

yuz = user_info(fact_name, fact_age, fact_gender)
print(yuz)

my_list = [12, 3]
b = my_list.append('hello')
c = my_list.pop(1)
print(b)  # None   没有返回值
print(c) # 3

# 函数定义参数和实际传入的参数个数要相等，而且顺序要一致。
# 函数定义的参数：形式参数，x,y,z
# 函数调用，使用的参数，实际参数，实际的值，1,2,3

# 函数体里面的内容只有当函数被调用的时候才会执行。
# 函数作用
# return
