#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/14 10:58
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

print("hello")

"""
类的属性： 包括类属性和实例属性
类属性： 类集体的属性


类属性：所有成员都具备的特征
类里面表示的变量，就是属性
类属性又称为类变量

类属性获取：
1， 类名.属性名
2,  实例名称.属性名

类属性的修改：
类名.属性名 = 新的属性值


实例属性，实例变量：
类成员自己独有的特征。并不是每个类成员都具备的。
吉祥： 喜欢重口味， 男， 名字， 半夜写代码

如何去定义一个具体的对象：
具体的对象的定义，会在类的下面定义固定的函数名称： __init__ (__int__)

def __init__(self): 
    pass
    
如何去使用对象，初始化一个对象出来， jixiang
初始化对象的时候： 类名(参数1， 参数2， 参数3，)
初始化对象定义的时候： __init__(self, 参数1, 参数2， 参数3) 
总结： 具体对象使用的时候实际上是调用 __init__ 函数
TypeError: __init__() should return None, not 'str' 
返回值只能是 None, 不能是其他值。规定


如何表示实例属性：
实例属性的定义： __init__里面： self.属性名 = 属性值
实例属性的使用：实例名称（不是类名）.属性名 
实例属性的修改： 实例名称.属性名 = new属性值

self: 是在类的定义当中，表示实例自己。 我自己


"""

class BigBoss:
    # 类属性 （）
    code_level = "very good"
    hair = 'very thin'
    hobby = '宅'

    def __init__(self, name, food, gender):
        """定义具体的对象，初始化函数， 初始化方法。"""
        print(name)
        print(food)
        print(gender)
        print("我自己", self)
        self.dalao_name = name
        self.food = food
        self.gender = gender

    def hello_word(self):
        """实例方法"""
        print(self.dalao_name, "哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇")
        return '哭出来啦，是正常的。'

# 获取类属性
print(BigBoss.code_level)
print(BigBoss.hair)
print(BigBoss.hobby)

BigBoss.hobby = 'party'
print(BigBoss.hobby)

# print(hobby)
# 初始化对象， 实例化对象， 对象生出来
baby = BigBoss('jixiang', '辣条', 'nan' )
print("code level ", baby.code_level)

# 获取实例属性：
print(baby.gender)
# print(BigBoss.gender)

print("外部对象自己", baby)
print(baby.hello_word())

# baby = BigBoss.__init__(BigBoss,'jixiang', '辣条', 'nan')
# print("code level ", baby.code_level)

