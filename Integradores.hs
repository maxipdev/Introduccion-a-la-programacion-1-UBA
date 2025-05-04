module Integradores where

-- Ejercicio 1

generarStock:: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs) = (x, contador x xs) : generarStock (quitarRepetidos x xs)

contador :: [Char] -> [String] -> Int
contador _ [] = 1 -- > Pq siempre como minimo aparace una vez 
contador elemento (x:xs) 
    | elemento == x = 1 + contador elemento xs 
    | otherwise = contador elemento xs

quitarRepetidos :: (Eq t) => t -> [t] -> [t]
quitarRepetidos _ [] = []
quitarRepetidos a (x:xs)
    | a == x = quitarRepetidos a xs 
    | otherwise = x : (quitarRepetidos a xs )

-- Ejercicio 2
type Cantidad = Int
type Producto = [Char]
type Precio = Float
type Stock = (Producto, Cantidad)
type ListaStock = [Stock]
type Precios = (Producto, Precio)
type ListaPrecios = [Precios]

-- Todos los que estan en la lsita tiene Stock
-- No hay repetidos
stockDelProducto:: Producto -> ListaStock -> Cantidad
stockDelProducto _ [] = 0
stockDelProducto elemento ((producto, cant):xs)
    | elemento == producto = cant 
    | otherwise = stockDelProducto elemento xs 

-- Ejercicio 3
-- Supongo que esta todo a la misma altura, es decir hay tanta cantidad de precios como produtos en cada lista
dineroEnStock:: ListaStock -> ListaPrecios -> Float
dineroEnStock [] _ = 0
dineroEnStock (x:xs) lPrecios = (dineroEnStock_aux x lPrecios) + (dineroEnStock xs lPrecios)

dineroEnStock_aux :: Stock -> ListaPrecios -> Float
dineroEnStock_aux _ [] = 0
dineroEnStock_aux (producto, cant) ((nameProduct, precio):ys) 
    | producto == nameProduct = precio * (fromIntegral cant)
    | otherwise = dineroEnStock_aux (producto, cant) ys


-- Ejercicio 4
aplicarOferta:: ListaStock -> ListaPrecios -> [(Producto, Float)]
aplicarOferta _ [] = []
aplicarOferta stock ((nameProduct, precio):ys)
    | funcion > 10 = (nameProduct, precio * 0.80) : aplicarOferta stock ys
    | funcion <= 10 = (nameProduct, precio) : aplicarOferta stock ys
    | otherwise = aplicarOferta stock ys
    where 
        funcion = stockDelProducto nameProduct stock

-- Ejericicio 5
type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maximo:: Tablero -> Int
maximo t = maximo_aux t 0 -- > SAbiendo que siempre me tiene q dar un numero mas grande q 0

maximo_aux:: Tablero -> Int -> Int
maximo_aux [] e = e -- > Doy el e mas grande
maximo_aux (t:ts) e = maximo_aux ts (maximo_Fila t e)      

maximo_Fila:: Fila -> Int -> Int
maximo_Fila [] e = e -- > Da el numero mas grande de la lista 
maximo_Fila (x:xs) e 
    | x > e = maximo_Fila xs x -- > Agrego al x como el mas grande
    | otherwise = maximo_Fila xs e 

-- Ejercicio 6
masRepetido:: Tablero -> Int
masRepetido t = verificador (concatenarTuplas t) 0 0

verificador :: [(Int, Int)] -> Int -> Int -> Int 
verificador [] _ valor = valor 
verificador ((a,b):xs) max valor
    | b > max = verificador xs b a 
    | otherwise = verificador xs max valor

concatenarTuplas:: Tablero -> [(Int, Int)]
concatenarTuplas t = unificar (agruparFilas t)

unificar:: [(Int, Int)] -> [(Int, Int)] -- Da lo mismo pero sin repetidos
unificar [] = []
unificar ((a,b):xs) 
    | cantidad > b = (a, cantidad) : unificar (quitar (a,b) xs) -- > dice q hay repetidos
    | otherwise = (a, cantidad) : unificar xs
    where 
        cantidad = sumarTuplas ((a,b):xs) (a,b)

-- Quito las tuplas repetidas
quitar:: (Int, Int) -> [(Int, Int)] -> [(Int, Int)]
quitar _ [] = []
quitar (a,b) ((x1, x2):xs)
    | a == x1 = quitar (a, b) xs -- > Lo quito
    | otherwise = (x1, x2) : quitar (a,b) xs 

