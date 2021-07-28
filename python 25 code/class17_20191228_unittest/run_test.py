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

"""
import os
import unittest

#1, 初始化 testloader
testloader = unittest.TestLoader()

# 2, 查找测试用例，加载
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')
suite = testloader.discover(case_path)

print(suite)

# report
report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)

file_path = os.path.join(report_path, 'test_result.txt')
# text.
with open(file_path,"w", encoding='utf-8') as f:
    # 初始化运行期， 是以普通文本生成测试报告 TextTestRunner
    runner = unittest.TextTestRunner(f, verbosity=2)
    # 运行测试用例
    runner.run(suite)

