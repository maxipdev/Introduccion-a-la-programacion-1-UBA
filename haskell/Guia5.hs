module Guia5 where 

-- Ejercicio 1
longitud:: [t] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

ultimo:: [t] -> t
ultimo lista = index lista ((longitud lista)-1)
    where 
        index (x:_) 0 = x -- > Es el valor de n más chico que se puede encontrar
        index (x:xs) n = index xs (n-1)

principio:: [t] -> [t]
principio lista = aux lista []
    where 
        aux lista nuevaLista
            | (longitud lista) == 1 = nuevaLista -- > Da la lista menos el ultimo elemento
            | otherwise = aux (tail lista) (nuevaLista ++ [head lista])

reverso:: [t] -> [t]
reverso s = aux s []
    where 
        aux s nuevaLista 
            | longitud s == 0 = nuevaLista -- > Da la lista pero al reves
            | otherwise = aux (tail s) ((head s):nuevaLista)

-- Ejericio 2
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e lista 
    | e == (head lista) = True
    | otherwise = pertenece e (tail lista) 


todosIguales:: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales lista = aux lista (head lista) 
    where 
        aux lista valor
            | (head lista == valor) && (longitud lista == 1) = True
            | (head lista == valor) && (longitud lista > 1) = aux (tail lista) valor
            | otherwise = False

todosDistintos:: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos lista = sumatoria (tail lista) (head lista)
    where 
        sumatoria lista elemento 
            | lista == [] = True
            | (verificador lista elemento) == True = sumatoria (tail lista) (head lista)
            | otherwise = False -- > Hay algun caso en q hay 2 elementos repetidos

        verificador lista elemento  
            | lista == [] = True -- > Por ahora todo bien
            | elemento /= head lista = verificador (tail lista) elemento
            | otherwise = False -- > Ya esta es falso pq hay 2 elementos repetidos 

hayRepetidos:: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos lista = sumatoria (tail lista) (head lista)
    where 
        sumatoria lista elemento 
            | lista == [] = False
            | (verificador lista elemento) == False = sumatoria (tail lista) (head lista)
            | otherwise = True -- > Hay algun caso en q hay 2 elementos repetidos

        verificador lista elemento  
            | lista == [] = False -- > Por ahora todo bien
            | elemento /= head lista = verificador (tail lista) elemento
            | otherwise = True -- > Ya esta es falso pq hay 2 elementos repetidos 

quitar:: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) 
    | n == x = xs 
    | otherwise = x:(quitar n xs)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) 
    | n == x = quitarTodos n xs
    | otherwise = x:(quitarTodos n xs)


eliminarRepetidos:: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x: eliminarRepetidos (quitarTodos x xs)

mismosElementos:: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista1 lista2 = sumatoria (eliminarRepetidos lista1) (eliminarRepetidos lista2)  
    where
        sumatoria [] _ = True -- > PQ recorrio todo y no se trabo, por lo tanto es true
        sumatoria (x:xs) lista2 
            | verificador x lista2 == True = sumatoria xs lista2
            | otherwise = False -- > Pq nos dio false antes, asi que es falsa

        verificador _ [] = False -- > False pq ya no hay ninguna coincidencia para ese numero --> Por lo tanto es falso ya que no hay ningun n E lista1 que sea igual a un k E Lista2
        verificador elemento_x (y:ys) 
            | elemento_x == y =  True -- > Si hay igualdad, ya esta, pq no hay repetidos
            | otherwise = verificador elemento_x ys -- > Prueba con otro elemento la igualdad

esCapicua :: (Eq t) => [t] -> Bool
esCapicua lista1 
    | lista1 == (reversa lista1) = True 
    | otherwise = False
    where 
        reversa [] = []
        reversa (x:xs) = (reversa xs) ++ [x]  -- > hace como un reverse 

-- Ejercicio 3
sumatoria:: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

productoria:: [Int] -> Int 
productoria [] = 1 -- > Pq al multplicar por 1 da el mismo numero
productoria (x:xs) = x * productoria xs

maximo:: [Int] -> Int -- > Tengo que buscar el mayor elemento de la lista
maximo (x:xs) = aux xs x 
    where 
        aux [] mayor = mayor
        aux (n:ns) mayor
            | n > mayor = aux ns n 
            | otherwise = aux ns mayor

-- Otra manera
maximo_2:: [Int] -> Int
maximo_2 [x] = x
maximo_2 (x:y:xs)
    | x > y = maximo_2 (x: xs)
    | otherwise = maximo_2 (y: xs)

sumarN :: Int -> [Int] -> [Int]
sumarN _ [] = []
sumarN n (x:xs) = (n + x) : sumarN n xs 

sumarElPrimero:: [Int] ->[Int]
sumarElPrimero (x:xs) = (x + x):sumarN x xs 

sumarElUltimo:: [Int] ->[Int]
sumarElUltimo lista = sumarN (obtenerUltimo lista) lista
    where
        obtenerUltimo (x:xs)
            | xs == [] = x
            | otherwise = obtenerUltimo xs
