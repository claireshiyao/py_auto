# author by claire
import logging
import pytest
from common import logger
from page_objects.bid_page import BidPage
from page_objects.home_page import HomePage
from page_objects.user_page import UserPage
from test_datas import invest_datas as ids

pytestmark = pytest.mark.invest
@pytest.fixture
def init(init_login):
    logging.info("invest测试用例自己的前置")
    bidpage = BidPage(init_login)
    # 1. 首页：选第一个标
    HomePage(init_login).click_first_bid()
    yield init_login, bidpage
    logging.info("invest测试用例自己的后置")


@pytest.mark.usefixtures("init")
class TestInvest:

    def test_invest_success(self, init):
        logging.info("投资功能-正常场景用例：投资1000元成功。用户可用余额减少1000，标余额减少1000")
        # 2. 标页面-获取投资前用户余额
        user_left_money_before_invest = init[1].get_user_left_money()
        # 3. 获取投资前标的余额
        bid_left_money_before_invest = init[1].get_bid_left_money()
        # 4. 投资1000元
        init[1].invest_and_click(ids.success['money'])
        # 5. 投标成功，点击激活按钮
        init[1].click_active_button()

        # 6. 个人页面-投资后用户余额
        user_left_money_after_invest = UserPage(init[0]).get_user_money().strip("元")
        # 7. 断言投资后用户余额是否少了1000元
        try:
            assert ids.success['money'] == int(float(user_left_money_before_invest) - float(user_left_money_after_invest))
        except:
            logging.exception("断言失败,投资后用户余额未减少所投资的金额")
            raise

        # 8. 回退到标页面并刷新
        init[0].back()
        init[0].refresh()
        # 9. 标页面-投资后标的余额
        bid_left_money_after_invest = init[1].get_bid_left_money()
        # 10. 断言投资后标的余额是否少了1000元
        try:
            assert ids.success['money'] == int((float(bid_left_money_before_invest) - float(bid_left_money_after_invest)) * 10000)
        except:
            logging.exception("断言失败,投资后标的可投余额未减少所投资的金额")
            raise

    @pytest.mark.parametrize("invalid", ids.invalid_invest_money)
    def test_invest_failed(self, invalid, init):
        logging.info("投资功能-异常场景用例：投资金额为负数，空，0，10的倍数但不是100的倍数。用户可用余额减少1000，标余额减少1000")
        # 2. 标页面-获取投资前用户余额
        user_left_money_before_invest = init[1].get_user_left_money()
        # 3. 获取投资前标的余额
        bid_left_money_before_invest = init[1].get_bid_left_money()
        # 4. 输入投资金额，点击投标按钮
        init[1].invest_and_click(invalid['money'])
        # 5. 获取弹出框错误信息
        error_msg = init[1].get_error_msg_from_popup_and_close()
        # 6. 刷新当前页面，获取用户余额、标余额
        init[0].refresh()
        user_left_money_after_invest = init[1].get_user_left_money()
        bid_left_money_after_invest = init[1].get_bid_left_money()
        # 7. 断言:投资失败弹出框中的错误提示信息是否正确；标的金额不变；用户的余额也不变
        assert invalid['check'] == error_msg
        assert user_left_money_before_invest == user_left_money_after_invest
        assert bid_left_money_before_invest == bid_left_money_after_invest


if __name__ == '__main__':
    pytest.main()




