import unittest
import average

class TestCase (unittest.TestCase):
    def test(self):
        self.assertEqual(average.ave([2,2,2]),2)
    def test2(self):
        self.assertRaises(ValueError,average.ave,[])
    def test3(self):
        self.assertRaises(TypeError,average.ave,([0,0],0))   
if (__name__ == '__main__'):
    unittest.main(verbosity=2)
