# 如果a 的类型是整型，那我打印我是大佬
# 如果a 的类型是float，那我就打印我是菜鸟
# 否则我就打印我要学python

# 运算
# python 遇到冒号要缩进
# if (条件表达式)
#     条件语句
# 只会进入符合条件的，其他分支就不会执行了
a = 1
print(type(a))
# if (type(a) == int and 'hello' == "hello"):
#     print("我是大佬")
# elif type(a) == float:
#     print("我是菜鸟")
# elif type(a) == str:
#     print("我是字符串")
# else:
#     print("我要学python")

# if type(a) == int:
#     print("大佬")
# if a == 1
#     print("菜鸟")
# else:
#     print("学python")  # 大佬，菜鸟都打印

if type(a) == int:
    print("大佬")
    if a == 1:
        print("菜鸟")
    else:
        print("学python")  # 大佬，菜鸟都打印
        if a == 4:
            print("4")
            # 打印大佬，菜鸟，后面不会执行、

# pass，冒号语句块里不执行任何东西,pass
if a == 1:
    pass
else:
    print("hello")
print("end")

