import unittest
import functions_for_testing as fft

class FunctionsTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(fft.sum(4, 5), 9)
        self.assertNotEqual(fft.sum(3, 4), 4)
        self.assertEqual(fft.sum(10, 15), 25)
        self.assertEqual(fft.sum(100, 150), 250)

    def test_sub(self):
        self.assertEqual(fft.sub(5, 1), 4)
        self.assertEqual(fft.sub(15, 3), 12)
        self.assertEqual(fft.sub(150, 250), -100)

    def test_mul(self):
        self.assertEqual(fft.mul(5, 2), 10)
        self.assertEqual(fft.mul(25, 4), 100)

    def test_div(self):
        try:
            fft.div(5, 0)
        except ZeroDivisionError:
            self.assertEqual(0,0)
        self.assertEqual(fft.div(10, 5), 2)
        self.assertEqual(fft.div(7, 20), 0.35)
        self.assertEqual(fft.div(21, 2), 10.5)
