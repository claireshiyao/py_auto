# 1.编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
# def func_weekdays():
#     list_match = ['退出', '周一', '周二', '周三', '周四', '周五', '周末', '周末']
#     while True:
#         weekday = int(input("请输入1-7中任意数字，输入0退出"))
#         if weekday == 0:
#             print("退出程序")
#             break
#         elif weekday in range(1, 8):
#             print(list_match[weekday])
#         else:
#             print("输入有误，请重新输入！")
# func_weekdays()

def func_weekdays(i):
    list_match = ['退出', '周一', '周二', '周三', '周四', '周五', '周末', '周末']
    if 1 <= i <= 7:
        print(list_match[i])
    else:
        print("输入有误，请重新输入！")

while True:
    i = int(input("请输入1-7中任意数字，输入0退出"))
    if i == 0:
        week = "退出程序"
        break
    else:
        func_weekdays(i)

# 2.列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
# 方法1：
list1 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
print(list(set(list1)))
# 方法2：
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


# 3.将两个变量的值进行交换（a = 100, b = 200）
# 交换之后，a = 200， b = 100， 使用函数。
# 定义函数
# 方法1：
def swap(a, b):
    tem = a
    a = b
    b = tem
    return a, b


print(swap(100, 200))


# 方法2：
def swap(a, b):
    a, b = (b, a)
    return a, b


print(swap(100, 200))


# 4.编写如下程序
# 尝试函数部分封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
def advice_BMI(weight, height):
    index_BMI = weight / height ** 2
    advice = None
    if index_BMI < 18.5:
        advice = '过轻'
    elif 18.5 <= index_BMI < 25:
        advice = '正常'
    elif 25 <= index_BMI < 28:
        advice = '过重'
    elif 28 <= index_BMI < 32:
        advice = '肥胖'
    else:
        advice = '严重肥胖'
    return advice


weight = float(input("请输入体重（单位：kg）："))
height = float(input("请输入身高（单位：m）："))
print(advice_BMI(weight, height))
