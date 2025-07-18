from queue import Queue as Cola

# Ejercicio 1
def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    cantidad: int = 0
    for i in range(len(s)):
        a: int = s[i]
        for j in range(i, len(s)):
            b: int = s[j]

            #miro que no tienen que ser el mismo elemento: 
            if a == b: 
                continue #queremos q no lo cuente

            #Verifico si cumple con la condición: 
            if a + b == n: 
                cantidad += 1

    return cantidad


# Ejercicio 2 
def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    persona: str = ""
    nueva_fila: list[tuple[str, str, int]] = []
    acceso_disponible: bool = True
    while not clientes.empty(): 
        cliente = clientes.get()

        #defino las variables:
        nombre: str = cliente[0]
        pago: str = cliente[1]
        cantidad: int = cliente[2]

        #verifico la condición: 
        if pago != "efectivo" and cantidad < 16: 
            if acceso_disponible: 
                persona = nombre
                acceso_disponible = False #cambio el acceso a False, pq ya se usa la caja
            else: # agrega pq ya hay una persona en la caja automatica => los tiene que mandar de nuevo a la fila
                nueva_fila.append((nombre, pago, cantidad)) 
        else: #agrega si no cumple la condición de afuera 
            nueva_fila.append((nombre, pago, cantidad)) 

    #guardo de nuevo en la cola: 
    for i in nueva_fila: 
        clientes.put(i)
    #retorno el valor de la persona que fue atendida por caja automatica: 
    return persona


# Ejercicio 3 
def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    lon: int = len(A)
    nueva_matriz: list[list[int]] = []
    for fila in range(lon): 
        nueva_fila: list[int] = []
        for columna in range(len(A[0])): 
            if columna == col1: #significa que estamos viendo esa columna
                #queremos que c sea igual a la posicion de la fila X, dependiendo de la operacion y que sea en la columna en la que se le esta pasando
                c: int = A[lon - 1 - fila][col2]
                nueva_fila.append(c) #guardo la nueva columna en la fila
            elif columna == col2: #significa que estamos viendo la columna en esa posicion
                c : int = A[lon - 1 - fila][col1] 
                nueva_fila.append(c)
            else: #significa que no son iguales, por lo tanto tienen que quedar como estaban antes: 
                nueva_fila.append(A[fila][columna])
        # una vez que termino de guardar la fila, la tengo que guardar en la nueva matriz
        nueva_matriz.append(nueva_fila)

    # una vez que terminamos de guradr todas las filas en la nueva matriz, hay que hacer el cambio en la matriz original: 
    # ademas sabiendo que las matrices tienen las mismas longitudes
    for f in range(lon): 
        #quiero que cada fila sea igual a la de la nueva matriz
        A[f] = nueva_matriz[f]



# Ejercicio 4
censo_3 = {'Juan': 'belgrano', 'Ana': 'lujan', "marcos": "lomas", "tomas": "lomas"}
censo_4 = {'Juan': 'belgrano', 'Ana': 'lujan', "marcos": "lomas", "tomas": "lomas"}

def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    res = {}
    parcial = []
    for i in censo1: 
        localidad = censo1[i]
        cantidad = 0
        for j in censo2: 
            if i == j:#si las personas son las mismas: quiero ver si siguen viviendo en el mismo lugar: 
                if censo1[i] == censo2[j]:
                    cantidad += 1 #significa que todavia sigue viviendo ahi 

        #tengo que guardar lso datos de la cantidad de personas viviendo en el municipio: si y solo si cantidad > 0
        if cantidad > 0: 
            parcial.append((localidad, cantidad))

    #guardo las cantidades correctas: 
    cargados = []
    for i in range(len(parcial)): 
        nombre: str = parcial[i][0]
        total: int = parcial[i][1]

        for j in range(i, len(parcial)): 
            name = parcial[j][0]
            suma = parcial[j][1]

            if name == nombre and name in cargados:
                total += suma

        #cargo el nombre: 
        cargados.append(nombre)

        #guardo lso datos: 
        res[nombre] = total

    return res          

print(mantuvieron_residencia(censo_3, censo_4))