import random

def pertenece(lista: list[int], e: int) -> bool:
    tamaño: int = len(lista)
    for i in range(tamaño):
        if e == lista[i]: return True
    return False

def pertenece2(lista: list[int], e: int) -> bool:
    for i in lista:
        if e == i: return True
    return False


def pertenece3(lista: list[int], e: int) -> bool:
    i: int = 0
    while i < len(lista):
        if e == lista[i]: return True
        i += 1
    return False

# Ejercicio 1.2
def divide_a_todos(lista: list[int], e: int) -> bool:
    for i in lista:
        if i % e != 0: return False # pq no divide a todos
    return True # caso final 


# Ejercicio 1.3
def suma_total(lista: list[int]) -> int:
    total: int = 0
    for i in lista:
        total += i
    return total 

# Ejercicio 1.4
def maximo(lista: list[int]) -> int:
    mas_grande = lista[0] # lo defino por defecto
    for i in lista:
        if i > mas_grande: 
            mas_grande = i
    return mas_grande

#Ejercicio 1.5
def minimo(lista: list[int]) -> int:
    mas_chico = lista[0] # lo defino por defecto
    for i in lista:
        if i < mas_chico: 
            mas_chico = i
    return mas_chico 

# ejercicio 1.6
def ordenados(lista: list[int]) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejercicio 1.7
def pos_maximo(lista: list[int]): 
    if len(lista) == 0: return -1

    maximo = lista[0]
    posicion = 0
    for i in range(len(lista)):
        if abs(lista[i]) > maximo: 
            maximo = abs(lista[i])
            posicion = i 
    return posicion

# Ejercicio 1.8
def pos_minimo(lista: list[int]): 
    if len(lista) == 0: return -1

    minimo = lista[0]
    posicion = 0
    for i in range(len(lista)):
        if abs(lista[i]) < minimo: 
            minimo = abs(lista[i])
            posicion = i 
    return posicion
 
# Ejercicio 1.9
def longitud_mayor_a_7(lista: list[str]) -> bool:
    for p in lista: 
        if len(p) > 7: 
            return True
    return False

# Ejercicio 1.10
def es_palindromo(palabra: str) -> bool:
    nueva_palabra = ""
    for i in range(len(palabra) -1, -1, -1):
        letra = palabra[i]
        nueva_palabra += letra

    return nueva_palabra == palabra
        
def es_palindromo2(palabra: str) -> str:
    nueva_palabra = palabra[::-1] 
    return nueva_palabra == palabra

# Ejercicio 1.11
def iguales_consecutivos(lista):
    contador = 1 # pq ya hay como miunimo un elemento
    for i in range(1, len(lista)): # lo hago asi para poder fijarme en el anterior 
        if lista[i] == lista[i - 1]:
            contador +=1 # marco q aparece una nueva coincidencia
            if contador == 3: 
                return True ## marca que es true pq ya llego a las 3 coincidencias
        else: 
            contador = 1 # si no hay coincidencias reiniciamos el contador
    return False # si en ningun momento hubo algo similar, da False pq no hubo coincidencias

# Ejercicio 1.12
def vocales_distintas(palabra): 
    palabra = palabra.lower()
    vocales = ["a", "e", "i", "o", "u"]
    vocales_usadas = []
    for i in palabra:
        if i in vocales: # miro que sea una vocal
            if not (i in vocales_usadas): #Miramos que la vocal no este adentro de las usadas
                vocales_usadas.append(i) #Si no esta en las vocales usadas la agregamos 
    if len(vocales_usadas) >= 3:
        return True 
    else : 
        return False

# Ejercicio 1.13
def pos_secuencias_mas_larga(lista):
    mejores_secuencias = []
    contador = 1
    posicion = 0
    for i in range(1 ,len(lista)):
        if lista[i - 1] < lista[i]:
            contador +=1
        else: 
            if contador > 1:
                mejores_secuencias.append((posicion, contador)) # guardo los datos para poder reinciar y despues comparar
            contador = 0
            posicion = i

    # Guardo la ultima secuencia si termino bien
    if contador > 1:
        mejores_secuencias.append((posicion, contador))

    # Compro cada elemento
    nueva_posicion = 0
    mas_elementos = 0
    for k in mejores_secuencias:
        if mas_elementos < k[1]:
            nueva_posicion = k[0]
            mas_elementos = k[1]
    return nueva_posicion
    
# Ejercicio 1.14
def cantidad_de_digitos_impares(lista): 
    contador = 0
    for i in lista:
        for k in obtener_digitos_de_un_num(i): 
            if k % 2 != 0: 
                contador += 1
    return contador 

def obtener_digitos_de_un_num(num):
    res = []
    while num > 0: 
        resto = num % 10 
        res.append(resto) #Guardo el resto pq es lo que necesito
        num = num // 10 # Elimino el resto

    return res

