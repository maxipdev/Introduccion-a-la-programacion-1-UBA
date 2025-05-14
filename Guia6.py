def suma(a: int, b: int) -> int:
    res: int = a + b
    return res


## Ejercicios clase 14/05/2025 
def es_multiplo_de(n:int, m: int) -> bool: ## miro su n es multiplo de m
    if n % m == 0: 
        return True
    else: return False

def devolver_el_doble_si_es_par(n:int) -> int:
    if n % 2 ==0 : return 2*n
    else: return n 

def grados(t: float) -> float: ## conversion de faren a cel
    return (t - 32) * (5/9)


def es_primo(n:int) -> bool:
    valor = True
    n = abs(n) ## hago q N sea positivo

    if n == 0 or n == 1:
        return False
    
    for i in range(2,n):
        if n % i == 0: 
            valor = False ## pq se hace q haya un divisor
            break
    return valor

def cuantos_primos_en_rango(n:int, m: int) -> int:
    minimo = min(n,m)
    maximo = max(n,m)

    contador: int = 0
    for i in range(minimo, maximo + 1):
        if es_primo(i): contador += 1

    return contador

print(cuantos_primos_en_rango(5,3))
print(cuantos_primos_en_rango(3,5))
