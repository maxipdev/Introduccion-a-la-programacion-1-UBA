# Clase 21 de mayo labo 1106. No es autocontenido, las explicaciones se dieron en clase. Cualquier consulta los esperamos la clase que viene.
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

cola = Cola()
cola.put(0)
cola.get()
cola.empty()
import unittest
def columna(k: int, m: list[list[int]]) -> list[int]:
    res: list[int] = []
    for fila in m:
        res.append(fila[k])        
    return res

def ordenada(lista: list[int]) -> bool:
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

def matriz_ordenada(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for n_columna in range(len(m[0])):
        res.append(ordenada(columna(n_columna, m)))
    return res

def columnas_ordenadas_feo(matriz: list[list[int]]) -> list[bool]:
    res : list[bool] = []
    tamaño_filas : int = len(matriz)
    tamaño_columnas : int = len(matriz[0])
    for col in range(tamaño_columnas):
        ordenada : bool = True
        for fila in range(1, tamaño_filas):
            if matriz[fila][col] < matriz[fila - 1][col]:
                ordenada = False
                break # Sale del ciclo interno (el de filas)
        res.append(ordenada)
    return res

def pila_a_lista(p: Pila) -> list[int]:
    res: list[int] = []
    while not p.empty():
        res.append(p.get())
    for i in range(len(res)-1):
        p.put(res[len(res)-i-1])
    return res

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    while cantidad > 0:
        res.put(random.randint(desde, hasta))
        cantidad = cantidad - 1
    return res

class TestEjercicio8(unittest.TestCase):
    def test_pila_vacia(self) -> None:
        self.assertTrue(generar_nros_al_azar(0, 0, 10).empty())

    def test_pila_10_elem_0_10(self) -> None:
        pila: Pila[int] = generar_nros_al_azar(10, 0, 10)
        cantidad: int = 0
        while not pila.empty():
            elemento: int = pila.get()
            if not (0 <= elemento <= 10):
                self.fail()
            cantidad += 1
        self.assertEqual(cantidad, 10)

    def test_pila_10_elem_10_20(self) -> None:
        pila: Pila[int] = generar_nros_al_azar(10, 10, 20)
        cantidad: int = 0
        while not pila.empty():
            elemento: int = pila.get()
            if not (10 <= elemento <= 20):
                self.fail()
            cantidad += 1
        self.assertEqual(cantidad, 10)

def buscar_el_maximo(p: Pila[int]) -> int:
    pila_auxiliar: Pila[int] = Pila()
    maximo: int = p.get()
    pila_auxiliar.put(maximo)
    while not p.empty():
        elem: int = p.get()
        if elem > maximo:
            maximo = elem
        pila_auxiliar.put(elem)
    while not pila_auxiliar.empty():
        p.put(pila_auxiliar.get())
    return maximo

def pertenece(lista: list[int], e: int) -> bool: 
    for elemento in lista: 
        if elemento == e: 
            return True
    return False

def armar_secuencia_de_bingo() -> Cola[int]: 
    res: Cola[int] = Cola()
    lista: list[int] = []
    for i in range(100):
        lista.append(i)
    random.shuffle(lista)
    for i in range(len(lista)):
        res.put(lista[i])
    return res

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int: 
    res: int = 0
    cantidad_bolillas_acertadas: int = 0
    cantidad_numeros_en_carton: int = len(carton)
    bolillero_auxiliar: Cola[int] = Cola()
    # Esto vale solamente porque asumimos que nos van a pasar un bolillero que tiene a todos los numeros de nuestro carton. Si no fuera asi este while no termina nunca.
    while not (cantidad_bolillas_acertadas == cantidad_numeros_en_carton): 
        bolilla_actual: int = bolillero.get()
        bolillero_auxiliar.put(bolilla_actual)
        if pertenece(carton, bolilla_actual): 
            cantidad_bolillas_acertadas += 1
        res += 1
    # Ciclo para terminar de vaciar el bolillero
    while not (bolillero.empty()): 
        bolilla_actual: int = bolillero.get()
        bolillero_auxiliar.put(bolilla_actual)
    
    # Ciclo para pasar del bolillero auxiliar al parametro
    while not (bolillero_auxiliar.empty()):
        num: int = bolillero_auxiliar.get()
        bolillero.put(num)

    return res

    