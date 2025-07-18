import random
from typing import Any
import os
from queue import Queue as Cola

# Constantes para dibujar
BOMBA = chr(128163)  # simbolo de una mina
BANDERA = chr(128681)  # simbolo de bandera blanca
VACIO = " "  # simbolo vacio inicial

# Tipo de alias para el estado del juego
EstadoJuego = dict[str, Any]

def existe_archivo(ruta_directorio: str, nombre_archivo:str) -> bool:
    """Chequea si existe el archivo en la ruta dada"""
    return os.path.exists(os.path.join(ruta_directorio, nombre_archivo))


#EJERCICIO 1. 
def colocar_minas(filas:int, columnas: int, minas:int) -> list[list[int]]:
    """    
    Crea el tablero del juego y coloca aleatoriamente la cantidad de minas en el tablero 

    Args: 
        filas: numero entero cantidad de filas del tablero.
        columnas: numero entero cantidad de columnas del tablero.
        minas: numero entero cantidad de minas a colocar en el tablero.

    Returns: 
        matriz del tablero con minas colocadas representadas con -1. 
    """
    res: list[list[int]] = []
    tablero_de_ceros: list[list[int]] = matriz_de_ceros(filas,columnas)          # usa matriz de ceros 
    posiciones: list[tuple[int,int]] = todas_las_posiciones(filas,columnas)      # genera tuplas de posiciones de la matriz
    posiciones_minas: list[tuple[int,int]] = minas_al_azar(posiciones, minas)
    for (i,j) in posiciones_minas:
        tablero_de_ceros[i][j] = -1                                              # donde hay ubicada una mina, coloca un -1 en su lugar en el tablero de ceros
        res = tablero_de_ceros
    return res 

def matriz_de_ceros (filas:int, col:int) -> list[list[int]] :
    """recibe un n: int fila y otro m: int como columna (pasados por colocar_minas) y crea un tablero solo de ceros de dimension n * m
    """
    res: list[list[int]] = []                                     
    i: int = 0
    j: int = 0
    for i in range(filas):
        filas = []                                                             #forma listas vacias cantidad de veces = cantidad de filas minas_al_azar
        for j in range(col):
            filas.append(0)                                                    # a cada fila la llena de los ceros (cantidad= n columnas) 
        res.append(filas)                                                      # agrega esa fila de ceros a res 
    return res 

def todas_las_posiciones (f:int,c:int) -> list[tuple[int,int]]:
    """recibe un int para representar a las filas y otro int para representar a las columnas. Va agregando todas las combinaciones lineales 
    (i,j) que recorren las dimensiones requeridas de filas y columnas. (i,j) son tuplas que representan la posicion (fila,columna) de cada 
    casillero de la matriz 
    """
    res: list[tuple[int,int]] = []                                
    for i in range (f):
        for j in range(c):
            res.append((i,j))
    return res 

def minas_al_azar (pos:list[tuple[int,int]], minas:int) -> list[tuple[int,int]]:  #toma todas las tuplas de posiciones posibles en la matriz y la cantidas de minas
    """"recibe pos: lista de tuplas que representa todas las posiciones dentro de la matriz del tablero. Tambien recibe un int que representa 
    la cantidad de minas que se quieren poner en el tablero. Luego, usando random sample toma aleatoriamente las posiciones. la cantidad de posiciones
    que toma es igual a la cantidad de minas. 
    """
    res: list[list[int]] = []
    res = random.sample(pos, minas)     
    return res 



#EJERCICIO 2. 

def calcular_numeros(tablero: list[list[int]]) -> None:
    """
    Modifica el tablero colocando a cada celda sin mina la cantidad de minas adyacentes. 
   
    Args: 
        tablero: matriz de enteros donde las celdas vacias estan representadas con 0 y las celdas con minas -1.

    Returns:
        None. La funcion modifica tablero. 
    """
    i: int = 0
    j: int = 0
    for i in range (len(tablero)):
        for j in range (len(tablero[0])):
            if tablero[i][j] == 0:
                tablero[i][j] = contador_minas_adyacentes(tablero, (i,j))

