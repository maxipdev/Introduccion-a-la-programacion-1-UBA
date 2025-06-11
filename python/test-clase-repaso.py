import unittest
from clase_repaso import *

# test del ejercicio 2
class test_filtrar_codigos_primos(unittest.TestCase): 
    def test_ultimos_3_primos(self): 
        self.assertEqual(filtrar_por_primos([12432423013, 9890809]), [12432423013, 9890809])
        self.assertEqual(filtrar_por_primos([12432423013, 9890809, 45456465222]), [12432423013, 9890809])
        self.assertEqual(filtrar_por_primos([555, 3041]), [3041])

    def test_sin_primos(self): 
        lista = [221222, 7545442]
        self.assertEqual(filtrar_por_primos(lista), [])
    def test_un_solo_codigo(self): 
        lista = [1097]
        self.assertEqual(filtrar_por_primos(lista), lista) 



if __name__ == '__main__':
    unittest.main(verbosity=2)

