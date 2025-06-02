import unittest
from Guia9 import *


class EjerciciosTest(unittest.TestCase):

    def test_sumar_cero(self):
        self.assertEqual(sumar(3,0), 3, "test_sumar_cero")

  #  def test_sumar_neg(self):
  #      self.assertEqual(sumar(3,-2), 1, "test_sumar_neg")

  #  def test_sumar_pos(self):
  #      self.assertEqual(sumar(3,5), 8, "test_sumar_pos")


if __name__ == '__main__':
    unittest.main(verbosity=2)



   
