# homework21
# 封装一个 LoggerHandler 类的模块
import logging


class LoggerHandler(logging.Logger):
    def __init__(self, name='logholder', level='DEBUG', file=None,
                 format='%(filename)s:%(lineno)d:%(name)s:%(levelname)s:%(message)s'):
        super().__init__(name)
        self.setLevel(level)
        fmt = logging.Formatter(format)

        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)

if __name__ == '__main__':
    logger = LoggerHandler(file='logger.txt')
    logger.debug('hello world')

