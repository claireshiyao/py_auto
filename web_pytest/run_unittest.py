# author by claire
import os
import time
import unittest

from API.HTMLTestRunnerNew import HTMLTestRunner
from common import dir_config

testloader = unittest.TestLoader()
suite = testloader.discover(dir_config.testcase_path)

test_time = time.strftime("%Y-%m-%d %H_%M_%M")
filename = "test_report_{}.html".format(test_time)
filepath = os.path.join(dir_config.report_path, filename)

with open(filepath, "wb") as f:
    runner = HTMLTestRunner(f, title="测试报告",
                            description='前程贷web unittest自动化测试报告',
                            tester='依可若'

    )
    runner.run(suite)
