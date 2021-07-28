# author by claire
import os

import yaml

class ReadYaml:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
    def open_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data

if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(dir_name, 'config.yaml')
    yaml_data = ReadYaml(file_name)
    print(yaml_data.open_yaml())


