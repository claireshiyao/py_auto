# author by claire
"""
通过发送的接口文档和地址，练习 requests 的使用：
1， 注册失败
2， 注册成功
3， 登录失败
4， 登录成功
# 根据上课演示内容：
# 通过设置不同的参数，params, data, json 观察结果。
# 通过设置不同的 headers 观察结果。
# 提交 requests 代码
"""

import requests


class Request:
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def post(self):
        res = requests.post(self.url, json=self.data, headers=self.headers, params=self.data)
        return res

# 注册成功
register = Request('http://120.78.128.25:8766/futureloan/member/register', {"X-Lemonban-Media-Type": "lemonban.v1", "Content-Type": "application/json"}, {"mobile_phone": 13711223347, "pwd": "dada12345678", "type": "1", "reg_name": "yikeruo"})
result = register.post()
print(result.json())

# 注册失败，必填参数为空。
# register = Request('http://120.78.128.25:8766/futureloan/member/register', {"X-Lemonban-Media-Type": "lemonban.v1", "Content-Type": "application/json"}, {"mobile_phone": 13711223347, "pwd": "", "type": "1", "reg_name": "yikeruo"})
# result = register.post()
# print(result.json())

# 登录成功
login = Request('http://120.78.128.25:8766/futureloan/member/login', {"X-Lemonban-Media-Type": "lemonban.v1", "Content-Type": "application/json"}, {"mobile_phone": 13711223347, "pwd": "dada12345678"})
result = login.post()
print(result.json())

# 登录失败，账号信息错误
# login = Request('http://120.78.128.25:8766/futureloan/member/login', {"X-Lemonban-Media-Type": "lemonban.v1", "Content-Type": "application/json"}, {"mobile_phone": 13711223347, "pwd": "dada111111"})
# result = login.post()
# print(result.json())






