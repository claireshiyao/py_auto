

# 不定长参数
# 我不知道需要定义多少个参数。

def sum(a, b):
    total = 0
    c = total + a + b
    return c


def sum_total(a, b, *args):
    """*args 表示剩下的多余的参数"""
    # 在函数定义里面，你可以用 *args 去接收多余的 位置参数。
    # 在函数定义里面， args 是元组。
    print(args)
    total = 0
    c = total + a + b
    for i in args:
        c += i
    return c

# 在函数的调用中，也可以用 *value
# 可以是列表，也可以是元组，  y: 序列类型 脱了衣服都一样
# {1,2, 3}

rest = {1,2,3}
# rest = [1,2,3]
# 脱衣服
print(sum_total(3,4, *rest ))
# print(sum_total(3,4, 1,2,3 ))





