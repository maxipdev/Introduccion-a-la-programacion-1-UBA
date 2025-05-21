import Test.HUnit

generarStock:: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs) 
    | (contador x xs) > 1 = (x, (contador x xs)): generarStock (quitarRepetidos x xs)
    | otherwise = (x, (contador x xs)): generarStock xs


quitarRepetidos:: (Eq t) => t -> [t] -> [t] -- > quita los elemtos repetidos, si es que hay 
quitarRepetidos _ [] = []
quitarRepetidos elemento (x:xs)
    | elemento == x = quitarRepetidos elemento xs
    | otherwise = x: (quitarRepetidos elemento xs)


contador :: [Char] -> [String] -> Int
contador _ [] = 1 -- > Pq ya teiene un caso de aparion por lo menos una vez 
contador elemento (y:ys)
    | elemento == y = 1 + (contador elemento ys)
    | otherwise = contador elemento ys

run = runTestTT test_stockMercaderia

test_stockMercaderia = test [
    "lista vacia" ~: generarStock [] ~?= [],
    "muchos elementos distintos" ~: generarStock ["clavo", "tuerca", "tornillo"] ~?= [("clavo", 1), ("tuerca", 1), ("tornillo", 1)],
    "un solo elemento repetido" ~: generarStock ["clavo", "clavo", "clavo", "clavo"] ~?= [("clavo", 4)],
    "varios repetidos" ~: generarStock ["clavo", "clavo", "clavo", "tuerca","tuerca"] ~?= [("clavo", 3), ("tuerca", 2)],
    "varias repeticiones desordenado" ~: generarStock ["clavo", "tuerca", "tornillo", "clavo", "clavo", "tuerca"] ~?= [("clavo", 3), ("tuerca", 2), ("tornillo", 1)]
    ]