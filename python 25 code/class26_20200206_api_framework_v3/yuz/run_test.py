#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

import os
import unittest
import time

from libs.HTMLTestRunnerNew import HTMLTestRunner
from config.setting import config

# 加载器
testloader = unittest.TestLoader()
suite = testloader.discover(config.case_path)
# 通过模块名，类名

# 测试报告
ts = str(int(time.time()))  # test_result_234.56.html
file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(config.report_path, file_name)


with open(file_path, 'wb') as f:
    # 使用 HTMLTestRunner
    runner = HTMLTestRunner(f,
                            title="前程贷接口测试报告",
                            description='前程贷接口测试报告',
                            tester='最帅的小马哥')
    runner.run(suite)







