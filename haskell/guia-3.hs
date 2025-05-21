-- Guia 3: 
-- Ejericio 1:
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

-- Ejercicio 2:
valorAbsoluto :: Int -> Int
valorAbsoluto x 
    | x < 1 = (-1)*x
    | x >= 1 = x 

valorAbsolutoFloat :: Float -> Float -- adapatado para lo que quiero
valorAbsolutoFloat x = sqrt(x^2) -- solo se puede hacere sto con floats pq sqrt necesita que sea float

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

enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo a b 
    | (a <= 3) && (b <= 3) = True
    | (a > 3 && a < 7) && (b > 3 && b < 7) = True
    | (a >= 7) && (b >= 7) = True
    | otherwise = False

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z 
    | x == y && x == z = 0
    | x == y = (z + y)
    | y == z = (x + y)
    | x == z = (x + y)
    | otherwise = x + y + z

esMultiploDe :: Int -> Int -> Bool
esMultiploDe a b = mod a b == 0

digitoUnidades:: Int -> Int 
digitoUnidades x = mod x 10

digitoDecenas :: Int -> Int
digitoDecenas x = mod x 100

-- Ejercicio 3
-- parte matematica: 
-- a * a + a * b * k = 0 ==> Formula dada, quiero encontarr algo que me el valor de k
-- ==> - (a * a) = a * b * k
-- ==> k = - (a * a) / (a * b)
-- ==> k = - a / b  =====> Este es el valor de K que estoy buscando y luego puedo verificar con eso

calculo :: Int -> Int -> Int -> Int -- ==> Es innecesaria esta funcion 
calculo a b k = a * a + a * b * k

estanRelacionados :: Int -> Int -> (Bool, Int)
estanRelacionados a b 
    | k == 0 = (True, m)
    | otherwise = (False, 0)
    where 
        k = mod (-a) b
        m = div (-a) b

-- Ejercicio 4
type TriplaInt = (Int, Int, Int)
type Tripla = (Float, Float, Float)
type Dupla = (Float, Float)
type Tupla = (Int, Int)

productoInterno :: Tupla -> Tupla -> Int
productoInterno (x, y) (a, b) = x * a + y * b 


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

todoMenor2 :: Dupla -> Dupla -> Bool
todoMenor2 tupla1 tupla2 
    | (fst tupla1 < fst tupla2) && (snd tupla1 < snd tupla2) = True
    | otherwise = False

distancia :: Tripla -> Tripla -> Tripla
distancia (x, y ,z) (a, b, c) = (valorAbsolutoFloat (x - a), valorAbsolutoFloat ( y - b), valorAbsolutoFloat (z - c))

sumaTerna :: TriplaInt -> Int
sumaTerna (x, y, z) = x + y + z

sumarSoloMultiplos :: TriplaInt -> Int -> Int
sumarSoloMultiplos (x, y, z) num = suma x + suma y + suma z
    where 
        suma a 
            | esMultiploDe a num == True = a
            | otherwise = 0

-- # F
-- Problema posPrimerPar tupla(int, int, int): int
-- requiere = {true}
-- asegura = {
--     devuelve el primer numero par de la tripla, en caso de que no haya se devuelve 4
-- }

posPrimerPar :: TriplaInt -> Int
posPrimerPar (x, y, z) 
    | mod x 2 == 0 = x
    | mod y 2 == 0 = y
    | mod z 2 == 0 = z
    | otherwise = 4


crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertirPar :: (a, b) -> (b, a)
invertirPar (x, y) = (y, x)

-- Ejercicio 5
todosMenores :: (Int, Int, Int) -> Bool -- ===> Funcion rarar, no hace lo que espero por el tema de los datos qu se envian a las funciones f y g
todosMenores (x, y, z) 
    | f x > g x && f y > g y && f z > g z = True
    |otherwise = False

problemaF :: Int -> Int
problemaF n
    | n > 7 = 2 * n - 1
    | otherwise = n * n

problemaG :: Int -> Int
problemaG n 
    | mod n 2 == 0 = div n 2
    | otherwise = 3 * n + 1


-- Ejercicio 6
esBiciesto :: Int -> Bool
esBiciesto anio 
    | (mod anio 4 /= 0) || ((mod anio 100 == 0 ) && (mod anio 400 /= 0)) = False
    | otherwise = True
    

-- Ejercicio 7
type Punto3D = (Float, Float, Float)
distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2)  = (valorAbsolutoFloat (x1 - x2)) + (valorAbsolutoFloat (y1 - y2)) + (valorAbsolutoFloat (z1 - z2))


-- Ejercicio 8 ============>>>>>>>>>>>>>>> MIrar pq contiene un error ____>>>> usar la de abajo que si funciona bien!!
comparar :: Int -> Int -> Int
comparar a b 
    | suma a < suma b = 1
    | suma a > suma b = - 1
    | suma a == suma b = 0
    where 
        suma num = ultimo num + anteUltimo num 
        ultimo = digitoUnidades num 
        anteUltimo num = digitoUnidades (digitoDecenas num)

-- ===>>>> Basicamnete la funcion que hcie antes pero ahora con los nombres que pide 
comparar2 :: Int -> Int -> Int
comparar2 a b 
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = - 1
    | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0


sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = unidad + decena
    where 
        num = valorAbsoluto x
        unidad = mod num 10
        decena = mod (div num 10) 10


-- ejercicio 9:
-- A) calcula el promedio de 2 numeros
-- B) si hacen lo mismo
-- C) no son iguales pq una recibe una tupla y la otra recibe elementos 