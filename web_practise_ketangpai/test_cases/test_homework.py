import logging
import time

import pytest

from page_objects.homework_page import HomeworkPage
from page_objects.class_page import ClassPage
from test_datas.class_page_data import join_success
from test_datas.homework_page_data import homework_upload_path

class TestHomework:
    @pytest.fixture
    def init_homework(self, init_login):
        logging.info("homework用例自己的前置")
        ClassPage(init_login).join_class(join_success["captcha"])
        init_login.refresh()
        hp = HomeworkPage(init_login)
        hp.enter_class_and_turn_to_homework()
        yield init_login, hp
        logging.info("homework用例自己的后置")

    @pytest.mark.usefixtures("init_homework")
    class TestHomework:
        def test_upload_homework(self, init_homework):
            init_homework[1].click_homework_link()
            if init_homework[1].check_add_homework_exists() == False:
                init_homework[1].click_update_button_and_confirm()
                init_homework[1].upload_homework(homework_upload_path)
            else:
                init_homework[1].upload_homework(homework_upload_path)
            time.sleep(3)
            init_homework[1].leave_a_message("作业已完成")
            init_homework[1].submit_and_confirm()
            try:
                assert init_homework[1].check_download_exists()
            except:
                logging.exception("上传作业正常场景，下载元素不可见断言失败")
                raise
            init_homework[0].back()
            try:
                assert init_homework[1].check_homework_status() == "已提交"
            except:
                logging.exception("上传作业正常场景，作业状态断言失败")
                raise
            init_homework[1].click_homework_link()


if __name__ == '__main__':
    pytest.main()
