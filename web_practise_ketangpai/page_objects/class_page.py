# author by claire
import time

from common.basepage import BasePage
from page_locators.class_page_locs import ClassPageLocs as locs

class ClassPage(BasePage):


    def join_class(self, class_code):
        self.click_element(locs.join_class_link, "课堂页面-点击加入课程")
        self.input_text(locs.class_captcha_input, class_code, "课堂页面-输入加课验证码")
        self.click_element(locs.join_button, "课堂页面-点击加入")

    def get_join_error_tip(self):
        self.wait_element_visible(locs.join_error_tip, "课堂页面-等待加课验证码错误提示元素可见")
        eles = self.get_elements(locs.join_error_tip, "课堂页面-获取加课验证码错误提示元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list

    def get_password_error_tip(self):
        self.wait_element_visible(locs.login_password_error_tip, "课堂页面-等待登录密码错误提示元素可见")
        eles = self.get_elements(locs.login_password_error_tip, "课堂页面-获取登录密码错误提示元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list

    def drop_class_and_confirm(self, password):
        self.click_element(locs.select_more_link, "课堂页面-点击web实战班级的更多元素")
        self.click_element(locs.drop_class_link, "课堂页面-点击退课链接元素")
        self.input_text(locs.login_password_input, password, "课堂页面-输入退课需验证的登录密码")
        self.click_element(locs.drop_class_confirm_button, "课堂页面-点击退课确认按钮")

    def drop_class_and_cancel(self, password):
        self.click_element(locs.select_more_link, "课堂页面-点击web实战班级的更多元素")
        self.click_element(locs.drop_class_link, "课堂页面-点击退课链接元素")
        self.input_text(locs.login_password_input, password, "课堂页面-输入退课需验证的登录密码")
        self.click_element(locs.drop_class_cancel_button, "课堂页面-点击退课取消按钮")

    def enter_class(self):
        self.click_element(locs.class_name_link, "课堂页面-点击web实战班级链接元素")

    def get_join_success_tip(self):
        self.wait_element_visible(locs.join_success_tip, "课堂页面-等待加课成功提示元素可见")
        eles = self.get_elements(locs.join_success_tip, "课堂页面-获取加课成功提示元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list

    def get_drop_success_tip(self):
        self.wait_element_visible(locs.drop_success_tip, "课堂页面-等待退课成功提示元素可见")
        eles = self.get_elements(locs.drop_success_tip, "课堂页面-获取退课成功提示元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list

    def check_class_title_visible(self):
        try:
            self.wait_element_visible(locs.class_name_link, "课堂页面-等待课堂标题元素可见")
        except:
            return False
        else:
            return True

    def check_grade_visible(self):
        try:
            self.wait_element_visible(locs.grade_link, "课堂页面-等待成绩链接元素可见")
        except:
            return False
        else:
            return True

    def enter_chat_page(self):
        self.click_element(locs.chat_button, "课堂页面-点击私信按钮进入聊天页面")
        self.switch_to_new_window("切换到私信页面新窗口")




