#!/usr/bin/python3
"""
@File    : login_datas.py
@Time    : 2019/12/2 21:41
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from web_basepage.TestDatas.Common_Datas import home_url


# 成功用例 - 数据
success_data = {"user": "18684720553", "passwd": "python","check_url":home_url}


# 用户名为空/密码为空/用户名格式不正确
wrong_datas = [
    {"user": "", "passwd": "python", "check": "请输入手机号"},
    {"user": "18684720553", "passwd": "", "check": "请输入密码"},
    {"user": "186847205", "passwd": "python", "check": "请输入正确的手机号"}
]

# 密码错误 / 用户名尚未注册