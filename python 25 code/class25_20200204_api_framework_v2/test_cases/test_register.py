import json
import unittest

from class25_20200204_api_framework_v2.common.excel_handler import ExcelHandler
from class25_20200204_api_framework_v2.common.random_phone_number import generate_phone_number
from class25_20200204_api_framework_v2.common.requests_handler import RequestsHandler
from class25_20200204_api_framework_v2.config.setting import config
from class25_20200204_api_framework_v2.libs import ddt
from class25_20200204_api_framework_v2.common.logger_handler import LoggerHandler
from class25_20200204_api_framework_v2.common.read_yml import ReadYaml

read_yaml = ReadYaml(config.config_path)
yaml_data = read_yaml.open_yaml()

@ddt.ddt
class TestRegister(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=yaml_data['logger']['file'])

    def setUp(self):
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register(self, test_data):
        # if '#exist_number#' in test_data['data']:
        #     # mobile_num = db.find("select...")
        #     # 查询数据库，随机找一个，直接使用该号码替换
        #     # test_data['data'] = test_data['data'].replace("#exist_phone#", mobile_num)
        #
        # if '#new_number#' in test_data['data']:
        #     # 查询数据库，如果数据库当中存在该手机号，那么再生成一次，直到不存在为止。
        #     while True:
        #         mobile_num = generate_phone_number()
        #         test_data['data'] = test_data['data'].replace("#exist_phone#", mobile_num)

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