def contador_minas_adyacentes (tablero: list[list[int]], posicion: tuple[int,int]) -> int:
    """recibe un tablero conformado de 0 y -1, y una determinada posicion de ese tablero representada como una tupla (i,j) --> (fila, columna). recorre las 8 posiciones del tablero 
    adyacentes a (i,j) , viendo cuantas minas encuentra y añadiendolas al contador (devuelve el contador).
    """
    i: int = posicion[0]
    j: int = posicion[1]
    contador: int = 0
    for desplazo_i in [-1,0,1]:
        for desplazo_j in [-1,0,1]:
            if desplazo_i == desplazo_j == 0:                     # en el caso que pasamos por (0,0) es la celda i,j que es de la que queremos ver adyacentes, por lo tanto la saltamos
                continue
            desplazos_i = i + desplazo_i                          # a la posicion i , se le suma desplazo_i para iterar en los casilleros adyacentes a i 
            desplazos_j = j + desplazo_j                          # lo mismo con j (segunda coordenada del casillero)
            if (0 <= desplazos_i < (len(tablero))) and (0 <= desplazos_j < len(tablero[0])):    #para asegurarse de que sean casilleros validos (por ej si es una esquina, no tendra la msima cantidad de casilleros que uno del centro)
                if tablero[desplazos_i][desplazos_j] == -1:                   # si el casillero adyacente tiene una mina
                    contador = contador + 1                                   # --> sumamos 1 al contador 
    return contador 


# EJERCICIO 3 
def crear_juego(filas:int, columnas:int, minas:int) -> EstadoJuego:
    """
    Crea el estado inicial de una partida como diccionario EstadoJuego . 
    
    Args:
        filas: numero entero cantidad de filas del tablero 
        columnas: numero entero cantidad de columnas del tablero 
        minas: numero entero cantidad de minas a colocar en el tablero 
    
    Returns: 
        EstadoJuego: diccionario que representa el estado del juego con las claves: filas, columnas, minas, juego_terminado, tablero, tablero_visible
    """
    filas: int = filas 
    columnas: int = columnas
    minas: int = minas
    tablero_inicial: list[list[int]] = colocar_minas(filas, columnas, minas)
    calcular_numeros(tablero_inicial)                           
    tablero: list[list[int]] = tablero_inicial
    tablero_visible: list[list[str]] = crear_tablero_visible(tablero)
    juego: dict[str, Any] = {
        'filas': filas,
        'columnas': columnas,
        'minas' : minas,
        'juego_terminado' : termino_el_juego(tablero, tablero_visible),
        'tablero' : tablero,
        'tablero_visible' : tablero_visible 
    }
    return juego 

def crear_tablero_visible(tablero: list[list[int]]) -> list[list[str]]:
    """esta funcion recibe un tablero "oculto" , formado por n entre (-1,0,...,8) y crea otra matriz de la misma dimension, pero con todos los }
    casilleros igual a " " . 
    """
    i: int = 0
    j: int = 0
    filas_visibles: list = []
    res: list[list[str]] = []
    for i in range (len(tablero)):
        filas_visibles = []
        for j in range(len(tablero[0])):
            filas_visibles.append(VACIO)
        res.append(filas_visibles)
    return res 

def termino_el_juego (tablero: list[list[int]], tablero_visible: list[list[str]]) -> bool:    
    """recibe un tablero "oculto" y un tablero visible y verifica si termino el juego (porque gano o perdio), devolviendo un bool (true si termino 
     y false si aun no termina de jugar)
    """
    if todas_celdas_seguras_descubiertas(tablero, tablero_visible) or mina_descubierta(tablero, tablero_visible):
        return True 
    else:
        return False 

def todas_celdas_seguras_descubiertas(tablero: list[list[int]], tablero_visible: list[list[str]]) -> bool:      
    """recibe un tablero oculto y otro visible. devuelve True si todas las celdas que no contienen minas, es decir las distintas a -1
    fueron abiertas. si fueron abiertas, en el tablero visible se va a encontrar el mismo valor que en el tablero original "oculto"
    que es la cantidad de minas adyacentes. 
    """
    i: int = 0                                                                                            
    j: int = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] != -1 :                                 #verifica que los casilleros que no tienen mina en tablero, tienen la misma cantidad de adyacentes en tablero visible --> ya fue descubierto
                if tablero_visible[i][j] != str(tablero[i][j]):             
                    return False                                      # si hay casilleros sin mina que aun no fueron descubiertos, retorna false --> todavia no ganó
            else:
                if tablero_visible[i][j] != VACIO and tablero_visible[i][j] != BANDERA:         # si es una celda en tablero que tiene mina, en tablero visible NO debe estar descubierto --> tiene una bandera o vacio 
                    return False
    return True

