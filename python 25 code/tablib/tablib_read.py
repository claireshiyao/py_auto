# author by claire
import tablib

with open('test_case.xls', 'rb') as f:
    data = tablib.import_set(f.read(), format='xls')
    # print(data)
    # print(data.json)

    for i in data._data:
        print(data._data)
        # [['baidu', 'get', '成功'], ['lemon', 'post', '成功']]

    # 插入行
    data.append(['xxx', 'post', '成功'])

    # 插入一列
    data.append_col(['失败', '失败', '失败'], header='实际结果')

    # 更新数据
    data._data[2][0] = '更新的网址'
    print(data)

    data.append(['xsy', 'put', 'c', 'c'], tags=['成功', 'put'])
    success = data.filter(tag='成功')

    print(success)




