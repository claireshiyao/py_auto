# author by claire
from common.basepage import BasePage
from page_locators.user_page_locs import UserPageLocs as locs

class UserPage(BasePage):


    # 11、获取用户余额
    def get_user_money(self):
        return self.get_ele_text(locs.user_left_money, "个人页面-获取用户余额")
