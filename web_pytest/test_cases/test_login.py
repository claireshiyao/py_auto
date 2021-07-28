# author by claire
import logging
import pytest

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from test_datas.login_datas import login_success_data as success
from test_datas.login_datas import login_wrong_data as wrong
from test_datas.login_datas import login_wrong_account as wrong_account

pytestmark = pytest.mark.login
@pytest.fixture
def init(init_driver):
    logging.info("login测试用例自己的前置")
    lp = LoginPage(init_driver)
    yield init_driver, lp
    logging.info("login测试用例自己的后置")

@pytest.mark.usefixtures("init")
class TestLogin:

    def test_login_success(self, init):
        logging.info("登录功能正常场景用例：登录成功")
        init[1].login(success['user'], success['passwd'])
        try:
            assert HomePage(init[0]).check_exit_link_exists()
            assert init[0].current_url == success["check"]
        except:
            logging.exception("登录断言失败")

    @pytest.mark.parametrize("case", wrong)
    def test_login_failed(self, case, init):
        logging.info("登录功能异常场景用例：用户名为空/密码为空/用户名格式不正确")
        init[1].login(case["user"], case["passwd"])
        try:
            assert case["check"] == init[1].get_error_msg()
        except:
            logging.exception("登录断言失败，表单提示信息错误")

    @pytest.mark.parametrize("casew", wrong_account)
    def test_login_failed_wrong_account(self, casew, init):
        logging.info("登录功能异常场景用例：用户名不存在/密码错误")
        init[1].login(casew["user"], casew["passwd"])
        try:
            assert casew["check"] == init[1].get_error_hint()
        except:
            logging.exception("登录断言失败，登录弹出框提示信息错误")

if __name__ == '__main__':
    pytest.main



