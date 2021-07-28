# author by claire
import time

from selenium.webdriver import ActionChains

from common.basepage import BasePage
from common.upload import upload
from page_locators.homework_page_locs import HomeworkPageLocs as locs
from page_locators.class_page_locs import ClassPageLocs as cls

class HomeworkPage(BasePage):
    def enter_class_and_turn_to_homework(self):
        self.click_element(cls.class_name_link, "课堂页面-点击班级链接")
        self.click_element(locs.homework_page_link, "班级页面-点击作业页面链接")

    def click_homework_link(self):
        self.click_element(locs.homework_link, "作业页面-点击作业链接")

    def click_update_button_and_confirm(self):
        self.click_element(locs.update_button, "作业页面-点击更新提交按钮")
        self.click_element(locs.update_confirm_button, "作业页面-点击更新提交确定按钮")

    def upload_homework(self, filepath):
        # ele = self.get_element(locs.add_homework_button, "作业页面-获取添加作业按钮元素")
        # self.scroll_into_view(ele)
        self.click_element(locs.add_homework_button, "作业页面-点击添加作业按钮")
        time.sleep(3)
        upload(filepath)

    def leave_a_message(self, message):
        self.execute_js_script("document.getElementById(\"mess1\").style.display='block';", "修改留言框display属性")
        ele1 = self.get_element(locs.message_input, "作业页面-获取留言输入框元素")
        # self.driver.execute_script("arguments[0].scrollIntoView(false)", ele)
        self.execute_js_script("var a = arguments[0]; a.value = arguments[1];", ele1, message, "修改留言框属性文本")
        ele2 = self.get_element(locs.message_save, "作业页面-获取留言保存按钮元素")
        ActionChains(self.driver).move_to_element(ele2).click().perform()


    def submit_and_confirm(self):
        self.click_element(locs.submit_button, "作业页面-点击提交按钮")
        self.click_element(locs.submit_confirm_button, "作业页面-点击知道了")

    def check_add_homework_exists(self):
        try:
            self.wait_element_visible(locs.add_homework_button, "作业页面-等待添加作业元素可见")
        except:
            return False
        else:
            return True

    def check_homework_status(self):
        self.wait_element_visible(locs.homework_status, "作业页面-等待作业状态按钮元素可见")
        eles = self.get_elements(locs.homework_status, "作业页面-获取作业状态按钮元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list

    def check_download_exists(self):
        try:
            self.wait_element_visible(locs.download_link, "作业页面-等待作业下载链接元素可见")
        except:
            return False
        else:
            return True





