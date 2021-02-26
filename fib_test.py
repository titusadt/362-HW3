import unittest
import fibonacci

class TestCase(unittest.TestCase):
   def test_1(self):
      self.assertEqual(fibonacci.find(2),1)
   
   def test_2(self):
      self.assertEqual(fibonacci.find(5),5)

   def test_3(self):
      self.assertEqual(fibonacci.find(7),13)

if __name__ == '__main__':
   unittest.main(verbosity=2)
