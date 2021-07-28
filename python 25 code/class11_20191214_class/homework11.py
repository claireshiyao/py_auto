# author by claire
"""
1、实现一个手机类，并实例化你的手机。
要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
尽量多的获取不同属性和使用不同的功能。
"""
class MobilePhone:
    brand = 'Huawei'
    model = 'P30'
    os = 'Android'
    def __init__(self, name, color, memory, pixel):
        self.name = name
        self.color = color
        self.memory = memory
        self.pixel = pixel
    def ring_up(self):
        return '可以打电话'
    def send_messages(self):
        return '可以发短信'
    def listen_to_music(self):
        return '可以听歌'
    def take_photos(self):
        return '可以拍照'

my_phone =  MobilePhone('xsy手机', 'black', '6GB', '1600万')
print(my_phone.name, '的品牌是', MobilePhone.brand)
print(my_phone.name, '的型号是', MobilePhone.model)
print(my_phone.name, '的颜色是', my_phone.color)
print(my_phone.name, '的内存是', my_phone.memory)
print(my_phone.name, '的像素是', my_phone.pixel)
print(my_phone.ring_up())
print(my_phone.send_messages())
print(my_phone.listen_to_music())
print(my_phone.take_photos())


"""
2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息
"""
class Cat:
    color = '灰色'
    age = '1岁'
    def __init__(self, name):
        self.name = name
    def eat_food(self):
        return '吃着美味的食物'
    def drink_beverages(self):
        return '喝着可口的饮料'
    def enjoy_life(self):
        return '非常享受的样子'
Tom = Cat('Tom')
print(Cat.color, '的', Tom.name, '猫，', '今年', Cat.age, ',', Tom.eat_food(), ',', Tom.drink_beverages(), ',', Tom.enjoy_life())


# 3.列举3个生活中类和对象的例子，用代码表示。
class Student:
    goal = '学习'
    curriculum = '英语'
    def __init__(self, name, age, gender, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby
    def school_life(self):
        return '每天要上八节课和晚自习'
    def school_excercise(self):
        return '每天6点半跑步和每天10点广播体操'
Zhang_San = Student("张三", 18, '男', '喜欢学英语')
print(Zhang_San.name)
print(Zhang_San.age)
print(Zhang_San.gender)
print(Zhang_San.hobby)
print("目标是", Student.goal, ",", "课程", Student.curriculum)
print(Zhang_San.school_life())
print(Zhang_San.school_excercise())

class Animal:
    appearance = '可爱'
    body_type = '小'
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def eat(self):
        return '喜欢啃骨头'
    def run(self):
        return '喜欢出去溜达'
Dog = Animal('旺旺', '白色')
print("白色的", Animal.body_type, "狗", Dog.name, "非常", Animal.appearance)
print(Dog.eat())
print(Dog.run())

class Bicycle:
    weight = '轻'
    size = '小'
    def __init__(self, name):
        self.name = name
    def ride_to_work(self):
        return '可以骑车去上班'
    def convenient(self):
        return '共享单车，随时可以骑行，不用担心堵车'
    def benefit_to_environment(self):
        return '节能环保'
Haluo = Bicycle('哈罗单车')
print(Haluo.name, Bicycle.weight, Bicycle.size)
print(Haluo.ride_to_work())
print(Haluo.convenient())
print(Haluo.benefit_to_environment())


"""
4.编写如下程序
创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
"""

class Restaurant:
    restaurant_name = "遇见湘"
    cooking_type = "湖南菜"
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def describe_restaurant(self):
        print("饭店名：", self.restaurant_name)
        print("美食种类：", self.cooking_type)
    def open_restaurant(self):
        print("饭店正在营业")
restaurant = Restaurant('遇见湘广州分店', 'Guangzhou')
print(restaurant.name)
print(Restaurant.cooking_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
