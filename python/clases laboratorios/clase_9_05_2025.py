# Ejercicio 4
# Ítem 2
def producto_1(n: int) -> int:
    res: int = 1 # 1 OE
    i: int = 1 # 1 OE
    while i <= n: # Toma 1 OE evaluar la condicion y la vamos a evaluar (n + 1) veces la condicion
        res = res * i # 2 OE --> (n veces)
        i = i + 1 # 2 OE --> (n veces)
    return res # 1 OE

#Calculo: 
# t(n) = 1 + 1 + (n + 1) + (2n) + (2n) + 1 = 5n + 4 
# t(n) = 2 + n(1 + 2 + 2) + 1 + 1 -- > otra manera de escribirlo
# nos quedo una función lineal, cuyo crecimiento depende de n 
# siempre se escribe un + 1 al final del n() pq es la condicon false del ciclo


# Ítem 4
def producto_3(n: int) -> int:
    res: int = 1 # 1 OE
    i: int = 1 # 1 OE
    while i <= n: # (N + 1) OE
        j: int = 1 # 1 OE -- n veces
        while j <= n: # (N + 1) OE --> n veces:
            res = res * i * j # 3 OE -- (n * n veces)
            j = j + 1 # 2 OE -- (n * n veces)
        i = i + 1 # 2 OE -- n veces
    return res # 1 OE

# Calculo: 
# t(n) = 1 + 1 + n( 1 + 1 + n (1 + 3 +2) + 1 + 2) + 1 + 1
#      = 2 + n( 6n + 5) + 2 = 6n^2 + 5n + 4 --> crecimiento cuadratico

# Ítem 7
def producto_6(n: int) -> int:
    res: int = 1 # 1 OE
    i: int = 1 # 1 OE
    while i <= 2**n: # 2 * (2^n + 1) OE
        producto: int = 1 # 1 OE -- 2^n veces
        j: int = 1 # 1 OE -- 2^n veces
        while j <= n: #(n + 1) OE -- 2^n veces
            if (i // (2 ** (j-1))) % 2 == 1: # 1 + 1 + 1 + 1 + 1 =  5 -- (2^n * n veces)
                producto = producto * j # 2 OE -- (2^n * n veces)
            else:
                producto = producto * 1 # 2 OE -- (2^n * n veces)
            j = j + 1 # 2 OE -- (2^n * n veces)
        i = i + 1 # 2 OE -- 2^n veces
        res = res * producto # 2 OE -- 2^n veces 
    return res # 1 OE 

# F(n) = 2 + 2^n( 2 + 2 +  n(1 + 5 + 2 + 2) + 1 + 2 + 2) + 2 + 1
#      = 5 + 2^n(9 + 10n) = 2^n(10n + 9) + 5 -- > es una funcón exponencial


# Ejercicio 5.5
# Requiere: es matriz cuadrada (#filas = #columnas)
def diagonal_principal_v1(m: list[list[int]]) -> list[int]:
    res: list[int] = [] # 1 OE
    n: int = len(m) # 1 + T_len(n) -- > se usa el n
    i: int = 0 # 1 OE
    while i < n: # (n + 1)
        j: int = 0 # 1 -- n veces
        while j < n: # (n + 1)-- n veces
            if i == j: # 1 -- (n*n) veces
                res.append(m[i][j]) # T_[.](n) + T_[.](n) (n veces) -- por el if que lo condiciona
                # T_append(i) (con i sumando entre 0 y n-1)
            j = j + 1 # 2 OE -- n*n veces
        i = i + 1 # 2 OE -- n veces
    return res # 1 OE

#Cálculo: 
#T(n) = 3 + T_len(n) + n(2 +n(1 + 1 + 2) + 1 + 2T_[.] + 2) + 1 + 1 + sum(T-append(i), desde 0 hasta n-1)
#     = t_len(n) + sum(T-append(i), desde 0 hasta n-1) + 5 + 4n² + 5n + 2n(T_[.](n))

# Requiere: es matriz cuadrada (#filas = #columnas)
def diagonal_principal_v2(m: list[list[int]]) -> list[int]:
    res: list[int] = [] # 1 OE
    n: int = len(m) # 1 + t_len(n)
    i: int = 0 # 1 OE
    while i < n: # (n+1) OE
        res.append(m[i][i])
        # T_[.](n) + T_[.](n) (n veces)
        # T_append(i) (con i sumando entre 0 y n-1)
        i = i + 1 # 2 OE -- n veces
    return res # 1 OE

# Calculo: 
#T(n) = 3 + T_len(n) + n(1 + 2T_[.](n) + 2) + 1 + 1 + sum(T-append(i), desde 0 hasta n-1)
#     = t_len(n) + sum(T-append(i), desde 0 hasta n-1) + 5 + 3n + 2n(T_[.](n))

# comparación entre ambas: 
#5 + 4n² + 5n !== 5 + 3n
# --> Por lo tanto el de abajo es una lineal haciendo que sea mejor que la primera, que es una cuadratica


# Ejercicio 6.1
def contar_pares(s: list[int]) -> int:
    res: int = 0 # 1 OE
    i: int = 0 # 1 OE 
    while i < len(s): # (n + 1) * T_len(n) + (n + 1)
        if s[i] % 2 == 0: # 2 OE + T_[.](n) -- n veces
            res = res + s[i]
            # 2 OE + T_[.](n) -- veces en el peor caso y 0 en el mejor caso (que serian que todos sean impares)
        i = i + 1 # 2 OE -- n veces
    return res # 1 OE

# la lsita vacía no vale, siempre hay que pensar una lista con elementos -- ya que termina dando el msimo polinomio, no los valores pero si no en si es lo msimo el polinomio

# Calculo: 
# T_mejor(n) = 2 + (n + 1)* T_len(n) + n (1 + 2 + T_[.](n) + 2) + 1 + 1
# T_peor(n) = 2 + (n + 1)* t_len(n) + n (1 + 2 + T_[.](n) + 2 + t_[.](n)) + 1 + 1

# las dos son lineales, pero una hace más operaciones que la otra

# Ejercicio 6.2
def suma_hasta_umbral(s: list[int], umbral: int) -> int:
    res: int = 0
    i: int = 0
    while i < len(s) and s[i] < umbral:
        res = res + s[i]
        i = i + 1
    return res