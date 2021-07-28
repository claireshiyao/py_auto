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
class TestInvest(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('invest')
    logger = logger

    def setUp(self):
        self.req = RequestsHandler()
        self.db = MyDBHandler()

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

        # 已投资总额
        loan_amount = self.db.query("select amount from loan where id = %s;", args=[loan_id, ])['amount']

        # 查询项目是否有已投资金额，如为空则默认已投资0元;
        invest_exist = self.db.query("select * from invest where loan_id = %s;", args=[loan_id, ])
        if invest_exist:
            invest_sum = self.db.query("select sum(amount) from invest where loan_id = %s;", args=[loan_id, ])['sum(amount)']
        else:
            invest_sum = 0
        # print(invest_sum)

        # 高于项目剩余可投金额
        above_loan_amount = loan_amount - invest_sum + 100
        if "$above_loan_amount$" in test_data['data']:
            test_data['data'] = test_data['data'].replace("$above_loan_amount$", str(above_loan_amount))

        # 可投金额
        left_loan_amount = Decimal(str(loan_amount)) - Decimal(str(invest_sum))
        if "$left_loan_amount$" in test_data['expected_result']:
            test_data['expected_result'] = test_data['expected_result'].replace("$left_loan_amount$", str(left_loan_amount))

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
            for k, v in json.loads(test_data['expected_result']).items():
                if k in res:
                    self.assertEqual(res[k], v)

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
