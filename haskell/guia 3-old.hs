doubleMe :: Int -> Int
doubleMe x = x + x +1


-- Con pattern matching
problemaF:: Int -> Int
problemaF 1 = 8
problemaF 4 = 131
problemaF 16 = 16

-- Con guardas: 
f :: Int -> Int
f n 
    | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1


h :: Int -> Int
h n = f(g(n)) 

k :: Int -> Int
k n = g(f(n)) 

-- ejercicio 2
maximo:: Int -> Int -> Int -> Int
maximo num1 num2 num3
    | (num1 >= num2) && (num1 >= num3)= num1mod a 100
    | otherwise = y 

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 n1 n2 n3 = maximo2 n1 (maximo2 n2 n3)

-- ejercicio 3 G 
-- hecho por casos
sumaDistintos_2 :: Int -> Int -> Int -> Int
sumaDistintos_2 x y z
    | (x == y) && (x == z) = 0
    | x == y = z
    | x == z = y
    | otherwise = x + y + z

digitoUnidades :: Int -> Int
digitoUnidades a = mod a 10

digitoDecenas :: Int -> Int
digitoDecenas a = div (mod a 100) 10
