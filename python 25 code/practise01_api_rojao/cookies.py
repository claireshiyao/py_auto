import requests

login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {"mobilephone": "18111111111", "pwd": "123456"}
res = requests.get(login_url, data)

print(res.json())
print(res.cookies)
print(res.cookies['JSESSIONID'])

# 获取 cookie
