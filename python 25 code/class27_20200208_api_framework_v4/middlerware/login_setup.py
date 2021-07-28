# author by claire
import jsonpath as jsonpath

from class27_20200208_api_framework_v4.common.requests_handler import RequestsHandler
from class27_20200208_api_framework_v4.config.setting import config
from class27_20200208_api_framework_v4.middlerware.read_yml import yaml_data
from jsonpath import jsonpath

def login():
    req = RequestsHandler()
    res = req.visit(config.host+'/member/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
    return res

class Context:
    token = ''
    member_id = None

def save_token():
    data = login()
    token = jsonpath(data, '$..token')[0]
    member_id = jsonpath(data, '$..id')[0]
    token_type = jsonpath(data, '$..token_type')[0]

    token = " ".join([token_type, token])

    Context.token = token
    Context.member_id = member_id

    return token
    return {"token": token, "member_id": member_id}

if __name__ == '__main__':
    data = save_token()
    print(data)

