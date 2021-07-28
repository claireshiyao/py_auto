import json
import os
import unittest
from decimal import Decimal

from common.db_handler import DBHandler
from common.excel_handler import ExcelHandler
from common.logger_handler import LoggerHandler
from common.requests_handler import RequestsHandler
from config.setting import config
from libs import ddt
from middlerware.helper import Context, replace_label
from middlerware.read_yml import yaml_data
import warnings


@ddt.ddt
class TestWithdraw(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('withdraw')
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
        # save_token()
        # self.token = Context.token
        # self.member_id = Context.member_id
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_withdraw(self, test_data):
        token = Context().token
        member_id = Context().member_id
        # 查询数据库
        sql = 'select * from member where id = %s;'
        user = self.db.query(sql, args=[member_id, ])
        before_money = user["leave_amount"]

        if "#above_leave_amount#" in test_data['data']:
            if before_money >= 500000:
                self.db.query('update member set leave_amount = 10000 where id = %s;',args=[member_id, ])
                before_money = self.db.query('select * from member where id = %s;', args=[member_id, ])['leave_amount']
            above_leave_amount = before_money + 1
            test_data['data'] = test_data['data'].replace("#above_leave_amount#", str(above_leave_amount))

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
            self.assertEqual(res['code'], test_data['expected_result'])
            if res['code'] == 0:
                # 提现金额
                money = json.loads(test_data['data'])['amount']

                sql = 'select * from member where id = %s;'
                after_user = self.db.query(sql, args=[member_id, ])
                after_money = after_user["leave_amount"]

                self.assertEqual(Decimal(str(before_money)) - Decimal(str(money)), Decimal(str(after_money)))

            self.excel_handler.write(config.data_path, 'withdraw', test_data['id'] + 1, 10, 'PASS')

        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'withdraw', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'withdraw', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()