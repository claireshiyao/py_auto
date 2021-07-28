# coding:utf-8

from jsonpath import jsonpath

# 该方法未考虑key不在参数2中，不全面。
def dict_in_json(a, b):
    for i, j in a.items():
        if j == jsonpath(b, "$..{}".format(i))[0]:
            print("参数{}的值True".format(i))
        else:
            print("参数{}的值False".format(i))
            return False
    return True

if __name__ == '__main__':
    a = {"d":2, "f":2}
    b = [{"a":1,"b":{"c":1,"d":2}},{"f":1}]
    print(dict_in_json(a, b))


