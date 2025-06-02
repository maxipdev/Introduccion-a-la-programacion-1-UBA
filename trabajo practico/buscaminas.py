import random
from typing import Any
import os

# Constantes para dibujar
BOMBA = chr(128163)  # simbolo de una mina
BANDERA = chr(128681)  # simbolo de bandera blanca
VACIO = chr(9733)  # simbolo vacio inicial

# Tipo de alias para el estado del juego
EstadoJuego = dict[str, Any]

def existe_archivo(ruta_directorio: str, nombre_archivo:str) -> bool:
    """Chequea si existe el archivo en la ruta dada"""
    return os.path.exists(os.path.join(ruta_directorio, nombre_archivo))

def colocar_minas(filas:int, columnas: int, minas:int) -> list[list[int]]:
    return [[]]


def calcular_numeros(tablero: list[list[int]]) -> None:
    return


def crear_juego(filas:int, columnas:int, minas:int) -> EstadoJuego:
    return {}


def obtener_estado_tablero_visible(estado: EstadoJuego) -> list[list[str]]:
    return [[]]

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
    [VACIO,  VACIO,  VACIO, -VACIO],
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
        pass # no hago nada, pq el estado es el mismo que antes
    elif estado["tablero-visible"][fila][columna] == VACIO: 
        estado["tablero-visible"][fila][columna] = BANDERA # le asigno la bandera en ese lugar
    elif estado["tablero-visible"][fila][columna] == BANDERA: 
        estado["tablero-visible"][fila][columna] = VACIO # le asigno la el vacio de nuevo en ese lugar




    pass


# Ejercicio 6
def descubrir_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
    return

# Ejercicio 7
def verificar_victoria(estado: EstadoJuego) -> bool:
    return True


def reiniciar_juego(estado: EstadoJuego) -> None:
    return


def guardar_estado(estado: EstadoJuego, ruta_directorio: str) -> None:
    return


def cargar_estado(estado: EstadoJuego, ruta_directorio: str) -> bool:
    return False