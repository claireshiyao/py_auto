# author by claire
import time

from selenium.webdriver.common.keys import Keys

from common.basepage import BasePage
from common.upload import upload
from page_locators.chat_page_locs import ChatPageLocs as locs


class ChatPage(BasePage):
    def select_class_and_find_xiaojian(self):
        self.click_element(locs.contact_button, "聊天页面-点击联系人按钮")
        self.click_element(locs.web_practise_list, "聊天页面-点击web实战班级")
        self.click_element(locs.Xiaojian_avatar, "聊天页面-点击小简头像")

    def send_text(self, message):
        self.input_text(locs.text_input, message, "聊天页面-输入消息文本")
        self.click_element(locs.send_button, "聊天页面-点击发送按钮")

    def send_file(self, filepath):
        self.click_element(locs.attachment_button, "聊天页面-点击附件按钮")
        time.sleep(3)
        upload(filepath)

    def keyboard_send(self, message):
        ele = self.get_element(locs.text_input, "聊天页面-获取聊天文本输入框元素")
        ele.send_keys(message, Keys.CONTROL, Keys.ENTER)

    def get_message_text(self):
        self.wait_element_exists(locs.message_text, "聊天页面-等待发送的消息文本存在")
        eles = self.get_elements(locs.message_text, "聊天页面-获取发送的消息文本元素")
        if len(eles) > 0:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            print(eles_list)
            return eles_list

    def check_file_download_exists(self):
        try:
            self.wait_element_exists(locs.download_link, "聊天页面-等待文件下载链接元素存在")
        except:
            return False
        else:
            return True

    def search_xiaojian(self, name):
        self.input_text(locs.search_input, name, "聊天页面-搜索框内输入文本")
        self.click_element(locs.search_xiaojian_avatar, "聊天页面-搜索后点击小简头像")

    def select_lately_message_and_click_xiaojian(self):
        self.click_element(locs.lately_button, "聊天页面-点击最近消息按钮")
        self.click_element(locs.lately_message_xiaojian_avatar, "聊天页面-点击最近消息中小简头像")

    def check_xiaojian_avatar_in_lately_message(self):
        self.click_element(locs.lately_button, "聊天页面-点击最近消息按钮")
        try:
            self.wait_element_visible(locs.lately_message_xiaojian_avatar, "聊天页面-点击最近消息中小简头像")
        except:
            return False
        else:
            return True

    def get_send_error_tip(self):
        self.wait_element_visible(locs.error_tip, "聊天页面-等待发送错误提示元素可见")
        eles = self.get_elements(locs.error_tip, "聊天页面-获取发送错误提示文本元素")
        if len(eles) == 1:
            return eles[0].text
        if len(eles) > 1:
            eles_list = []
            for ele in eles:
                eles_list.append(ele.text)
            return eles_list

    def click_send_button(self):
        self.click_element(locs.send_button, "聊天页面-点击发送按钮")



