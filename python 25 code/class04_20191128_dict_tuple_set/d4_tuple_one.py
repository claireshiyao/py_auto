# author by claire
tuple_demo = ()
print(tuple_demo)  #()

#TODO:坑：1个元素的元组，不是一个元组，而是去掉括号以后的原始数据类型
# 如果想表示一个元素的元组，记得务必在元素后面加一个逗号。
tuple_demo2 = (1)
tuple_demo3 = 1
print(tuple_demo2)  #1
print(tuple_demo3)  #1
tuple_demo4 = (1,)  # 长度为1
print(tuple_demo4)  #(1,)

# 元组解包，需要一一对应
name1,name2 = ('1','2')
print(name1)
print(name2)
a,b = 3,4  #也可以a,b = [3,4]
print(a)
print(b)

family_name,name,*other = ('a','b','c','d')
print(*other)  #c d