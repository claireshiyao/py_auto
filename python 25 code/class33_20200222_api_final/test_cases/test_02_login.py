import json
import unittest

from common.excel_handler import ExcelHandler
from common.requests_handler import RequestsHandler
from config.security_setting import s_config
from config.setting import config
from libs import ddt
from common.random_phone_number import generate_phone_number
from middlerware.my_db_handler import MyDBHandler
from middlerware.my_logger_handler import logger


@ddt.ddt
class TestLogin(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('login')
    logger = logger

    def setUp(self):
        self.req = RequestsHandler()
        self.db = MyDBHandler()

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_login(self, test_data):

        # 已注册账户登陆
        if '#exist_number#' in test_data['data']:
            mobile_num = s_config.mobile_phone
            pwd = s_config.pwd
            wrong_pwd = pwd + '1'
            if mobile_num:
                test_data['data'] = test_data['data'].replace("#exist_number#", str(mobile_num))
                test_data['data'] = test_data['data'].replace("#pwd#", pwd)
                test_data['data'] = test_data['data'].replace("#wrong_pwd#", wrong_pwd)

        # 未注册账户登陆
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
            for k, v in json.loads(test_data['expected_result']).items():
                if k in res:
                    self.assertEqual(res[k], v)
                    self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'PASS')
        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'login', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'login', test_data['id'] + 1, 9, f'{res}')


if __name__ == '__main__':
    unittest.main()

