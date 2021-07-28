



import yaml
# 读取 yaml 配置, 加载配置项
f = open('python25.yaml', encoding='utf-8')

data = yaml.load(f.read(), Loader=yaml.FullLoader)
print(data)

f.close()


# with open('python25.yaml') as f:
#     data = yaml.load(f.read(), Loader=yaml.FullLoader)