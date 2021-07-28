import json
import unittest

from class24_20200118_api_framework_v1.common.excel_handler import ExcelHandler
from class24_20200118_api_framework_v1.common.requests_handler import RequestsHandler
from class24_20200118_api_framework_v1.config.setting import config
from class24_20200118_api_framework_v1.libs import ddt


@ddt.ddt
class TestRecharge(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')

    def setUp(self):
        self.req = RequestsHandler()
        excel_handler = ExcelHandler(config.data_path)
        login_data = excel_handler.read('login')
        self.login_res = self.req.visit(config.host + login_data[0]['url'], login_data[0]['method'], json=json.loads(login_data[0]['data']),
                        headers=json.loads(login_data[0]['headers']))

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        excel_handler = ExcelHandler(config.data_path)
        headers_info = json.loads(test_data['headers'])
        headers_info['Authorization'] = "Bearer {}".format(self.login_res['data']['token_info']['token'])
        json_data = json.loads(test_data['data'])
        json_data['member_id'] = self.login_res['data']['id']
        res = self.req.visit(config.host + test_data['url'],
                        test_data['method'],
                        json=json_data,
                        headers=headers_info
                             )
        try:
            self.assertEqual(res['msg'], test_data['expected_result'])
            excel_handler.write(config.data_path, 'recharge', test_data['id'] + 1, 10, 'PASS')
        except AssertionError as e:
            print("断言失败，用例不通过")
            excel_handler.write(config.data_path, 'recharge', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            excel_handler.write(config.data_path, 'recharge', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()