# author by claire
import requests
import unittest
class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
    def visit(self, method, url, data=None, json=None, params=None, **kwargs):
        res = self.session.request(method, url, data=data, json=json, params=params, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.data2 = {"method": "POST",
                      "url": "http://120.78.128.25:8766/futureloan/member/login",
                      "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
                      "data": {"mobile_phone": "18122", "pwd": "12"},
                      "expected": "无效的手机格式"
                      }

    def test_login_2_fail(self):
        request = RequestHandler()
        res2 = request.visit(self.data2['method'], self.data2['url'], json=self.data2['data'], headers=self.data2['headers'])
        self.assertIn(self.data2['expected'], res2.values())

    def tearDown(self):
        RequestHandler().close_session()
        print("测试用例2执行完毕。")

if __name__ == '__main__':
    unittest.main()