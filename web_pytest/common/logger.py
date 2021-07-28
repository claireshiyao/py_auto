import logging
import time
from logging.handlers import RotatingFileHandler

from common import dir_config

format = "%(asctime)s %(filename)s %(funcName)s %(levelname)s [line:%(lineno)d %(message)s]"
datefmt = "%a %d %b %Y %H:%M:%S"

handler_1 = logging.StreamHandler()
cur_time = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))

handler_2 = RotatingFileHandler(dir_config.log_path+"/web_automated_test_{}.log".format(cur_time), backupCount=20, encoding='utf-8')

logging.basicConfig(format=format, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])