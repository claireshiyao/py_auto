import json
import unittest

from class24_20200118_api_framework_v1.common.excel_handler import ExcelHandler
from class24_20200118_api_framework_v1.common.requests_handler import RequestsHandler
from class24_20200118_api_framework_v1.config.setting import config
from class24_20200118_api_framework_v1.libs import ddt


@ddt.ddt
class TestRegister(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    def setUp(self):
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register(self, test_data):
        excel_handler = ExcelHandler(config.data_path)
        res = self.req.visit(config.host + test_data['url'],
                        test_data['method'],
                        json=json.loads(test_data['data']),
                        headers=json.loads(test_data['headers']))
        try:
            self.assertEqual(res['msg'], test_data['expected_result'])
            excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'PASS')
        except AssertionError as e:
            print("断言失败，用例不通过")
            excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()