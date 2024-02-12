# unittest
- ClassName should conventionally start with Test in Pascal Case
- Methods which are used to name your test cases should start with test_
- The test runner will run all methods which start with test_

## Example
'''import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 4, "Should be 4")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 5")

if __name__ == '__main__':
    # Here you call the unittest differently by mentioning unittest.main()
    unittest.main()  
    '''



