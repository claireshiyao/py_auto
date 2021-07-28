import pytest

# pytestmark = pytest.mark.nmb

def aaa():
    pass


# @pytest.mark.nmb
class TestAA:

    # pytestmark = pytest.mark.nmb

    def test_bbb(self):
        print("bbbb")
        self.bbb()
        assert "hello" == "World!"

    @pytest.mark.demo
    def test_hello_pytest(self):
        print("hello,pytest!!!")

    def bbb(self):
        print("*************88")



@pytest.mark.demo
def test_aaa():
    print("aaaaaaa")
    assert True