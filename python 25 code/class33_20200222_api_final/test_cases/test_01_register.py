import json
import unittest

from common.excel_handler import ExcelHandler
from common.random_phone_number import generate_phone_number
from common.requests_handler import RequestsHandler
from config.setting import config
from libs import ddt
from middlerware.my_db_handler import MyDBHandler
from middlerware.my_logger_handler import logger



@ddt.ddt
class TestRegister(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')
    logger = logger

    def setUp(self):
        self.req = RequestsHandler()
        self.db = MyDBHandler()

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_register(self, test_data):
        if '#exist_number#' in test_data['data']:
            mobile_num = self.db.query("select * from member limit 1;")
            # 查询数据库，随机找一个，直接使用该号码替换
            if mobile_num:
                test_data['data'] = test_data['data'].replace("#exist_number#", mobile_num['mobile_phone'])
            else:
                # 接口注册成功/数据库插入数据
                pass

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
            self.logger.error("断言失败，用例不通过：{}".format(e))
            self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()
