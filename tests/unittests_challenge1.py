'''
Unittest for Challenge 1
To run the test in the terminal, go to root directory (programming_challenges/)
and run `make test1`
'''

import unittest
from src import challenge1 as c1


class TestPractice(unittest.TestCase):

    def test_sort_elements(self):
        result = c1.sort_elements([1054, 3.14, -1, 27, 3.14, -1, 69005])
        answer = [-1, -1, 3.14, 3.14, 27, 1054, 69005]
        self.assertEqual(result, answer)
        result = c1.sort_elements([])
        self.assertEqual(result, [])

    def test_sort_unique(self):
        result = c1.sort_unique([1054, 3.14, -1, 27, 3.14, -1, 69005])
        answer = [-1, 3.14, 27, 1054, 69005]
        self.assertEqual(result, answer)
        result = c1.sort_unique([])
        self.assertEqual(result, [])

    def test_sort_mixed_type(self):
        result = c1.sort_mixed_type([])
        self.assertEqual(result, [])
        result = c1.sort_mixed_type([1054, '3.14', -1, 27, 3.14, '-1', '69005'])
        answer = [-1, '-1', 3.14, '3.14', 27, 1054, '69005']
        self.assertEqual(result, answer)

    def test_is_palidrome(self):
        result = c1.is_palindrome('abba')
        self.assertTrue(result)
        result = c1.is_palindrome('ratsliveonoevilstar')
        self.assertTrue(result)
        result = c1.is_palindrome('elephant')
        self.assertTrue(not result)

    def test_reverse(self):
        result = c1.reverse('elephant')
        self.assertEqual(result, 'tnahpele')
        result = c1.reverse(list(range(10)))
        self.assertEqual(result, list(range(9, -1, -1)))
        result = c1.reverse([1054, '3.14', -1, 27, 3.14, '-1', '69005'])
        answer = ['69005', '-1', 3.14, 27, -1, '3.14', 1054]
        self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()
