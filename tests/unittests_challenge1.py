import unittest
import challenge1 as c1


class TestPractice(unittest.TestCase):

    def test_sort_elements(self):
        result = c1.sort_elements([1054, 3.14, -1, 27, 69005])
        expected = [-1, 3.14, 27, 1054, 69005]
        self.assertEqual(result, expected)
        result = c1.sort_elements([])
        self.assertEqual(result, [])

    def test_sort_unique(self):
        result = c1.sort_elements([1054, 3.14, -1, 27, 3.14, -1, 69005])
        expected = [-1, 3.14, 27, 1054, 69005]
        self.assertEqual(result, expected)
        result = c1.sort_unique([])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
