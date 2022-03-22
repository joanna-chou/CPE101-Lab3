# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Joanna Chou
# Section: 07

import unittest
from conditional import *


# You can delete pass after writing your code
class TestCases(unittest.TestCase):
    def test_min_of_2(self):
        self.assertEqual(min_of_2(3.22, 50), 3.22)
        self.assertEqual(min_of_2(-231.0, 0), -231.0)
        self.assertEqual(min_of_2(5, 24.3), 5)

    def test_min_of_3(self):
        self.assertEqual(min_of_3(8, 63, 0.38), 0.38)
        self.assertEqual(min_of_3(-11, 33.3, 0), -11)
        self.assertEqual(min_of_3(69, 3243.12, -92.1), -92.1)

    def test_rental_late_fee(self):
        self.assertEqual(rental_late_fee(2), 0)
        self.assertEqual(rental_late_fee(2222), 100)
        self.assertEqual(rental_late_fee(10), 15)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
