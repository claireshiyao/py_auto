#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import yaml
from configparser import ConfigParser

class ConfigHandler(ConfigParser):

    def __init__(self, file, encoding='utf-8'):
        """
        参数：
        - file: 配置文件的路径名。
        """
        # config = ConfigParser()
        super().__init__()
        self.read(file, encoding=encoding)





def read_yaml(file, encoding='utf-8'):
    with open(file, encoding=encoding) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)

# data
def write_yaml(file, data, encoding='utf-8'):
    """写入yaml.
    中文如何处理？？？？
    """
    with open(file, encoding=encoding, mode='w') as f:
        yaml.dump(data, stream=f, allow_unicode=True)




if __name__ == '__main__':
    # 读取
    # config = ConfigHandler('python25.ini')
    # a = config.get('teachers', 'name')
    # print(a)

    # f = open('python25.yaml')
    # print(f)

    # 先读取 yaml 数据
    data = read_yaml('python25.yaml')


    write_yaml('python27.yaml', data)

    # 获取
    # config = ConfigHandler('python25.ini')
    # print(config['teachers'])
    #
    # config['teachers']['name'] = 'benben'
    #
    # print(config['teachers']['name'])
    #
    # with open('python25.ini', 'a', encoding='utf-8') as f:
    #     config.write(f)

