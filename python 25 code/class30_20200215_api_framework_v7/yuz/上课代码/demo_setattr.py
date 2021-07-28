#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


class Demo:

    member_id = 2
    token = 'abc'


if __name__ == '__main__':
    # print(Demo.memer_id)
    # print(Demo.memer_id)
    # 不想让他报错
    a = getattr(Demo, 'memer_id', '闲人')
    print(a)

