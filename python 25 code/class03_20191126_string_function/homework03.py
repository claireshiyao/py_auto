# author by claire
# 1、删除如下列表中的"矮穷丑"，写出能想到的所有方法
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# 方法1：remove
# info.remove("矮穷丑")
# print(info)
# 方法2：pop
info.pop(3)
print(info)
# 方法3
del info[3]

# 2、现在有一个列表 li2=[1，2，3，4，5]，

# 第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
li2 = [1,2,3,4,5]
li2.insert(0,0)
li2.insert(4,66)
li2.extend([11,22,33])
print(li2)

# 第二步：对li2进行排序处理
# 正序处理
li2.sort()
print(li2)
# 倒序处理
li2.sort(reverse=True)
print(li2)

# 第三步：请写出删除列表中元素的方法，并说明每个方法的作用
# 删除指定的元素，remove()
# li2.remove(66)
# # 删除指定索引的元素，pop
# li2.pop(0)
# # pop不带参数，默认删除最后一个元素
# li2.pop()
# # 删除所有的元素clear()
# li2.clear()
# 从内存中直接清除，del
# del li2
# 从内存中直接清除指定索引的元素，del
# del li2[0]

# 3、有5道小题（使用列表操作完成）：
# a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
name = input("姓名：")
sex = input("性别：")
age = input("年龄：")
PersonalInfo = [name,sex,age]
print(PersonalInfo)
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
weight = input("身高：")
contact = input("联系方式：")
PersonalInfo.extend([weight,contact])
print(PersonalInfo)
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
PersonalInfo.remove(contact)
print(PersonalInfo)
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
nickname = input("花名：")
PersonalInfo.insert(1,nickname)
weight2 = input("请重新输入身高：")
PersonalInfo[4] = weight2
print(PersonalInfo)
# e, 你进一步添加自己的兴趣，至少需要 3 项。
hobby1 = input("兴趣1：")
hobby2 = input("兴趣2：")
hobby3 = input("兴趣3：")
PersonalInfo.append([hobby1,hobby2,hobby3])
print(PersonalInfo)

