import unittest

from src.KataClass import KataClass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        kata_class = KataClass()
        kata_sum = kata_class.add(1, 1)
        self.assertEqual(2, kata_sum)  # add assertion here


if __name__ == '__main__':
    unittest.main()