def mina_descubierta (tablero:list[list[int]], tablero_visible: list[list[str]]) -> bool:        
    """funcion que verifica SI PERDIÓ. recibe un tablero y un tablero visible. perdió si en el tablero_visible hay una BOMBA, es decir 
    que descubrio una celda en la que habia una mina.
    """
    i: int = 0
    j: int = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == -1 :                # si el casillero en tablero tiene una mina 
                if tablero_visible[i][j] == BOMBA:        # si la descubrio --> en tablero visible en esa posicion hay BOMBA --> perdio
                    return True
    return False                       # si no encuentra ninguna bomba descubierta en el tablero devuelve False (no perdio aun)


# EJERCICIO 4 . 
def obtener_estado_tablero_visible(estado: EstadoJuego) -> list[list[str]]:
    """
    Recibe un estado juego (diccionario con claves: filas, col, minas, juego_terminado, tablero, tablero_visible)
    y retorna una copia del valor de tablero_visible.
    
    Args: 
        estado: diccionario EstadoJuego que representa el estado de una partida del juego  

    Returns: 
        copia de la matriz tablero_visible del EstadoJuego dado que representa lo que el jugador visualiza del tablero. 
    """
    estado: EstadoJuego
    res: list[list[str]] = estado['tablero_visible']
    return res 


# Ejercicio 5
def marcar_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
    """
    Función que establece una bandera en la posicion seleccionda y en el caso de que ya estuviera marcada con una bandera, se la quita
    """
    # verifico condiciones para marcar el estado:
    if estado['juego_terminado'] == True or estado['tablero_visible'][fila][columna] != VACIO and estado['tablero_visible'][fila][columna] != BANDERA: 
        return # no hago nada, pq el estado es el mismo que antes
    elif estado['tablero_visible'][fila][columna] == VACIO: 
        estado['tablero_visible'][fila][columna] = BANDERA # le asigno la bandera en ese lugar
    else : # esto es siempre asi, ya que se filtra, puede ser un vacio o un numero o una bandera, no puede ser otra cosa
        estado['tablero_visible'][fila][columna] = VACIO # le asigno la el vacio de nuevo en ese lugar


