import unittest
from Guia8_diccionarios import *

# Ejercicio 16 
class test_ejercicio_16(unittest.TestCase): 
    def test_lista_vacia(self): 
        self.assertEqual(calcular_promedio_por_cada_estudiante([]), {})

    def test_un_solo_estudiante(self): 
        self.assertEqual(calcular_promedio_por_cada_estudiante([("juan", 10)]), {"juan": 10})
    
    def test_varios_estudiantes(self): 
        self.assertEqual(calcular_promedio_por_cada_estudiante([("juan", 10), ("mak", 7)]), {"juan": 10, "mak": 7})

    def varias_notas_de_un_mismo_estudiante(self): 
        self.assertEqual(calcular_promedio_por_cada_estudiante([("juan", 10), ("juan", 4)]), {"juan": 7})

    def vasrias_notas_y_varios_estudiantes(self): 
        self.assertEqual(calcular_promedio_por_cada_estudiante([("juan", 10), ("mak", 7), ("juan", 8), ("mak", 3)]), {"juan": 9, "mak": 5})

if __name__ == '__main__':
    unittest.main(verbosity=2)
