import unittest
import modLib as ml

class TestCeilingFunction(unittest.TestCase):
    def test_integer_input(self):
        self.assertEqual(ml.ceil(5), 5, "Should return the input when it is an integer")
    
    def test_positive_float_input(self):
        self.assertEqual(ml.ceil(5.3), 6, "Should return the smallest integer greater than the input for positive floats")
    
    def test_negative_float_input(self):
        self.assertEqual(ml.ceil(-2.7), -2, "Should return the smallest integer greater than the input for negative floats")
    
    def test_zero_input(self):
        self.assertEqual(ml.ceil(0), 0, "Should return 0 for input 0")
    
    def test_negative_integer_input(self):
        self.assertEqual(ml.ceil(-3), -3, "Should return the input when it is a negative integer")

class TestFloorFunction(unittest.TestCase):
    def test_integer_input(self):
        self.assertEqual(ml.floor(5), 5, "Should return the input when it is an integer")
    
    def test_positive_float_input(self):
        self.assertEqual(ml.floor(5.7), 5, "Should return the largest integer less than the input for positive floats")
    
    def test_negative_float_input(self):
        self.assertEqual(ml.floor(-2.3), -3, "Should return the largest integer less than the input for negative floats")
    
    def test_zero_input(self):
        self.assertEqual(ml.floor(0), 0, "Should return 0 for input 0")
    
    def test_negative_integer_input(self):
        self.assertEqual(ml.floor(-3), -3, "Should return the input when it is a negative integer")


class TestSqrtFunction(unittest.TestCase):

    def test_sqrt_positive_int(self):
        self.assertAlmostEqual(ml.sqrt(9), 3.0, places=4)

    def test_sqrt_positive_float(self):
        self.assertAlmostEqual(ml.sqrt(9.0), 3.0, places=4)

    def test_sqrt_zero(self):
        with self.assertRaises(ValueError):
            ml.sqrt(0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            ml.sqrt(-1)

    def test_sqrt_precision(self):
        self.assertAlmostEqual(ml.sqrt(2), 1.4142, places=4)


if __name__ == '__main__':
    unittest.main()