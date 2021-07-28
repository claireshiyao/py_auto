# author by claire
import logging
import time

import pytest

from page_objects.chat_page import ChatPage
from page_objects.class_page import ClassPage
from test_datas import chat_page_data as cds
from test_datas.class_page_data import join_success
from page_locators.chat_page_locs import ChatPageLocs as locs

@pytest.fixture
def init_chat(init_login):
    logging.info("chat用例自己的前置")
    ClassPage(init_login).join_class(join_success["captcha"])
    init_login.refresh()
    ClassPage(init_login).enter_chat_page()
    cp = ChatPage(init_login)
    yield init_login, cp
    logging.info("chat用例自己的后置")

@pytest.mark.usefixtures("init_chat")
class TestChat:

    def test_select_contact_in_class(self, init_chat):
        logging.info("测试选择班级联系人聊天正常场景")
        init_chat[1].select_class_and_find_xiaojian()
        init_chat[1].send_text(cds.chat_text_message)
        init_chat[0].refresh()
        try:
            assert init_chat[1].get_message_text()[-1] == cds.chat_text_message
        except:
            logging.exception("选择班级联系人聊天正常场景，文本消息发送断言失败")
            raise

    def test_send_by_keyboard(self, init_chat):
        logging.info("测试键盘快捷键发送消息正常场景")
        init_chat[1].select_class_and_find_xiaojian()
        init_chat[1].keyboard_send(cds.keyboard_message)
        init_chat[0].refresh()
        try:
            assert init_chat[1].get_message_text()[-1] == cds.keyboard_message
        except:
            logging.exception("键盘快捷键发送消息正常场景，消息发送断言失败")
            raise


    def test_search_contact_and_chat(self, init_chat):
        logging.info("测试搜索联系人聊天正常场景")
        init_chat[1].search_xiaojian("小简")
        init_chat[1].send_text(cds.search_message)
        init_chat[0].refresh()
        try:
            assert init_chat[1].get_message_text()[-1] == cds.search_message
        except:
            logging.exception("搜索联系人聊天正常场景，文本消息发送断言失败")
            raise

    # @pytest.mark.smoke
    def test_send_file(self, init_chat):
        logging.info("测试聊天附件发送正常场景")
        init_chat[1].send_file(cds.chat_file_path)
        time.sleep(3)
        init_chat[0].refresh()
        try:
            assert init_chat[1].check_file_download_exists()
        except:
            logging.exception("聊天附件发送正常场景，附件发送断言失败")
            raise

    def test_chat_in_lately_message(self, init_chat):
        logging.info("测试最近消息聊天正常场景")
        init_chat[1].select_class_and_find_xiaojian()
        init_chat[1].send_text(cds.chat_text_message)
        init_chat[0].refresh()
        try:
            assert init_chat[1].check_xiaojian_avatar_in_lately_message()
        except:
            logging.exception("最近消息聊天正常场景，最近消息未找到头像，断言失败")
            raise
        try:
            init_chat[1].select_lately_message_and_click_xiaojian()
            init_chat[1].send_text(cds.lately_message)
            init_chat[0].refresh()
            assert init_chat[1].get_message_text()[-1] == cds.lately_message
        except:
            logging.exception("最近消息聊天正常场景，文本消息发送断言失败")
            raise

    @pytest.mark.smoke
    def test_send_empty_message(self, init_chat):
        logging.info("测试发送消息为空异常场景")
        init_chat[1].select_class_and_find_xiaojian()
        init_chat[1].click_send_button()
        try:
            assert init_chat[1].get_send_error_tip() == cds.error_tip
        except:
            logging.exception("发送消息为空异常场景，断言失败")
            raise






