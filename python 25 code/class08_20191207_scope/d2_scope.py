# author by claire

# 函数的相互调用
# 函数的作用域

def main():
    # name, offer定义在函数体里面
    name = "xsy"
    offer = '40k'

# print(name) #报错，未定义。
# print(offer)#报错，未定义。

main()

# 局部变量：函数体内定义的变量，只能在函数体里面生效。
# 全局变量：函数体外面的变量，可以在函数体里面使用。

name = '闲人'


def dalao():
    print("{} is dalao".format(name))


dalao()

# 变量的使用，局部，全局
# 不止要拿，还要改。


name = '闲人'


def dalao():
    name = 'andy'
    print("{} is dalao".format(name))  # 调用andy


dalao()
print(name)  #调用闲人

# 函数的参数是局部变量！
# id()查看某个值或者变量在内存中的地址。

# 全局变量和局部变量的修改

# 局部变量能在函数体当中修改吗？
# 全局变量能在函数体里面被修改吗？
# 如果想修改全局变量，告诉别人，经过别人的同意。

name = '晓峰'

def dalao():
    # name = 'xsy'
    # name = 'xsy2'
    global name
    name = name + '彼'
    print("{} is dalao".format(name))

print(dalao())  # 返回None
print(name)  # 晓峰彼

# global全局变量声明，但是现阶段不建议使用这个关键字
# global造成数据紊乱

# 内置函数：python自己定义的。
# print(), input(), len(),max(),type(),min(),id(),sorted()
# sum(),round()
# zip()后面讲
# range() 不是函数，是类class
# join()不是内置函数

# 获取帮助信息
# print(help(range))

# 枚举enumerate
for index, i in enumerate([1, 3, 5, 7]):
    print(index, i)
# 0 1
# 1 3
# 2 5
# 3 7

print("1 + 5")
print(eval("1 + 5"))  # 6
# eval()  脱字符串的衣服，把字符串转化为python代码
