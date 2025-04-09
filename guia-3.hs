-- Guia 3: 
-- Exercise 1:
f :: Int -> Int 
f 1 = 8
f 4 = 131
f 16 = 16 

g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

fog :: Int -> Int
fog x = f (g (x))

gof :: Int -> Int
gof x = g (f (x)) 

-- Exercise 2:
valorAbsoluto :: Int -> Int
valorAbsoluto x 
    | x < 1 = (-1)*x
    | x >= 1 = x 

maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto a b 
    | (valorAbsoluto a) > (valorAbsoluto b) = valorAbsoluto a
    | (valorAbsoluto b) > (valorAbsoluto a) = valorAbsoluto b
    | otherwise = valorAbsoluto a

numeroMayor :: Int -> Int -> Int
numeroMayor a b 
    | a > b = a
    | b > a = b
    | otherwise = b

maximo3 :: Int -> Int -> Int -> Int
maximo3 a b c = numeroMayor a (numeroMayor b c)

algunoEsCero :: Int -> Int -> Bool
algunoEsCero a b 
    | a == 0 || b == 0 = True
    | otherwise = False

algunoEsCero_patter :: Int -> Int -> Bool
algunoEsCero_patter 0 _ = True
algunoEsCero_patter _ 0 = True
algunoEsCero_patter _ _ = False


-- Ejercicio 4
-- Especificacion: 
-- Problema todoMenor (tupla1:(float, float), tupla2:(float, float)): Bool {
--  requiere {true}
--  asegura: {
--  decide si el primer elemento de tupla 1 es menor al priemr elemento de tupla 2 y asi con los siguientes
--}
--}

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor tupla1 tupla2 
    | (fst tupla1 < fst tupla2) && (snd tupla1 < snd tupla2) = True
    | otherwise = False

-- otra manera: es hacerlo con lso elementos de cada tupla
-- y si lo renombro: 
type Dupla = (Float, Float)

todoMenor2 :: Dupla -> Dupla -> Bool
todoMenor2 tupla1 tupla2 
    | (fst tupla1 < fst tupla2) && (snd tupla1 < snd tupla2) = True
    | otherwise = False

-- # F
-- Problema posPrimerPar tupla(int, int, int): int
-- requiere = {true}
-- asegura = {
--     devuelve el primer numero par de la tripla, en caso de que no haya se devuelve 4
-- }

type TriplaInt = (Int, Int, Int)
posPrimerPar :: TriplaInt -> Int
posPrimerPar (x, y, z) 
    | mod x 2 == 0 = x
    | mod y 2 == 0 = y
    | mod z 2 == 0 = z
    | otherwise = 4


-- Ejercicio 6
esBiciesto :: Int -> Bool
esBiciesto anio 
    | (mod anio 4 /= 0) || ((mod anio 100 == 0 ) && (mod anio 400 /= 0)) = False
    | otherwise = True
    

-- Ejercicio 7
valorAbsolutoFloat :: Float -> Float -- adapatado para lo que quiero
valorAbsolutoFloat x = sqrt(x^2) -- solo se puede hacere sto con floats pq sqrt necesita que sea float

type Punto3D = (Float, Float, Float)
distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2)  = (valorAbsolutoFloat (x1 - x2)) + (valorAbsolutoFloat (y1 - y2)) + (valorAbsolutoFloat (z1 - z2))


-- ejercicio 9:
-- A) calcula el promedio de 2 numeros
-- B) si hacen lo mismo
-- C) no son iguales pq una recibe una tupla y la otra recibe elementos 