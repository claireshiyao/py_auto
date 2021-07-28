# author by claire

tuple_a = ('a1','a2',['a3','a4','a5'])
# 不能修改元组元素tuple_a[2] = ['新列表']

tuple_a[2][0] = '新列表'
print(tuple_a)
# ('a1', 'a2', ['新列表', 'a4', 'a5'])
# 元组的不可变是相对的，不是里面所有的内容完全不能变。
# 只要看索引的前面是不是一个可变的类型

tuple_b = ('b1','b2',{'b3':'b03'})
# 索引前面是元组，代表要修改元组的元素，所以不能使用tuple_b[2]='hello'

tuple_b[2]["b3"]='b003'
print(tuple_b)  #字典可变
# ('b1', 'b2', {'b3': 'b003'})