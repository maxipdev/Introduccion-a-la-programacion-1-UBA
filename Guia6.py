import math

# Ejericico 1
def hola_mundo (): 
    print("hola mundo")

hola_mundo()   

# 
def imprimir_un_verso ():
    verso = "Is this the real life?\nIs this just fantasy?\nCaught in a landslide,\nNo escape from reality."
    print(verso)

imprimir_un_verso()

# 
def raiz_de_dos():
    valor = math.sqrt(2)
    valor_a_mostar = round(valor, 4)
    print(valor_a_mostar)

raiz_de_dos()

# 
def factorial_de_dos():
    print(2*1)

factorial_de_dos()

# 
def perimetro():
    return  2*(math.pi)

perimetro()

# Ejercico 2
def imprimir_saludo(nombre: str) -> str:
    print(f'Hola {nombre}, como estas?')

imprimir_saludo("abumeyang")

#
def raiz_cuadrada_de_un_numero(num: int) -> float:
    operacion = math.sqrt(num)
    print(operacion)

raiz_cuadrada_de_un_numero(2)

#
def fahrenheit_a_celsius(t: float) -> float:
    return ((t-32)*5)/9

temperatura = fahrenheit_a_celsius(90)
print(temperatura)

# 
def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo*2)

imprimir_dos_veces("me gusta la noche...")

#
def es_multiplo_de(n: int, m: int) -> bool:
    ## Buscamos ver si n es un multiplo de m
    ## tomo sus absolutos ya que habla de enteros
    n = abs(n)
    m = abs(m)
    for k in range(1, n):
        cuenta = m*k
        if cuenta > n: return False ## pq la cuenta es mas grande que n lo que hace que n no pueda ser un multiplo de ese numero 
        elif n == cuenta: return True ## sie encontro algun multiplo
    return False ## en caso de que no encuentre ningun multiplo

print("pruebo multiplos")
print(es_multiplo_de(2,2))
print(es_multiplo_de(4,2))
print(es_multiplo_de(3,2))
print(es_multiplo_de(17,8))

#
def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2) ## solo pq el ejercicio lo pide que hay que usar esta función

print("pruebo pares")
print(es_par(17))
print(es_par(8))

#
## cantidad de pizzas necesarias para que cada comensal coma esa cantidad de porciones como minimo
def cantidad_de_pizzas(comensales: int, cant_de_porciones: int):
    porciones_pizza = 8 ## 8 porciones por pizza
    cuenta = (comensales * cant_de_porciones)/porciones_pizza
    return math.ceil(cuenta) ## siempre da pizzas por demas como pide

print("pruebo pizzas")
print(cantidad_de_pizzas(2,4))
print(cantidad_de_pizzas(4,4))
print(cantidad_de_pizzas(8,4))
print(cantidad_de_pizzas(4,5))