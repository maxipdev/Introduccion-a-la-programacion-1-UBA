module Parcial where

type Frase = [Char]
type Mapeo = [(Char, Char)]
type C = Char

hayQueCodificar::Char -> [(Char, Char)] -> Bool
hayQueCodificar _ [] = False -- > Da falso pq no hay más lista que recorrer
hayQueCodificar x ((a,_):ys)
    | x == a = True
    | otherwise = hayQueCodificar x ys

-- Ejercicio 2
cuantasVecesHayQueCodificar::Char -> [Char] -> [(Char, Char)] -> Int 
cuantasVecesHayQueCodificar c frase mapeo
    | hayQueCodificar c mapeo == False = 0
    | otherwise = cantidadDeVecesQueaparece c frase

cantidadDeVecesQueaparece::Char -> [Char] -> Int 
cantidadDeVecesQueaparece _ [] = 0
cantidadDeVecesQueaparece c (x:xs)
    | c == x = 1 + cantidadDeVecesQueaparece c xs
    | otherwise = cantidadDeVecesQueaparece c xs 

-- EJercicio 3
-- Se supone que cada elemento de la frase esta en el mapeo por lo menos una vez
-- requiere: {Existe al menos un c que pertenece a frase y hayQueCodificar(c, mapeo)=true} 
laQueMasHayQueCodificar::[Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar frase mapeo = contador frase mapeo 0 ' ' -- > Siempre da uno diferente a '' ya que siempre por condicon hay un elemento q aparece por lo minimo una vez 

-- laQueMasHayQueCodificar :: [Char] -> [(Char,Char)] -> Char
contador::[Char] -> [(Char, Char)] -> Int -> Char -> Char 
contador [] _ _ valor = valor 
contador (x:xs) mapeo veces valor 
    | cuenta > veces = contador xs mapeo (cuenta) x 
    | otherwise = contador xs mapeo veces valor 
    where 
        cuenta = cuantasVecesHayQueCodificar x (x:xs) mapeo

-- Ejercicio 4
codificarFrase::[Char] -> [(Char, Char)] -> [Char] 
codificarFrase [] _ = []
codificarFrase (x:xs) mapeo 
    | (hayQueCodificar x mapeo) = (codificar x mapeo) : codificarFrase xs mapeo -- > Vuelvo a mirar
    | otherwise = x: codificarFrase xs mapeo -- > Miro el siguiente elemento

codificar:: Char -> [(Char, Char)] -> Char 
codificar c ((a,b):ys)
    | c == a = b 
    | otherwise = codificar c ys
