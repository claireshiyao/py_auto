# author by claire
'''
def func_name(params1, params2): #形式参数
    # 函数体
    # 函数体里的内容在外部无法查看
    return value
'''


def dalao(name):
    new_name = 'DALAO' + name
    return new_name
    # 函数体里面程序遇到return就终止，不会再往下面运行。
    print("xsy是大佬")


new = dalao('xsy')
print(new)


def get_bmi(height):
    if height > 185:
        return '高'
    print("不是高富帅")
    if height < 34:
        return '矮'
    print("不是矮矬穷")
    return '普通人'
    print("普通人的生活也很好")  # 不管什么条件，该句永远不会执行


print(get_bmi(190))  # 打印高
print(get_bmi(170))  # 打印高富帅，矮矬穷


a = 4
if a < 3:
    print("hello")
else:
    pass
print("正常")