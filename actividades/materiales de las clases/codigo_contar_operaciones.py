# Ejercicio 4
# Ítem 2
def producto_1(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= n:
        res = res * i
        i = i + 1
    return res

# Ítem 4
def producto_3(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= n:
        j: int = 1
        while j <= n:
            res = res * i * j
            j = j + 1
        i = i + 1
    return res

# Ítem 7
def producto_6(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= 2**n:
        producto: int = 1
        j: int = 1
        while j <= n:
            if (i // (2 ** (j-1))) % 2 == 1:
                producto = producto * j
            else:
                producto = producto * 1
            j = j + 1
        i = i + 1
        res = res * producto
    return res


# Ejercicio 5.5
# Requiere: es matriz cuadrada (#filas = #columnas)
def diagonal_principal_v1(m: list[list[int]]) -> list[int]:
    res: list[int] = []
    n: int = len(m)
    i: int = 0
    while i < n:
        j: int = 0
        while j < n:
            if i == j:
                res.append(m[i][j])
            j = j + 1
        i = i + 1
    return res

# Requiere: es matriz cuadrada (#filas = #columnas)
def diagonal_principal_v2(m: list[list[int]]) -> list[int]:
    res: list[int] = []
    n: int = len(m)
    i: int = 0
    while i < n:
        res.append(m[i][i])
        i = i + 1
    return res


# Ejercicio 6.1
def contar_pares(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        if s[i] % 2 == 0:
            res = res + s[i]
        i = i + 1
    return res


# Ejercicio 6.2
def suma_hasta_umbral(s: list[int], umbral: int) -> int:
    res: int = 0
    i: int = 0
    while i < len(s) and s[i] < umbral:
        res = res + s[i]
        i = i + 1
    return res