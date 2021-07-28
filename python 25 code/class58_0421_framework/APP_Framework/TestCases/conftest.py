"""
======================
Author: 柠檬班-小简
Time: 2020/4/21 21:03
Project: py25-app
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest
import yaml
from appium import webdriver

from APP_Framework.Common.dir_config import config_dir

@pytest.fixture
def login_app():
    # 打开app  noReset=True
    driver = init()
    # 确认已登陆。如果说未登陆，我就去登陆。
    pass



@pytest.fixture
def init_app():
    # 打开app，要求是未登陆状态。noReset = False
    pass


# 启动appium的会话
def init(port=4723,**kwargs):
    # 打开app
    with open(config_dir + "/config.yaml", encoding="utf-8") as fs:
        desired_caps = yaml.load(fs, Loader=yaml.FullLoader)

    # 增加启动参数/修改启动参数
    for key,value in kwargs.items():
        desired_caps[key] = value

    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port), desired_caps)
    return driver

# npm - 命令行安装appium - 无界面 - 命令行参数
# desktop -

