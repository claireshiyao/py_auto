#!/usr/bin/env python3
#-*- coding:utf-8 -*-
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
f = open(config.yaml_config_path, encoding='utf-8')
#
yaml_data = yaml.load(f, Loader=yaml.FullLoader)
print(yaml_data)

@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

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

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_register(self, test_data):

        # 判断 test_data['json'] 如果出现了 #exist_phone#, 使用 generate_mobile
        # 随机生成一个手机号码？ 替换 #exist_phone#
        if '#exist_phone#' in test_data['json']:
            # mobile = generate_mobile()
            # 查询数据库，如果数据库当中存在该手机号，那么我们直接使用这个号码。。
            mobile = self.db.query('select * from member limit 1;')

            # {'id': 10020, 'reg_name': '管理员', 'pwd': '12345678', 'mobile_phone': '15950123654', 'type': 0, 'leave_amount': Decimal('50000.00'), 'reg_time': datetime.datetime(2019, 12, 24, 23, 32, 4)}, {'id': 11203, 'reg_name': '普通', 'pwd': '12345678', 'mobile_phone': '15950123655', 'type': 1, 'leave_amount': Decimal('12000.00'), 'reg_time': datetime.datetime(2019, 12, 24, 23, 43, 1)}
            if mobile:
            # 直接查询数据库，随机找一个，直接使用该号码替换
            # 替换
                test_data['json'] = test_data['json'].replace("#exist_phone#", mobile['mobile_phone'])
            else:
                # 随机生成一个鹅  13823456785， 数据库当中还是不存在。
                # 注册成功, 通过接口注册， 直接通过插入数据库
                pass

        if '#new_phone#' in test_data['json']:
            while True:
                gen_mobile = generate_mobile()
                # 查询数据库，如果数据库当中存在该手机号，那么我们再生成一次，直到不存在为止
                mobile = self.db.query('select * from member where mobile_phone=%s;', args=[gen_mobile])
                # 直接查询数据库，随机找一个，直接使用该号码替换
                # 替换
                if not mobile:
                    break

            test_data['json'] = test_data['json'].replace("#exist_phone#", mobile['mobile_phone'])


        # 访问接口，得到实际结果, 字符串？
        res = self.req.visit(config.host + test_data['url'],
                            test_data['method'],
                            json=json.loads(test_data['json']),
                            headers=json.loads(test_data['headers'])
                                    )
        # 获取预期结果  test_data['expected']
        # 断言
        # self.assertEqual(eval(test_data['expected'])['code'],  res['code']  )

        try:
            self.assertEqual(test_data['expected'], res['code'])
            # 写入 excel 数据
            self.excel_handler.write(config.data_path,
                                     'register',
                                     test_data['case_id'] + 1,
                                     9,
                                     '测试通过')

        except AssertionError as e:
            # 记录 logger
            self.logger.error("测试用例失败: {}".format(e))
            # 手动抛出异常，否则测试用例会自动通过
            self.excel_handler.write(config.data_path,
                                     'register',
                                     test_data['case_id'] + 1,
                                     9,
                                     '测试失败')
            raise e




        # 如果出现断言失败，要讲失败的用例记录到 logger 当中
        # AssertionError

        # 把实际结果写入 excel 文档
        # headers.item()



        
        
        

