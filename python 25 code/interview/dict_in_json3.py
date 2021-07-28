# coding:utf-8
import json

from jsonpath import jsonpath


# 该方法测试用例使用可断言，但main下面断言失败，暂不用。
def if_dict_in_json(a, b):
    for i, j in a.items():
        if i in b:
            if j == jsonpath(b, "$..{}".format(i))[0]:
                pass
                # print("参数{}的值True".format(i))
            else:
                print("参数{}的值False".format(i))
                return False
        else:
            print("数据中无参数{}".format(i))
            return False
    return True

if __name__ == '__main__':
    a = {"d":2, "f":1}
    b = {"a":1,"b":{"c":1,"d":2},"f":1}
    # b2 = json.loads(b)
    # print(type(b2))
    print(if_dict_in_json(a, b))



