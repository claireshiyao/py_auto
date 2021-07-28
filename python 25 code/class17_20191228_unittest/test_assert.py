"""

断言方式:
assertTrue, 判断条件
assertEqual,
assertGreater,   a > b
assertIn,  a in b
self.assertRegex(), 正则表达式匹配
"""
import unittest


class TestLogin(unittest.TestCase):
    def test_login_success(self):
        #
        expected = 1
        actual = 2

        # 提示方式更加具体，会把预期结果和实际结果打印出来
        # self.assertEqual(expected, actual)

        # self.assertTrue( expected == actual)

        self.assertGreater(expected, actual)
        self.assertRegex()


if __name__ == '__main__':
    unittest.main()