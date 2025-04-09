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
