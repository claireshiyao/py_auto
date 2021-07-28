#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/12/19 20:58
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""
如果所有的父类都具有同样的一个方法
继承顺序的问题，1， 找自己； 2， 根据代码当中继承的父类的先后循序查找


"""

class GamePlayer():

    def play(self):
        print("正在玩游戏")


class Phone:
    recharge = True

    # def play(self):
    #     print("正在打电话")

    def send_msg(self):
        print("发送短信")


class MusicPlayer():
    def play(self):
        print("播放音乐")


class SmartPhone(Phone, MusicPlayer, GamePlayer):

    # def play(self):
    #     self.caputure_video()
    #     print("智能手机正在打电话")

    def caputure_video(self):
        print("正在视频")

smart = SmartPhone()
smart.play()
