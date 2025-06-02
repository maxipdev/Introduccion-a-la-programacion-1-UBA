import random
from typing import Any
import os
from queue import Queue as Cola

# Constantes para dibujar
BOMBA = chr(128163)  # simbolo de una mina
BANDERA = chr(128681)  # simbolo de bandera blanca
VACIO = chr(9733)  # simbolo vacio inicial

# Tipo de alias para el estado del juego
EstadoJuego = dict[str, Any]

# Ejercicio 5
tablero = [
    [1, -1,  1,  0],
    [1,  1,  1,  0],
    [1,  1,  2,  1],
    [1, -1,  2, -1],
]

tablero_visible = [
    [VACIO,  VACIO,  VACIO,  VACIO],
    [VACIO,  VACIO,  VACIO,  VACIO],
    [VACIO,  VACIO,  VACIO,  VACIO],
    [VACIO,  VACIO,  VACIO,  VACIO],
]

estado: EstadoJuego = {
    "filas": 4, 
    "columnas": 4,
    "minas": 3,
    "juego-terminado": False,
    "tablero": tablero,
    "tablero-visible": tablero_visible
}

# esta funcion sirve para marar una celda, es decir para ponerle una bandera 
def marcar_celda(estado: EstadoJuego, fila: int, columna: int) -> None:

    # verifico condiciones para marcar el estado:
    if estado["juego-terminado"] == True or estado["tablero-visible"][fila][columna] != VACIO and estado["tablero-visible"][fila][columna] != BANDERA: 
        return # no hago nada, pq el estado es el mismo que antes
    elif estado["tablero-visible"][fila][columna] == VACIO: 
        estado["tablero-visible"][fila][columna] = BANDERA # le asigno la bandera en ese lugar
    elif estado["tablero-visible"][fila][columna] == BANDERA: 
        estado["tablero-visible"][fila][columna] = VACIO # le asigno la el vacio de nuevo en ese lugar



# print(estado["tablero-visible"])
# marcar_celda(estado, 2, 1)
# print(estado["tablero-visible"])
# # marcar_celda(estado, 2, 1)
# # print(estado["tablero-visible"])

# Ejercicio 6
# verifica si estan todas las celdas descubiertas
def todas_las_celdas_seguras_descubiertas(estado: EstadoJuego) -> bool: 
    tablero_visible = estado["tablero-visible"]
    tablero = estado["tablero"]

    for fila in range(estado["filas"]): 
        for columna in range(estado["columnas"]): 
            # lo que hace es fijarse que en el tablero (el q estan las respuestas) no haya ninguna bomba en ese lugar
            # en caso de que no haya, se pide que el usuario la haya descubierto, es decir no tenga una bandera en esa posicion o que no la haya tocado
            # si cumple estas condicones descubrio esa fila
            # ignora a las columnas que tienen bombas, pq esas no se tienen que descubir 
            if tablero[fila][columna] != -1 : #ignora las que son bombas --> Las saltea
                if tablero_visible[fila][columna] == VACIO or tablero_visible[fila][columna] == BANDERA:
                    return False # da un error pq no se descubrieron todas
    
    return True # si no hubo ningun error

# obteien todos los posibles caminos, si hay adyacentes multiples o solo da el valor a mostrar en caso de que sea != 0
def caminos_recorridos(estado: EstadoJuego, fila: int, columna: int) -> None: 
    tablero = estado["tablero"]
    tablero_visible = estado["tablero-visible"]

    celdas_vistas: list[tuple[int, int]] = []
    cola: Cola = Cola()
    # agrego el primer elemento por defecto, es el que se selecciono
    cola.put((fila, columna))

    while not cola.empty():
        celda = cola.get() # 0 = fila y 1 = columna

        # lo hago por el opuesto: 
        if celda in celdas_vistas or tablero_visible[celda[0]][celda[1]] == BANDERA: 
            continue # se reinicia el ciclo pq no tiene que ejecutar algo que esta repetido o si es una bandera, ya que no la tiene que mostrar

        # agrego a las celdas vistas: 
        celdas_vistas.append(celda)
        
        #muestro la celda en pantalla
        tablero_visible[celda[0]][celda[1]] = tablero[celda[0]][celda[1]]

        #verifico si es un cero, en caso de serlo necesito sus adyacentes: 
        if tablero[celda[0]][celda[1]] == 0: 
            adyacentes = obtener_adyacentes(estado, celda[0], celda[1])
            
            #recorro cada adyacente
            for i in adyacentes: 
                # evita que se añadan a la cola celdas que ya fueron verificadas
                # en caso de qeu todavia no se hayan verificado se guradan igual en la cola pero despues se rechazan arriba
                # se hace esto para evitar que se repita tantes veces el codigo del principio, seria como un metodo de filtro
                if i not in celdas_vistas: 
                    cola.put(i)

# Funcion para obtener las adyacentes
def obtener_adyacentes(estado: EstadoJuego, fila: int, columna: int) -> list[tuple[int, int]]: 
    adyacentes: list[tuple[int]] = []

    cantidad_de_filas: int = estado["filas"]
    cantidad_de_columnas: int = estado["columnas"] 

    # defino los posibles movimientos: 
    movimientos: list[tuple[int]] = [
        (-1, -1), (-1, 0), (-1, 1),  # arriba izquierda, arriba, arriba derecha
        (0, -1),          (0, 1),    # izquierda,       , derecha
        (1, -1),  (1, 0), (1, 1)     # abajo izquierda, abajo, abajo derecha
    ]

    # Recorrro todos los movimientos posibles
    for x,y in movimientos: 
        nueva_fila: int = fila + x 
        nueva_columna: int = columna + y

        # Verifica que este dentro del rango: 
        if 0 <= nueva_fila < cantidad_de_filas and 0 <= nueva_columna < cantidad_de_columnas: 
            adyacentes.append((nueva_fila, nueva_columna))

    return adyacentes

# funcion que pide el ejercicio
def descubrir_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
    
    # Verifico condciones: 
    if estado["juego-terminado"] == True: 
        return # no tiene que hacer nada más porque ya no puede jugar porque perdio
    
    if estado["tablero"][fila][columna] == -1: 
        estado["juego-terminado"] = True # termina el juego
        estado["tablero-visible"][fila][columna] = BOMBA # pongo la bomba en el tablero
    
    elif estado["tablero"][fila][columna] != -1:
        # se fija si todas las celdas fueron descubiertas, en caso que si, se termian el juego, el usuario ganó 
        if todas_las_celdas_seguras_descubiertas(estado): 
            estado["juego-terminado"] = True # termina el juego
        else: # en este caso, significa q el usuario no gano, entonces hay que mostrar el resultado de esa celda 
            caminos_recorridos(estado, fila, columna)
 

# # Ejercicio 7
def verificar_victoria(estado: EstadoJuego) -> bool:
    if todas_las_celdas_seguras_descubiertas(estado): 
        if estado["juego-terminado"] != True: 
            estado["juego-terminado"] = True
        return True
    else: return False






