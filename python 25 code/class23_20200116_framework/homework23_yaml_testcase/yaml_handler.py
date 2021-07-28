import os

import yaml

class YamlHandler:
    def __init__(self, file, encoding='utf-8'):
        self.file = file
        self.encoding = encoding
    def read_yaml(self):
        with open(self.file, encoding=self.encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)
    def write_yaml(self, new_file, data):
        with open(new_file, 'w', encoding=self.encoding) as f:
            yaml.dump(data, stream=f, allow_unicode=True)

if __name__=='__main__':
    dir_name = os.path.dirname(os.path.abspath(__file__))
    yaml_file1 = os.path.join(dir_name, 'python25.yaml')
    yaml_file2 = os.path.join(dir_name, 'python26.yaml')
    yamlhandler = YamlHandler(yaml_file1)
    data = yamlhandler.read_yaml()
    yamlhandler.write_yaml(yaml_file2, data)