pares:: [Int] -> [Int] 
pares [] = []
pares (x:xs) 
    | esPar x = x: (pares xs)
    | otherwise = pares xs 
    where 
        esPar x
            | mod x 2 == 0 = True
            | otherwise = False

multiplosDeN:: Int -> [Int] -> [Int]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) = (n*x) : (multiplosDeN n xs)


-- >>>>>  FALTA TERMINAR ->>>>>>>>>>>>>>
-- ordenar:: [Int] -> [Int]
-- ordenar lista = ordenar_aux lista

-- ordenar_aux:: [Int] -> [Int]
-- ordenar_aux [x] = [x]
-- ordenar_aux lista = (masGrande) : (quitar masGrande lista) -- > agarro el mas grande y despues lo quirto de la prxima lista en la recur
--     where 
--         masGrande = maximo lista


ordenar:: [Int] -> [Int]
ordenar [x] = [x]
ordenar lista = ordenar (quitar (maximo lista) lista) ++ [maximo lista]

-- Ejercicio 4
-- A)
sacarBlancosRepetidos:: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos lista = sacarBlancosRepetidos_aux lista False -- > Lo inicio con false

sacarBlancosRepetidos_aux :: [Char] -> Bool -> [Char]
sacarBlancosRepetidos_aux [] _ = []
sacarBlancosRepetidos_aux (x:xs) valor
    | (x == ' ') && (valor == True) = sacarBlancosRepetidos_aux xs True -- > Pq detecto un espacio en blanco
    | (x == ' ') && (valor == False) = x: (sacarBlancosRepetidos_aux (xs) True) -- > Pq detecto un espacio en blanco, pero esta vez es nuevo
    | otherwise = x: (sacarBlancosRepetidos_aux xs False) -- > Pq el siguente es una letra y no un espacio vacio

-- B)
contarPalabras:: [Char] -> Int
contarPalabras [] = 0
contarPalabras lista
    | (head sinBlancosExtras == ' ') && ((verificadorDelUltimoElemento sinBlancosExtras) == True)= contarPalabras_aux (tail sinBlancosExtras) -1 -- > Pq nos esta dando un +1 palabra por el error en el espacio
    | (head sinBlancosExtras == ' ') && ((verificadorDelUltimoElemento sinBlancosExtras) == False)= contarPalabras_aux (tail sinBlancosExtras) 
    | verificadorDelUltimoElemento sinBlancosExtras == True = contarPalabras_aux (tail sinBlancosExtras) -1 -- > Pq suma uno demas
    | otherwise = contarPalabras_aux sinBlancosExtras  -- > No hay espacio al principio ni al final
    where 
        sinBlancosExtras = sacarBlancosRepetidos lista 

verificadorDelUltimoElemento:: [Char] -> Bool
verificadorDelUltimoElemento (x:xs) 
    | x == ' ' && xs == [] = True -- > Hay espacio en el ultimo elemento
    | x /= ' ' && xs == [] = False -- > Pq no hay espacio en el ultimo elemento 
    | otherwise = verificadorDelUltimoElemento xs 
 
contarPalabras_aux :: [Char] -> Int -- > Suponemos que el primer caracter y el ultimo son diferentes de ' '
contarPalabras_aux [] = 1 -- > Pq siempre empieza con una palbara como minimo
contarPalabras_aux (x:xs) 
    | x == ' ' = 1 + contarPalabras_aux xs
    | otherwise = contarPalabras_aux xs

-- C)
palabras :: [Char] -> [[Char]]
palabras [] = [] -- > Si no hay plabras no se hace nada
palabras (' ': xs) = palabras xs -- > Ignora el primer espacio
palabras lista = (nuevaPalabra lista) : (palabras (saltarPalabra lista)) -- > Concatena todo

nuevaPalabra :: [Char] -> [Char]
nuevaPalabra [] = [] -- > Caso en el que se llegue al final de la lista
nuevaPalabra (' ': _) = [] -- > Caso en el que se detecte un espacio, la funcion se frena
nuevaPalabra (x:xs) = x: nuevaPalabra xs 

saltarPalabra :: [Char] -> [Char]
saltarPalabra [] = [] -- > Caso base en el que al finla no se termine de recorrer todo
saltarPalabra (' ':xs) = xs -- > Se detiene en el primer espacio
saltarPalabra (_:xs) = saltarPalabra xs -- > Da la siguinete plabra, o sea espera a que llegue un espacio para mandarla 

-- D)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga lista = palabraMasLarga_aux (palabras lista) 0 ""

palabraMasLarga_aux :: [[Char]] -> Int -> [Char] -> [Char]
palabraMasLarga_aux [] _ palabra = palabra
palabraMasLarga_aux (x:xs) maxValor palabra
    | contadorDePalbras x > maxValor = palabraMasLarga_aux xs (contadorDePalbras x) x -- > Establezco el más grande
    | otherwise = palabraMasLarga_aux xs maxValor palabra -- > Continua con los datos

contadorDePalbras :: [Char] -> Int
contadorDePalbras [] = 0
contadorDePalbras (x:xs) = 1 + contadorDePalbras xs

-- E)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

-- F)
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ [' '] ++ aplanar xs

