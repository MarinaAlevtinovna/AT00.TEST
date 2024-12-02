import unittest

from main import add, subtract, divide, multiply

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertEqual(divide(4, 2), (2, 0))
        self.assertEqual(divide(20, 5), (4, 0))
        self.assertNotEqual(divide(4, 2), (3, 0))

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)



if __name__ == '__main__':
    unittest.main()