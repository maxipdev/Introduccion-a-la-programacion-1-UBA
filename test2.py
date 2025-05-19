import unittest
from Guia7 import *

class Test_ejericio_pertenece(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertFalse(pertenece([], 1))
        self.assertFalse(pertenece2([], 1))
        self.assertFalse(pertenece3([], 1))

    def test_no_pertenece(self):
        self.assertFalse(pertenece([1], 2))
        self.assertFalse(pertenece([1, 2, 3, 4], 10))

        ## Para el pertenece 2
        self.assertFalse(pertenece2([1], 2))
        self.assertFalse(pertenece2([1, 2, 3, 4], 10))

        ## Para el pertenece 3
        self.assertFalse(pertenece3([1], 2))
        self.assertFalse(pertenece3([1, 2, 3, 4], 10))

    def test_si_pertenece(self):
        self.assertTrue(pertenece([1, 2, 3, 4], 3))
        self.assertTrue(pertenece([1], 1))

        ## Para el pertenece 2
        self.assertTrue(pertenece2([1, 2, 3, 4], 3))
        self.assertTrue(pertenece2([1], 1))

        ## Para el pertenece 3
        self.assertTrue(pertenece3([1, 2, 3, 4], 3))
        self.assertTrue(pertenece3([1], 1))


class Test_ejercicio_suma(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(suma_total([]), 0)

    def test_un_elemento(self):
        self.assertEqual(suma_total([1]), 1)
        self.assertEqual(suma_total([100]), 100)

    def test_muchos_elementos(self):
        self.assertEqual(suma_total([1,2,3,4,5]), 15)
        self.assertEqual(suma_total([1,2]), 3)
        self.assertEqual(suma_total([1,2,3, -1]), 5)


class test_ejercicio_ceros_en_pares(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(ceros_en_posiciones_pares2([]), [])
    
    def 



if __name__ == '__main__':
    unittest.main(verbosity=2)