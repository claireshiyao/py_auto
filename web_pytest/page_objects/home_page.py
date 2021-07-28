# author by claire

from common.basepage import BasePage
from page_locators.home_page_locs import HomePageLocs as locs


class HomePage(BasePage):

    # 退出链接是否存在
    def check_exit_link_exists(self):
        try:
            self.wait_element_visible(locs.exit_link, "主页面-等待退出链接可见")
        except:
            return False
        else:
            return True

    # 点击第一个竞标项目进行抢投标
    def click_first_bid(self):
        self.click_element(locs.bid_button, "主页面-点击抢投标按钮")



