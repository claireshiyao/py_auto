#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
from class_21_logger封装.d1_demo_logger import d1
from class_21_logger封装.logger_handler_2 import logger

# logger = LoggerHandler('python25', file='demo_log_.txt')


def main():
    print('hello')
    logger.info('hello')
    d1()


def hello():
    logger.error("hello world")


if __name__ == '__main__':
    main()