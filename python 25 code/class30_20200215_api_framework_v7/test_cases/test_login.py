import json
import os
import random
import unittest

from class30_20200215_api_framework_v7.common.excel_handler import ExcelHandler
from class30_20200215_api_framework_v7.common.requests_handler import RequestsHandler
from class30_20200215_api_framework_v7.config.setting import config
from class30_20200215_api_framework_v7.libs import ddt
from class30_20200215_api_framework_v7.common.db_handler import DBHandler
from class30_20200215_api_framework_v7.common.logger_handler import LoggerHandler
from class30_20200215_api_framework_v7.common.random_phone_number import generate_phone_number
from class30_20200215_api_framework_v7.middlerware.read_yml import yaml_data


@ddt.ddt
class TestLogin(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('login')
    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=os.path.join(config.log_path, yaml_data['logger']['file']))

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
    def test_login(self, test_data):
        if '#exist_number#' in test_data['data']:
            mobile_num = yaml_data['user']['mobile_phone']
            pwd = yaml_data['user']['pwd']
            wrong_pwd = pwd + '1'
            if mobile_num:
                test_data['data'] = test_data['data'].replace("#exist_number#", str(mobile_num))
                test_data['data'] = test_data['data'].replace("#pwd#", pwd)
                test_data['data'] = test_data['data'].replace("#wrong_pwd#", wrong_pwd)

        if '#new_number#' in test_data['data']:
            while True:
                mobile_num = generate_phone_number()
                # 查询数据库，如果数据库当中存在该手机号，那么再生成一次，直到不存在为止。
                db_mobile = self.db.query("select * from member where mobile_phone = %s;", args=[mobile_num])
                if not db_mobile:
                    break
            test_data['data'] = test_data['data'].replace("#new_number#", mobile_num)

        res = self.req.visit(config.host + test_data['url'],
                    test_data['method'],
                    json=json.loads(test_data['data']),
                    headers=json.loads(test_data['headers']))
        try:
            self.assertEqual(res['msg'], test_data['expected_result'])
            self.excel_handler.write(config.data_path, 'login', test_data['id'] + 1, 10, 'PASS')
        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'login', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'login', test_data['id'] + 1, 9, f'{res}')


if __name__ == '__main__':
    unittest.main()

