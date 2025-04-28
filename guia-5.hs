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

mayor:: [Int] -> Int -- > Tengo que buscar el mayor elemento de la lista
mayor (x:xs) = aux xs x 
    where 
        aux [] mayor = mayor
        aux (n:ns) mayor
            | n > mayor = aux ns n 
            | otherwise = aux ns mayor

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

ordenar:: [Int] -> [Int]
ordenar (x:xs) = verificar x xs 
    where 
        verificar x (n:ns) mayor
            | n > x = verificar 