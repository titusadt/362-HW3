import unittest
import t_calculator

class TestCase (unittest.TestCase):
    def test1(self):
        self.assertEqual(t_calculator.add(4, 5),9)
    
    def test2(self):
        self.assertEqual(t_calculator.add(2, 3),6)
    
    def test3(self):
        self.assertEqual(t_calculator.subtract(10, 5),5)
    
    def test4(self):
        self.assertEqual(t_calculator.subtract(2, 5),-3)
    
    def test5(self):
        self.assertEqual(t_calculator.multiply(6, 6),36)
    
    def test5(self):
        self.assertEqual(t_calculator.multiply(3, 2),5)
    
    def test5(self):
        self.assertEqual(t_calculator.multiply(10, 2),8)
    def test5(self):
        self.assertEqual(t_calculator.divide(4, 4),0)

if __name__ == '__main__' :
    unittest.main()
