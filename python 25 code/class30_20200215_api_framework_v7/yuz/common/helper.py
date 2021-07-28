#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import random


def generate_mobile():
    """随机生成一个手机号码。。    1[3,5,8,9] + 9"""
    phone = '1' + random.choice(["3", "5", "7", "8", "9"])
    for i in range(9):
        num = random.randint(1, 9)
        phone += str(num)
    return phone

if __name__ == '__main__':
    print(generate_mobile())

