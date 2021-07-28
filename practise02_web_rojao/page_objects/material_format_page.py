# author by claire
import time

from selenium.webdriver.remote.webdriver import WebDriver

from common.basepage import BasePage
from page_locators.material_format_page_locs import MaterialFormatPageLocs as locs
from page_locators.home_page_locs import HomePageLocs as hlocs

class MaterialFormatPage(BasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_material_format_iframe(self):
        self.click_element(hlocs.Ads_management, "点击广告管理")
        self.click_element(locs.meterial_format, "点击素材格式")
        self.switch_to_iframe(locs.meterial_format_iframe, "切换至素材格式iframe")

    def delete_record(self):
        self.click_element(locs.check_box, "点击复选框")
        self.click_element(locs.delete_button, "点击删除按钮")
        self.driver.switch_to.default_content()
        self.click_element(locs.confirm_button, "点击确定按钮")
        time.sleep(3)
        self.click_element(locs.confirm_button, "点击确定按钮")

    def add_record(self, name):
        self.click_element(locs.add_button, "点击新增")
        self.input_text(locs.meterial_format_name, name, "输入素材格式名称")
        self.click_element(locs.material_type, "勾选文字素材类型")
        self.click_element(locs.add_confirm, "点击确定")
        time.sleep(3)
        self.click_element(locs.add_confirm, "点击确定")
        time.sleep(3)
        self.driver.switch_to.default_content()

    def get_tip(self):
        self.wait_element_visible(locs.tip, "等待提示元素可见")
        eles = self.get_elements(locs.tip, "获取提示文本元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list


