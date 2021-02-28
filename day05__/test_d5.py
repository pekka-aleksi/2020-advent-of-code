import unittest

from day05__.d5 import Day5


class Test(unittest.TestCase):


    def setUp(self):
        self.a = "FBFBBFFRLR"
        self.b = "BFFFBBFRRR"
        self.c = "FFFBBBFRRR"
        self.d = "BBFFBBFRLL"

    def test_a(self):
        x = Day5()
        self.assertEqual(x(self.a), (44, 5, 357))

    def test_b(self):
        x = Day5()
        self.assertEqual(x(self.b), (70, 7, 567))

    def test_c(self):
        x = Day5()
        self.assertEqual(x(self.c), (14, 7, 119))

    def test_d(self):
        x = Day5()
        self.assertEqual(x(self.d), (102, 4, 820))

    def test_e(self):
        x = Day5()
        self.assertEqual(x("BBBBBBBRRR"), (127, 7, 127*8+7))

    def test_f(self):
        x = Day5()
        self.assertEqual(x("FFFFFFFLLL"), (0, 0, 0))

    def test_g(self):
        x = Day5()
        self.assertEqual(x("FFFFFFFRRR"), (0, 7, 7))

    def test_h(self):
        x = Day5()
        self.assertEqual(x("BBBBBBBLLL"), (127, 0, 127*8))