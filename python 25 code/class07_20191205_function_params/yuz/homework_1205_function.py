
"""
1.编写如下程序

尝试函数部分封装：

a.用户输入1-7七个数字，分别代表周一到周日

b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”：

c.如果输入0，退出循环

d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

# 写注释，把思路写下来

"""

def main():
    """主流程"""
    pass


# main()


def get_week_name(num):
    """根据 num 的值，得到周几"""

    dict_week = {"1":"周一","2":"周二","3":"周三","4":"周四","5":"周五","6":"周末","7":"周末"}

    # if:
    # elif:
    # elif:
    # if num == '1':
    #     # print('周一')
    #     return '周一'
    # elif num == '2':
    #     return '周二'

    if num == '0':
        return 'break'
    elif num not in dict_week.keys():
        return "error"
    else:
        # dict_week['1']  '周一'
        return dict_week[num]


# def get_week_name(num):
#     if num == '1':
#         print("今天是周一")
#     elif num == '2':
#         print("今天")

def main():
    while True:
        num = input("请输入1-7七个数字：")
        # 根据 num 的值，得到周几（get_week_name(num) ）
        out = get_week_name(num)
        if out == "break":
            break
        elif out == "error":
            print("输入信息有误")
            continue
        else:
            print("今天是", out)

main()



"""
2.列表去重

将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素

set, 去重
"""
def deduple(my_list):
    # my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
    return list(set(my_list))
#
#
# # 方法二：
def deduple(my_list):
    new_lis = []
    for item in my_list:
        if item not in new_lis:
            new_lis.append(item)
            print("去除重复元素之后列表new_lis为：{}".format(new_lis))
    return new_lis

# a = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# deduple(a)



"""
3.将两个变量的值进行交换（a = 100, b = 200）

交换之后，a = 200， b = 100， 使用函数。
"""

def swap(a, b):
    return b, a

#
def swap2(a, b):
    # 3， 4
    #
    temp = a
    a = b
    b = temp
    return a, b


"""


4.编写如下程序

尝试函数部分封装：

输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数

a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8

b.根据BMI指数，给与相应提醒

低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
"""


#
#
# height = input('请输入身高：')
# weight = input('请输入体重：')
#
# def numify(my_str):
#     """把字符串转化成小数。"""
#     if my_str.isdigit():
#         return int(my_str)
#     if "." in my_str:
#         for e in my_str.split("."):
#             if not e.isdigit():
#                 break
#         return float(my_str)
#     return False

# #
# height_num = numify(height)
# weight_num = numify(weight)
#
# if height_num and weight_num:
#     bmi = get_bmi(height_num, weight_num)
#     print(bmi)
#     if not bmi:
#         print("输入数据有误")
#     elif bmi < 18.5:
#         print("过轻")
#     elif 18.5 <= bmi <= 25:
#         print("正常")
#     elif 25 < bmi < 28:
#         print("肥胖")
#     else:
#         print("严重肥胖")
# else:
#     print('数据错误')

def get_bmi(height, weight):
    return weight / height ** 2

def get_warning(bmi):
    """根据 bmi 的值，输出提示"""
    if  bmi < 18.5:
        return '过轻'
    elif 18.5 <= bmi <= 25:
        return "正常"
    elif 25 < bmi < 28:
        return '肥胖'
    else:
        return '过于肥胖'

def main_4():
    height = float(input('请输入身高：'))
    weight = float(input('请输入体重：'))

    # 根据 height 和 weight 计算 bmi
    # 1, 可以复用，2 可读性强，3， 代码更加简洁
    #  calc_bmi(height, weight)
    bmi = get_bmi(height, weight)

    # 根据 bmi 的值，输出提示
    print(get_warning(bmi))


main_4()

