# author by claire
from common.basepage import BasePage
from page_locators.bid_page_locs import BidPageLocs as locs


class BidPage(BasePage):

    # 标页面-获取用户可用余额
    def get_user_left_money(self):
        return self.get_ele_attribute(locs.money_input, "data-amount", "标页面-获取用户余额属性")

    # 获取标的可投余额
    def get_bid_left_money(self):
        return self.get_ele_text(locs.bid_left_money, "标页面-获取标的可投余额")

    # 输入投资金额，点击投标
    def invest_and_click(self, amount):
        self.input_text(locs.money_input, amount, "标页面-输入投资金额")
        self.click_element(locs.invest_button, "标页面-点击投标按钮")

    # 投资成功，出现弹框，点击激活按钮
    def click_active_button(self):
        self.click_element(locs.active_button, "标页面-点击激活按钮")

    def get_error_msg_from_popup_and_close(self):
        msg = self.get_ele_text(locs.bid_failed_popup, "标页面-获取投资失败弹框错误信息")
        self.click_element(locs.bid_failed_close_popup, "标页面投资失败弹框-点击确定按钮关闭弹框")
        return msg