# Ejercicio 6
def caminos_recorridos(estado: EstadoJuego, fila: int, columna: int) -> None: 
    """
    Función que muestra la celda marcada y sus adyacentes solo si y solo si la celda seleccionada (fila X columna) en el tablero es cero y no tiene una bandera en la posicion adyacente a la celda
    
    Args: 
        estado: dict[str, any], estado principal del juego
        fila: int que este en el rango 0 <= fila < longitud del tablero
        columna: int que este en el rango 0 <= fila < longitud del tablero[0]
    
    return: 
        None: modifica el estado principal del juego


    """
    tablero: list[list[int]] = estado['tablero']
    tablero_visible: list[list[int]] = estado['tablero_visible']

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
        tablero_visible[celda[0]][celda[1]] = str(tablero[celda[0]][celda[1]])

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
    """
    Función que mediante una fila y una columna busca todos sus adyacentes en el tablero en en caso de que la celda (fila X columna) en el tablero tenga como valor al cero en dicha posicion y los devuelve

    Args: 
        estado: dict[str, any], estado principal del juego
        fila: int que este en el rango 0 <= fila < longitud del tablero
        columna: int que este en el rango 0 <= fila < longitud del tablero[0]
    
    return: 
        devuelve una lista que contiene una tupla de enteros -> list[tuple[int, int]]
    """
    adyacentes: list[tuple[int, int]] = []

    cantidad_de_filas: int = estado['filas']
    cantidad_de_columnas: int = estado['columnas'] 

    # defino los posibles movimientos: 
    movimientos: list[tuple[int, int]] = [
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


def buscador_de_bombas(tablero: list[list[int]], tablero_visible:  list[list[int]]) -> None: 
    """ 
    Obtiene todas las minas del tablero y las muestra en el tablero visible

    Args: 
        tablero: list[list[int]] que contiene numeros del 0 al 8, el cual todas las filas pertenecientes a tablero tienen la misma longitud

        tablero_visible: list[list[int]] que contiene los caracteres de BOMBA y VACIO y numeros del 0 al 8, el cual todas las filas pertenecientes a tablero_visible tienen la misma longitud

    return: 
        None: la función modifica el tablero

    """
    for fila in range (len(tablero)):  # se tiene que tienen las mismas longitudes el tablero vsible y el normal
        for columna in range(len(tablero)): 
            if tablero[fila][columna] == -1: 
                tablero_visible[fila][columna] = BOMBA # se agrega la bomba en el tablero visible


# funcion que pide el ejercicio
def descubrir_celda(estado: EstadoJuego, fila: int, columna: int) -> None:
    """
    Recibe una celda (fila X columna) en la cual marca la celda descubierta y sus adyacentes en caso de encontrar un cero en dicha posicion o muestra todas las bombas que hay en el tablero y modifica el eatsdo a juego terminado en caso de encontrar un -1 en la posicion
    
    Args: 
        estado: dict[str, Any]
        fila: int dentro del rango 0 al 8 inclusive 
        columna: int dentro del rango 0 al 8 inclusive

    return: 
        None: modifica el estado del juego
    """
    # Verifico condciones: 
    if estado['juego_terminado'] == True: 
        return # no tiene que hacer nada más porque ya no puede jugar porque perdio
    
    if estado['tablero'][fila][columna] == -1: 
        estado['juego_terminado'] = True # termina el juego
        buscador_de_bombas(estado["tablero"], estado["tablero_visible"]) #muesta todas las bombas
    
    else:
        caminos_recorridos(estado, fila, columna)
        # se fija si todas las celdas fueron descubiertas, en caso que si, se termian el juego, el usuario ganó 
        if todas_celdas_seguras_descubiertas(estado["tablero"], estado["tablero_visible"]): 
            estado['juego_terminado'] = True # termina el juego


# # Ejercicio 7
def verificar_victoria(estado: EstadoJuego) -> bool:
    """
    Función que verifica la victoria del usuario, devuelve True en caso de que todas las celdas seguras hayan sido descubiertas y False en el caso contrario 
    """
    return todas_celdas_seguras_descubiertas(estado["tablero"], estado["tablero_visible"])


# Ejercicio 8
def reiniciar_juego(estado: EstadoJuego) -> None:
    """
    Modifica el parametro estado para reiniciar los tableros.

    Args:
        estado: un EstadoJuego valido a ser modificado.

    Returns:
        Modifica las claves 'tablero','tablero_visible' y 'juego_terminado' del parametro recibido.
    """
    #Crea nuevos valores para estado['tablero'], estado['tablero_visible'] y estado['juego_terminado'].
    tablero_previo: list[list[int]] = estado['tablero']
    while estado['tablero'] == tablero_previo:
        nuevo_estado = crear_juego(estado['filas'], estado['columnas'], estado['minas'])
        # Asigna los nuevos valores al mismo diccionario.
        estado['tablero'] = nuevo_estado['tablero']
        estado['tablero_visible'] = nuevo_estado['tablero_visible']
        estado['juego_terminado'] = nuevo_estado['juego_terminado']
        
    return


# Ejercicio 9
def guardar_estado(estado: EstadoJuego, ruta_directorio: str) -> None:
    """
    Crea dos archivos de texto basado en las claves de un EstadoJuego.

    Args:
        estado: un EstadoJuego valido a ser leido.
        ruta_directorio: una ruta valida para una carpeta.

    Returns:
        Dos archivos de texto en la ruta especificada.
    """
    tablero_guardado = open(os.path.join(ruta_directorio, 'tablero.txt'), "w")
    for fila in estado['tablero']:
        for i in range(len(fila)):
            if i < len(fila) - 1:
                tablero_guardado.write(str(fila[i]))
                tablero_guardado.write(",")
            else:
                tablero_guardado.write(str(fila[i]) + "\n")
    tablero_guardado.close()
    tablero_visible_guardado = open(os.path.join(ruta_directorio, 'tablero_visible.txt'), "w")
    for fila in estado['tablero_visible']:
        for i in range(len(fila)):
            if i < len(fila) - 1:
                if str(fila[i]) == VACIO:
                    tablero_visible_guardado.write("?")
                elif str(fila[i]) == BANDERA:
                    tablero_visible_guardado.write("*")
                else:
                    tablero_visible_guardado.write(fila[i])
                tablero_visible_guardado.write(",")
            else:
                if str(fila[i]) == VACIO:
                    tablero_visible_guardado.write("?" + "\n")
                elif str(fila[i]) == BANDERA:
                    tablero_visible_guardado.write("*" + "\n")
                else:
                    tablero_visible_guardado.write(fila[i] + "\n")
    tablero_visible_guardado.close()
    return

def contar_ocurrencias(lista: list[Any], elemento: Any) -> int:
    """Recibe una lista y un elemento y recorre la lista contando cuantas veces aparece el elemento en ella. Devuelve la cantitad de ocurrencias del elemento.
    """
    contador: int = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

def sacar_elemento(lista: list[Any], elemento: Any) -> None:
    """Recibe una lista y un elemento y recorre la lista comparando cada posición con el elemento recibido. Si el valor de una posición es igual al elemento,
        elimina el valor de la lista.
    """
    i: int = 0
    while i < len(lista):
        if lista[i] == elemento:
            lista.pop(i)
        i += 1
    return

def comparar_cantidad(lista: list[list[any]], lista2: list[list[any]], elemento: Any) -> bool:
    """Recibe dos listas de listas y un elemento, y recorres ambas listas chequeando que cada sublista tenga la misma cantidad de ocurrencias del elemento recibido.
        De ser asi, cuenta la cantidad de veces que aparece el elemento en cada lista y lo guarda en cantidad_uno y cantidad_dos. En caso contrario, devuelve False.
        Si cantidad_uno y cantidad_dos son distintos, devuelve False. Sino, devuelve True
    """
    cantidad_uno: int = 0
    for i in range(len(lista)-1):
        if contar_ocurrencias(lista[i+1], elemento) != contar_ocurrencias(lista[i], elemento):
            return False
        else:
            cantidad_uno += 1
    cantidad_dos: int = 0
    for i in range(len(lista2)-1):
        if contar_ocurrencias(lista2[i+1], elemento) != contar_ocurrencias(lista2[i], elemento):
            return False
        else:
            cantidad_dos += 1
    if cantidad_uno != cantidad_dos:
        return False
    return True

def string_a_caracteres(lista: list[str]) -> list[list[str]]:
    """Recibe una lista de strings y la convierte en una lista de listas de strings, donde cada sublista esta 
       conformada por los caracteres del string que ocupaba esa posición.
    """
    nueva_lista: list[str] = []
    for i in range(len(lista)):
        #Convierte el string de lista[i] en una lista de listas de strings, y la agrega a nueva_lista.
        nueva_lista.append(list(lista[i])) 
        
    #Sobreescribe la lista original con su nueva versión.
    lista: list[list[str]] = nueva_lista 
    return lista

def contar_y_formatear_minas(tablero: list[list[str]]) -> tuple[list[list[str]], bool, int]:
    """ Recibe un tablero con los signos separados de los números y los condensa en un mismo elemento, chequeando tambien que haya minas y contandolas.
        Devuelve una tupla bool-int indicando la presencia de minas y su cantidad.
    """
    hay_mina: bool = False
    cantidad_minas: int = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])-1):
            #Chequea que el indice no sobrepase el rango, ya que cuando sacamos elementos podría intentarse acceder a indices fuera de rango.
            if j > len(tablero[i])-1: 
                break
            elif tablero[i][j] == "-" and tablero[i][j+1] == "1":
                #Agrega el signo '-' al elemento siguiente.
                tablero[i][j+1] = "-" + tablero[i][j+1]
                #Borra de la lista la entrada con el signo '-' solo.
                tablero[i].pop(j) 
                hay_mina: bool = True
                cantidad_minas += 1
    return tablero, hay_mina, cantidad_minas

