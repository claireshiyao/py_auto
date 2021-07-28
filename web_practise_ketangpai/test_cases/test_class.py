# author by claire
import logging

import pytest

from page_objects.class_page import ClassPage
from test_datas import class_page_data as cds


@pytest.fixture
def init(init_login):
    logging.info("class测试用例自己的前置")
    lp = ClassPage(init_login)
    yield init_login, lp
    logging.info("class测试用例自己的后置")


@pytest.mark.usefixtures("init")
class TestClass:
    # @pytest.mark.smoke
    def test_join_class_success(self, init):
        logging.info("测试加课功能正常场景用例：加课成功")
        # 确认未加入该班级，如果已加入，则先退课
        class_exist = init[1].check_class_title_visible()
        if class_exist == True:
            init[1].drop_class_and_confirm(cds.drop_success["password"])
        init[0].refresh()
        init[1].join_class(cds.join_success["captcha"])
        try:
            assert init[1].get_join_success_tip() == cds.join_success["check"]
            assert init[1].check_class_title_visible() == True
        except:
            logging.exception("加课成功场景用例，断言失败")
            raise

    # @pytest.mark.smoke
    def test_repeat_join_class(self, init):
        logging.info("测试重复加入同一课程场景用例")
        # 如果未加入该课程，前置先加入该课程
        if init[1].check_class_title_visible() == True:
            init[1].join_class(cds.join_success["captcha"])
        else:
            init[1].join_class(cds.join_success["captcha"])
            init[0].refresh()
            init[1].join_class(cds.join_success["captcha"])
        try:
            assert init[1].get_join_error_tip() == cds.repeat_join["check"]
        except:
            logging.exception("重复加入同一课程用例，断言失败")
            raise

    @pytest.mark.parametrize("fail", cds.join_fail)
    def test_join_class_fail(self, fail, init):
        logging.info("测试加课正常场景用例：加课失败")
        init[1].join_class(fail["captcha"])
        try:
            assert init[1].get_join_error_tip() == fail["check"]
        except:
            logging.exception("加课反向用例场景用例，断言失败")
            raise

    def test_drop_class_success(self, init):
        logging.info("测试退课功能正常场景用例：退课成功")
        init[1].join_class(cds.join_success["captcha"])
        init[0].refresh()
        init[1].drop_class_and_confirm(cds.drop_success["password"])
        try:
            assert init[1].get_drop_success_tip() == cds.drop_success["check"]
            assert init[1].check_class_title_visible() == False
        except:
            logging.exception("退课成功场景用例，断言失败")
            raise

    @pytest.mark.parametrize("fail", cds.drop_fail)
    def test_drop_class_fail(self, fail, init):
        logging.info("测试退课失败场景用例：退课失败")
        init[1].join_class(cds.join_success["captcha"])
        init[0].refresh()
        init[1].drop_class_and_confirm(fail["password"])
        try:
            assert init[1].get_password_error_tip() == fail["check"]
            init[0].refresh()
            assert init[1].check_class_title_visible() == True
        except:
            logging.exception("退课反向用例场景，断言失败")
            raise

    def test_drop_class_cancel(self, init):
        logging.info("测试退课功能取消正常场景用例：退课取消成功")
        init[1].join_class(cds.join_success["captcha"])
        init[0].refresh()
        init[1].drop_class_and_cancel(cds.drop_success["password"])
        try:
            assert init[1].check_class_title_visible() == True
        except:
            logging.exception("退课取消成功场景用例，断言失败")
            raise

    def test_enter_class(self, init):
        logging.info("测试进入班级功能正常场景用例")
        init[1].join_class(cds.join_success["captcha"])
        init[0].refresh()
        init[1].enter_class()
        try:
            assert init[1].check_grade_visible() == True
        except:
            logging.exception("进入班级功能成功场景用例，断言失败")
            raise

if __name__ == '__main__':
    pytest.main()







