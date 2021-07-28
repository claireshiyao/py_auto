#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pymysql
from pymysql.cursors import DictCursor


class DBHandler:

    def __init__(self, host, port,
               user, password,
               charset, database=None,
               cursorclass=DictCursor, **kw):
        """初始化"""
        self.conn = pymysql.connect(host=host, port=port,
                               user=user, password=password,
                               charset=charset, database=database,
                               cursorclass=cursorclass, **kw)
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        """查询语句"""
        self.cursor.execute(sql, args)
        # TODO: 提交事务
        self.conn.commit()
        # 获取结果
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        """关闭连接"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # 参数读取配置文件
    # print(yaml_data)
    db = DBHandler(host="10.10.2.225",
                   port=3306,
                   user="root",
                   password="Rojao@123",
                   database="szxn",
                   charset="utf8")
    res = db.query("select id from adv_schedule where adv_position_id = '1068421632208187442' and status = 4;", one=False)
    print(res)