-- G)
aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos [] _ = [] -- > Si es una lista vacia
aplanarConNBlancos [x] _ = x -- > Si es el ultimo elemento no hago nada, es decir no sumo espacios
aplanarConNBlancos (x:xs) n = x ++ (crearBlancos n) ++ aplanarConNBlancos xs n

crearBlancos :: Int -> [Char]
crearBlancos 0 = []
crearBlancos n = ' ' : crearBlancos (n-1)

-- Ejercicio 5
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada lista = aux lista 0
    where 
        aux [] _ = []
        aux (x:xs) suma = (x + suma): (aux xs (x + suma))
    
-- B)   
esPrimo :: Int -> Bool
esPrimo n 
    | n < 2 = False
    | otherwise = not (aux n 2) -- > Es lo ouesto a si tiene divisores, e empiza con 2 ya que es el primer primo
    where 
        aux n d -- > Busca si tiene divisores desde 2 hasta d^2
            | d * d > n = False -- > Frena pq ya no hay mas divisiores
            | mod n d == 0 = True -- > Quiere decir q lo divide
            | otherwise = aux n (d + 1) -- > Se prueba con el siguinte d

descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs)
    | esPrimo x = [[x]] ++ descomponerEnPrimos xs -- > solo si es primo 
    | otherwise = [factorizar x] ++ descomponerEnPrimos xs 

factorizar:: Int -> [Int]
factorizar n = factorizarDesde n 2 
    where 
        factorizarDesde 1 _ = []
        factorizarDesde n d -- > Es 2 pq es el primer divisor primo que existe
            | mod n d == 0 = d: factorizarDesde (div n d) d 
            | otherwise = factorizarDesde n (d + 1) -- > Se prueba con el siguinet divisor

-- Ejercicio 6
-- A)
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool -- > Me pasan un laista de contactos y ques tiene la forma de contacto
enLosContactos _ [] = False
enLosContactos nombre ((name, tel):xs)
    | nombre == name = True  
    | otherwise = enLosContactos nombre xs

-- B)
agregarContactos :: Contacto -> ContactosTel -> ContactosTel
agregarContactos (nombre, tel) [] = [(nombre, tel)] 
agregarContactos (nombre, tel) ((name, phone):xs) = agregarContactos_aux (nombre, tel) ((name, phone):xs) False

agregarContactos_aux :: Contacto -> ContactosTel -> Bool -> ContactosTel 
agregarContactos_aux (nombre, tel) [] False = [(nombre, tel)] -- > SI no coincidde ninguno, crea el contacto
agregarContactos_aux _ [] _ = [] -- >  Caso base para la recursion
agregarContactos_aux (nombre, tel) ((name, phone):xs) estado
    | (nombre == name) && (estado == False) = (name, tel) : (agregarContactos_aux (nombre, tel) xs True) -- > Actualiza el contacto y da la lista de contactos actulizada
    | (nombre == name) && estado = agregarContactos_aux (nombre, tel) xs estado -- > no hacemos nada pq ya fue agregado
    | otherwise = (name, phone) : agregarContactos_aux (nombre, tel) xs estado -- > Mantiene los contactos existentes

-- C)
eliminarContactos :: Nombre -> ContactosTel -> ContactosTel
eliminarContactos _ [] = []
eliminarContactos nombre ((name,tel):xs)
    | nombre == name = eliminarContactos nombre xs
    | otherwise = (name, tel) : eliminarContactos nombre xs


-- Ejercicio 7
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker n [] = False
existeElLocker n ((id, _):xs)
    | n == id = True
    | otherwise = existeElLocker n xs 

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion -- > Asegura que los loquers que se ingresan a bucar si existen
ubicacionDelLocker n ((id, (_, ubicacion)):xs)
    | n == id = ubicacion
    | otherwise = ubicacionDelLocker n xs 

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker n ((id, (dispo, _)):xs)
    | n == id = dispo
    | otherwise = estaDisponibleElLocker n xs 


ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker n ((id, (dispo, ubi)):xs)
    | n == id && dispo = (id, (False, ubi)) : ocuparLocker n xs 
    | otherwise = (id, (dispo, ubi)): ocuparLocker n xs 

-- enLosContactos ::  Nombre -> ContactosTel -> Bool
-- enLosContactos nombre ContactosTel 
--     where 
--         aux nombre elemento
--             | nombre == fst ContactosTel 

-- enLosContactos:: Nombre -> ContactosTel -> Bool
-- enLosContactos _ [] = False
-- enLosContactos nombre (x:xs)
--     | fst x == nombre = True
--     | otherwise = enLosContactos nombre xs 

-- enLosContactos:: Nombre -> ContactosTel -> Bool
-- enLosContactos _ [] = False
-- enLosContactos nombre ((nombreActual, telefonoActual):xs)
--     | nombreActual == nombre = True
--     | otherwise = enLosContactos nombre xs 

-- enLosContactos:: Nombre -> ContactosTel -> Bool
-- enLosContactos _ [] = False
-- enLosContactos nombre ((nombreActual, _):xs)
--     | nombreActual == nombre = True
--     | otherwise = enLosContactos nombre xs 

