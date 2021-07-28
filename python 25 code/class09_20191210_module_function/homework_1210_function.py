"""
第二题：数据转换

# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# 要求一：把上述数据转换为以下格式
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
# 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
res = [
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
"""


def transform(cases):
    # if type(cases) != list:
    # 判断类型的

    if not isinstance(cases, list):
        print("不是 list")
        return

    new_cases = []

    title = cases[0]

    for case in cases[1:]:
        # [1, '用例1', 'www.baudi.com', '001', 'ok'],   ['case_id', 'case_title', 'url', 'data', 'excepted'],
        # {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
        dict_case = {}
        # 可以同时获取索引和值
        for i, column in enumerate(case):
            # 0, 1
            # dict_case['case_id'] = 1
            # dict_case['case_title'] = '用例1'
            dict_case[title[i]] = column
        new_cases.append(dict_case)
    return new_cases


def transform_zip(cases):
    if type(cases) != list:
        print("不是 list")
        return

    new_cases = []
    title = cases[0]
    for i in cases[1:]:
        # title = ['case_id', 'case_title', 'url', 'data', 'excepted']
        # i = [1, '用例1', 'www.baudi.com', '001', 'ok']
        # [(case_id, 1), (case_title, '用例1'), (url, 'wwww.)]
        # zip
        new_dict = dict(zip(title, i))
        new_cases.append(new_dict)
    return new_cases


def filter(cases, id):
    new_cases = []
    for c in cases:
        if c['case_id'] > id:
            new_cases.append(c)
    return new_cases


cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# a = transform(cases)
# print(a)
# print(filter(a, 3))
# print(transform_zip(cases))

if __name__ == '__main__':
    a = transform(cases)
    print(a)

    b = filter(a, 3)
    print(b)


