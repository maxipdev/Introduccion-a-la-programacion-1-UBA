from queue import Queue as Cola
import random

#Ejercicio 8
def generar_numeros_al_azar(cantidad, desde, hasta) -> Cola[int]:
    cola = Cola()

    for i in range(cantidad):
        num = random.randint(desde, hasta)
        cola.put(num)

    return cola.queue

# Ejercicio 9
def cantiad_de_elementos(cola: Cola) -> int:
    lista = []
    contador = 0
    while not cola.empty():
        lista.append(cola.get())
        contador += 1

    for i in lista:
        cola.put(i)

    return contador

def crear_cola_ejemplo(cantidad): 
    cola = Cola()
    for i in range(cantidad): 
        cola.put(i)
    print(cola.queue)
    return cola

# Ejercicio 10
def buscar_el_maximo(cola: Cola)-> int: 
    maximo = cola.get()
    lista = []
    lista.append(maximo) #Lo guardo
    while not cola.empty():
        elemento = cola.get()
        if elemento > maximo: 
            maximo = elemento
    # Restauro la cola
    for i in lista: 
        cola.put(i)
    return maximo

# Ejercicio 11
def buscar_nota_maxima(cola: Cola) -> tuple[str, int]: 
    lista = []
    elemento = cola.get()
    max_num = elemento[1]
    max_nombre = elemento[0]

    lista.append(elemento)

    while not cola.empty():
        elemento = cola.get()
        if elemento[1] > max_num:
            max_num = elemento[1]
            max_nombre = elemento[0]
        lista.append(elemento)
    
    for i in lista:
        cola.put(i)

    return (max_nombre, max_num)

# cola = Cola()
# cola.put(("matematica", 5))
# cola.put(("ingles", 8))
# cola.put(("fisica", 3))
# cola.put(("esuducacion fisica", 1))
# cola.put(("historia", 7))
# print(cola.queue)
# print(buscar_nota_maxima(cola))

# Ejercicio 12
def intercalar(c1: Cola, c2: Cola) -> Cola[int]:
    cola = Cola()
    lista1 = []
    lista2 = []

    while not c1.empty():
        elemento1 = c1.get()
        elemento2 = c2.get()

        lista1.append(elemento1)
        lista2.append(elemento2)

        cola.put(elemento1)
        cola.put(elemento2)

    for i in lista1: 
        c1.put(i)
    for i in lista2:
        c2.put(i)

    return cola.queue

# c1 = Cola()
# for i in range(0, 40, 2):
#     c1.put(i)
# c2 = Cola()
# for i in range(1, 40, 2):
#     c2.put(i)

# print(c1.queue)
# print(c2.queue)
# print("resultado:")
# print(intercalar(c1, c2))

# Ejercicio 13
def armar_carton() -> Cola[int]: 
    posibles_numeros = []
    for i in range(0, 100) :
        posibles_numeros.append(i)

    print(posibles_numeros)
    random.shuffle(posibles_numeros)
    carton = []
    for i in range(12): 
        num = posibles_numeros[i]
        carton.append(num)

    return carton

def armar_secuencia_de_bingo() -> Cola[int]: 
    bolillero = Cola()
    lista = []
    for i in range(0, 100): 
        lista.append(i)
    # Se mezclan los elemetos
    random.shuffle(lista)
    for i in lista: 
        bolillero.put(i)

    return bolillero

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola) -> int:
    cantidad_de_jugadas_necesesarias_para_ganar = 0
    acertados = 0
    while (not bolillero.empty()):
        if acertados == 12:
            break 
        cantidad_de_jugadas_necesesarias_para_ganar += 1
        bolilla = bolillero.get()
        print("bolilla: ", bolilla)
        for i in carton: 
            if i == bolilla: 
                acertados += 1
    return cantidad_de_jugadas_necesesarias_para_ganar

# print(jugar_carton_de_bingo(armar_carton(), armar_secuencia_de_bingo()))

# Ejercicio 14
def pacientes_urgentes(cola: Cola) -> int:
    count: int = 0
    lista = []
    while not cola.empty():
        paciente = cola.get() 
        lista.append(paciente)
        if paciente[0] < 4 :
            count += 1
    for i in lista: 
        cola.put(i)

    return count

# cola = Cola()
# cola.put((1, "toro"))
# cola.put((7, "toro"))
# cola.put((8, "toro"))
# cola.put((5, "toro"))
# cola.put((2, "toro"))
# cola.put((6, "toro"))
# cola.put((3, "toro"))

# print(pacientes_urgentes(cola))

# Ejercicio 15
def atencion_a_clientes(cola: Cola) -> Cola: 
    fila_prioridad = Cola()
    fila_preferencial = Cola()
    fila_general = Cola()

    fila = Cola()

    while not cola.empty(): 
        persona = cola.get()
        if persona[3]: # Si tiene prioridad pregunto
            fila_prioridad.put(persona)
        elif persona[2]: # si tiene preferencial con el banco
            fila_preferencial.put(persona)
        else: 
            fila_general.put(persona)
    
    while not fila_prioridad.empty(): 
        fila.put(fila_prioridad.get())
    while not fila_preferencial.empty(): 
        fila.put(fila_preferencial.get())
    while not fila_general.empty(): 
        fila.put(fila_general.get())
    
    return fila


def crear_clientes_ejemplo():
    cola = Cola()
    for i in range(1, 11):
        nombre = f"persona {i}"
        edad = random.randint(18, 90)
        if edad > 65:
            edad = True
        else :
             edad = False
        dni = i
        selector = random.randint(1, 30)
        if selector % 2 == 0: 
            preferencial_bancaria = True
        else : 
            preferencial_bancaria = False

        cola.put((nombre, dni, preferencial_bancaria, edad))
    print(cola.queue)
    return cola

crear_clientes_ejemplo()

h = atencion_a_clientes(crear_clientes_ejemplo())
print("orden actualizado......")
print(h.queue)