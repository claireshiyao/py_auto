
import os
import unittest

import time

from class19_20200102_excel_ddt.HTMLTestRunnerNew import HTMLTestRunner
from class19_20200102_excel_ddt.test_cases.test_login import TestLogin

testloader = unittest.TestLoader()

suite = testloader.loadTestsFromTestCase(TestLogin)


suite_total = unittest.TestSuite()
suite_total.addTests(suite)


dir_path = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)


ts = str(int(time.time()))

file_name = 'test_result_{}.html'.format(ts)


file_path = os.path.join(report_path, file_name)

with open(file_path, 'wb') as f:
    # 使用 HTMLTestRunner
    runner = HTMLTestRunner(f,
                            title="测试报告",
                            description='登录接口的测试报告',
                            tester='依可若')
    runner.run(suite_total)



