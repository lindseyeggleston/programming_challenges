'''
Unittest for Challenge 2
To run the test in the terminal, go to root directory (programming_challenges/)
and run `make two`
'''

import unittest
from programming_challenges import challenge2 as c2


class TestPractice(unittest.TestCase):

    def test_fizz_buzz(self):
        result = c2.fizz_buzz(30)
        answer = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11,
                  'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz',
                  'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29,
                  'FizzBuzz']
        self.assertEqual(result, answer)

    def test_find_prime(self):
        result = c2.find_prime(1)
        self.assertEqual(result, [])
        result = c2.find_prime(97)
        answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(result, answer)

    def test_fibonacci_sequence(self):
        result = c2.fibonacci_sequence(1)
        self.assertEqual(result, 1)
        result = c2.fibonacci_sequence(2)
        self.assertEqual(result, 1)
        result = c2.fibonacci_sequence(4)
        self.assertEqual(result, 3)
        result = c2.fibonacci_sequence(12)
        self.assertEqual(result, 144)


if __name__ == '__main__':
    unittest.main()
