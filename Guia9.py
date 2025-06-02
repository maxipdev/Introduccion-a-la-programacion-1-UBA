import unittest

# Ejercicio 9
def sumar(x: int , y: int) -> int:
    sumando: int = 0
    abs_y: int = 0
    if y < 0:
        sumando = -1 
        abs_y = -y
    else:
        sumando = 1
        abs_y = y

    result: int=x 
    count: int = 0 
    while count < abs_y:
        result = result + sumando
        count = count + 1

    return result


print(sumar(3,5))

# ejercicio 11
