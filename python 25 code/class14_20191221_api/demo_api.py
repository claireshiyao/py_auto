#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

from flask import Flask

app = Flask(__name__)


@app.route("/login")  # 接口地址, @装饰器
def login():
    # 图像识别
    # 开门
    # 返回数据（天气），
    return "逆流已经登录成功"

# login()
# /login 地址和 login 函数绑定在一起
# 访问  /login 地址的时候， 函数会被调用

if __name__ == '__main__':
    app.run()
