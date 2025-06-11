# Ejercicio 1
def stock_productos(lista: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    res: dict[str, tuple[int, int]] = {}
    for nombre, valor in lista: 
        # verico que ese producto no haya sido añadido al diccionario antes, pq en caso de que haberlo hecho, no es necesario volverlo a mirar:
        if nombre in res: 
            continue # se saltea este valor y va hacia el que sigue
        # en caso de que no este se agrega
        maximo: int = valor # los pongo por defecto
        minimo: int = valor # los pongo por defecto
        for name, value in lista: 
            if nombre == name: 
                # miro el más grande
                if value > maximo: 
                    maximo = value
                #miro el más chico
                if value < minimo: 
                    minimo = value
        # una vez que recorrio todo la lista comparando con ese valor,  lo agrega al diccionario
        res[nombre] = (minimo, maximo)
    return res


lista = [("collares", 1), ("pipetas", 100), ("juguetes", 5), ("collares", 7), ("collares", 3)]

#print(stock_productos(lista))

# Ejercicio 2
def filtrar_por_primos(codigo_barra : list[int]) -> list[int]:
    res = []
    for i in codigo_barra:
        ultimos_tres = i % 1000
        if es_primo(ultimos_tres): 
            res.append(i)
    return res
        

def es_primo(num: int) -> bool: 
    i = 2 # empieza con el 2 pq el uno siempre dividide a todos
    while i < num: 
        if num % i == 0: 
            return False
        i += 1
    return True # en caso de que sea primo

# Ejercicio 3
def subsecuencia_mas_larga(lista: list[str]) -> int:
    contador = 0
    posicion_inicial = 0
    cambio_posicion = False
    lista_de_resultados: list[tuple[int, int]] = []
    for i in range(len(lista)): 
        if lista[i] == "gato" or lista[i] == "perro": 
            if contador == 0: 
                posicion_inicial = i
            contador += 1
        else: 
            lista_de_resultados.append((contador, posicion_inicial))
            contador = 0

    lista_de_resultados.append((contador, posicion_inicial))

    cant_base = 0
    coordenadas = 0
    for cantidad, posicion in lista_de_resultados: 
        if cantidad > cant_base : 
            cant_base = cantidad
            coordenadas = posicion
    return coordenadas

# print(subsecuencia_mas_larga(["perro", "gato", "perro", "perro", "perro", "gato", "gato", "perro", "perro"]))
# print(subsecuencia_mas_larga(["perro", "perro", "hamster", "perro", "caballo", "perro", "gato", "gato", "perro", "perro"]))

# Ejercicio 4
grilla = [
    ["lopez", "martinez", "ocantos", "lobos", "sanchez", "lopez", "ocantos"],
    ["lopez", "martinez", "ocantos", "lobos", "sanchez", "lopez", "ocantos"],
    ["lopez", "martinez", "ocantos", "lobos", "sanchez", "lopez", "ocantos"],
    ["lopez", "martinez", "ocantos", "lobos", "sanchez", "lopez", "ocantos"],

    ["martinez", "lopez", "lobos", "ocantos", "ocantos", "lopez", "ocantos"],
    ["martinez", "lopez", "lobos", "ocantos", "ocantos", "martinez", "ocantos"],
    ["martinez", "lopez", "lobos", "ocantos", "ocantos", "martinez", "ocantos"],
    ["martinez", "lopez", "lobos", "ocantos", "sanchez", "martinez", "ocantos"],
]

def un_responsable_por_turno(grilla: list[list[str]]): 
    res = []
    for columna in range(len(grilla[0])):
        valor_mañana = True
        valor_tarde = True
        responsable_mañana = grilla[0][columna]
        responsable_tarde = grilla[4][columna]
        for fila in range(0, 4): 
            if responsable_mañana != grilla[fila][columna]:
                valor_mañana = False
                break 
            
        for fila in range(4, 8): 
            if responsable_tarde != grilla[fila][columna]:
                valor_tarde = False
                break 
        #agrego el resultado en la respuesta: 
        res.append((valor_mañana, valor_tarde))
    return res


h = un_responsable_por_turno(grilla)
print(h)