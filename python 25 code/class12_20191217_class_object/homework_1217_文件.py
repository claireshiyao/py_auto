# name,age,gender,hobby,motto
# yuze,17,男,假正经, I am yours
# cainiao,18,女,看书,Lemon is best!


"""
1.编写如下程序

创建一个txt文本文件，来添加数据

a.第一行添加如下内容：

name,age,gender,hobby,motto

b.从第二行开始，每行添加具体用户信息，例如：

yuze,17,男,假正经, I am yours

cainiao,18,女,看书,Lemon is best!

c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：

person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "", "motto": "hehe"}

d.将所有用户信息写入到txt文件中之后，然后再读出
"""

person_info = [
    {"name": "yuze", "age": 17, "gender": "男", "hobby": "假正经", "motto": "I am yours"},
    {"name": "cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"},
]


def get_value_lines(info):
    """获取每一行的数据
    列表转化成行的字符串形式
    [{}, {}]  ==> name, yuz,
    """
    lines = ''
    for person in info:
        {"name": "yuze", "age": 17, "gender": "男", "hobby": "假正经", "motto": "I am yours"},
        line = []
        # ['yuze', 17, '男']
        for e in person.values():
            line.append(str(e))
        # 列表转化成字符串

        line_str = ','.join(line) + '\n'
        lines += line_str
    return lines


def main():
    """主体逻辑"""
    # os.path
    # ['name', 'age',]
    #
    # title = person_info[0].keys()
    with open('info.txt', 'w+') as f:
        f.write('name,age,gender,hobby,motto\n') # byte

    data = get_value_lines(person_info)
    with open('info.txt', 'a', encoding='utf-8') as f:
        f.write(data)
    with open('info.txt', 'r', encoding='utf-8') as f:
        print(f.read())

main()


"""
2.编写如下程序
有两行数据，存放在txt文件里面：
url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456

url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）

[{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
"""


# ['url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456', 'url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000' ]
# {'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'}

'url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456'

def convent_to_dict(line):
    # infos 是三个部分的列表

    # [url:/futureloan/mvc/api/member/register, 'mobile:18866668888' , 'pwd:123456']
    infos = line.split('@')
    info_dict = {}
    for info in infos:
        # info_list = ['url', ''/futureloan/mvc/api/member/register'']
        info_list = info.split(':')

        info_dict[info_list[0]] = info_list[1]
        # info_dict[key] = value
        # info_list['url'] = '/futureloan/mvc/api/member/register'
        # info_list['mobile'] = 'fowo2rof'
        # info_list['pwd'] = '1234'
    return info_dict


f = open('demo.txt', encoding='utf-8')
lines = f.readlines() # []
# f.read()
# 列表，字符串
new_lines = []
for line in lines:
    # line ===》 'url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456'
    new = convent_to_dict(line.rstrip())
    new_lines.append(new)
print(new_lines)

"""
3.编写如下程序
优化去生鲜超市买橘子程序
a.收银员输入橘子的价格，单位：元／斤
b.收银员输入用户购买橘子的重量，单位：斤
c.计算并且 输出 付款金额
新需求：
d.使用捕获异常的方式，来处理用户输入无效数据的情况
"""



# 输入橘子价格
# def main():
price = input('橘子价格：元/斤')
# 输入重量
weight = input('重量：斤')

try:
    price = float(price)
    weight = float(weight)
    print('总共需要付：{:.2f} 元'.format(price * weight))
except ValueError:
    print('请输入数字')
except :
    print("hello")

# main()


"""
3.编写如下程序

优化剪刀石头布游戏程序

a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）

b.电脑随机出拳

c.比较胜负，显示用户胜、负还是平局

新需求：

d.使用捕获异常的方式，来处理用户输入无效数据的情况

e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
"""


# def fight(my_choice):
#     import random
#     compute_choice = random.randint(1, 3)
#     if (my_choice, compute_choice) in [(1,2), (2,3),(3,1)]:
#         return 'win'
#     elif my_choice == compute_choice:
#         return 'peace'
#     return 'fail'
# #
# history_res = {'win':0, 'peace':0, 'fail':0}
# while True:
#     my_choice = input("请输入：")
#     try:
#         my_choice = int(my_choice)
#     except ValueError:
#         print("请输入数字")
#         continue
#     if my_choice == 4:
#         print("退出")
#         print("""
#         +++++++++++++++++++++++
#         战绩：
#         胜利{win},
#         平局{peace},
#         失败{fail}
#         ++++++++++++++++++++++++
#         """.format(**history_res))
#         # 没哟特别大的意义。
#         break
#
#     if my_choice in [1, 2, 3]:
#         res = fight(my_choice)
#         print("you {}".format(res))
#         history_res[res] += 1

