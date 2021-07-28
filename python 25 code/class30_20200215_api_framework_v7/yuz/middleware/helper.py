#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import re

from common.requests_handler import RequestsHandler
from config.setting import config
from middleware.yaml_handler import yaml_data


def login():
    """登录。 返回的是 token.  访问接口。
    1, 从登录的 excel 当中读取
    2， 从配置文件当中读取。
    """
    req = RequestsHandler()
    res = req.visit(config.host + '/member/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
    return res


def login_admin():
    pass

# Context().loan_id()


class Context:
    token = ''
    member_id = None


    @property
    def loan_id(self):
        """查询数据库，得到 loan_id.
        临时变量保存到 Context 当中

        return 返回 loan 标当中的 id 值
        """
        pass

    @property
    def token(self):
        pass




def save_token():
    """保存 token 信息"""
    data = login()

    from jsonpath import jsonpath
    token = jsonpath(data, '$..token')[0]
    token_type = jsonpath(data, '$..token_type')[0]
    member_id = jsonpath(data, '$..id')[0]
    # 拼接 token
    token = " ".join([token_type, token])
    # return (token, member_id)

    Context.token = token
    Context.member_id = member_id
    return {"token": token, "member_id": member_id }


def replace_label(target):
    """while 循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        # 如果能够匹配
        key = re.search(re_pattern, target).group(1)
        # Content.token
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target

if __name__ == '__main__':
    print(login())
    data = save_token()
    print(data)

