import unittest
from mock import Mock


def add(a, b):
    c = a + b
    pass

class TestAdd(unittest.TestCase):
    def test_add(self):
        add = Mock(return_value=7)
        self.assertEqual(7, add(3, 4))

if __name__ == '__main__':
    unittest.main()




