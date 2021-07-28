# 1. 将用户输入的所有数字相乘之后对20取余数，用户输入的数字个数不确定
def cal(*args):
    """将用户输入的所有数字相乘之后对20取余数"""
    num = 1
    for value in args:
        num *= value
    mod = num % 20
    return mod


def main():
    numbers = input("请输入需要计算的数字（以逗号分隔）:")
    list_num = numbers.split(",")
    new_list = []
    for i in list_num:
        new_list.append(int(i))
    res = cal(*new_list)
    print("输入的所有数字相乘之后对20取余数为{}".format(res))


main()

# 2. 编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def func1(*args):
    """检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回"""
    for i in args:
        length = len(i)
        if length > 2:
            return i[:2]
        else:
            return i
res = func1([1, 2, 3, 4])
print(res)

# 3. 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
def func2(*args):
    if str1 not in dict1.values():
        dict1["name2"] = str1
    return dict1


str1 = "xsy2"
dict1 = {"name": "xsy", "age": 18}
print(func2(*str1, *dict1))

# 4. 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
def calculator(a, b):
    if i == 1:
        num = a + b
    elif i == 2:
        num = a - b
    elif i == 3:
        num = a * b
    elif i == 4:
        num = a / b
    return num


i = int(input("请选择【1】加 【2】减 【3】乘 【4】除 "))
print(calculator(1, 3))

# 5. 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
# 编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
def join_team(gender, age):
    """指出是否可以加入球队"""
    if (15 <= age <= 22) and (gender == "女"):
        return '可以加入球队'
    else:
        return '不可以加入球队'


def main():
    i = 0
    sum = 0
    while i < 10:
        gender = input("性别：")
        age = int(input("年龄："))
        out = join_team(gender, age)
        print(out)
        if out == '可以加入球队':
            sum += 1
        i += 1
    print("满足条件的总人数为：{}".format(sum))


main()
