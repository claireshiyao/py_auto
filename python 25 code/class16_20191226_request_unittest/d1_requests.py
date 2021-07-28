import requests

# 访问接口
# url = 'http://120.78.128.25:8766/futureloan/member/register'
# headers = {"X-Lemonban-Media-Type": "lemonban.v1"}
# data = {"mobile_phone": "18111111111", "pwd": "12345678"}
#
# # 一定要添加 headers 关键字参数，不能以位置参数传递。
# # 因为放到了可变长参数里面
# # content-type 不需要添加，为什么？？ json 关键字参数就是表示 content-type = json,
# # data 关键字参数就是表示 表单格式，
# # params 参数就是表示 query string
# res = requests.post(url, params=data, headers=headers)
#
# print(res.json())


# 登陆接口
# token 放在什么地方。
# token 可以放到请求体当中？？ 根据接口文档。 只是一种协议，开发人员和你之间定义的协议
# cookie 可以放到请求体当中？ HTTP 协议

url = 'http://120.78.128.25:8766/futureloan/member/login'
headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}

res = requests.post(url, json=data, headers=headers)
# print(res.json())

# 充值
recharge_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
token = res.json()['data']['token_info']['token']
id = res.json()['data']['id']
headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": "Bearer {}".format(token)}
data = {
	"member_id": id,
	"amount": 100
}

res = requests.post(recharge_url, json=data, headers=headers)
print(res.json())


# 如果我要访问其他的接口
