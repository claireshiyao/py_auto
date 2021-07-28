#!/usr/bin/python3
"""
@File    : home_page.py
@Time    : 2019/11/29 21:38
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from web_basepage.Common.basepage import BasePage
from web_basepage.PageLocators.home_page_loc import HomePageLoc as loc


class HomePage(BasePage):

    # 检测 退出元素 是否存在。
    def check_user_exist(self):
        return self.check_element_visible(loc.exit_loc,"首页_检测退出元素是否存在")

    # 点击第一个标，进入标页面。
    def click_first_bid(self):
        self.click_element(loc.bid_button,"首页_点击第一个抢投标按钮")