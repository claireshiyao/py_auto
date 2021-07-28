# author by claire
import os

import yaml

from class27_20200208_api_framework_v4.config.setting import config


class ReadYaml:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
    def read(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            data = yaml.load(f, yaml.FullLoader)
        f.close()
        return data


yaml_data = ReadYaml(config.config_path).read()
print(yaml_data)


