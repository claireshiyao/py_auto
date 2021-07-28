# coding:utf-8
import json

from jsonpath import jsonpath

# 完整版
def dict_in_json(a, b):
    try:
        for i, j in a.items():
            if str(j) == str(jsonpath(b, "$..{}".format(i))[0]):
                pass
            else:
                return False
        return True
    except:
        return False

if __name__ == '__main__':
    a = {"d":"2", "f":"1"}
    b = [{"a":1,"b":{"c":1,"d":2}},{"f":1}]
    print(dict_in_json(a, b))



