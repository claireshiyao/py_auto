#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


import json
import unittest

import yaml

from common.db_handler import DBHandler
from common.excel_handler import ExcelHandler
from common.helper import generate_mobile
from common.logger_handler import LoggerHandler
from common.requests_handler import RequestsHandler
from config.setting import config
from libs import ddt



# yaml 读取
from middleware.helper import save_token, Context

f = open(config.yaml_config_path, encoding='utf-8')
#
yaml_data = yaml.load(f, Loader=yaml.FullLoader)
print(yaml_data)

@ddt.ddt
class TestRecharge(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('invest')

    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=yaml_data['logger']['file'])

    def setUp(self):
        self.req = RequestsHandler()

        self.db = DBHandler(host=yaml_data['database']['host'],
                       port=yaml_data['database']['port'],
                       user=yaml_data['database']['user'],
                       password=yaml_data['database']['password'],
                       database=yaml_data['database']['database'],
                       charset=yaml_data['database']['charset'])

        # 登录
        # 结果
        save_token()    # 访问登录接口，得到 token 值和 member_id
        # save_loan_id()

        # self.token = Context.token
        # self.memember_id = Context.member_id



    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        """充值接口"""
        # 1， 替换 json 数据当中的 member_id,   #member_id#" 替换成 Context.member_id
        # 2， 访问接口， 得到实际结果
        # 3， 断言实际结果 == 预期结果

        token = Context.token
        member_id = Context.member_id

        # 查询数据库,  查询 member_id = member_id 的用户余额。
        sql = 'SELECT * FROM member WHERE id=%s;'
        user = self.db.query(sql, args=[member_id, ])
        before_money = user["leave_amount"]


        if "#member_id#" in test_data["json"]:
            test_data['json'] = test_data['json'].replace("#member_id#", str(member_id))

        # 错误的用户名  71025， +1，  -1，  + 2， 3，
        # if "*wrong_member*" in test_data["json"]:
        #     test_data['json'] = test_data['json'].replace("*wrong_member*", str(member_id + 1))

        # 充值
        # 正则表达式。非常非常难，主要难得记。



        print(test_data)

        # 读取excel当中的 headers, 得到字典
        headers = json.loads(test_data['headers'])
        # 添加 Authorization 头信息
        headers['Authorization'] = token

        # 得到实际结果
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['json']),
                             headers=headers)

        # 断言 1：
        self.assertEqual(res['code'], test_data['expected'])
        # 第二次断言：成功用例需要进行数据库校验。 金额
        # 判断是否为成功用例，如果是成功用例，校验数据库。
        # if test_data["tag"] == "succeess":
        if res['code'] == 0:
            # 查看数据库结果，  充值金额 + 充值之前的余额 ==  充值之后的金额
            money = json.loads(test_data['json'])['amount']

            # self.new_db = DBHandler(host=yaml_data['database']['host'],
            #                     port=yaml_data['database']['port'],
            #                     user=yaml_data['database']['user'],
            #                     password=yaml_data['database']['password'],
            #                     database=yaml_data['database']['database'],
            #                     charset=yaml_data['database']['charset'])


            # 获取充值之后的余额
            # sql = 'SELECT * FROM member WHERE id=%s;'
            # after_user = self.new_db.query(sql, args=[member_id, ])
            # after_money = after_user["leave_amount"]
            # self.new_db.close()

            sql = 'SELECT * FROM member WHERE id=%s;'
            after_user = self.db.query(sql, args=[member_id, ])
            after_money = after_user["leave_amount"]

            self.assertEqual( before_money - money ,   after_money )
            # 其他的断言




