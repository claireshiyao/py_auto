#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 17:37

from APP_Framework.Common.basepage import BasePage
from APP_Framework.PageLocators.userPage_locator import UserPageLocator as loc

from APP_Framework.Common import logger
import logging

class UserPage(BasePage):

    # 获取收藏的数目
    def get_favirate_counts(self):
        counts = self.get_text(loc.fav_count_loc, "个人页面_收藏题目个数")
        logging.info("用户当前的收藏的题目数量为：{}".format(counts))
        return counts

    # 进入收藏列表当中 - 进入第一个题库中
    def click_favirated_counts_link(self):
        self.click_element(loc.fav_count_loc,"个人页面_点击收藏题目个数")

    # 点击收藏的题库列表当中，第一个题库类型
    def click_favirated_first_tiku_type(self):
        self.click_element(loc.fav_tiku_type_loc,"个人页面_收藏的题库类别_点击第1个题库类")



