factorial :: Integer -> Integer
factorial n
    | n > 0 = n * factorial (n -1)
    | n == 0 = 1

-- Ejercicio 1
fibonaci :: Int -> Int
fibonaci 0 = 0
fibonaci 1 = 1
fibonaci n = fibonaci(n-1) + fibonaci(n-2) 

-- -- Ejercicio 2
parteEntera :: Float -> Int
parteEntera num 
    | num < 1 = 0
    | otherwise = 1 + parteEntera (num -1)

-- Ejercicio 3
esDivisible :: Int -> Int -> Bool
esDivisible a b = aux a b 
    where 
        aux x y 
            | x < 0 = False
            | x == 0 = True
            | otherwise = aux (x -y) y

-- Ejercicio 7
{--
los numeros de i tiene que ser =< a la cantidadDeDigitos de n
--}
cantDigitos :: Int -> Int 
cantDigitos n 
    | n < 10 = 1 
    | otherwise = 1 + cantDigitos(div n 10)

-- ==> VERIFICAR EJERCICIO
iesimoDigito :: Int -> Int -> Int
iesimoDigito n i = mod (div n 10^((cantDigitos n) -i)) 10 -- ==> es una formula cerrada

iesimoDigito_2 :: Int -> Int -> Int -- ==> Realizada con recu
iesimoDigito_2 n i 
    | cantDigitos n == i = mod n 10 
    | otherwise = iesimoDigito_2 (div n 10) i

-- Ejericio 9
ultimo :: Int -> Int
ultimo n = mod n 10

primero :: Int -> Int
primero n = mod n (cantDigitos n)

-- esCapicua :: Int -> Bool
-- esCapicua n 
--     | n < 10 = True
--     | pr == ul = esCapicua()
--     where
--         pr = primero n 
--         ul = ultimo n





