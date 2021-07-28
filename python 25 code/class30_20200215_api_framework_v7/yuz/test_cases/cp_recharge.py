#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""注册相关测试用例"""
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
from middleware import Context, ctx
from middleware.login import login, save_token

f = open(config.yaml_config_path, encoding='utf-8')
#
yaml_data = yaml.load(f, Loader=yaml.FullLoader)
print(yaml_data)


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')

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
        user = save_token()
        # self.token = Context.token




    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        #
        if '#member_id#' in test_data['json']:
            test_data['json'] = test_data['json'].replace("#member_id#", str(ctx.member_id))

        headers = json.loads(test_data['headers'])
        headers['Authorization'] = ctx.token

        a = ctx

        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['json']),
                             headers=headers
                             )



        self.assertEqual(res['code'], test_data['expected'])



