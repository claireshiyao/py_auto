# author by claire
import re


from class27_20200208_api_framework_v4.common.requests_handler import RequestsHandler
from class27_20200208_api_framework_v4.config.setting import config
from class27_20200208_api_framework_v4.middlerware.read_yml import yaml_data
from jsonpath import jsonpath

from class30_20200215_api_framework_v7.common.db_handler import DBHandler


def login():
    req = RequestsHandler()
    res = req.visit(config.host+'/member/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
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
        loan_id = self.db.query('select id from loan where status = %s;', args=[2, ])
        self.db.close()
        return loan_id

    def wrong_loan_id(self):
        wrong_loan_id = self.db.query('select id from loan where status != %s;', args=[2, ])
        self.db.close()
        return wrong_loan_id

    @property
    def token(self):
        data = login()
        token = jsonpath(data, '$..token')[0]
        token_type = jsonpath(data, '$..token_type')[0]
        token = " ".join([token_type, token])
        return token

    @property
    def member_id(self):
        data = login()
        member_id = jsonpath(data, '$..id')[0]
        return member_id

    @property
    def wrong_member_id(self):
        wrong_member_id = Context.member_id + 1
        return wrong_member_id


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

