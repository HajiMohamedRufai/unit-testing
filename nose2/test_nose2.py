import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 2, 3)

if __name__ == '__main__':
    unittest.main()
