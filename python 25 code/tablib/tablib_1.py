# author by claire

# 1. 支持xlsx, xls, csv, json, yaml, html, 数据库
# 2. 没有中文文档
# 3. pip install tablib
# import tablib
#
# 4. 核心概念
# tablib.Dataset()   #sheet
# tablib.Databook()  # workbook
#
# 5. Dataset
import tablib
headers = ['url', 'method', 'expected']

data = [
      ['baidu', 'get', '成功'],
      ['lemon', 'post', '成功']
]

data1 = tablib.Dataset(*data, headers=headers, title='test_case1')
# print(data1)
# print(data1.json)
# print(data1.html)
# print(data1.vaml)
# print(data1.xls)
# print(data1.xlsx)
data2 = tablib.Dataset(*data, headers=headers, title='test_case2')

# with open('test_case.xls', 'wb') as f:
#       f.write(data1.xls)

# 6. Databook
data_book = tablib.Databook([data1, data2])
with open('test_case2.xls', 'wb') as f:
      f.write(data_book.xls)


