#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import logging


class LoggerHandler():

    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(filename)s:%(lineno)d:%(name)s:%(levelname)s-%(message)s'):

        logger = logging.getLogger(name)

        # 设置级别
        logger.setLevel(level)

        fmt = logging.Formatter(format)

        # 初始化处理器
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            logger.addHandler(file_handler)
        stream_handler = logging.StreamHandler()

        # 设置 handler 的级别
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        logger.addHandler(stream_handler)

        self.logger = logger

    def debug(self, msg):
        return self.logger.debug(msg)

    def info(self, msg):
        return self.logger.info(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

    def critical(self, msg):
        return  self.logger.critical(msg)


if __name__ == '__main__':
    logger = LoggerHandler()
    logger.debug('hello world')