# Ejercicio 2.1
def ceros_en_posiciones_pares(s: list[int]):
    for i in range(len(s)):
        if (i+1) % 2 == 0: 
            s[i] = 0

lista = [1,2,3,4,5,5]
ceros_en_posiciones_pares(lista)

# Ejercicio 2.2
def ceros_en_posiciones_pares2(lista: list[int]) -> list[int]:
    s = lista.copy()
    for i in range(len(s)):
        if (i+1) % 2 == 0: 
            s[i] = 0  
    return s

# Ejercicio 2.3
def sin_vocales(palabra: str) -> str: 
    vocales = "aeiou"
    palabra = palabra.lower()
    nueva_palabra = ""
    for i in palabra:
        if not i in vocales: 
            nueva_palabra += i
    return nueva_palabra

# Ejercicio 2.4
def remplazar_vocales(palabra: str) -> str: 
    palabra= palabra.lower()
    vocales = "aeiou"
    nueva_palabra = ""
    for i in palabra:
        if i in vocales:
            nueva_palabra += "-"
        else: 
            nueva_palabra += i 
    return nueva_palabra

# Ejercicio 2.5
def da_vuelta_str(palabra): 
    nueva = ""
    for i in range(len(palabra)-1, -1, -1):
        nueva += palabra[i]
    return nueva

# Ejercicio 2.6
def eliminar_repetidos(palabra):
    nueva = ""
    for i in palabra: 
        if not i in nueva: 
            nueva += i
    return nueva

# Ejercicio 3
def resultado_materia(lista: list[int]) -> int:
    cantidad = len(lista)
    suma = sum(lista)
    promedio = suma / cantidad

    estado_de_promocion = True
    for nota in lista:
        if nota < 4: 
            estado_de_promocion = False
            break
    ## Empeizan las condiciones:
    if estado_de_promocion and promedio >= 7:
        return 1
    elif estado_de_promocion and 4 <= promedio < 7: 
        return 2
    elif estado_de_promocion == False or promedio < 4:
        return 3
    
# Ejercicio 4
def saldo_actual(movimientos: list[str, int]) -> int:
    total = 0
    for i in movimientos:
        if i[0] == "R": 
            total -= i[1]
        elif i[0] == "I":
            total += i[1]
    return total

# Ejercicio 5.1
def pertenece_a_cada_uno_version1(lista: list[list[int]], e: int, res: list[bool]) -> None:
    for s in lista: 
        if pertenece2(s, e): 
            res.append(True)
        else:
            res.append(False)

matriz = [
    [1, 2, 3],
    [3, 5, 6],
    [7, 3, 9]
]
res = []
pertenece_a_cada_uno_version1(matriz, 3, res)

# Ejercicio 5.2 --> Hace lo mismo q el anterior, solko cambia el asegura q es más fuerte

# Ejercicio 5.3
def pertenece_a_cada_uno_version3(lista: list[list[int]], e: int) -> list[bool]:
    valor = []
    for s in lista: 
        if pertenece2(s, e): 
            valor.append(True)
        else:
            valor.append(False) 
    return valor

# Ejercicio 5.4
# Pensar: 
# 1) ¿Cómo cambia este problema respecto de la version 1? Pensar en relaci´on de fuerza entre: implementacion en Python y las especificaciones. 
# 2) ¿Se puede usar la implementacion del ejercicio 2 para la especificaci´on del 1? 
# 3) ¿Se puede usar la implementaci´on del ejercicio 1 para la especificaci´on del 2? Justificar su respuesta.

# Respuestas: 
# 1) cambia en la manera en la q hay q pasarle los datos en uno y como los devuelve, sabiendo que para el ej 1 la condicion del asegura es más debil
# 2) si se puede ya que en el ejercicio 2 dice que len(s) = len(res) y lo que pide la condicion q len(s) >= len(res)
# 3) no pq la implementacion del 2 habla de q len(s) == len(res), pero la especificacion del 1 dice que len(s) >= len(res), por lo tatno no quedan en cuenta los casos en los que s puede ser > q res 

# Ejercicio 6.1
def es_matriz(matriz: list[list[int]]) -> bool:
    if len(matriz) == 0 : return False ## Pq no existen matrices vacias
    if len(matriz[0]) == 0: return False ##Pq no existen matrices vacias 
    cantidad_de_columnas_que_tiene_que_tener = len(matriz[0])

    for m in matriz: 
        if not len(m) == cantidad_de_columnas_que_tiene_que_tener:
            return False
    return True

matriz2 = [
    [1, 2, 3],
    [3, 5, 6],
    [7, 3, 9]
]
# Ejercicio 6.2
matriz3 = [
    [10, 2, 3, 7],
    [30, 5, 6],
    [70, 8, 9]
]

def filas_ordenadas(matriz) :
    res = []
    for i in matriz:
        if ordenados(i):
            res.append(True)
        else: 
            res.append(False)
    return res

