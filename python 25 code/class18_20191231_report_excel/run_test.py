#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
收集测试用例: TestLoader, 加载器，加载测试用例
放到测试集合（测试套件） TestSuite

1, 初始化 testloader
2, suite = testloader.discover(文件夹路径， 'demo_*.py')  发现测试用例
3, 如果你想运行的用例，放到指定的文件夹当中，

# TestRunner,
1, 运行用例
2， 生成测试报告


几种加载测试用例的方式：
1， 用的最多，整个项目一起加载，使用：discover
2, 你想只测试某一个具体的某块，功能，使用  loadTestsFromTestCase  或者 loadTestsFromModule
3, pytest,


HTMLTestRunner, 不是unittest 自带的。需要自己去安装。
1，安装方式不是通过 pip
2, 他是别人写好的一个模块，你可以直接下载下来的 .py
3, 复制到项目目录下，然后倒入。
4， 第二种方式：我们可以放到 python 的公共库当中

"""
import os
import unittest

#1, 初始化 testloader
import time

from class_18_report.HTMLTestRunnerNew import HTMLTestRunner
from class_18_report.test_cases import test_login, test_register
from class_18_report.test_cases.test_login import TestLogin
from class_18_report.test_cases.test_rechage import TestRecharge
from class_18_report.test_cases.test_register import TestRegister

testloader = unittest.TestLoader()

# 2, 查找测试用例，加载
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')



# suite = testloader.discover(case_path)
# 加载两个模块当中的测试用例，保存到测试套件当中
# suite = testloader.loadTestsFromModule(test_login)
# suite2 = testloader.loadTestsFromModule(test_register)


# 添加指定的测试类
suite = testloader.loadTestsFromTestCase(TestLogin)
suite2 = testloader.loadTestsFromTestCase(TestRecharge)

# 讲这两个测试套件合并添加到一个总的测试套件套件
suite_total = unittest.TestSuite()
suite_total.addTests(suite)
suite_total.addTests(suite2)


# suite = testloader.loadTestsFromName()

print(suite)

# report
report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)

# 什么格式？？
ts = str(int(time.time()))  # test_result_234.56.html

file_name = 'test_result_{}.html'.format(ts)


file_path = os.path.join(report_path, file_name)
# text.

# TODO: 一定要使用二进制的方式代开
with open(file_path, 'wb') as f:
    # 使用 HTMLTestRunner
    runner = HTMLTestRunner(f,
                            title="史上最帅的测试报告",
                            description='那是真的帅',
                            tester='最帅的小马哥')
    runner.run(suite_total)



