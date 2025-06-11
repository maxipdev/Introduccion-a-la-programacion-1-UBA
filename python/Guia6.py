import math

# Ejericico 1
def hola_mundo (): 
    print("hola mundo")  

# 
def imprimir_un_verso ():
    verso = "Is this the real life?\nIs this just fantasy?\nCaught in a landslide,\nNo escape from reality."
    print(verso)

# 
def raiz_de_dos():
    valor = math.sqrt(2)
    valor_a_mostar = round(valor, 4)
    print(valor_a_mostar)

raiz_de_dos()

# 
def factorial_de_dos():
    print(2*1)


# 
def perimetro():
    return  2*(math.pi)

# Ejercico 2
def imprimir_saludo(nombre: str) -> str:
    print(f'Hola {nombre}, como estas?')


#
def raiz_cuadrada_de_un_numero(num: int) -> float:
    operacion = math.sqrt(num)
    print(operacion)


#
def fahrenheit_a_celsius(t: float) -> float:
    return ((t-32)*5)/9

temperatura = fahrenheit_a_celsius(90)


# 
def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo*2)


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
#
def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2) ## solo pq el ejercicio lo pide que hay que usar esta función


#
## cantidad de pizzas necesarias para que cada comensal coma esa cantidad de porciones como minimo
def cantidad_de_pizzas(comensales: int, cant_de_porciones: int):
    porciones_pizza = 8 ## 8 porciones por pizza
    cuenta = (comensales * cant_de_porciones)/porciones_pizza
    return math.ceil(cuenta) ## siempre da pizzas por demas como pide


# Ejericio 3
def alguno_es_0(x:int, y:int) -> bool:
    return  x == 0 or y == 0 

def ambos_son_0(x:int, y:int) -> bool:
    return  x == 0 and y == 0 

def nombre_largo(nombre: str) -> bool:
    return 3 <= len(nombre) <= 8

def es_biciesto(año) -> bool:
    return (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)

# Ejercicio 4
def peso_pino(altura: int):
    altura: int = altura * 100 # paso la altura a centrimetros:

    hasta_300 = min(altura, 300)
    despues_300 = max(altura - 300, 0)

    return hasta_300 * 3 + despues_300 * 2

def es_peso_util(peso: int) -> bool:
    return 400 <= peso <= 1000 

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))

# Ejercicio 5.1
def devolver_el_doble_si_es_par(n: int) -> int:
    if n % 2 == 0 : return 2 * n 
    else: return n

# Ejercicio 5.2
## es decir da el mismo número si y solo si es par, pero si no lo es da el numero siguiente, o sea un impar
def devolver_valor_si_es_par_si_no_el_que_sigue(numero): 
    if numero % 2 == 0 : return numero
    else : return numero + 1

# Ejercicio 5.3 
## le da prioridad a si es multiplo de nueve
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n): 
    if n % 9 == 0: return n * 3
    elif n % 3 == 0 : return n * 2
    else : return n 

# Ejercicio 5.4
def lindo_nombre(name): 
    if len(name) >= 5 : 
        return "Tu nombre tiene muchas letras!"
    else : 
        return "Tu nombre tiene menos de 5 caracteres"

# Ejercicio 5.5
def el_rango(n): 
    if n < 5: 
        return 'menor'
    elif 10 <= n <= 20:
        return ' Entre 10 y 20'
    else : 
        return 'mayor'

# Ejercicio 5.6
def decir_accion(sexo, edad):
    if sexo == "M" and edad >= 65 :
        return "Vai in vacanza"
    elif sexo == "F" and edad >= 60: 
        return "Vai in vacanza"
    elif edad < 18 : 
        return "Vai in vacanza" 
    else : 
        return "debi laborare"

# Ejercicio 6.1
def escribir_los_numeros():
    cant = 1
    while not (cant == 101) :
        print(cant)
        cant += 1

# Ejercicio 6.2
def numeros_pares():
    count = 10
    while not count == 41:
        if count % 2 == 0:
            print(count)
        count += 1

# Ejercicio 6.3
def imprimir_la_palabra_10_veces():
    count = 0
    while not count == 10:
        print("eco")
        count += 1

# Ejercico 6.4
def despegue(desde): 
    while not desde == 0: 
        print(desde)
        desde -= 1
    print("despegue....")

# Ejercicio 6.5
def viaje_en_el_tiempo(partida: int, llegada: int) -> int:
    partida = partida - 1
    while not (partida == (llegada - 1)):
        print(f"Viajo al año pasado, estamos en el año: {partida}")
        partida -= 1


# Ejercicio 6.6
def conocer_a_aristoteles(partida):
    partida = partida - 20 
    while not (partida < 0):
        print(f"Viajo al año: {partida} DC")
        partida -= 20

    ## ahora desde antes de cristo
    desde = 0
    hasta = -384
    while not (desde < hasta -1):
        if desde == 0:
            print(f"Viajo al año : {abs(desde)}")
        print(f"Viajo al año : {abs(desde)} AC")
        desde -= 20
    
    print("hola aristoteles")

# Ejercicio 7 --> Pasar todo a for (es lo que pide)
def escribir_numeros_for():
    for i in range(101):
        print(i)

def numeros_pares_for():
    for i in range(10, 42):
        if i % 2 == 0:
            print(i)

def despegue_for(desde):
    for i in range(desde + 1, 0, -1):
        print(i)


### Y ASI CON TODAS LAS FUNCIONES

# Ejercicio 8
def ejericio_1():
    x = 5
    y = 7
    x = x + y
    print(x)

def ejercicio_2():
    x = 5
    y = 7
    z = x + y
    y = z* 2

    print(y)

def ejercicio_3():
    x = 5
    y = 7 
    x = "hora"
    y = x * 2
    print(y)

def ejercicio_4():
    x = False
    print(not x)

def ejercicio_6():
    x = True
    y = False
    res = x and y 
    x = res and x 
    print(x)


# Ejercicio 9
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

# PReguntas: 
# 1. ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
# 2. ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# 3. En cada función, realizar la ejecución simbólica.
# 4. Dar la especificación para cada función, rt y ro.

print(ro(ro(ro(1)))) ## La 1 es 7
# print(rt(rt(1,0))) # el resultado es error por el tema de los parametros que deja al volver a llamar a la funcion
print(rt(1,1), ro(5))