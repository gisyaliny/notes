import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5),15)
        self.assertEqual(calc.add(-1, 1), 0)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(3, 1), 2)
        self.assertEqual(calc.subtract(5, 5), 0)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.subtract(-1, 1), -1)
        
        ## Test Raise Error is right or not
        self.assertRaises(ValueError,calc.divide,10,0)
        
        ## Same to above but different format
        with self.assertRaises(ValueError):
            calc.divide(1,0)
                
if __name__ == "__main__":
    unittest.main()       
    