# Ejercicio 6.3
def columnas(matriz: list[list[int]], c: int) -> list[int]:
    valores = []
    for i in matriz:
        valores.append(i[c])
    return valores

# Ejercicio 6.4
def columnas_ordenadas(matriz): 
    valores = []
    for c in range(len(matriz[0])):
        columna = columnas(matriz, c)
        valores.append(ordenados(columna))
    return valores

matriz4 = [
    [10, 2],
    [30, 5],
    [70, 8]
]

# Ejercicio 6.5
def trasponer(matriz): 
    nuevas_filas = []
    for c in range(len(matriz[0])):
        nuevas_filas.append(columnas(matriz, c))
    return nuevas_filas

a = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 4, 1]
]

at = [
    [1, 4],
    [2, 5],
    [3, 6]
]

# Ejercicio 6.6
tablero = [
    ["O", "X", " "],
    [" ", "O", " "],
    ["X", "O", " "]
]

def quien_gana_ta_te_ti(matriz): 
    opciones = ["X", "O"]
    gano = ""
    for i in opciones:
        if verificando_opciones(matriz, i) == True:
            gano = i
            break #Rompe el cliclo pq ya no es necesario mirar el otro
    if gano == "X":
        return 1
    elif gano == "O":
        return 0
    else: 
        return 2 #Este es el de empate

def verificando_opciones(matriz, valor):
    longitud = len(matriz)
    #miro si las filas hay algun ganador, es decir horizontalemete:
    for i in matriz:
        if i[0] == valor and i[1] == valor and i[2] == valor:
            return True # PQ ya hay un ganador
    #Como no se econtro un gandor horizontalemnte lo busco verticalmente
    for c in range(longitud):
        filas_de_columnas = columnas(matriz, c)
        if filas_de_columnas[0] == valor and filas_de_columnas[1] == valor and filas_de_columnas[2] == valor:
            return True #Hay un ganador por columnas
    #Si no hay gandor por columnas, ni filas, me fijo si hay en diagolaes
    opcion1 = matriz[0][0] == valor and matriz[1][1] == valor and matriz[2][2] == valor
    opcion2 = matriz[0][2] == valor and matriz[1][1] == valor and matriz[2][0] == valor

    if opcion1 or opcion2: 
        return True
    #Si nadie gano se devuelve False
    return False

# Ejercicio 7.1
def solicitar_estudiantes():
    lista_de_estudiantes = []
    res = input("ingrese el nombre de un estudiante: ")
    res = res.lower()
    while not (res == "" or res == "listo"):
        lista_de_estudiantes.append(res)
        res = input("ingrese el nombre de un estudiante: ")
        res = res.lower()

    return lista_de_estudiantes

#Ejercicio 7.2
def historial_sube():
    historial = []
    print("C => MONTO A CARGAR, D=> MONTO A RESTAR")
    res = input("ingrese su operacion: ")
    res = res.upper()

    while not res == "X":
        if res == "C":
            monto = int(input("monto a cargar: "))
            historial.append(("C", monto))
            res = input("ingrese su operacion: ")
            res = res.upper()
        elif res == "D":
            monto = int(input("monto a descontar: "))
            historial.append(("D", monto))
            res = input("ingrese su operacion: ")
            res = res.upper()
    
    return historial

# Ejercicio 7.3
def obtener_numero_random():
    numero = random.randint(1,12)

    while (numero == 8 or numero == 9):
        numero = random.randint(1,12)
    
    return numero

def juego():
    jugadas = []
    suma = 0
    print("jugando..")
    estado = True

    while estado == True:
        numero = obtener_numero_random()
        print(f"Su carta es: {numero}")
        jugadas.append(numero)
        ## Se verifica el tipo de suma
        if numero == 10 or numero == 11 or numero == 12:
            suma += 0.5
        else: 
            suma += 1

        print(f"Puntaje actual: {suma}")
        ## Se verifica como va el usuario
        if suma > 7.5:
            print("usted pierde")
            estado = False
        else: 
            user = input("desea seguir jugando: (SI/NO)")
            user = user.lower()

            if user == "no":    
                print(f"🟩 Usted se plantó con {suma} puntos.")
                estado = False
    
    return jugadas

# Ejercicio 7.4
def seguridad_de_contraseña(contraseña: str):
    mayusculas: bool = False
    minusculas: bool = False
    numeros: bool = False

    for i in contraseña:
        if "A" <= i <= "Z":
            mayusculas = True
        elif "a" <= i <= "z":
            minusculas = True
        elif "0" <= i <= "9" : ##Solo pq es un string la plabra que se le pasa
            numeros = True

    ## Analizo las condiciones
    if mayusculas and minusculas and numeros and len(contraseña) > 8: 
        return "Verde"
    elif len(contraseña) < 5:
        return "Rojo"
    else : 
        return "Amarilla"
    




