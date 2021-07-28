#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xiaojian
# Time: 2019/3/18 17:28

from APP_Framework.Common.basepage import BasePage
from APP_Framework.PageLocators.tikuPage_locator import TikuPageLocator as loc

import time
import random


class TikuPage(BasePage):
    tiku_type_name = None  # 所选的题库类型名称

    # 选择题库类型
    def select_tiku_type_by_random(self):
        # 获取当前页面的所有题库
        self.wait_ele_visible(loc.titu_type_loc, "题库列表页面_等待题库列表可见")
        time.sleep(0.5)
        type_eles = self.get_element(loc.titu_type_loc, "题库列表页面_获取当前页面所有题库类型", find_all=True)
        # 随机题库类型 - 生成随机数
        index = random.randint(0, len(type_eles) - 1)
        self.tiku_type_name = type_eles[index].text  # 获取题库名称
        # 元素定位替换
        tiku_title_loc = (loc.tiku_title_loc[0], loc.tiku_title_loc[1].format(self.tiku_type_name))
        # 点击对应的题库，进入题库。若题库类型不在当前页面，需要滚动操作。
        self.click_element(tiku_title_loc, "题库列表页面_点击题库类型进入题目难度页面")

    # 选择题目难度等级
    def select_topic_level_by_random(self):
        """
        :param level_name:初级、中级、高级
        :return:None
        """
        level_name = ["初级", "中级", "高级"]
        index = random.randint(0, len(level_name) - 1)
        self.wait_ele_visible(loc.firstLevel_loc, "题目难度页面_等待难度级别出现")
        if level_name[index] == "初级":
            self.click_element(loc.firstLevel_loc, "题目难度页面_选择初级难度")
        elif level_name[index] == "中级":
            self.click_element(loc.secondLevel_loc, "题目难度页面_选择中级难度")
        elif level_name[index] == "高级":
            self.click_element(loc.thirdLevel_loc, "题目难度页面_选择高级难度")

    # 随机选择套题
    def select_topic_suite_by_random(self):
        self.wait_ele_visible(loc.suite_title_loc, "套题页面_等待套题元素出现")
        time.sleep(0.5)
        # 获取当前所有的套题数
        suites = self.get_element(loc.suite_title_loc, "套题页面_获取当前页面所有套题", find_all=True)
        index = random.randint(0, len(suites) - 1)
        # 随便选择一套并点击
        suites[index].click()

    # 获取题目的小标题内容
    def get_topic_small_title(self):
        self.wait_ele_visible(loc.topic_small_title, "题目页面_等待题目小标题可见")
        return self.get_text(loc.topic_small_title,"题目页面_获取题目小标题")

    # 收藏开关操作 - 点击收藏按钮
    def click_favirate_button(self):
        self.wait_ele_visible(loc.favirate_switch_loc, "题目页面_等待收藏开关可见")
        self.click_element(loc.favirate_switch_loc, "题目页面_点击收藏开关")

    # 获取收藏成功的提示信息
    def get_favirage_ok_msg(self):
        pass

    # 获取取消收藏的提示信息
    def get_cancel_favirate_msg(self):
        pass

    # 答案开关操作 - 点击答案按钮
    def click_answer_button(self):
        self.wait_ele_visible(loc.answer_switch_loc, "topic页面_等待答案开关可见")
        self.click_element(loc.answer_switch_loc, "topic页面_点击答案开关")

    # 答案区域是否呈现 - 是为True,否为False
    def answerArea_is_visibled(self):
        try:
            self.wait_ele_visible(loc.answer_content_loc, 'topic页面_等待答案内容呈现', 7)
        except:
            return False
        else:
            return True


