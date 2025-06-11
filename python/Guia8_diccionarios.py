from queue import LifoQueue as Pila

# Ejercicio 16
def calcular_promedio_por_cada_estudiante(notas: list[str, float]) -> dict[str, float]: 
    res = {}
    for i in range(len(notas)):
        suma_notas = 0
        cantidad_de_notas = 0
        estudiante = notas[i][0]
        
        for nombre, nota in notas: 
            if nombre == estudiante: 
                suma_notas += nota
                cantidad_de_notas += 1
        
        ## una vez que recorrio a todos los alumnos calculo el proemdio del estuadiante:
        promedio = suma_notas / cantidad_de_notas
        res[estudiante] = promedio

    return res

notas = [
    ("Ana", 9.0),
    ("Luis", 8.0),
    ("Ana", 7.0),
    ("Luis", 6.0),
    ("Carlos", 10.0)
]

## calcular_promedio_por_cada_estudiante(notas)

# Ejercicio 17
historiales = {
    "maximo": Pila(),
    "milagros": Pila(),
    "fernando": Pila()
}

## esta usuando inpout en los diccionarios
def visitar_sitio_web(historiales: dict[str, Pila[str]], usuario: str, sitio: str) : 
    if usuario in historiales: 
        historiales[usuario].put(sitio) #lo que se hace aca es agregar el sitio mediante el put, ya que es una pila, y sabiendo que con historiales[usuario] se obtiene el valor
    else: 
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)


# visitar_sitio_web(historiales, "pedro", "anase")
# visitar_sitio_web(historiales, "maximo", "gagagagagaga")
# visitar_sitio_web(historiales, "txuza", "epiii")
# visitar_sitio_web(historiales, "melga", "hhhhh")
# visitar_sitio_web(historiales, "maximo", "pepepepepepeppe")
# visitar_sitio_web(historiales, "milagros", "totototo")
# visitar_sitio_web(historiales, "melga", "fdsfdsfs")
# visitar_sitio_web(historiales, "fernando", "kkkk")

# for i in historiales: 
#     print(historiales[i].queue)

# ejercicio 17.3
def navegar_hacia_atras(historiales: dict[str, Pila], usuario: str):
    # como ya se sabe por requiesitos que el usuario esta en historiales y no esta vacaia 
    # obtengo el historial entero del usuario y le quito el ultimo de la pila
    historiales[usuario].get() ##le quita el ultimo elemento

# navegar_hacia_atras(historiales, "maximo")

# print("cambios....")
# for i in historiales: 
#     print(historiales[i].queue)


# Ejercicio 18.1
def agregar_producto(inventario: dict, nombre: str, precio: float, cantidad: int):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}

# Ejericicio 18.2
def actualizar_stock(inventario, nombre, cantidad): 
    inventario[nombre]["cantidad"] = cantidad

# Ejercicio 18.3
def actualizar_precio(inventario: dict, nombre: str, precio: float): 
    inventario[nombre]["precio"] = precio

# ejercicio 18.4
def calcular_valor_inventario(inventario): 
    suma_total = 0

    for producto in inventario.values(): 
        cantidad = producto["cantidad"]
        precio = producto["precio"]
        suma_total += cantidad * precio

    return suma_total

inventario: dict[str, dict[str, float | int]] = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # D