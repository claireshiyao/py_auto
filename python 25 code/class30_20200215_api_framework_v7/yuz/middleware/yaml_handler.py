#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import yaml

from config.setting import config


class YamlHandler:

    def __init__(self, file):
        self.file = file


    def read(self, encoding='utf-8'):
        f = open(self.file, encoding=encoding)
        # TODO: f.read() 和 f 都可以做为参数
        data = yaml.load(f, yaml.FullLoader)
        f.close()
        return data


# 读取本项目当中的yaml 配置项
yaml_data = YamlHandler(config.yaml_config_path).read()
print(yaml_data)


