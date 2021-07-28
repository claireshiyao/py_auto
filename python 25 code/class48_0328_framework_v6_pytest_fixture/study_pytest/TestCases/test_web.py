import pytest
from selenium import webdriver




@pytest.fixture(scope="class")
def mycc():
    print("======我是类级别的前置！！，开始======")
    yield
    print("======我是类级别的后置，再见======")




# 测试用例
# def test_baidu():
#     print("1111111111111111111111111")
#
# @pytest.mark.usefixtures("init")
# def test_taobao():
#     print("taobao.......")


# @pytest.mark.usefixtures("init")  # 夹的是测试函数 #
@pytest.mark.usefixtures("mycc")  # 夹的是测试类
class TestAA:


    def test_aa(self):
        print("***********  test_aa  ***********")

    # @pytest.mark.usefixtures("init")
    def test_bb(self):
        print("***********test_bb***********")

    def test_baidu(self,init):  # init = driver对象 # init = (driver,True)
        print("baidu.......")
        init.find_element_by_id("kw").send_keys("nmb")

    # 假设这个类下面，有10个用例，只有1个用例的前置后置不太一样，你会怎么处理？
    # 拎取出来当成函数。

