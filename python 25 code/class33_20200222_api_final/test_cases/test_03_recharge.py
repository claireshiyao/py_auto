import json
import unittest
from decimal import Decimal

from common.excel_handler import ExcelHandler
from common.requests_handler import RequestsHandler
from config.setting import config
from libs import ddt
from middlerware.helper import Context, replace_label
from middlerware.my_db_handler import MyDBHandler
from middlerware.my_logger_handler import logger


@ddt.ddt
class TestRecharge(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')
    logger = logger

    def setUp(self):
        self.req = RequestsHandler()
        self.db = MyDBHandler()

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        token = Context().token
        member_id = Context().member_id
        # 查询数据库
        sql = 'select * from member where id = %s;'
        user = self.db.query(sql, args=[member_id, ])
        before_money = user["leave_amount"]

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
            if res['code'] == 0:
                # 充值金额
                money = json.loads(test_data['data'])['amount']

                sql = 'select * from member where id = %s;'
                after_user = self.db.query(sql, args=[member_id, ])
                after_money = after_user["leave_amount"]

                self.assertEqual(Decimal(str(before_money)) + Decimal(str(money)), Decimal(str(after_money)))

            self.excel_handler.write(config.data_path, 'recharge', test_data['id'] + 1, 10, 'PASS')

        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'recharge', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'recharge', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()