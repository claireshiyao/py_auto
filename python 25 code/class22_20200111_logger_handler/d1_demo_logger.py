#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
from class_21_logger封装.logger_handler_2 import logger

# logger = LoggerHandler('python21', file='demo_log.txt')

def d1():
    print('hello')
    logger.info("D1")

if __name__ == '__main__':
    d1()