import unittest

import HomeWork7

class TestFizzBuzz(unittest.TestCase):

    def test_with_range(self):
        self.assertEqual(HomeWork7.fizzbuzz(range(1, 21)),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                          'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                          'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz'])

    def test_normal(self):
        self.assertEqual(HomeWork7.fizzbuzz([1, 27, 45, 4, 7, 8, 9, 0]),
                          [1, 'Fizz', 'FizzBuzz', 4, 7, 8, 'Fizz', 'FizzBuzz'])

    def test_empty(self):
        self.assertListEqual(HomeWork7.fizzbuzz([]), [])

    def test_typing(self):
        self.assertIsInstance(HomeWork7.fizzbuzz([3, 5, 4, 15]), list)

class TestToRoman(unittest.TestCase):

    def setUp(self):
        print ('start')

    def test_eq(self):
        self.assertEqual(HomeWork7.to_roman(26), 'XXVI')
        self.assertEqual(HomeWork7.to_roman(5), 'V')
        self.assertEqual(HomeWork7.to_roman(49), 'XLIX')
        self.assertEqual(HomeWork7.to_roman(4857), 'MNDCCCLVII')
        self.assertEqual(HomeWork7.to_roman(159), 'CLIX')

    def test_err(self):
        with self.assertRaises(HomeWork7.NonValidInput):
            HomeWork7.to_roman('string')
        with self.assertRaises(HomeWork7.NonValidInput):
            HomeWork7.to_roman(50001)
        with self.assertRaises(HomeWork7.NonValidInput):
            HomeWork7.to_roman(-10)

    def tearDown(self):
        print('end')



