
# 一个session， 一次会话对象。
# 1， 没开一次浏览器（session 过期时间默认）
# sesssion (jsession='sfsfwef')


# 如何操作 cookie

# 登陆
import requests

# login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# data = {"mobilephone": "18111111111", "pwd": "123456"}
# res = requests.get(login_url, data)
#
# print(res.json())
#
# # 获取 cookie
# cookies = res.cookies
#
# # 充值：
# recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
#
# recharge_data = {"mobilephone":"18111111111", "amount":"1000"}
#
# res = requests.post(recharge_url, data=recharge_data, cookies=cookies)
# print(res.text)


# session
session = requests.Session()

login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {"mobilephone": "18111111111", "pwd": "123456"}
res = session.post(login_url, data)


print(res.json())

recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'

recharge_data = {"mobilephone": "18111111111", "amount": "1000"}
res = session.post(recharge_url, data=recharge_data)
print(res.text)

session.close()

# 初始化另外的session
# session_another = requests.Session()
# res = session_another.post(recharge_url, data=recharge_data)
# print(res.text)



