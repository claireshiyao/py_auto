# author by claire

#列表：存储多个数据，获取单个元素，可读性不强。列表没有标记，key
#字典：存储多个数据，获取单个元素。

# 字典：有标记，key:value
# 表示方法：{key1:value1,key2:value2}
info = {"name":"xsy","age":18,"gender":"女","favor_movie":"年少有你"}
# 获取某个元素，通过key值获取
age = info["age"]
print(age)

# 字典表示
# key:value
# key:不可变类型，唯一
# list不能作为key值
# 字符串，元组不可变，一般使用字符串作为key值。
# 唯一：
xsy = {"name":"a","name2":"b"}
# print(xsy["name"])
# 获取长度
print(len(xsy))
# 字典是无序的数据类型，列表有序。
# 不能使用索引获取print(xsy[1])

# python3.6，第一次打印和第二次打印可能会不一样
# Python3.7,是按照添加顺序去显示。
# 内存当中，列表里所有的数据是存在一起的。
# 字典中每一个key,value存在不同地方。

# 字典是可变类型，增删改
# 添加字典元素
xsy["name3"]="c"
xsy["name4"]=["d","e"]
print(xsy)

#修改字典元素
xsy["name3"] = "c2"
print(xsy)
# 输入字典元素是双引号，打印出来自动使用单引号
# 字典里面双引号和单引号没有区别。
# 字典元素修改和添加的方式一样。
# 当key值不存在时，则为添加元素。
# 当key值存在时，则为修改元素。

# 删除字典元素
# 随机删除，没有参数，python3.7是删除最后一个。
# xsy.popitem()
# print(xsy)
# 删除指定的key
xsy.pop('name')
print(xsy)

# 其他的方法，清除
# xsy.clear()
# print(xsy)

print(xsy.items())
# 通过元组存储每组数据
# dict_items([('name2', 'b'), ('name3', 'c2'), ('name4', ['d', 'e'])])

print(xsy.keys())
# dict_keys(['name2', 'name3', 'name4'])
print(xsy.values())
# dict_values(['b', 'c2', ['d', 'e']])

# 1. 无序的，可变的类型
# 2. key:唯一，不可变类型，value:随意
# 3. 增删改，与列表差不多
# 4. items(),keys(),values()



