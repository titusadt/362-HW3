import unittest
import concat

class TestCase (unittest.TestCase):
    def testConcat(self):
        self.assertEqual(concat.concatenate("Temi", "Adewunmi"),"Temi Adewunmi")
    def testConcat2(self):   
        self.assertRaises(ValueError,concat.concatenate,"","Blue")
    def testConcat3(self):
        self.assertRaises(TypeError,concat.concatenate,"20","twenty")
if __name__ == '__main__' :
    unittest.main(verbosity=2)
