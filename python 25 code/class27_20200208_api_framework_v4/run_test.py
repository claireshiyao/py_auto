import os
import time
import unittest

from class24_20200118_api_framework_v1.config.setting import config
from class24_20200118_api_framework_v1.libs.HTMLTestRunnerNew import HTMLTestRunner

testloader = unittest.TestLoader()

suite = testloader.discover(config.case_path)

ts = str(int(time.time()))

file_name = 'test_result_{}.html'.format(ts)


file_path = os.path.join(config.report_path, file_name)

with open(file_path, 'wb') as f:
    # 使用 HTMLTestRunner
    runner = HTMLTestRunner(f,
                            title="测试报告",
                            description='前程贷注册接口的测试报告',
                            tester='依可若')
    runner.run(suite)



