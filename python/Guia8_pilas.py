from queue import LifoQueue as Pila
import random

# Ejercicio 1.1
def convertir_pila_a_lista(pila: Pila[int]) -> list[int]: ##Solo para poder mostrarla por consola
    lista = []
    while not pila.empty(): ##Mientras la pila no este vacia
        num = pila.get()
        lista.append(num)

    ## Vuelvo a armar la pila 
    for i in range(len(lista) -1, -1, -1):
        pila.put(lista[i])

    ##Retorno la lista (así se puede ver por pantalla)
    return lista

## Esto es lo que pide el ejericicio, lo anterior es para que yo pueda ver el resultado
def generar_numeros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila: Pila[int] = Pila()
    for i in range(cantidad):
        num: int = random.randint(desde, hasta)
        pila.put(num)
    print(pila.queue)
    return pila

# Ejercicio 1.2
def cantidad_de_elementos (pila: Pila) -> int: 
    contador = 0
    ##los gurado en una pila para luego restauralos a la original
    pila_repuesto = Pila()
    while not pila.empty():
        contador += 1 ##Le sumo uno
        num = pila.get()
        pila_repuesto.put(num)
    ## una vez q termino de contar, guardo en la pila orgiginal pq es lo q me pide el ejercicio
    while not pila_repuesto.empty():
        num = pila_repuesto.get()
        pila.put(num)
    
    return contador ## Retorno el contador

## Ejermplo para probarlo
# pila = Pila()
# for i in range(1, 10):
#     pila.put(i)

# print(cantidad_de_elementos(pila))

# Ejercicio 1.3
def buscar_el_maximo(pila: Pila) -> int:
    pila_interna = Pila()
    maximo = pila.get() ## Obtengo el ultimo y lo trato como el mas grande
    pila_interna.put(maximo) ##lo gurado en la pila de respuesto

    while not pila.empty():
        elemento = pila.get()
        if elemento > maximo:
            maximo = elemento
        ## lo guardo en la de repuesto:
        pila_interna.put(elemento)

    #restauro la pila original
    while not pila_interna.empty():
        pila.put(pila_interna.get())

    return maximo

# pila2 = Pila()
# for i in range(1, 10):
#     num = random.randint(-1, 30)
#     pila2.put(num)
# print(pila2.queue)

# print(buscar_el_maximo(pila2))

# Ejercicio 1.4
def buscar_nota_maxima(pila: Pila[tuple[str, int]]) -> tuple[str, int] : 
    elemento = pila.get()
    mejor_nota = elemento[1]
    mejor_nombre = elemento[0]

    ##Lo guardo en una pila interna: 
    pila_interna = Pila()
    pila_interna.put(elemento)

    while not pila.empty():
        elemento = pila.get()
        nota = elemento[1]
        nombre = elemento[0]

        if nota > mejor_nota:
            mejor_nota = nota
            mejor_nombre = nombre

        pila_interna.put(elemento) ##Lo guardo en la pila de repuesto
    
    return mejor_nombre
    
# pila3 = Pila()
# pila3.put(("matematica", 5))
# pila3.put(("ingles", 8))
# pila3.put(("fisica", 3))
# pila3.put(("esuducacion fisica", 1))
# pila3.put(("historia", 7))
# print(pila3.queue)
# print(buscar_nota_maxima(pila3))

# Ejercicio 1.5
def esta_bien_balanceada(palabra: str) -> bool: 
    pila = Pila()

    for i in palabra: 
        if i == "(": 
            pila.put(i)
        elif i == ")":
            if pila.empty(): 
                return False # PQ no se puede abrir un parentesis con la lista vacia
            else: 
                pila.get() # Quito ese parentesis
    return pila.empty() #PQ si la pila no esta vacia, significa q quedo algo si cerrar, y por lo tanto esta mal balanceada

# print(esta_bien_balanceada("1 + (2 * 3)"))
# print(esta_bien_balanceada("1 + ( 2 x 3 = ( 2 0 / 5 ) )"))
# print(esta_bien_balanceada("10 * ( 1 + ( 2 * (-1)))"))
# print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))
# print(esta_bien_balanceada("())"))

# Ejercicio 1.6
def evaluar_expresion(expresion: str) -> int:
    operandos = Pila()
    operadores = "*-+/"
    for i in expresion:
        if (not i in operadores) and i != " ":
            operandos.put(int(i))
        elif i in operadores:
            ## Cambio los valores de el num es decir en las opereacions por la forma en la que se guradn en las pilas
            num1 = operandos.get()
            num2 = operandos.get()
            if i == "+":
                operandos.put(num2 + num1)
            elif i == "-":
                operandos.put(num2 - num1)
            elif i == "*":
                operandos.put(num2 * num1)
            elif i == "/":
                operandos.put(num2 / num1)

    return operandos.get() ## Resultado final 

# h = evaluar_expresion("3 4 + 5 * 2 -")
# print(h)

# Ejercicio 1.7
def intercarlar(p1: Pila, p2: Pila): 
    pila1 = Pila()
    pila2 = Pila()
    pila_final = Pila()

    while not p1.empty():
        pila1.put(p1.get())
    while not p2.empty():
        pila2.put(p2.get())

    while not pila1.empty(): #Miro solo lo de pila 1 pq es == en logitud al de pila 2
        pila_final.put(pila1.get())
        pila_final.put(pila2.get())
    
    return pila_final.queue 

# p1 = Pila()
# for i in range(0, 40, 2):
#     p1.put(i)
# p2 = Pila()
# for i in range(1, 40, 2):
#     p2.put(i)

# print(p1.queue)
# print(p2.queue)
# print("resultado:")
# print(intercarlar(p1, p2))




