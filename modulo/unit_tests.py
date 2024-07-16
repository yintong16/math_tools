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


class TestEularPhi(unittest.TestCase):
    def test_eular_phi(self):
        self.assertEqual(ml.eular_phi(1), 0)
        self.assertEqual(ml.eular_phi(2), 1)
        self.assertEqual(ml.eular_phi(3), 2)
        self.assertEqual(ml.eular_phi(4), 2)
        self.assertEqual(ml.eular_phi(5), 4)
        self.assertEqual(ml.eular_phi(6), 2)
        self.assertEqual(ml.eular_phi(10), 4)
        self.assertEqual(ml.eular_phi(13), 12)

class TestEulerFunction(unittest.TestCase):
    def test_euler_coprime(self):
        # Test cases where a and n are coprime
        self.assertEqual(ml.euler_mod(2, 5, 9), 2**5 % 9)
        self.assertEqual(ml.euler_mod(3, 4, 7), 3**4 % 7)
    
    def test_euler_not_coprime(self):
        # Test case where a and n are not coprime, expecting None since the function prints instead of returning a value
        self.assertIsNone(ml.euler_mod(2, 4, 4))
    
    def test_euler_power_zero(self):
        # Test case where power is 0, should return 1 as anything to the power of 0 is 1
        self.assertEqual(ml.euler_mod(3, 0, 7), 1)

    def test_euler_phi_n_is_one(self):
        # Test case where phi(n) is 1, which is the case for n=2, expecting a^0 % n which is 1
        self.assertEqual(ml.euler_mod(3, 10, 2), 1)

    def test_euler_phi_n_is_six(self):
        # Test case where phi(n) is 1, which is the case for n=2, expecting a^0 % n which is 1
        self.assertEqual(ml.euler_mod(5, 10, 7), 2)

class TestFermatFactorization(unittest.TestCase):
    def test_even_number(self):
        # Test factorization of an even number
        self.assertEqual(sorted(ml.fermat_facterization(8)), [2, 2, 2])

    def test_prime_number(self):
        # Test factorization of a prime number (should return the number itself)
        prime = 13
        self.assertEqual(ml.fermat_facterization(prime), [prime])

    def test_odd_composite_number(self):
        # Test factorization of an odd composite number
        self.assertEqual(sorted(ml.fermat_facterization(15)), [3, 5])

    def test_large_number(self):
        # Test factorization of a larger number
        self.assertEqual(sorted(ml.fermat_facterization(100)), [2, 2, 5, 5])

    def test_composits(self):
        # Test factorization of a larger number
        self.assertEqual(sorted(ml.fermat_facterization(42)), [2, 3, 7])

    def test_very_large_prime(self):
        # Test factorization of a very large prime number (for performance, not accuracy)
        large_prime = 104729  # This is actually a prime number
        self.assertEqual(ml.fermat_facterization(large_prime), [large_prime])

class TestFastIsPrimeFunctions(unittest.TestCase):
    def test_fast_isPrime(self):
        # Test fast_isPrime function
        self.assertFalse(ml.fast_isPrime(1))
        self.assertTrue(ml.fast_isPrime(2))
        self.assertTrue(ml.fast_isPrime(3))
        self.assertFalse(ml.fast_isPrime(4))
        self.assertTrue(ml.fast_isPrime(5))
        self.assertFalse(ml.fast_isPrime(9))
        self.assertTrue(ml.fast_isPrime(13))

class TestGenPrimeFunctions(unittest.TestCase):
    def test_genPrime(self):
        # Test genPrime function
        self.assertEqual(ml.genPrime(5), [2, 3, 5])
        self.assertEqual(ml.genPrime(10), [2, 3, 5, 7])
        self.assertEqual(ml.genPrime(20), [2, 3, 5, 7, 11, 13, 17, 19])



if __name__ == '__main__':
    unittest.main()