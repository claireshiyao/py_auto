#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
配置文件的几种方式：
1， py 文件存储的数据， 变量， 类；
2， yaml ,通用的。   1，冒号后面空格； 2， 缩进用 空格键， 不要使用 tab 键
3， ini, 文件，传统的。使用频率高，但是现在


为什么测试完接口还需要进行ui测试：
- 接口注重的是 服务端测试， 并不能测 前端显示

为什么测试了 ui, 还需要进行接口：
- 界面上没有问题：： 虽然说都是显示同一个答案，登录成功， ，服务器内部
- ui 有问题，定位问题，定位bug,


测试流程：
1， 需求分析
2， 测试计划
3， 测试用例
4， 用例评审
5， 用例执行
6， 测试报告

"""

import yaml

with open("python25.yaml") as f:
    yaml.load(f, Loader= yaml.FullLoader)




