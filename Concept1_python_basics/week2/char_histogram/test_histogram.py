import unittest
from histogram import histogram


class TestHistogram(unittest.TestCase):
    def test_histogram(self):
        tests = [(histogram(""), {}),
            (histogram("    "), {' ': 4}),
            (histogram("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}),
            (histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3}),
            (histogram("Some very long string here with different casing"),
            {
                'S': 1,
                'o': 2,
                'm': 1,
                'e': 6,
                ' ': 7,
                'v': 1,
                'r': 4,
                'y': 1,
                'l': 1,
                'n': 4,
                'g': 3,
                's': 2,
                't': 3,
                'i': 4,
                'h': 2,
                'w': 1,
                'd': 1,
                'f': 2,
                'c': 1,
                'a': 1
            })]

        for actual, expected in tests:
            with self.subTest(f'Expected: {expected}'):
                self.assertEqual(actual, expected)
       
if __name__ == '__main__':
    unittest.main()




