# author by claire
import re


from common.requests_handler import RequestsHandler
from config.setting import config
from middlerware.read_yml import yaml_data
from jsonpath import jsonpath

from common.db_handler import DBHandler


def login():
    req = RequestsHandler()
    res = req.visit(config.host+'/member/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
    # req.close_session()
    return res

class Context:
    # token = ''
    # member_id = None
    # loan_id = None
    def __init__(self):
        self.db = DBHandler(host=yaml_data['database']['host'],
                            port=yaml_data['database']['port'],
                            user=yaml_data['database']['user'],
                            password=yaml_data['database']['password'],
                            database=yaml_data['database']['database'],
                            charset=yaml_data['database']['charset'])


    @property
    def loan_id(self):
        l_id = self.db.query("select id from loan where status = 2 limit 10;")
        l_id_value = l_id['id']
        self.db.close()
        return l_id_value

    @property
    def token(self):
        data = login()
        t = jsonpath(data, '$..token')[0]
        token_type = jsonpath(data, '$..token_type')[0]
        bearer_token = " ".join([token_type, t])
        return bearer_token

    @property
    def member_id(self):
        data = login()
        m_id = jsonpath(data, '$..id')[0]
        return m_id


def replace_label(target):
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        key = re.search(re_pattern, target).group(1)
        target = re.sub(re_pattern, str(getattr(Context(), key)), target, 1)
    return target


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
    # data = save_token()
    # print(data)
    a = getattr(Context(), 'member_id')
    print(a)

