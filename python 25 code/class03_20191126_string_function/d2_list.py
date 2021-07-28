# author by claire

# 列表，存储很多数据
# 变量：存储数据

# boy = '晓峰'
# boys = ['a','b',3,['c','d'],'e']
# # 如果想取出其中的某个元素，通过索引获取。
# print(boys[2])
# # 获取多个，切片
# print(boys[2:3])  #[3]
# # 如果子元素中是列表，继续通过索引获取，切片也可以。
# print(boys[-2][0:])  #['c', 'd']

boys = ['a']
# 添加新的元素，一次只能添加一个，添加到最后
new_boy = boys.append('b')
print(boys) #['a', 'b']
# append() 返回None
print(new_boy) #None

#添加多个
boys.extend(['c','d','e','f'])
print(boys)

#往指定位置添加，insert
boys.insert(0,'a2')
print(boys)

#删除
boys.remove('a2')
print(boys)
#删除指定的索引
#当pop没有参数，所有，默认最后一个
boys.pop(0)
print(boys)
# 也可以取出pop的数据 a = boys.pop(0)

# 删除所有的元素clear()
# boys.clear()
# print(boys)   #[]

# #不要使用del，从内存中直接清除
# del boys
# print(boys)

# 修改
boys[2] = 'd1'
print(boys)

# index，获取索引
print(boys.index('d1'))

# 逆序
boys.reverse()
print(boys)

# sort 排序，通常对字母、数字进行排序
girls = ['ab','de','bc']
girls.sort()
print(girls)
# 倒序排序
girls.sort(reverse=True)
print(girls)


