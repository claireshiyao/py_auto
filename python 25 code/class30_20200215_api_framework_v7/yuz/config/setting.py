#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import os


class Config:

    # 项目路径
    root_path = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path, 'data/cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_cases')

    # config 路径
    config_path = os.path.join(root_path, 'config')

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # log 路径
    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(report_path):
        os.mkdir(report_path)


    yaml_config_path = os.path.join(config_path, 'config.yaml')



class DevConfig(Config):

    # 项目的域名
    host = 'http://120.78.128.25:8766/futureloan'



config = DevConfig()

