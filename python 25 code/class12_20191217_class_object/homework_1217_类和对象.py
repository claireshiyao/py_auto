


"""
1、实现一个手机类，并实例化你的手机。

要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。

尽量多的获取不同属性和使用不同的功能。
"""

# 属性：是否是所有的手机都一样

class Mobile:
    # 类属性
    if_capture = ''

    def __init__(self, brand, model, color):
        self.brand = brand
        self.module = model
        self.color = color

    def call(self, phone_num):
        return '我正在打电话 给{}'.format(phone_num)

    def send_msg(self, phone_num):
        return '正在打电话'



# mobile = Mobile('华为', 'p30', '黑色')
# #
# # print(mobile.color)


#
#
# class MobilePhone(object):
#
#     def __init__(self, band, model):
#         self.band = band
#         self.model = model
#
# #
#     def call(self, phone_number):
#         print('呼叫电话号码{}'.format(self.phone_number))
# #
#     def send_message(self,phone_number, sms_content, *args):
#         # TODO ： 不要一个 *args 就完了。
#         return f'给 {phone_number}发送内容：{sms_content}'
#
#     def listen_music(self, music_name):
#         return f'正在播放歌曲：{music_name}'




# Q2：灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息
# object ==> 对象

# 总结：1， 如果你不清楚到底是类属性还是实例，那么先给他做成实例。

#
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, food_name='美味的'):
        print('一只叫{} 的猫，正在吃美味的食物'.format(self.name))

    def drink(self, drink_name='矿泉水'):
        print(f'一只叫{self.name}的猫，正在喝可口的饮料')


tom = Cat()




# Q4: 编写如下程序

# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。

# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。

# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant(object):

    def __init__(self, name, cooking_type):
        self.restaurant_name = name
        self.cooking_type = cooking_type
        # self.cooking_type = kargs

    def describe_restaurant(self):
        # 类里面去获取实例的属性 self.属性名称
        print('本饭店叫{}，拥有的美食种类有{}').format(self.restaurant_name, self.cooking_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name}正在营业')

#
res = Restaurant("饭店名", ['红烧肉', '茄子', '叫花鸡'])
print(res.cooking_type)
