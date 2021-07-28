#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
unittest 运行方式：
1， unittest 右键,   pycharm 带的
2， python 代码 main : unittest.main()，
3,  python -m unittest

断言方式：
self.assertEqual(expected, actual)   # 提示能够提示出预期结果和实际结果
self.assertTrue(表达式)   # 预期结果和实际结果没有具体的提示
#

条件准备：前置条件和后置条件  def setUp(self):  def tearDown(self):
前置条件, 测试用例执行之前都会执行的代码
后置条件，测试用例执行之后会执行的代码。


测试用例执行流程：
1， 初始化加载器。   testloader = unittest.TestLoader()
2, 查找测试用例。    suite = testloader.discover(文件夹， 'test_*.py')
# 其他的加载方式。

3， 打开一个 with open() as f:
4, 初始化运行器：   runner = 运行器(f)
5， 运行测试用例 “ ” runner.run(suite)
"""

# 测试用例执行
# 用例数据管理，Excel