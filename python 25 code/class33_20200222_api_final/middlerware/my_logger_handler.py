import os

from common.logger_handler import LoggerHandler
from config.setting import config
from middlerware.read_yml import yaml_data


class MyLoggerHandler(LoggerHandler):
    def __init__(self):

        super().__init__(name=yaml_data['logger']['name'],
                               level=yaml_data['logger']['level'],
                               file=os.path.join(config.log_path, yaml_data['logger']['file']))

logger = MyLoggerHandler()