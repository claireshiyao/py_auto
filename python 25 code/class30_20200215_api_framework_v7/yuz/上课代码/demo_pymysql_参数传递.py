#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
python 操作数据库：
mysql, oracle, sqlserver, mongodb, access,

操作 MySQL 数据库，db-api, pymysql,

1， 建立连接， conn  = pymysql.connect()
2,  建立游标   cursor = conn.cursor()
3,  执行 sql, cursor.execute()
4,  获取结果   cursor.fetch...()
5,  关闭。

"""

import pymysql


# 建立连接
# TODO: utf-8   ===>  utf8,
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='120.78.128.25', port=3306,
                       user='future', password='123456',
                       charset='utf8', database='futureloan',
                       cursorclass=DictCursor)

# 游标， 数据库操作当中一个重要的概念。
cursor = conn.cursor()
# 执行sql语句
mobile = '13712341234'
# 传递参数的第一种方式：format， 不要用 format 传递数据；
# 2: args 参数  %s, 占坑符，，  args = 列表 或者元组
cursor.execute('select * from member where mobile_phone=%s and id=%s;', args=[mobile, 23 ])

user = cursor.fetchone()
print(user)



# 数据库操作：


