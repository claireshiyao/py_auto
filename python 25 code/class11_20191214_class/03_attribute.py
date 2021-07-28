# author by claire

"""
类的属性：包括类属性和实例属性
类属性：类集体的属性

类属性：成员都具备的特征
类里面的变量就是属性
又称为类变量
获取：
1) 类名.属性名
2) 实例名.属性名

可以修改属性：
类名.属性名 = 新属性值

实例属性，实例变量：
类成员自己独有的特征。

定义具体的对象：
初始化函数，初始化方法
在类的下面定义固定的函数名称：
__init__(self,参数1，参数2，参数3)

使用对象，初始化对象
类名（参数1，参数2，参数3）

总结：具体对象使用的时候实际上是调用init函数
init函数返回只能是None

实例属性的定义：self.属性名 = 属性值
实例属性使用：实例名称.属性名
实例属性修改：实例名称.属性名 = 新的属性值

self: 在类的的定义当中，表示实例自己


"""
class BigBoss:
    code = "excellent"
    hair = "thin"
    hobby = "games"
    def __init__(self, name, food, gender):
        print(name)
        print(food)
        print(gender)
        self.dalao_name = name
        self.food = food
        self.gender = gender
        # return None
print(BigBoss.code)
BigBoss.hobby = "singing"  # 属性修改了
print(BigBoss.hobby)

# 初始化对象，实例化对象
real_object = BigBoss('xsy', 'spicy food', 'girl')
print("code:", real_object.code)

# 获取实例属性
print(real_object.gender)
