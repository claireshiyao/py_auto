import json
import random
import unittest

from class27_20200208_api_framework_v4.common.excel_handler import ExcelHandler
from class27_20200208_api_framework_v4.common.requests_handler import RequestsHandler
from class27_20200208_api_framework_v4.config.setting import config
from class27_20200208_api_framework_v4.libs import ddt
from class27_20200208_api_framework_v4.middlerware.login_setup import Context, save_token


@ddt.ddt
class TestRecharge(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('withdraw')

    def setUp(self):
        self.req = RequestsHandler()
        save_token()
        self.token = Context.token
        self.member_id = Context.member_id

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        headers_info = json.loads(test_data['headers'])
        headers_info['Authorization'] = self.token
        test_data['data'] = test_data['data'].replace("#member_id#", str(self.member_id))
        wrong_member_id = random.randint(71000, 71026)
        if wrong_member_id != self.member_id:
            test_data['data'] = test_data['data'].replace("#wrong_member_id#", str(wrong_member_id))
        res = self.req.visit(config.host + test_data['url'],
                        test_data['method'],
                        json=json.loads(test_data['data']),
                        headers=headers_info
                             )
        try:
            self.assertEqual(res['msg'], test_data['expected_result'])
            self.excel_handler.write(config.data_path, 'withdraw', test_data['id'] + 1, 10, 'PASS')
        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'withdraw', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'withdraw', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()