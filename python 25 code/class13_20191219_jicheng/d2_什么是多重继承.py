"""
多重继承，子类可以同时继承多个父类，这些父类所有的特性（属性，方法）子类都可以使用。

class 子类名(父类1，父类2，父类3):
    pass


类名：    类名():    类名(object):
所有的类都是继承自 object 类的
所有的类都是 object 的子类
int str
"""
class Game(object):
    pass



class GamePlayer():

    def play_game(self):
        print("正在玩游戏")


class Phone:
    recharge = True

    def call(self):
        print("正在打电话")

    def send_msg(self):
        print("发送短信")


class MusicPlayer():
    def play(self):
        print("播放音乐")


class SmartPhone(Phone, MusicPlayer, GamePlayer):

    def call(self):
        self.caputure_video()
        print("智能手机正在打电话")

    def caputure_video(self):
        print("正在视频")


smart = SmartPhone()
smart.play()
smart.play_game()
