# author by claire

# 对 requests 发送请求封装成类：
# 1， 支持 session 管理（可以定义 session 属性）
# 2， 封装 visit 方法（可以发送 get 和 post 请求）

import requests

class RequestHandler:

    def __init__(self):
        self.session = requests.Session()

    def visit(self,  url, method, data=None, json=None, params=None, **kwargs):
        if method.lower() == 'post':
            res_post = self.session.post(url, data=data, json=json, **kwargs)
            return res_post.json()
        elif method.lower() == 'get':
            res_get = self.session.get(url, params=params, **kwargs)
            return res_get.json()
        else:
            return "请使用post或者get方法"
    def session_close(self):
        self.session.close()
#
#
request = RequestHandler()
login_data = {"mobilephone": "18111111111", "pwd": "123456"}
recharge_data = {"mobilephone": "18111111111", "amount": "1000"}
print(request.visit("http://test.lemonban.com/futureloan/mvc/api/member/login", "post", login_data))
print(request.visit("http://test.lemonban.com/futureloan/mvc/api/member/recharge", "post", recharge_data))
request.session_close()


if __name__ == '__main__':
    print("充值成功")

# 参考答案:
# import requests
# class HTTPHandler:
#
#     def __init__(self):
#         self.session = requests.Session()
#
#     def visit(self, url, method, params=None, data=None, json=None, **kwargs):
#         res = self.session.request(url, method, params=params, data=data, json=json, **kwargs)
#         try:
#             return res.json()
#         except ValueError:
#             print("not json")

