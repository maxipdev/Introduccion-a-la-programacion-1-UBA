import unittest
from Guia6 import *

class test_suma(unittest.TestCase):
    def test_suma_negativa(self):
        self.assertEqual(suma(-4,-7),-11)

    def test_suma_positiva(self):
        self.assertEqual(suma(2,3),5)
    
class test_doble_de_un_num(unittest.TestCase):
    def test_pares(self):
        self.assertEqual(devolver_el_doble_si_es_par(2),4)
        self.assertEqual(devolver_el_doble_si_es_par(10),20)

    def test_impares(self):
        self.assertEqual(devolver_el_doble_si_es_par(1),1)
        self.assertEqual(devolver_el_doble_si_es_par(13),13)

    # def test_cero(sefl): HACER!!!!!!!!!
    #     self.as

# class Grados(unittest.TestCase): MIRARLO
#     def test_1(self):
#         self.assertAlmostEqual(grados(140.0),60.5)
#         self.assertNotAlmostEqual(grados(140.0), 60.5)


class test_primos(unittest.TestCase):
    def test_uno_y_cero(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))

    def test_si_es_primo(self):
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(13))
    
    def test_si_es_compuesto(self):
        self.assertFalse(es_primo(10))
        self.assertFalse(es_primo(33))

    def test_si_es_negativo(self):
        self.assertTrue(es_primo(-2))
        self.assertTrue(es_primo(-13))
        self.assertFalse(es_primo(-1))
        self.assertFalse(es_primo(-4))


class contador_primos(unittest.TestCase):
    def test_si_n_menor_que_m(self):
        self.assertEqual(cuantos_primos_en_rango(2,7), 4)
    
    def test_n_igual_que_m(self):
        self.assertEqual(cuantos_primos_en_rango(5,5),1)
        self.assertEqual(cuantos_primos_en_rango(4,4),0)

    def test_si_n_mayor_que_m(self):
        self.assertEqual(cuantos_primos_en_rango(7,2),4)
    
    def test_n_positivo_m_negativo(self):
        self.assertEqual(cuantos_primos_en_rango(-3,3),4)

    def test_n_negativo_m_positivo(self):
        self.assertEqual(cuantos_primos_en_rango(3,-3),4)





if __name__ == '__main__':
    unittest.main(verbosity=2)


 