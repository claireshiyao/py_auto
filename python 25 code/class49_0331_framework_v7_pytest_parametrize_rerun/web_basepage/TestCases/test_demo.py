import pytest

pytestmark = pytest.mark.demo

# @pytest.mark.usefixtures("myMo")
def test_aa():
    print("11111111111111111111")



class Testaa:



    def test_demo(self):
        print("demo")

    def test_bb(self):
        print("bb")

    def test_false(self):
        print("====== 我是失败的用例 +++=====")
        assert False