def convertir_en_entero(tablero: list[list[str]]) -> list[list[str]]:
    """Recibe un tablero conformado por listas de strings y convierte cada string en un entero. 
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            tablero[i][j] = int(tablero[i][j])
    return tablero

def valor_adyacentes_valido(tablero: list[list[str]]) -> bool:
    """Recibe un tablero y recorre sus sublistas elemento por elemento comprobando que el numero de minas adyacentes para cada casilla sea valido.
    """
    for i in range(len(tablero)): 
        for j in range(len(tablero[i])):
            if tablero[i][j] != -1 and tablero[i][j] != contador_minas_adyacentes(tablero, (i,j)):
                return False
    return True

def validar_y_reformar_visible(tablero: list[list[int]], tablero_visible: list[list[str]]) -> bool:
    """Recibe un tablero y su contraparte visible y compara casilla por casilla para chequear que los valores de ambos tableros se correspondan entre si. 
       Reemplaza "*" por BANDERA y "?" por VACIO.
    """
    for i in range(len(tablero_visible)): 
        for j in range(len(tablero_visible[i])):
            celda: str = tablero_visible[i][j]
            if celda == "*":
                tablero_visible[i][j] = BANDERA
            elif celda == "?":
                tablero_visible[i][j] = VACIO
            elif celda in ['0','1','2','3','4','5','6','7','8']:
                if int(celda) != tablero[i][j]:
                    return False
            else:
                return False
    return True

def hay_vacio_adyacente(tablero: list[list[int]], tablero_visible: list[list[str]]) -> bool:
    """Devuelve True si hay al menos una celda VACI0 en tablero_visible que
       coincide con un número mayor a 0 en el tablero.
    """
    for i in range(len(tablero_visible)):
        for j in range(len(tablero_visible[i])):
            if tablero_visible[i][j] == VACIO and tablero[i][j] > 0:
                return True
    return False

def cargar_estado(estado: EstadoJuego, ruta_directorio: str) -> bool:
    """
    Verifica varias condiciones para el parametro estado y lo modifica.

    Args:
        estado: un EstadoJuego valido a ser evaluado y modificado
        ruta_directorio: una ruta valida para una carpeta con archivos .txt.

    Returns:
        True si el estado fue validado y cargado, false en caso contrario.
    """
    res: bool = False
    if existe_archivo(ruta_directorio, "tablero.txt") == True and existe_archivo(ruta_directorio, "tablero_visible.txt") == True:
        tablero_a_cargar = open(os.path.join(ruta_directorio, 'tablero.txt'), "r")
        tablero_visible_a_cargar = open(os.path.join(ruta_directorio, 'tablero_visible.txt'), "r")

        #Crea listas de strings con las lineas de ambos tableros.
        lineas_tablero: list[str] = tablero_a_cargar.readlines() 
        lineas_visible: list[str] = tablero_visible_a_cargar.readlines() 

        tablero_a_cargar.close()
        tablero_visible_a_cargar.close()

        #Verifica que ambos tableros tengan la misma cantidad de lineas.
        if len(lineas_tablero) == len(lineas_visible): 
            #convierte las lineas de ambos archivos en tableros (listas de listas de strings).
            tablero: list[list[str]] = string_a_caracteres(lineas_tablero)
            tablero_visible: list[list[str]] = string_a_caracteres(lineas_visible)

            #Verifica que cada linea y cada tablero tenga la misma cantidad de comas.
            if comparar_cantidad(tablero, tablero_visible, ",") == True: 
                #Saca los saltos de linea y las comas de ambos tableros.
                for i in range(len(tablero)):
                    sacar_elemento(tablero[i], "\n")
                    sacar_elemento(tablero[i], ",")
                for i in range(len(tablero_visible)):
                    sacar_elemento(tablero_visible[i], ",")
                    sacar_elemento(tablero_visible[i], "\n")

                #Inicia variables para chequear la presencia de minas y su cantidad.
                hay_mina: bool = False 
                cantidad_minas: int = 0 

                #Chequea si hay minas y condensa el signo "-" y "1" en uno solo donde sea necesario.
                chequeo_minas: tuple[list[list[str]],bool,int] = contar_y_formatear_minas(tablero) 

                #Asigna el valor correspondiente de la tupla a cada variable.
                tablero: list[list[str]] = chequeo_minas[0]
                hay_mina: bool = chequeo_minas[1]
                cantidad_minas: int = chequeo_minas[2] 

                #Convierte los strings de las sublistas del tablero en enteros.
                tablero: list[list[int]] = convertir_en_entero(tablero)

                #Chequea la presencia de minas, la correctitud de cada valor del tablero y su correspondencia con el tablero visible
                if hay_mina == True and valor_adyacentes_valido(tablero) == True and validar_y_reformar_visible(tablero, tablero_visible) == True:
                    #Chequea que al menos una de las posiciones con VACIO en tablero_visible coincida con un numero mayor a 0 en la misma posición de tablero
                    if hay_vacio_adyacente(tablero, tablero_visible) == True:
                    
                        res: bool = True
                    
    if res == True:
        #Modifica el estado recibido con la información de los tableros cargados.
        estado['minas'] = cantidad_minas
        estado['juego_terminado'] = False
        estado['tablero'] = tablero
        estado['tablero_visible'] = tablero_visible
        estado['filas'] = len(tablero)
        estado['columnas'] = len(tablero[0])
            
        return True

    return False