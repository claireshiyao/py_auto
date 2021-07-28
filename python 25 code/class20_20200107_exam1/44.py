# author by claire
"""
4.
编写如下程序
从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出
提示：
a.
1!等于
1
b.
2!等于
1 * 2
c.
3!等于
1 * 2 * 3
d.n!等于
1 * 2 * 3 * ... * n
"""

# num = int(input("请输入一个数字："))
# i = 1
# res = 1
# while i <= num:
#     res *= i
#     i += 1
# print("阶乘的结果是：{}".format(res))


def is_int(int_num):
    """ check whether int_num is integer! """
    if isinstance(int_num, str):  # 判断是否为字符串类型
        if int_num.isdigit():
            return True
        else:
            return False
    elif isinstance(int_num, int):  # 判断是否为整数类型
        return True
    else:
        return False


def count_factorial(one_num):
    """ count one_num's fatorial """
    result = 1
    if one_num < 0:
        print("{}为负数，没有阶乘！".format(one_num))
        return None
    elif one_num in (0, 1):
        return 1
    else:
        for i in range(1, one_num + 1):
            result *= i
        return result

input_num = input("请输入一个正整数：")
if is_int(input_num):
    input_num = int(input_num)
    print("{}的阶乘为：{}".format(input_num, count_factorial(input_num)))
else:
    print("输入的{}有误，请输入一个正整数!".format(input_num))
