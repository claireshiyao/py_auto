#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""

前置条件, 用例关联。

充值接口的测试：
前置条件：登录，我们得到充值需要的 token,  13712341234 ， member_id,


jsonpath 作用：
1， 操作方式更简单
2， 有通用的表达方式可以获取指定的值


Context 环境管理方式：
将项目当中要使用的所有的临时变量存储到 Context 当中，
使用 类属性的方式。


投资的前置条件：
1， 登陆，
2， 标的状态是竞标中，要从数据库当中查找出一个符合条件的标的。 可投标，
#  loan_id 是正在竞标当中的。
# sql, select * from loan where status=2;


投资验证：
1， 接口返回数据是否正确
2，余额是否正确。




"""
