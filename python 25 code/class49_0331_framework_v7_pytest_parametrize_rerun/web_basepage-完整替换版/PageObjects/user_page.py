#!/usr/bin/python3
"""
@File    : user_page.py
@Time    : 2019/12/4 21:14
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from web_basepage.Common.basepage import BasePage
from web_basepage.PageLocators.user_page_loc import UserPageLoc as loc


class UserPage(BasePage):

    # 获取用户余额
    def get_user_left_money(self):
        text = self.get_element_text(loc.user_leftMoney, "个人页面_获取用户余额")
        return text.strip("元")