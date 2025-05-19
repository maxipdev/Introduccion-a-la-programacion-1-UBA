def pertenece(lista: list[int], e: int) -> bool:
    tamaño: int = len(lista)
    for i in range(tamaño):
        if e == lista[i]: return True
    return False

def pertenece2(lista: list[int], e: int) -> bool:
    for i in lista:
        if e == i: return True
    return False


def pertenece3(lista: list[int], e: int) -> bool:
    i: int = 0
    while i < len(lista):
        if e == lista[i]: return True
        i += 1
    return False


# Ejercicio 1.3
def suma_total(lista: list[int]) -> int:
    total: int = 0
    for i in lista:
        total += i
    return total 

# Ejercicio 2.1
def ceros_en_posiciones_pares(s: list[int]):
    for i in range(len(s)):
        print(i)
        if (i+1) % 2 == 0: 
            s[i] = 0

lista = [1,2,3,4,5,5]
ceros_en_posiciones_pares(lista)
print(lista)

# Ejercicio 2.2
def ceros_en_posiciones_pares2(lista: list[int]) -> list[int]:
    s = lista.copy()
    for i in range(len(s)):
        if (i+1) % 2 == 0: 
            s[i] = 0  
    return s