-- Sumo las cantidades de la tupla
sumarTuplas:: [(Int, Int)] -> (Int, Int) -> Int
sumarTuplas [] (a,b) = b  -- Suma asi mismo
sumarTuplas ((e, cant):xs) (a,b) 
    | e == a = cant + sumarTuplas xs (a,b) -- > Sumo las cantidades de cada elemento
    | otherwise = sumarTuplas xs (a,b)

-- Agrupamos por filas
agruparFilas:: Tablero -> [(Int, Int)]
agruparFilas [] = []
agruparFilas (t:ts) = iterar_fila t ++ agruparFilas ts -- > Genera una mega listas

-- Itera sobre cada elemetno de la lista
iterar_fila :: Fila -> [(Int, Int)]
iterar_fila [] = []
iterar_fila (x:xs) 
    | (cantidadDeApariciones xs x) > 1 = (x, cantidadDeApariciones xs x) : iterar_fila (quitarElementos x xs) -- > Indica que hay mas de un elemento
    | otherwise = (x, cantidadDeApariciones xs x) : iterar_fila xs 

-- Quita los elementos repetidos
quitarElementos:: Int -> Fila -> Fila -- >  Quita los elementos repetidos
quitarElementos _ [] = []
quitarElementos n (x:xs)
    | n == x = quitarElementos n xs
    | otherwise = x : quitarRepetidos n xs  

-- Calcula la cantidad de apariciones de un elemento en la lista
cantidadDeApariciones:: Fila -> Int -> Int -- > Da la cantiad de apariciones de un num en una fila
cantidadDeApariciones [] _ = 1 -- > Pq siempre aparece como minimo una vez
cantidadDeApariciones (x:xs) n
    | x == n = 1 + cantidadDeApariciones xs n
    | otherwise = cantidadDeApariciones xs n

-- Ejercicio 7
valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino _ [] = []
valoresDeCamino t ((y,z):cs) = elemento : valoresDeCamino t cs
    where 
        elemento = index (index t (y-1)) (z-1)   

index:: [t] -> Int -> t 
index (x:_) 0 = x
index (_:xs) n = index xs (n-1)

-- Ejericio 8
fibonacci:: Int -> Int 
fibonacci 0 = 0
fibonacci 1 = 1 
fibonacci n = fibonacci (n-1) + fibonacci (n-2) 

-- dice que cada numero q esta en la secuencia tiene que ser igual a lo que da fibonacci en ese numero n, empezando con n hasta que la len de la lista sea 0
esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [] _ = True
esCaminoFibo (x:xs) n 
    | x == fibonacci n = esCaminoFibo xs (n+1)
    | otherwise = False

-- Ejercicio 9
divisoresPropios:: Int -> [Int]
divisoresPropios n = aux n 1 -- > Pq el primer divisor es el 1
    where
        aux n d 
            | d == n = [] -- > damos vacio y que pare ya que non nos interesa q un número se divida asi mismo   
            | mod n d == 0 = d : aux n (d+1)  
            | otherwise = aux n (d+1)

-- Ejercicio 10
sonAmigos:: Int -> Int -> Bool 
sonAmigos x y 
    | suma (divisoresPropios x) == y && suma (divisoresPropios y) == x = True
    | otherwise = False
    where 
        suma [] = 0
        suma (x:xs) = x + suma xs

-- Ejercicio 11 
{--El enunciado dice que no hay que ejecutar numero smas grande de 4, es decir no es recomendable para n > 4 --}
losPrimerosNPerfectos:: Int -> [Int] -- > Da los primeros n perfectos
losPrimerosNPerfectos n = aux n 1 0 -- > Primer númeroy el 0 es de que no hay perfetos acumulados
    where 
        aux n m k -- > donde k = cantidad de pefetctos que se acumulan 
            | k == n = [] -- > para aca pq si quiero al elemento en la posicion n, no quiero al de n+1
            | esPerfecto m = m : aux n (m+1) (k+1) -- > Aumento k pq es perfecto
            | otherwise = aux n (m+1) k -- > no aumento k pq no es perfecto

esPerfecto :: Int -> Bool
esPerfecto x 
    | x == suma (divisoresPropios x) = True
    | otherwise = False 
    where 
        suma [] = 0
        suma (x:xs) = x + suma xs

-- Ejercicio 12
listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos [] = []
listaDeAmigos (x:xs) = verificador x xs ++ listaDeAmigos xs
    where 
        verificador _ [] = []
        verificador e (y:ys)
            | sonAmigos e y = (e,y) : verificador e ys
            | otherwise = verificador e ys