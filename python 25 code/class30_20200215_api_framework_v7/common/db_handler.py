#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pymysql
import yaml
from pymysql.cursors import DictCursor

from class26_20200206_api_framework_v3.config.setting import config

from class26_20200206_api_framework_v3.common.read_yml import ReadYaml


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
    read_yaml = ReadYaml(config.config_path)
    yaml_data = read_yaml.open_yaml()
    # print(yaml_data)
    db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   database=yaml_data['database']['database'],
                   charset=yaml_data['database']['charset'])
    res = db.query("select * from member limit 2;", one=False)
    print(res)
