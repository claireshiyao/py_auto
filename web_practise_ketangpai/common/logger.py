# author by claire

import logging
import os
import time
from logging.handlers import RotatingFileHandler

from common import dir_config

format = "%(asctime)s %(filename)s %(funcName)s %(levelname)s [line:%(lineno)d %(message)s]"
datefmt = "%a %d %b %Y %H:%M:%S"

handler1 = logging.StreamHandler()
curdate = time.strftime("%Y-%m-%d")
curtime = time.strftime("%H_%M_%S")

filename = "web_auto_test.{}.{}.log".format(curdate, curtime)
handler2 = RotatingFileHandler(os.path.join(dir_config.log_path, filename), backupCount=20, encoding="utf-8")

logging.basicConfig(format=format, datefmt=datefmt, level=logging.INFO, handlers=[handler1, handler2])

