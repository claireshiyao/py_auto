#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
"""存储配置项"""
import sys


class LoggerConfig:
    logger_name = 'python27'
    logger_file = 'python27.txt'
    level = 'DEBUG'


class ProductLoggerConfig(LoggerConfig):
    level = 'WARNING'


# if sys.platform == 'linux':
#     config = ProductLoggerConfig
# else:
#     config = LoggerConfig