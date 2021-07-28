import json
import random
import unittest

from common.excel_handler import ExcelHandler
from common.requests_handler import RequestsHandler
from config.setting import config
from libs import ddt
from middlerware.helper import Context, replace_label
from middlerware.my_db_handler import MyDBHandler
from middlerware.my_logger_handler import logger


@ddt.ddt
class TestAdd(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('add')
    logger = logger

    def setUp(self):
        self.req = RequestsHandler()
        self.db = MyDBHandler()

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_add(self, test_data):
        token = Context().token
        member_id = Context().member_id

        # 会员不存在
        if '$new_member_id$' in test_data['data']:
            while True:
                new_member_id = random.randint(70000, 79999)

                db_member_id = self.db.query("select * from member where id = %s;", args=[new_member_id, ])
                if not db_member_id:
                    break
            test_data['data'] = test_data['data'].replace("$new_member_id$", str(new_member_id))

        # 用户不正确
        if '#wrong_member_id#' in test_data['data']:
            test_data['data'] = test_data['data'].replace("#wrong_member_id#", str(member_id + 1))

        test_data['data'] = replace_label(test_data['data'])

        headers_info = json.loads(test_data['headers'])
        headers_info['Authorization'] = token

        res = self.req.visit(config.host + test_data['url'],
                        test_data['method'],
                        json=json.loads(test_data['data']),
                        headers=headers_info
                             )
        try:
            for k, v in json.loads(test_data['expected_result']).items():
                if k in res:
                    self.assertEqual(res[k], v)
                    self.excel_handler.write(config.data_path, 'register', test_data['id'] + 1, 10, 'PASS')

        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'add', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'add', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()