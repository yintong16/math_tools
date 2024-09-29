import unittest
from Subset_sum import super_increasing_sequence_verifier

class TestSuperIncreasingSequenceVerifier(unittest.TestCase):

    def test_empty_sequence(self):
        self.assertTrue(super_increasing_sequence_verifier([]))

    def test_single_element_sequence(self):
        self.assertTrue(super_increasing_sequence_verifier([1]))

    def test_valid_super_increasing_sequence(self):
        self.assertTrue(super_increasing_sequence_verifier([1, 3, 7, 15]))

    def test_invalid_super_increasing_sequence(self):
        self.assertFalse(super_increasing_sequence_verifier([1, 3, 4, 8]))

    def test_sorted_sequence(self):
        self.assertTrue(super_increasing_sequence_verifier([3,7,19,43,89,195]))


if __name__ == '__main__':
    unittest.main()