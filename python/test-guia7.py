import unittest
from Guia7 import *

# Ejercicio 1.1
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

# Ejercicio 1.3
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

# Ejercicio 1.12
class Test_ejercicio_vocales_distintas(unittest.TestCase):
    def test_todo_mayuscula(self):
        self.assertTrue(vocales_distintas("PALINDROMO"))
        self.assertFalse(vocales_distintas("ALGO"))

    def test_todo_minuscula(self):
        self.assertTrue(vocales_distintas("abecedario"))
        self.assertFalse(vocales_distintas("que"))

    def test_mayusculas_y_minusculas_combinadas(self):
        self.assertTrue(vocales_distintas("ameriCA"))
        self.assertTrue(vocales_distintas("OceANo"))
        self.assertFalse(vocales_distintas("Osti"))

    def test_sin_vocales(self):
        self.assertFalse(vocales_distintas("chph"))

    def test_todas_vocales_distintas(self):
        self.assertTrue(vocales_distintas("aeiou"))
        self.assertFalse(vocales_distintas("aaaaee"))

# Ejericio 2.1
class test_ejercicio_ceros_en_pares(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(ceros_en_posiciones_pares2([]), [])
    
# Ejercicio 2.2
class Test_ejercicio_sin_vocales(unittest.TestCase):
    def test_todas_vocales(self):
        self.assertEqual(sin_vocales("AAA"), "")
        self.assertEqual(sin_vocales("ooo"), "")

    def test_ninguna_vocal(self):
        self.assertEqual(sin_vocales("prjp"), "prjp")
        self.assertEqual(sin_vocales("GSMHSG"), "gsmhsg")

    def test_combinadas(self):
        self.assertEqual(sin_vocales("america"), "mrc")
        self.assertEqual(sin_vocales("SANCHEZ"), "snchz")

# Ejercicio 2.3
class Test_ejercicio_remplazar_vocales(unittest.TestCase):
    def test_todas_vocales(self):
        self.assertEqual(remplazar_vocales("AAA"), "---")
        self.assertEqual(remplazar_vocales("ooo"), "---")

    def test_ninguna_vocal(self):
        self.assertEqual(remplazar_vocales("prjp"), "prjp")
        self.assertEqual(remplazar_vocales("GSMHSG"), "gsmhsg")

    def test_combinadas(self):
        self.assertEqual(remplazar_vocales("america"), "-m-r-c-")
        self.assertEqual(remplazar_vocales("SANCHEZ"), "s-nch-z")

# Ejercicio 3
class Test_ejercicio_3(unittest.TestCase): 
    def test_promocion(self):
        self.assertEqual(resultado_materia([7,9,10]), 1)
    
    def test_no_promocion(self): 
        self.assertEqual(resultado_materia([8,4]), 2)

    def test_desaprobado(self): 
        self.assertEqual(resultado_materia([10,3,5]), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)