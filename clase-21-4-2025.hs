-- Ejercicio 14
sumaPotencias:: Int -> Int -> Int -> Int
sumaPotencias _ 0 _  = 0
sumaPotencias q n m = sumatoria q n m + sumaPotencias q (n-1) m
     where 
        sumatoria _ _ 0  = 0
        sumatoria q a b = q^(a+b) + sumatoria q a (b-1) -- > El a es el mismo pq no cambia

-- Ejercicio 16
menorDivisor:: Int -> Int -- > Bien hecho, cambiar en la guia
menorDivisor n = aux n n 1
    where 
        aux n k z
            | k == 1 = z 
            | mod n k == 0 = aux n (k-1) k
            | otherwise = aux n (k-1) z 
        
-- Hecho en clase ==> Igual que la otra
menorDivisor_2 :: Int -> Int
menorDivisor_2 n = menorDivisorDesde n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde 1 _ = 1 
menorDivisorDesde n k 
    | mod n k == 0 = k
    | otherwise = menorDivisorDesde n (k+1)





------------------------------------------------
-- esPrimo :: Int -> Bool
-- esPrimo x 
--     | x < 2 = False
--     |otherwise = not (tieneDivisores x 2) -- > Se pone el 2 pq el 1 es divisior de todos y se quiere ver si desde 2 hsta x-1 hay algun divisor más, se le poone el not por un tema de escritura, ya que es lo contrario a lo que devuleve tieneDivisaores lo que necesitamos para que sea primo
--     where
--         tieneDivisores n d 
--             | d * d > n = False -- > Pq dice que si es mayor a eso ya no hay mas divisiores, siempre un numero es divor si es mas grande, Por Ej: si n> d significa q todavia hay mas divisores
--             | mod n d == 0 = True
--             | otherwise = tieneDivisores n (d+1)

-- esSumaInicialDePrimosAux
-- Ejericio 19
-- sumaPrimos :: Int -> Int
-- sumaPrimos n = []

-- crearPrimo:: Int -> Int -- > Crea el primer primo que encuentra, es decir si n == 1 crea el 2 y si n == 4 crea el 5
-- crearPrimo n 
--     | esPrimo n == True = n 
--     | otherwise = crearPrimo (n+1)

-- verificador :: Int -> Bool
-- verificador n = aux n crearPrimo n
--     where
--         aux n k 
--             | n < k = False
--             | n > k = 
--             | otherwise = aux n (aux_2 k) 

--         aux_2 k 
--             | k == crearPrimo (k+1) = (k+2)
--             |otherwise = crearPrimo k

-- esSumaInicialDePrimos:: Int -> Bool
-- esSumaInicialDePrimos n 
--     | n < 2 = False -- > Pq el 1 no se puede sumar con 1 +1 primos
--     | otherwise = False


-- Resolucion clase
esPrimo :: Int -> Bool
esPrimo n = menorDivisor_2 n == n

esSumaInicialDePrimos:: Int -> Bool
esSumaInicialDePrimos 0 = False
esSumaInicialDePrimos n = esSumaInicialDePrimosAux

esSumaInicialDePrimosAux:: Int -> Int -> Bool
esSumaInicialDePrimosAux n k 
    | n == 0 = True -- > Caso base
    | n < 0 = False
    | esPrimo k = esSumaInicialDePrimosAux (n-k) (k+1) -- > Le resta al n por el valor actual de k (primo) y luego le suma uno
    | otherwise = esSumaInicialDePrimosAux n (k+1)

-- Ejemplo de como funciona
{--
n = 17
k = 2
==> 17 - 2  =15
==> n = 15 y k = 3
==> 15 - 3 = 12
n = 12 y k = 4 -- no es par el 4
n = 12 y k = 5 
12 - 5 = 7
n = 7 y k = 6 -- no e spar el 6
n = 7 y k = 7
7 - 7 = 0 --> Cumple con el caso base
--}


-- Ejemplo de como hacer nEsimoPrimo:
nEsimoPrimo :: Int -> Int
nEsimoPrimo 1 = 2
nEsimoPrimo n = nEsimoPrimoAux n 1 1

nEsimoPrimoAux :: Int -> Int -> Int -> Int
nEsimoPrimoAux n i c 
    | esPrimo 1 && n == c = i 
    | esPrimo 1 && n /= c = nEsimoPrimoAux n (i+1) (c+1)
    | otherwise = nEsimoPrimoAux n (i+1) c




-- primerosPrimos:: Int -> [Int]
-- primerosPrimos n = [d | d <- [2 .. n], esPrimo d]

-- sumaPrimos:: [Int] -> Int -> Int
-- sumaPrimos lista n
--     | n < 0 = 0
--     | otherwise = lista !! n + sumaPrimos lista (n-1)

-- esSumaInicialDePrimos:: Int -> Bool
-- esSumaInicialDePrimos n 
--     | n > (sumaPrimos (primerosPrimos n) n)  = True
--     | otherwise = False
