from queue import Queue as Cola
# Ejercicio 1: 

lista = [1,1,1,2,2,4,5,5,5,5,1,1,3,3]

def maximas_cantidades_consecutivos(lista): 
    elementos_evaluados = []
    res = {}
    for i in range(len(lista)):
        a = lista[i]
        #guardo el elemento como visto: 
        if a not in elementos_evaluados: 
            elementos_evaluados.append(a)
        else: 
            continue # lo pasamos pq ya no lo necesitamso más, pq ya fue evaluado

        mejor = []
        contador = 0 
        for k in range(i, len(lista)): 
            b = lista[k]

            if a == b: 
                contador += 1 #sumo 1 más pq hay otra aparicion
            else:
                mejor.append(contador) #guardo los datos previos antes que se reinicie 
                contador = 0 
        #miro cual fue la mejor respeusta:
        actual = 0
        for i in mejor: 
            if i > actual: 
                actual = i
        #guardo el elemento en el diccioanrio: 
        res[a] = actual

        #en caso de que el contador no sea 0, significa que hay elementos todavia no guardados: 
        # lo hago aca abajo pq sino la ora parte lo sebreescribe
        if contador > 0: 
            res[a] = contador # se gurada exacto, pq son los ultimos elementos
            contador = 0 # lo rinicio para que no haya más problemas

    return res

#print(maximas_cantidades_consecutivos(lista))

# Ejercicio 2:
matriz = [
    [2, 3, 5],
    [7, 11, 15], 
    [18, 81, 25]
]

def es_primo(num: int)-> bool: 
    n = 2 #pq sabemos que el 1 divide a todos
    while n < num: 
        if num % n == 0: 
            return False
        n += 1
    return True

def maxima_cantidad_de_primos(matriz: list[list[int]]) -> int: 
    res_parciales = []
    for columna in range(len(matriz)): 
        cantidad = 0
        for fila in range(len(matriz)): 
            celda = matriz[fila][columna]
            if es_primo(celda): 
                cantidad += 1
        #guardo los resultados: 
        res_parciales.append(cantidad) # gurad la columna con la cantidad de primos que hay

    #miro cual es la columna con más cantidad de primos: 
    mejor = 0
    for i in res_parciales:
        if i > mejor: 
            mejor = i
    return mejor

# print(maxima_cantidad_de_primos(matriz))

# Ejercicio 3
cola: Cola[int,int] = Cola()
cola.put((3,2))
cola.put((4,6))
cola.put((-2,5))
cola.put((0,0))
cola.put((2,0))
cola.put((-3,-3))
cola.put((1,0))
cola.put((5, -5))
cola.put((3,1))

def tuplas_positivas_Y_negativas(cola: Cola[tuple[int, int]]): 
    colas_positivas: list[tuple[int, int]] = []
    colas_negativas: list[tuple[int, int]] = []
    
    while not cola.empty(): 
        x, y = cola.get()
        if x * y > 0: 
            colas_positivas.append((x,y))
        elif x * y < 0: 
            colas_negativas.append((x,y))
        
    #guardo lo elementos de cada lista en la cola, ya que se estaba modificando: 
    for i in colas_positivas: 
        cola.put(i)
    for j in colas_negativas: 
        cola.put(j)

# print(cola.queue)
# tuplas_positivas_Y_negativas(cola)
# print(cola.queue)

# Ejercicio 4
cuenta = "10+5-3+5"
def resolver_cuenta(cuenta: str) -> float: 
    operadores = ["+", "-"]
    inicial = True
    digito = ""
    operacion = []
    es_decimal = False
    for i in cuenta: 
        print(i == ".")
        if i in operadores: 
            # solo hago estas cosas en caso de que no empieze con operador 
            if not inicial:
                operacion.append(digito)
                digito = "" #lo reinicio
            operacion.append(i) #guardo el operador 
        else: 
            if i == ".": 
                es_decimal = True # significa que hay que usar float
            inicial = False
            digito += i

    #guardo el ultimo elemento en caso de que haya: 
    if digito != "": 
        operacion.append(digito)
        digito = "" # lo reinicio ahora

    #una vez que terminamos de guardar todos los elementos hago las operaciones: 
    valor = 0
    k = 0
    print(operacion)

    if operacion[0] in operadores: 
        if operacion[0] == "+":
            valor = float(operacion[1])
        else:
            valor = -float(operacion[1])

        k = 2 #pq ya usamos los primeros 2 valores
    else: 
        valor = float(operacion[0])
        k = 1

    while k < len(operacion): 
        operador = operacion[k]
        digito = float(operacion[k + 1])
        #siempre es asi pq lo que se llega a usar es el digito siempre y en caso del operador al incio, usa operador y digito, por lo tanto el prxomo elemento es un digito

        if operador == "+":
            valor += digito
        else:
            valor -= digito

        k += 2 # le sumamos 2, pq usamos 2 elementos

    if es_decimal: 
        return valor
    else: 
        return int(valor)

print(resolver_cuenta(cuenta))