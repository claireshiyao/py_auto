import json
import os
import random
import unittest

from class27_20200208_api_framework_v4.common.excel_handler import ExcelHandler
from class27_20200208_api_framework_v4.common.requests_handler import RequestsHandler
from class27_20200208_api_framework_v4.config.setting import config
from class27_20200208_api_framework_v4.libs import ddt
from class27_20200208_api_framework_v4.common.db_handler import DBHandler
from class27_20200208_api_framework_v4.common.logger_handler import LoggerHandler
from class27_20200208_api_framework_v4.common.random_phone_number import generate_phone_number
from class27_20200208_api_framework_v4.middlerware.read_yml import yaml_data


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
            mobile_num = self.db.query("select * from member limit 1;")
            wrong_pwd = str(random.randint(10000000, 99999999))
            if mobile_num:
                test_data['data'] = test_data['data'].replace("#exist_number#", mobile_num['mobile_phone'])
                test_data['data'] = test_data['data'].replace("#pwd#", mobile_num['pwd'])
                test_data['data'] = test_data['data'].replace("#wrong_pwd#", wrong_pwd)
            else:
                self.req.visit(config.host + 'member/register',
                               'post', yaml_data['user'],
                               {"X-Lemonban-Media-Type": "lemonban.v2"})

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

