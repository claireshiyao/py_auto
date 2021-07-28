import unittest

from class19_20200102_excel_ddt import ddt

from class19_20200102_excel_ddt.common.request_handler import RequestHandler
from class19_20200102_excel_ddt.common.excel_handler import Excel

import os

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "test_cases_0102.xlsx")

test_data = Excel(file_path).read_datas('Sheet1')
print(test_data)

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.request = RequestHandler()
        print("正在准备测试数据")

    def tearDown(self):
        print("测试用例执行完毕。")
        self.request.session.close()

    @ddt.data(*test_data)
    def test_login(self, data_info):
        res = self.request.visit(data_info['url'], data_info['method'], headers=eval(data_info['headers']), json=eval(data_info['data']))
        self.assertEqual(data_info['expected'], res['msg'])

if __name__ == '__main__':
    unittest.main()






