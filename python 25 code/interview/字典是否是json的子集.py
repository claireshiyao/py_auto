# coding:utf-8
#3、判断一个单层字典是否是json的子集，参数1所有key-value都在参数2中
# 例：入参1{"d":2},入参2: [{"a":1,"b":{"c":1,"d":2}},{"f":1}],返回True，否则返回False

from jsonpath import jsonpath


def dict_in_json(a, b):
    keys = []
    for key in a.keys():
        keys.append(key)
    values = []
    for value in a.values():
        values.append(value)
    num = len(keys)
    i = 0
    while i <= num-1:
        if values[i] == jsonpath(b, "$..{}".format(keys[i]))[0]:
            print("第{}组键值对True".format(i+1))
        else:
            print("第{}组键值对False".format(i+1))
            return False
        i += 1
    return True

a = {"d":2, "f":2}
b = [{"a":1,"b":{"c":1,"d":2}},{"f":1}]
print(dict_in_json(a, b))


