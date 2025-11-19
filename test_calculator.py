#https://github.com/<git@github.com:egdwashwa/lab11-LG-MV.git>
#Partner 1: <Leon Grigoruk>
#Partner 2: <Megan Vu>

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 3), -3)
        self.assertEqual(sub(-2, -3), 1)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,2),2)
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(-3,-5),15)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10,2),5)
        self.assertEqual(div(30,5),6)
        self.assertEqual(div(12,4),3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(8, 2), 3)
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(1, 10), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(9,12),15)
        self.assertEqual(hypotenuse(12,16),20)

    def test_sqrt(self): # 3 assertions
        #Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
        #Test basic function
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(16),4)
        #fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
