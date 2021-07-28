# #1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
price = input("购买金额:")
price1 = int(price)
if price1 >= 50 and price1 <= 100:
    discount = 0.1
    final_price = price1 * (1 - discount)
    print("折扣为{},最终价格为{}".format(discount,final_price))
elif price1 > 100:
    discount = 0.2
    final_price = price1 * (1 - discount)
    print("折扣为{},最终价格为{}".format(discount,final_price))
elif price1 > 0 and price1 < 50:
    discount = 0
    final_price = price1 * (1 - discount)
    print("折扣为{},最终价格为{}".format(discount, final_price))

# 老师答案
price = int(input("购买金额:"))
price_after = price
if 50 <= price <= 100:
    price_after = price * (1 - 0.1)
elif price > 100:
    price_after = price * (1 - 0.2)
print(price_after)


# 2、判断是否为闰年
year = input("年份:")
year1 = int(year)
if year1 % 4 == 0 and year1 % 100 != 0:
    print("{}年是闰年".format(year1))
elif year1 % 100 == 0 and year1 % 400 == 0:
    print("{}年是闰年".format(year1))
else:
    print("{}年不是闰年".format(year1))

# 老师讲解
year = int(input("年份:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("这是一个闰年")
else:
    print("这不是一个闰年")


# 3、使用遍历循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：
import random
for i in range(3):
    print("请按下面提示出拳:")
    print("石头[1] 剪刀[2] 布[3] 退出[4]")
    a = input("请输入要出的拳:")
    b = int(a)
    r = random.randint(1,3)
    if b >= 1 and b <= 3:
        if b == 1:
            if r == 1:
                print("您的出拳为：石头，电脑出拳：石头")
                print("平局")
                continue
            elif r == 2:
                print("您的出拳为：石头，电脑出拳：剪刀")
                print("您胜利了")
                continue
            else:
                print("您的出拳为：石头，电脑出拳：布")
                print("您输了")
                continue
        if b == 2:
            if r == 1:
                print("您的出拳为：剪刀，电脑出拳：石头")
                print("您输了")
                continue
            elif r == 2:
                print("您的出拳为：剪刀，电脑出拳：剪刀")
                print("平局")
                continue
            else:
                print("您的出拳为：剪刀，电脑出拳：布")
                print("您胜利了")
                continue
        if b == 3:
            if r == 1:
                print("您的出拳为：布，电脑出拳：石头")
                print("您胜利了")
                continue
            elif r == 2:
                print("您的出拳为：布，电脑出拳：剪刀")
                print("您输了")
                continue
            else:
                print("您的出拳为：布，电脑出拳：布")
                print("平局")
                continue
    elif b == 4:
        print("游戏结束")
        break

# 老师讲解
while True:
    choice = input("请输入猜拳：石头[1] 剪刀[2] 布[3] 退出[4]")
    if choice == '4':
        print("退出游戏")
        break
    import random  # (写文件最上方)
    computer_choice = random.randint(1, 3)
    if (computer_choice == 1 and choice == '3')
        or (computer_choice == 2 and choice == '1')
        or (computer_choice == 3 and choice == '2'):
        print("我赢了")
    elif computer_choice == choice:
        print("平局")
    else:
        print("失败")

# 4、求三个整数中的最大值（提示：三个整数使用input提示用户输入）
a = input("请输入第一个整数：")
b = input("请输入第二个整数：")
c = input("请输入第三个整数：")
a1 = int(a)
b1 = int(b)
c1 = int(c)
if a1 < c1 and b1 < c1:
    print("最大值为{}".format(c))
elif b1 < a1 and c1 < a1:
    print("最大值为{}".format(a))
elif a1 < b1 and c1 < b1:
    print("最大值为{}".format(b))

# 老师讲解1
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
max_num = a
if a < b:
    max_num = b
if max_num < c:
    max_num = c
print(max_num)

# 老师讲解2
a = 4
b = 7
c = 9
print(max(a,b,c))

# 老师讲解3
list_my = [a, b, c]
list_my.sort()
print(list_my[-1])

# 老师讲解4
max_num = list_my[0]
for i in list_my:
    if i > max_num:
        max_num = i
print(max_num)


# 5、分别使用for和while打印九九乘法表
# 提示：
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

# 方法1：for循环
for i in range(1, 10):
    for j in range(1, i + 1):
        k = i * j
        print("{} * {} = {}".format(j, i, k),end='\t')
    print("")

# 方法2：while循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        k = i * j
        print("{} * {} = {}".format(j, i, k), end='\t')
        j += 1
    i += 1
    print("")

# 老师讲解1：
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{} * {} = {}".format(j, i, j * i),end='\t')
    print()

# 老师讲解2：
for i in range(1, 10):
    for j in range(1, i + 1):
            print("{} * {} = {}".format(j, i, j * i),end='\t')
    print()


# 6、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 当中, 请把这 5 个人分别从 black_list 当中删除，最后 black_list 为空。
black_list = ['卖茶叶','卖面膜','卖保险','卖花生','卖手机']
num = len(black_list)
for i in range(num):
    black_list.pop(0)
    print(black_list)

# 老师讲解1
black_list = ['卖茶叶','卖面膜','卖保险','卖花生','卖手机']
for wx in black_list[:]:
    black_list.remove(wx)
    # index + 1
print(black_list)

# 总结
# for 循环修改列表
# 以后千万不要在for循环中直接修改列表
# 如果要修改，copy

# 老师讲解2
black_list = ['卖茶叶','卖面膜','卖保险','卖花生','卖手机']
while len(black_list) > 0:
    black_list.pop(0)
print(black_list)

# 7、选做：不需要提交，不需要提交，不需要提交哦。课上不讲解，课后发答案。
# 使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
