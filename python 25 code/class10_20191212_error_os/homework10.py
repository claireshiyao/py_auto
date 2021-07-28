"""
1.编写如下程序
创建一个txt文本文件，来添加数据
a.第一行添加如下内容：
name,age,gender,hobby,motto
b.从第二行开始，每行添加具体用户信息，例如：
yuze,17,男,假正经, I am yours
cainiao,18,女,看书, Lemon is best!
c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "", "motto": "hehe"}
d.将所有用户信息写入到txt文件中之后，然后再读出
"""

# 方法一：

# import os
# person_info = [{"name": "xsy", "age": "18", "gender": "女", "hobby": "唱歌", "motto": "keep fighting!"},
#                 {"name": "fzm", "age": "19", "gender": "女", "hobby": "英语", "motto": "You can do it!"},
#                 {"name": "ckw", "age": "18", "gender": "女", "hobby": "画画", "motto": "Nothing is impossible!"}]
# title = tuple(person_info[0])  # ('name', 'age', 'gender', 'hobby', 'motto')
# title = ','.join(title)  # name,age,gender,hobby,motto
# first_person = tuple(person_info[1].values())
# first_person = ','.join(first_person)
# second_person = tuple(person_info[2].values())
# second_person = ','.join(second_person)
# third_person = tuple(person_info[2].values())
# third_person = ','.join(third_person)
#
# dir_name = os.path.dirname(os.path.abspath(__file__))
# info = os.path.join(dir_name, "person_info.txt")
# with open(info, mode='w+', encoding='utf-8') as f:
#     f.write(title.__str__()+'\n'+first_person.__str__()+'\n'+second_person.__str__()+'\n'+third_person.__str__())
# f.close()
# f = open(info, 'r', encoding='utf-8')
# print(f.read())
# f.close()

# 方法二：（没有实现题目要求）
person_info = [{"name": "xsy", "age": "18", "gender": "女", "hobby": "唱歌", "motto": "keep fighting!"},
                {"name": "fzm", "age": "19", "gender": "女", "hobby": "英语", "motto": "You can do it!"},
                {"name": "ckw", "age": "18", "gender": "女", "hobby": "画画", "motto": "Nothing is impossible!"}]
def get_values(infos):
    lines = ''
    for person in infos:
        list1 = []
        for value in person.values():
            list1.append(str(value))
        line1 = ",".join(list1)+'\n'
        lines += line1
    return lines


def main():
    with open("info.txt", mode='w+', encoding='utf-8') as f:
        f.write('name, age, gender, hobby, motto\n')
    with open("info.txt", mode='a+', encoding='utf-8') as f:
        f.write(get_values(person_info))
    with open("info.txt", 'r', encoding='utf-8') as f:
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
# 方法一:

# import os
#
# dir_name = os.path.dirname(os.path.abspath(__file__))
# future_loan = os.path.join(dir_name, 'futureloan.txt')
# f = open(future_loan, encoding='utf-8')
# lines = f.readlines()
# # ['url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\n', 'url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000\n']
#
# def lines_to_dict():
#     list1 = lines[0].replace('\n', '')
#     list1 = list1.split('@')  # ['url:/futureloan/mvc/api/member/register', 'mobile:18866668888', 'pwd:123456']
#     a1 = list1[0].split(':')  # ['url', '/futureloan/mvc/api/member/register']
#     b1 = list1[1].split(':')  # ['mobile', '18866668888']
#     c1 = list1[2].split(':')  # ['pwd', '123456']
#     d1 = [a1, b1, c1]
#     dict1 = dict(d1)  # {'url': '/futureloan/mvc/api/member/register', 'mobile': '18866668888', 'pwd': '123456'}
#
#     list2 = lines[1].replace('\n', '')
#     list2 = list2.split('@')
#     a2 = list2[0].split(':')
#     b2 = list2[1].split(':')
#     c2 = list2[2].split(':')
#     d2 = [a2, b2, c2]
#     dict2 = dict(d2)  # {'url': '/futureloan/mvc/api/member/recharge', 'mobile': '18866668888', 'amount': '1000'}
#
#     return [dict1, dict2]

# print(lines_to_dict())

# 方法二：(没实现要求)
import os

dir_name = os.path.dirname(os.path.abspath(__file__))
future_loan = os.path.join(dir_name, 'futureloan.txt')
f = open(future_loan, encoding='utf-8')
lines = f.readlines()

def lines_to_dict(line):
    info_dict = {}
    list = line.split('@')
    for i in list:
        j = i.split(':')
        info_dict[j[0]] = j[1]
    return info_dict

list_new = []
for line in lines:
    new = lines_to_dict(line.strip())
    list_new.append(new)
print(list_new)

"""
3.编写如下程序
优化去生鲜超市买橘子程序
a.收银员输入橘子的价格，单位：元／斤
b.收银员输入用户购买橘子的重量，单位：斤
c.计算并且 输出 付款金额
新需求：
d.使用捕获异常的方式，来处理用户输入无效数据的情况
"""
def payment_amount(price, weight):
    value = float(price) * float(weight)
    return value

if __name__ == '__main__':
    price = input("价格（元/斤）：")
    weight = input("重量(斤)：")
try:
    print(payment_amount(price, weight))
except Exception as e:
    print("数据无效", e)
