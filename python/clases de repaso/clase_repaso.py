from queue import Queue as Cola 
from queue import LifoQueue as Pila

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


# un_responsable_por_turno(grilla)

# Ejercicio 5
registro = {
    "maixmo": (50, 35, 41, 100, 0),
    "adolfo": (75, 0, 11, 100, 15),
    "nicolas": (4, 35, 1, 100, 63),
    "pedro": (0, 0, 61, 0, 61),
}

def promedio_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]: 
    res = {}
    for i in registro: 
        cant_salas: int = 0
        tiempo: float = 0
        for j in registro[i]: 
            if 0 <= j <= 60: 
                cant_salas += 1
                tiempo += j
        # cargo el diccionario: 
        if tiempo > 0 and cant_salas > 0: 
            res[i] = (cant_salas, float(tiempo / cant_salas))
        else: 
            res[i] = (0, 0)

    return res

# print(promedio_salidas(registro))

# Ejercicio 6
tiempos = [1, 0,  2, 4, 6, 61, 3, 7, 3, 5, 7]
def tiempo_mas_rapido(tiempo_in_sala: list[int]) -> int: 
    longitud = len(tiempo_in_sala)
    # datos por defecto
    tiempo = 0
    posicion = 0
    for i in range(longitud):
        valor = tiempo_in_sala[i]
        if valor == 0 or valor == 61: 
            continue
        if tiempo < valor : 
            tiempo = valor
            posicion = i
    return posicion

# print(tiempo_mas_rapido(tiempos))

# Ejercicio 7
def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]: 
    valores_parciales = []
    racha = 0
    posicion = 0
    actualizar_posicion = False

    for i in range(len(tiempos)): 
        if 1 <= tiempos[i] <= 60: 
            # en caso de que la racha sea 1, esto es pq se actualizo, le agrego la posicion correcta
            if actualizar_posicion : 
                posicion = i
                actualizar_posicion = False # una vez q la actualiza se desactiva
            racha += 1
        else : 
            #guardo los valores previos:
            if racha > 0: 
                valores_parciales.append({"racha": racha, "posicion_inicial": posicion, "posicion_final": i -1})  # se pone el -1 pq se buisca la posicion anterior
            # reinicio los valores:
            racha = 0 
            posicion = 0
            actualizar_posicion = True
    # guardo el ultimo elemento: 
    if racha > 0 :
        valores_parciales.append({"racha": racha, "posicion_inicial": posicion, "posicion_final": len(tiempos) - 1})

    #comparo cual tiene una mayor racha
    mejor_racha = 0
    inicial = 0
    final = 0
    for i in valores_parciales: 
        if i["racha"] > mejor_racha: 
            inicial = i["posicion_inicial"]
            final = i["posicion_final"]
            mejor_racha = i["racha"]
    return (inicial, final)

# print(racha_mas_larga([1, 2, 3, 4]))              # ➜ (0, 3)
# print(racha_mas_larga([3, 4, 15, 34, 61, 55, 27])) # ➜ (0, 3)
# print(racha_mas_larga([0, 0, 1, 2, 3, 61, 4, 5]))  # ➜ (2, 4)

# Ejercicio 8
amigos_por_salas = [
  [0, 0, 15, 0],   # ✅ cumple: 1º, 2º y 4º no fueron (0), 3º sí fue (15)
  [0, 0, 0, 0],    # ❌ no cumple: el 3º no fue (0)
  [0, 0, 61, 0],   # ✅ cumple: el 3º fue (aunque no salió)
  [0, 1, 30, 0],   # ❌ no cumple: el 2º sí fue
  [1, 0, 45, 0],   # ❌ no cumple: el 1º sí fue
  [0, 0, 0, 0]
]

def escape_solitario(amigos_por_salas: list[list[int]]) -> list[int]: 
    res = []
    for j in range(len(amigos_por_salas)): 
        sala = amigos_por_salas[j]
        jugador = 1 # emoieza con el amigo ese
        estado = True
        for amigo in sala: 
            if jugador != 3: 
                if amigo != 0:
                    estado = False 
                    break  # sale del ciclo pq no lo esta cumpliendo
            else : # jugador == 3
                if amigo == 0: 
                    estado = False 
                    break

            jugador += 1 # actualizamos el jugador 
             
        if estado : 
            res.append(j) # agrego la sala pq cumple la condicion
    return  res

