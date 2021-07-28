# author by claire

import logging

import pytest
from common.random_string import generate_random_string
from page_objects.material_format_page import MaterialFormatPage


@pytest.fixture
def init(init_login):
    logging.info("素材格式测试用例自己的前置")
    mp = MaterialFormatPage(init_login)
    yield init_login, mp
    logging.info("素材格式测试用例自己的后置")

@pytest.mark.usefixtures("init")
class TestMaterialFormat:
    @pytest.mark.smoke
    def test_delete(self, init):
        init[1].enter_material_format_iframe()
        init[1].delete_record()
        assert init[1].get_tip() == "操作成功"


    def test_add(self, init):
        name = generate_random_string(6)
        init[1].enter_material_format_iframe()
        init[1].add_record(name)
        assert init[1].get_tip() == "操作成功"






