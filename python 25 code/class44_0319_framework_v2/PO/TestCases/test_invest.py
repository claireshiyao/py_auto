import unittest
from selenium import webdriver
import ddt

from PO.PageObjects.login_page import LoginPage
from PO.PageObjects.home_page import HomePage

from PO.TestDatas import Global_Datas as GD
from PO.TestDatas import login_datas as lds


class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 访问登陆页面
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        # 登陆 - 使用公共投资人帐号
        LoginPage(self.driver).login(*GD.user_invest)

    def tearDown(self) -> None:
        self.driver.quit()

    # 正向场景  - 投资成功 - 投资2000块 - 用户余额/标余额是否发生变化
    def test_invest_success(self):
        """
        :return:
        """
        # 1、首页 - 选第一个标
        # 11、标页面 - 获取用户余额
        # 111、标页面 - 获取标的余额
        # 2、标页面 - 输入金额2000，点投标
        # 3、标页面 - 在投标成功的弹出框里，点击
        # 查看并激活
        # 按钮

        # 1、钱有没有少2000 - 灵活可用
        # 4）个人页面 - 获取用户余额
        # 断言：投前额 - 投后额 == 2000
        #
        # 2、标的可投余额少2000
        # 5）个人页面 - 回退到上一页；刷新
        # 6）标页面 - 获取标的余额
        # 断言：(投前标额 - 投后标额) * 10000 == 2000
        pass


class TestKTP:

    def test_01_fqkq(self):
        pass

    def test_02_kq(self):
        pass

    def test_03_gbkq(self):
        pass

    #
    def test_04_xskkq(self):
        pass

class TestJZY:
    pass
