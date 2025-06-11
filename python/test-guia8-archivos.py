import unittest
from Guia8_archivos import *

# Ejercicio 22 -- > Verificar
# class test_ejercicio_22(unittest.TestCase): 
#     def test_sin_archivos(self): 
#         self.assertEqual(clonar_sin_comentarios("texto-5.txt", "texto-2.txt"))
    
#     def test_todos_comentariso(self): 
#         self.assertEqual(clonar_sin_comentarios("texto-6.txt", "texto-2.txt"))
#         self.assertEqual(clonar_sin_comentarios("texto-7.txt", "texto-2.txt"))


# Ejercicio 20
class test_ejercicio_20(unittest.TestCase): 
    def test_archivo_vacio (self): 
        self.assertEqual(agrupar_por_longitud("texto-2.txt"), {})
    
    def test_todas_del_msimo_tamaño(self): 
        self.assertEqual(agrupar_por_longitud("texto-5.txt"), {4: 5})     
    
    def test_todas_diferentes(self): 
        self.assertEqual(agrupar_por_longitud("texto-9.txt"), {3: 1, 4: 1, 5: 1, 6: 1})     

# Ejercicio 21
class test_ejercicio_21(unittest.TestCase): 
    def test_hay_una_sola_oalabra(self): 
        self.assertEqual(palabra_mas_frecuente("texto-10.txt"), "hola")     
    
    def test_todas_diferentes(self): 
        self.assertEqual(palabra_mas_frecuente("texto-1.txt"), "yo")     




if __name__ == '__main__':
    unittest.main(verbosity=2)
