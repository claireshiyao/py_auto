# author by claire
from test_datas.global_datas import home_url

login_success_data = {"user": "13760246701", "passwd": "python", "check": home_url}

login_wrong_data = [
        {"user": "", "passwd": "python", "check": "请输入手机号"},
        {"user": "13760246701", "passwd": "", "check": "请输入密码"},
        {"user": "1376024670", "passwd": "python", "check": "请输入正确的手机号"}
    ]

login_wrong_account = [
    {"user": "13760246701", "passwd": "pytho", "check": "帐号或密码错误!"},
    {"user": "13760246702", "passwd": "python", "check": "此账号没有经过授权，请联系管理员!"}
    ]
