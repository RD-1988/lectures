import unittest
import leading

class testleadingsubstring(unittest.TestCase):
    '''Tests for leading_substrings.'''

    def test_leading_bear(self):
        inputted = "bear"
        output = leading.leading_substrings(inputted)
        output_expected = ['b', 'be', 'bea', 'bear']
        self.assertEqual(output_expected, output, "test on bear fails")


    def test_leading_empty(self):
        inputted = ""
        output = leading.leading_substrings(inputted)
        output_expected = []
        self.assertEqual(output_expected, output, "")



