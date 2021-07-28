# author by claire
# 一、请指出下面那些为可变类型的数据，那些为不可变类型的数据
# 1、 (11)  #   整型, 不是元组，不可变
# 2、 {11，22}  集合，可变
# 3、 ([11,22,33])  可变
# 4、 {"aa":111}    可变
# 可变类型：{11，22}、{"aa":111} ([11,22,33])
# 不可变类型：(11)、

# 二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
# 要求一：去除列表中的重复元素
li = [11,22,33,22,22,44,55,77,88,99,11]
set_a = list(set(li))
print(set_a)
# 要求二：删除 77，88，99这三个元素
li.remove(77)
li.remove(88)
li.remove(99)
print(li)

# #方法2:
# li.sort()
# li.pop(-1)
# li.pop(-1)
# li.pop(-1)
#
# #方法3：
# index_77 = li.index(77)


# 三、有下面几个数据 ，
# # t1 = ("aa",11)      t2= ("bb",22)    li1 = [("cc",11)]
# # 请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}
# # 要注意字典中元素的位置（使用python3.5以下的同学不用考虑位置）
t1 = ("aa",11)
t2= ("bb",22)
li1 = [("cc",11)]

# 方法1：
# t3 = {t1[0]:t1[1],li1[0][0]:li1[0][1],t2[0]:t2[1]}

# # 方法2：
# t3 = li1[0]  # ('cc', 11)
# list1 = [t1,t3,t2] # [('aa', 11), ('cc', 11), ('bb', 22)]
# print(dict(list1))

# # 方法3: 老师讲解
new_list = {}
t1_key = t1[0]
new_list[t1_key] = t1[1]
print(new_list)

new_list[li1[0][0]]  = li1[0][1]
print(new_list)

new_list[t2[0]] = t2[1]
print(new_list)

# 方法4：老师讲解
# my_tuple = (t1,li1[0],t2)
# #序列类型可转化为字典
# #[(key,value),(key,value)]
# print(dict(my_tuple))


