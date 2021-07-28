import json
import random
import unittest
from decimal import Decimal

from class28_20200211_api_framework_v5.common.db_handler import DBHandler
from class28_20200211_api_framework_v5.common.excel_handler import ExcelHandler
from class28_20200211_api_framework_v5.common.requests_handler import RequestsHandler
from class28_20200211_api_framework_v5.config.setting import config
from class28_20200211_api_framework_v5.libs import ddt
from class28_20200211_api_framework_v5.middlerware.login_setup import Context, save_token
from class28_20200211_api_framework_v5.middlerware.read_yml import yaml_data


@ddt.ddt
class TestRecharge(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')

    def setUp(self):
        self.req = RequestsHandler()
        self.db = DBHandler(host=yaml_data['database']['host'],
                            port=yaml_data['database']['port'],
                            user=yaml_data['database']['user'],
                            password=yaml_data['database']['password'],
                            database=yaml_data['database']['database'],
                            charset=yaml_data['database']['charset'])
        save_token()
        # self.token = Context.token
        # self.member_id = Context.member_id

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        token = Context.token
        member_id = Context.member_id
        # 查询数据库
        sql = 'select * from member where id = %s;'
        user = self.db.query(sql, args=[member_id, ])
        before_money = user["leave_amount"]

        if "#member_id#" in test_data['data']:
            test_data['data'] = test_data['data'].replace("#member_id#", str(member_id))

        if "#wrong_member_id#" in test_data['data']:
            test_data['data'] = test_data['data'].replace("#wrong_member_id#", str(member_id + 1))

        headers_info = json.loads(test_data['headers'])
        headers_info['Authorization'] = token

        # wrong_member_id = random.randint(1, 999999)
        # if wrong_member_id != self.member_id:
        #     test_data['data'] = test_data['data'].replace("#wrong_member_id#", str(wrong_member_id))

        res = self.req.visit(config.host + test_data['url'],
                        test_data['method'],
                        json=json.loads(test_data['data']),
                        headers=headers_info
                             )
        try:
            self.assertEqual(res['code'], test_data['expected_result'])
            if res['code'] == 0:
                # 充值金额
                money = json.loads(test_data['data'])['amount']
                # self.new_db = DBHandler(host=yaml_data['database']['host'],
                #                     port=yaml_data['database']['port'],
                #                     user=yaml_data['database']['user'],
                #                     password=yaml_data['database']['password'],
                #                     database=yaml_data['database']['database'],
                #                     charset=yaml_data['database']['charset'])


                # 充值之后的余额
                # sql = 'select * from member where id = %s;'
                # after_user = self.new_db.query(sql, args=[member_id, ])
                # after_money = after_user["leave_amount"]
                # self.new_db.close()

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