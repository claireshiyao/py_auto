import json
import os
import random
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


@ddt.ddt
class TestInvest(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('invest')
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

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_invest(self, test_data):
        token = Context().token
        member_id = Context().member_id
        loan_id = Context().loan_id
        # print(loan_id)
        # 查询数据库
        sql = 'select * from member where id = %s;'
        user = self.db.query(sql, args=[member_id, ])
        before_money = user["leave_amount"]

        loan_amount = self.db.query("select amount from loan where id = %s;", args=[loan_id, ])['amount']

        invest_exist = self.db.query("select * from invest where loan_id = %s;", args=[loan_id, ])
        if invest_exist:
            invest_sum = self.db.query("select sum(amount) from invest where loan_id = %s;", args=[loan_id, ])['sum(amount)']
        else:
            invest_sum = 0
        # print(invest_sum)

        above_loan_amount = loan_amount - invest_sum + 100

        if "$above_loan_amount$" in test_data['data']:
            test_data['data'] = test_data['data'].replace("$above_loan_amount$", str(above_loan_amount))

        wrong_loan_id = self.db.query('select id from loan where status != 2 limit 100;')['id']
        if "#wrong_loan_id#" in test_data['data']:
            test_data['data'] = test_data['data'].replace("#wrong_loan_id#", str(wrong_loan_id))

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
                # 投资金额
                money = json.loads(test_data['data'])['amount']

                sql = 'select * from member where id = %s;'
                after_user = self.db.query(sql, args=[member_id, ])
                after_money = after_user["leave_amount"]

                self.assertEqual(Decimal(str(before_money)) - Decimal(str(money)), Decimal(str(after_money)))

            self.excel_handler.write(config.data_path, 'invest', test_data['id'] + 1, 10, 'PASS')

        except AssertionError as e:
            print("断言失败，用例不通过")
            self.excel_handler.write(config.data_path, 'invest', test_data['id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.excel_handler.write(config.data_path, 'invest', test_data['id'] + 1, 9, f'{res}')

if __name__ == '__main__':
    unittest.main()
