import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    """
    Test that it can sum a list of integers
    """
    def test_list_int(self):
        result = sum([1, 2, 3])
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of Fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)    

    
if __name__ == '__main__':
    unittest.main()


