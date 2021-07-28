# author by claire

# 不定长参数：不知道需要定义多少个参数

def sum(a, b):
    total = 0
    c = total + a + b
    return c

def sum_total(a, b, *args):
    """*args表示剩下的多余的参数"""
    # 在函数定义里面，可用args接收多余的位置参数
    # 在函数定义里面，args是元组
    print(args)   # (5, 6, 7)
    total = 0
    c = total + a + b
    for i in args:
        c += i
    return c

# 在函数调用时，也可以用*value
# 可以是列表，也可以是元组，都是序列类型
# 不可以用集合，无序
rest = [1,2,3]
print(sum_total(3,4,*rest))







