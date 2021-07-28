from configparser import ConfigParser

# 初始化
config = ConfigParser()

# 读取文件
config.read('python25.ini', encoding='utf-8')

a = config.get('teachers', 'name')
print(a)
print(type(a))


# 1， 封装 logger 模块， 继承。  小技巧，在定义的模块当中初始化，
# 2， 配置文件， python, yaml, ini了解使用方法，
# python: 直接通过模块下面的变量
# python: 类，你可以继承

# yaml
# 1, 语法， key:value   - - -   {}   []
# 2, 读取，  pyyaml   yaml.load（f,read(), Loader=...）

# ini
# 1, 数据类型是字符串。
