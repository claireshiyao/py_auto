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
    def close_session(self):
        self.session.close()

class TestLogin(unittest.TestCase):

    def setUp(self):

        self.data1 = {"method": "POST",
            "url": "http://120.78.128.25:8766/futureloan/member/login",
            "headers" : {"X-Lemonban-Media-Type": "lemonban.v2"},
            "data":{"mobile_phone": "18111111111", "pwd": "12345678"},
            "expected": "OK"
        }

    def test_login_1_success(self):
        request = RequestHandler()
        res1 = request.visit(self.data1['method'], self.data1['url'], json=self.data1['data'], headers=self.data1['headers'])
        self.assertIn(self.data1['expected'], res1.values())

    def tearDown(self):
        RequestHandler().close_session()
        print("测试用例1执行完毕。")

if __name__ == '__main__':
    unittest.main()