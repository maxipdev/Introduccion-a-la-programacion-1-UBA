from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import unittest

def columna(k: int, m: list[list[int]]) -> list[int]:
    res = []
    for fila in m: 
        res.append(fila[k])
    return res


def ordenada(lista: list[int]) -> bool:
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res = []
    for col in range(len(m[0])): ## col = numero de columna
        res.append(ordenada(columna(col,m)))
    return res 


m = [[1,2,3],[2,4,5],[3,5,6]]
columnas_ordenadas(m)

#casos de test:
# matrix cudrada
# matriz rectangular 
# todas ordenadas 
# todas desordenadas 
# algunas ordenadas 


def numeros_random(desde, hasta):
    res = random.randint(desde, hasta)
    return res

# Ejercicio Guia 8 1.1
def generar_numeros_al_azar(cantidad: int, desde: int, hasta: int):
    pila = Pila()
    for i in range(0, cantidad):
        numero = numeros_random(desde, hasta)
        pila.put(numero)
    return pila.queue ## se usa asi para poder ver la pila

def mostrar_pila(p: Pila) -> None: 
    res = []
    for i in p: 
        res.append(p.get())


### TEST
# class Test(unittest.TestCase):
#     def test_pila_vacia(self):
#         self.assertTrue(generar_numeros_al_azar(0,0,10).empty())
#     def test_pila_10_elemento_0_10(self): 
#         pila = generar_numeros_al_azar(10, 0, 10)
#         cantidad = 0
#         while not pila.empty():
#             elemento = pila.geCola[Z] t()


# print(generar_numeros_al_azar(10, 1, 99))

# Ejercicio 1.3
def buscar_el_maximo(p: Pila[int]) -> int:
    listaDeElementos = []
    mas_grande = p.get() ## siempre hay uno pq el enunciado lo dice que no hay
    listaDeElementos.append(mas_grande)
    while not p.empty: 
        elemento = p.get()
        listaDeElementos.append(elemento)
        if elemento > mas_grande : mas_grande = elemento

    ## tengo que volver a poner todos los elementos
    for i in listaDeElementos:
        p.put(i)
    ## doy el mas grande
    return mas_grande


## otra manera es hacerlo con una pila auxilair y guaradra ahi y depues vovler a la pila original por logica de las pilas ya que 
# si hay una pila1 = [1,2,3,4] pasa a pila2 = [4,3,2,1] y si volves a pila1 queda igual 
# crea la pila2 adentro de la funcion   

pila2 = Pila()
pila2.put(1)
pila2.put(2)
pila2.put(3)
pila2.put(4)
print(pila2.queue)
print(buscar_el_maximo(pila2))
print(pila2.queue)


# ejercicio 2.13.1
# def creo_numeros_random():
#     res = random.randint(0, 99)
#     return res

# def armar_secuencia_de_bingo() -> Cola[int]:
#     carton = []
#     cantidad_de_numeros_carton = 12
#     for i in 12:
#         carton.append(creo_numeros_random())
#     return carton

# print(armar_secuencia_de_bingo())


