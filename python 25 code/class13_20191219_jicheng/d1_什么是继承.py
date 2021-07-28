"""
1,  类和对象的定义
2， 类和对象的使用
3， 属性，类属性，实例属性。 类属性=类变量， 实例属性=实例变量
4， 方法。 实例方法，静态方法，类方法。


类的继承
1， 功能机， 智能手机
是否，phone 里面所有的属性和方法， smartphone 都可以使用。
Phone >>>>  SmartPhone  phone 是父亲

如何继承
class 类名(父类名):
    pass

继承以后，子类可以使用父类的所有的属性和方法。
如果父类和子类具有相同的方法和属性，子类会使用自己的方法和属性。 重写
"""

class Phone:

    recharge = True

    def call(self):
        print("正在打电话")

    def send_msg(self):
        print("发送短信")


class SmartPhone(Phone):

    # def call(self):
    #     print("正在打电话")
    #
    # def send_msg(self):
    #     print("发送短信")

    def call(self):
        self.caputure_video()
        print("智能手机正在打电话")

    def caputure_video(self):
        print("正在视频")


smart = SmartPhone()
smart.call()
print(smart.recharge)



# class Phone:
#     # 如果你不自己定义一个 __init__
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def call(self,  record=True):
#         if record == True:
#             self.record()
#         print("正在打电话")
#
#     def record(self):
#         print(" {} 正在进行录音".format(self))
#
#     def __repr__(self):
#         """返回对象打印出来的效果。名字固定用法"""
#         return self.model