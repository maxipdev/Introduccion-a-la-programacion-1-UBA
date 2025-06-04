from queue import Queue as Cola 

# Ejercicio 1
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


# print(nivel_de_ocupacion(camas_por_piso))
# print (2 / 3)

# Ejercicio 2
def cambiar_una_matriz(a): 
    maximo  = len(a[0]) * len(a)
    for i in range(len(a)): 
        for j in range(len(a[0])): 
            if a[i][j] != maximo: 
                a[i][j] += 1
            else :
                a[i][j] = 1

matriz = [[1,2,3], [4,5,6], [7,3,1]]
cambiar_una_matriz(matriz)

print("resultado", matriz)

# Ejercicio 3
def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]: 
    res = {}
    for clave in registro: 
        cantidad_salas_que_salio: int = 0
        suma_tiempo: int = 0

        for j in registro[clave]: 
            if 0 < j and j < 61: 
                cantidad_salas_que_salio += 1
                suma_tiempo += j 

        if cantidad_salas_que_salio == 0: 
            res[clave] = (cantidad_salas_que_salio, float(0))
        else: 
            res[clave] = (cantidad_salas_que_salio, float(suma_tiempo / cantidad_salas_que_salio))
    
    return res

registro = {"maxi": [3, 5, 40], "luca": [46, 55, 28], "juan": [37, 49, 60], "kevin": [0, 61, 61]}

h = promedio_de_salidas(registro)
print(h)

# Ejercicio 4
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

print(reordenar_cola_priorizando_vips(fila).queue)