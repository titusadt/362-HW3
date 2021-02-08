import unittest
import c_volume

class TestCase (unittest.TestCase):
    def test_volume(self):
        #This is the normal check
        self.assertEqual(c_volume.volume(2),8)
    def test_volume2(self):
       #This is checking for the negative number
        self.assertRaises(ValueError,c_volume.volume,0)
    def test_volume3(self):
        #This is to check if it isnt an integer
        self.assertRaises(ValueError,c_volume.volume,-1)
       
if __name__ == '__main__' :
    unittest.main(verbosity=2)
