
# Ejericicio 19
def contar_lineas(nombre_archivo) : 
    archivo = open(f"archivos-python/{nombre_archivo}", "r")

    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

#print(contar_lineas("texto-1.txt"))


# Ejercicio 19.2
def existe_palabra(nombre_archivo, palabra) : 
    archivo = open(f"archivos-python/{nombre_archivo}", "r")

    info = archivo.read()
    archivo.close()

    return palabra in info

# print(existe_palabra("texto-1.txt", "naaa"))

# Ejercicicio 19.3
def cantidad_de_apariciones(nombre_archivo, palabra): 
    archivo = open(f"archivos-python/{nombre_archivo}", "r")

    lineas = archivo.readlines()
    archivo.close()

    print(lineas)

    lista_de_palbras_nuevas = []

    for i in lineas:
        i = i.strip()
        nueva_palabra = "" 
        for k in range(len(i)): 
            if i[k] != " ": 
                nueva_palabra += i[k]
            else : 
                lista_de_palbras_nuevas.append(nueva_palabra)
                nueva_palabra = ""

        ## Agrego la ultima palabra en caso de que no se haya añadido : 
        if nueva_palabra != "" : 
            lista_de_palbras_nuevas.append(nueva_palabra) ## PQ si no hay un espaco hay vexes que no añade la ultima palabra

    print(lista_de_palbras_nuevas)

    #miro cuantas veces aparece la palabra 
    cantidad = 0
    for i in lista_de_palbras_nuevas: 
        if i == palabra: 
            cantidad += 1
    
    return cantidad

#print(cantidad_de_apariciones("texto-1.txt", "yo"))

# Ejercicio 20
def separar_por_palabras(lista) -> list: 
    lista_de_palbras_nuevas = []

    for i in lista:
        i = i.strip()
        nueva_palabra = "" 
        for k in range(len(i)): 
            if i[k] != " ": 
                nueva_palabra += i[k]
            else : 
                lista_de_palbras_nuevas.append(nueva_palabra)
                nueva_palabra = ""

        ## Agrego la ultima palabra en caso de que no se haya añadido : 
        if nueva_palabra != "" : 
            lista_de_palbras_nuevas.append(nueva_palabra) ## PQ si no hay un espaco hay vexes que no añade la ultima palabra

    return lista_de_palbras_nuevas

def agrupar_por_longitud(nombre_archivo): 
    archivo = open(f"archivos-python/{nombre_archivo}", "r")

    lineas = archivo.readlines()
    archivo.close()

    lista_de_palbras: list[str] = separar_por_palabras(lineas)

    print(lista_de_palbras)
    diccionario: dict = {}

    for i in lista_de_palbras:
        longitud = len(i)
        if longitud in diccionario: 
            diccionario[longitud] += 1
        else: 
            diccionario[longitud] = 1

    return diccionario

# print(agrupar_por_longitud("texto-1.txt"))

# Ejercicio 21
def palabra_mas_frecuente(nombre_archivo): 
    archivo = open(f"archivos-python/{nombre_archivo}", "r")   
    lineas = archivo.readlines()
    archivo.close()

    palabras_lista = separar_por_palabras(lineas)
    res = {}

    for i in palabras_lista: 
        if i in res: 
            res[i] += 1 #Le sumo uno a su valor
        else: 
            res[i] = 1 # le agrego su primera participacion
    
    #miro cual es la mas grande
    mayor = {"palabra": 0, "cantidad": 0} # siempre va camabiar pq como minimo aparace una vez en el texto
    for palabra, cantidad in res.items(): 
        if cantidad > mayor["cantidad"]:
            mayor["cantidad"] = cantidad
            mayor["palabra"] = palabra
    return mayor["palabra"]

#print(palabra_mas_frecuente("texto-1.txt")) 

# Ejercicio 22
def clonar_sin_comentarios(nombre_archivo_1, nombre_archivo_2):
    archivo1 = open(f"archivos-python/{nombre_archivo_1}", "r")  
    archivo2 = open(f"archivos-python/{nombre_archivo_2}", "w") # Aca como no existe lo crea, y si existe le borra el contenido

    #Leo el primer archivo:
    lineas = archivo1.readlines()
    archivo1.close()
    
    for i in lineas: 
        if i[0] != "#":
            archivo2.writelines(i) # no le agergo el "espacio/enter" pq ya viene includio al hacer readlines()
    archivo2.close() #Se terminan de guardar los cambios que solicite 

#clonar_sin_comentarios("texto-1.txt", "texto-2.txt")

# Ejercicio 23
def invertir_lineas(nombre_archivo_1, nombre_archivo_2):
    archivo1 = open(f"archivos-python/{nombre_archivo_1}", "r")  
    archivo2 = open(f"archivos-python/{nombre_archivo_2}", "w")

    lineas = archivo1.readlines()
    print(len(lineas))
    archivo1.close()
    for i in range(len(lineas) -1, -1, -1): 
        archivo2.write(lineas[i].strip())
        archivo2.write("\n")
    archivo2.close()

invertir_lineas("texto-3.txt", "texto-4.txt")
