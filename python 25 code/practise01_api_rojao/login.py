# coding:utf-8
import requests

from practise01_api_rojao.requests_handler import RequestsHandler

# req = RequestsHandler()
res = requests.get('http://10.10.1.217:7088/nias/captcha.jpg', 'get')

# print(res.json())
print(res.cookies)
# <RequestsCookieJar[<Cookie JSESSIONID=0241bd8b-5513-4526-8f5e-025336fb38ed for 10.10.1.217/nias>]>