# print(escape_solitario(amigos_por_salas))

# Ejercicio 9
torneo = {
    "mateo" : "me desvío siempre",
    "torko": "me la banco y no me desvío",
    "mirko": "me desvío siempre",
    "tomas": "me la banco y no me desvío",
    "alberto": "me la banco y no me desvío",
    "pedro": "me la banco y no me desvío",
}

def torneo_de_gallinas(estrategias) : 
    puntajes = {}
    # lleno la lista con los participantes (asi es automatico): 
    for i in estrategias: 
        puntajes[i] = 0 # valor por defecto
    
    # creo los jugadores: 
    jugadores = []
    for jugador in estrategias.keys(): 
        jugadores.append(jugador)

    for participante in range(len(estrategias)): 
        for oponente in range(participante + 1, len(estrategias)) :
            # obtengo los nombres de cada jugador
            a = jugadores[participante]
            b = jugadores[oponente]

            estrategia_participante = estrategias[a]
            estrategias_oponente = estrategias[b]

            if estrategia_participante == "me desvío siempre" and estrategias_oponente == "me desvío siempre" : 
                puntajes[a] -= 10
                puntajes[b] -= 10
            elif estrategia_participante == "me desvío siempre" and estrategias_oponente == "me la banco y no me desvío": 
                puntajes[a] -= 15
                puntajes[b] += 10
            elif estrategia_participante == "me la banco y no me desvío" and estrategias_oponente == "me desvío siempre": 
                puntajes[a] += 10
                puntajes[b] -= 15
            else : # los 2 no se desvian 
                puntajes[a] -= 5
                puntajes[b] -= 5

    return puntajes

# print(torneo_de_gallinas(torneo))

# Ejercicio 10
fila = Cola()
fila.put(("a", "común"))
fila.put(("b", "común"))
fila.put(("c", "vip"))
fila.put(("d", "vip"))
fila.put(("e", "común"))
fila.put(("f", "vip"))


def reordenar_cola_priorizando_vips(cola: Cola) -> Cola[str]: 
    usuariso_vistos: list[(str, str)] = []
    
    fila_vips = Cola()
    fila_comunes = Cola()

    nueva_fila = Cola()

    while not cola.empty(): 
        cliente = cola.get()
        print(cliente)
        usuariso_vistos.append(cliente)

        if cliente[1] == "común": 
            fila_comunes.put(cliente[0])
        else : 
            fila_vips.put(cliente[0])
    
    # creo la nueva fila fusionada
    while not fila_vips.empty(): 
        nueva_fila.put(fila_vips.get())
    while not fila_comunes.empty(): 
        nueva_fila.put(fila_comunes.get())

    # recreo la fila inicial
    for i in usuariso_vistos: 
        cola.put(i)

    return nueva_fila

# print(reordenar_cola_priorizando_vips(fila).queue)

# Ejercicio 11
def cuantos_sufijos_son_palindromos(texto: str) -> int: 
    cantidad_palindormos = 0
    if es_palindromo(texto): 
        cantidad_palindormos += 1
    palabra = texto
    while len(palabra) > 1 :
        palabra = crear_sufijos(palabra)
        if es_palindromo(palabra): 
            cantidad_palindormos += 1
    return cantidad_palindormos

def crear_sufijos(palabra: str) -> str : 
    sufijo = ""
    for i in range(1, len(palabra)): 
        sufijo += palabra[i]

    return sufijo

def es_palindromo(palabra: str) -> bool: 
    pila = Pila()
    # agrego las letras
    for i in palabra: 
        pila.put(i)
    # verifco que sean iguales cada letra: 
    for i in palabra: 
        if i != pila.get(): # nunca daria error, pq se supone que siempre hay la misma cantidad de letras en plabra que en la pila, ya que ahi se cargan todos los elementos
            return False
    return True

# print(cuantos_sufijos_son_palindromos(input("decime una palabra y te digo cuantos palindromos hay contando sus sufijos: ")))

