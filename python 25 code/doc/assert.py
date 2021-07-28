import unittest

class TestRegister(unittest.TestCase):
    def test_register(self):
        self.assertIn("'mobile_phone': '13595271250'", "{'mobile_phone': '13595271250', 'pwd': None}")

if __name__ == '__main__':
    unittest.main
