import json
import os
import unittest

from class26_20200206_api_framework_v3.common.excel_handler import ExcelHandler
from class26_20200206_api_framework_v3.common.random_phone_number import generate_phone_number
from class26_20200206_api_framework_v3.common.requests_handler import RequestsHandler
from class26_20200206_api_framework_v3.config.setting import config
from class26_20200206_api_framework_v3.libs import ddt
from class26_20200206_api_framework_v3.common.logger_handler import LoggerHandler
from class26_20200206_api_framework_v3.common.read_yml import ReadYaml
from class26_20200206_api_framework_v3.common.db_handler import DBHandler

read_yaml = ReadYaml(config.config_path)
yaml_data = read_yaml.open_yaml()

@ddt.ddt
class TestRegister(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')
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
    def test_register(self, test_data):
        if '#exist_number#' in test_data['data']:
            mobile_num = self.db.query("select * from member limit 1;")
            # 查询数据库，随机找一个，直接使用该号码替换
            if mobile_num:
                test_data['data'] = test_data['data'].replace("#exist_phone#", mobile_num['mobile_phone'])
            else:
                # 接口注册成功/数据库插入数据
                pass

        if '#new_number#' in test_data['data']:
            while True:
                mobile_num = generate_phone_number()
                # 查询数据库，如果数据库当中存在该手机号，那么再生成一次，直到不存在为止。
                db_mobile = self.db.query("select * from member where mobile = %s;", args=[mobile_num])
                if not db_mobile:
                    break
            test_data['data'] = test_data['data'].replace("#new_phone#", mobile_num)

        res = self.req.visit(config.host + test_data['url'],
                        test_data['method'],
                        json=json.loads(test_data['data']),
                        headers=json.loads(test_data['headers']))
        try:
            self.assertEqual(res['msg'], test_data['expected_result'])
            self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'PASS')
        except AssertionError as e:
            self.logger.error("断言失败，用例不通过：{}".format(e))
            self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()