# Ejercicio 12
VACIO = " "
tablero = [
    ["O", VACIO, "X"],
    ["X", "X", "K"],
    ["O", VACIO, "X"]
]

def quien_gano_tateti_v2(tablero: list[list[str]])-> int : 
    # primero analizo las columnas y despues paso a las filas, sabiendo que es una matriz cuadrada: 
    ganador_x = False
    ganador_o = False 
       
    for columna in range(len(tablero[0])):
        # antes de que empieze cada columna se reinician los datos: 
        elemento_anterior = VACIO
        contador = 0

        for fila in range(len(tablero)):
            actual = tablero[fila][columna]
            
            # reinicio los datos 
            if actual == VACIO: 
                elemento_anterior = VACIO
                contador = 0
                
            elif actual == elemento_anterior: 
                contador += 1
   
            else: # reinicia pq empieza de nuevo:
                contador = 1 
                elemento_anterior = actual
                
        # una vez que termino de recorrer la fila, verifico si alguien ya gano
        if contador == 3 : 
            if elemento_anterior == "X": 
                ganador_x = True
            elif elemento_anterior == "O": 
                ganador_o = True
    
    if ganador_x and ganador_o: 
        return 3 # trampa
    elif ganador_x : 
        return 1
    elif ganador_o: 
        return 2
    else : 
        return 0 # empate
    
## print(quien_gano_tateti_v2(tablero))

# Ejercicio 13
urgentes = Cola()
postergrables = Cola()
for i in range(0, 10, 2): 
    urgentes.put(i)

for i in range(1, 10, 2): 
    postergrables.put(i)

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola: 
    # sabiendo que len(urgentes) == len(postergables)
    res: Cola[int] = Cola()
    while not urgentes.empty(): 
        res.put(urgentes.get())
        res.put(postergables.get())

    return res

print(orden_de_atencion(urgentes, postergrables).queue)

# Ejercico 14
registros = [
    (1, "clamidia"), 
    (2, "calculos renales"),
    (3, "covid-19"),
    (4, "fiebre amarilla"),
    (5, "anginas"),
    (6, "covid-19"),
    (7, "covid-19"),
    (8, "covid-19"),
]

infecciosas = ["fiebre amarilla", "covid-19", "clamidia"]
def alarma_epidemologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]: 
    pacientes_atendidos: int = len(registros)
    res: dict[str, float] = {}
    lista_de_enfermedades_infeccisosas = []
    for id, enfermedad in registros : 
        if enfermedad in infecciosas: 
            lista_de_enfermedades_infeccisosas.append(enfermedad)

    for i in lista_de_enfermedades_infeccisosas: 
        cantidad: int = 0
        for k in lista_de_enfermedades_infeccisosas: 
            if i == k:
                cantidad += 1 
        
        porcentaje: float = float(cantidad / pacientes_atendidos)
        if porcentaje >= umbral: 
            res[i] = porcentaje

    return res 

#print(alarma_epidemologica(registros, infecciosas, 0.1))

# Ejercicio 15
horas = {
    101: [8, 9, 7, 8],        # total: 32
    203: [10, 10, 10],         # total: 29
    305: [8, 8, 8, 8],        # total: 32
    402: [6, 7, 6, 50],        # total: 26
}

def suma_elemetos(lista: int): 
    total = 0
    for i in lista : 
        total += i
    return total

def empleado_del_mes(horas: dict[int, list[int]]) -> list[int]: 
    mejor_horas = 0
    majores_empleados = []
    for i in horas: 
        suma_horas = suma_elemetos(horas[i])
        if suma_horas >= mejor_horas: 
            if suma_horas > mejor_horas: 
                mejor_horas = suma_horas 
            majores_empleados.append(i)
    return majores_empleados

print(empleado_del_mes(horas))

# ejercicicio 16
def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]: 
    res: list[float] = []
    for piso in camas_por_piso: 
        cantidad_de_camas_ocupadas: float = 0
        for cama in piso: 
            if cama == True : 
                cantidad_de_camas_ocupadas += 1
        # calcula el resultado del piso, ya que piso = cantidad de camas
        res.append(cantidad_de_camas_ocupadas / len(piso))
    return res
        
camas_por_piso = [[True, False, True], [False, False, True], [True, True, True]]