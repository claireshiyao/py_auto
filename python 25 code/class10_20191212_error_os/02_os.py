# author by claire

import os
print(os.getcwd())
# E:\PycharmProjects\python25\class10_20191212

# python指令运行脚本，路径会变，指的是在哪个路径运行的这个脚本。

print(os.path.abspath(__file__))
# E:\PycharmProjects\python25\class10_20191212\02_os.py
# 绝对路径

# 文件夹名称
a = os.path.dirname(os.path.abspath(__file__))
# E:\PycharmProjects\python25\class10_20191212

# 路径拼接
print(os.path.join(a, 'xsy.txt'))
# E:\PycharmProjects\python25\class10_20191212\xsy.txt

data_path = os.path.join(a, 'data')
# os.mkdir(data_path)  创建目录

print(os.path.isdir(data_path))  # 是否是目录
print(os.path.isfile(a))  # 是否是文件

# 路径是否存在
print(os.path.exists(data_path))  # True

xianren_path = os.path.join(a, 'xianren')
if not os.path.exists(xianren_path):
    os.mkdir(xianren_path)
    # 如果不存在，创建目录







