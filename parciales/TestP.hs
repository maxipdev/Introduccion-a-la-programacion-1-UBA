module TestP where

import Test.HUnit 
import Parcial


runEjercicio2 = runTestTT testEj2
runEj3 = runTestTT test3
runEjercicio4 = runTestTT testEj4

testEj2 = test [ 
    "caso 2"~: cuantasVecesHayQueCodificar 'h' ['h','o','l','a'] [('h', 'o')] ~?= 1,
    "sin la palabra en la frase" ~: cuantasVecesHayQueCodificar 'h' ['k','o','l','a'] [('h', 'o')] ~?= 0, -- > Pq no hay coincidencia
    "sin la palabra en general"~: cuantasVecesHayQueCodificar 'h' ['k','o','l','a'] [('k', 'o')] ~?= 0, -- > Pq no esta en mapeo es 0,
    "caso 2"~: cuantasVecesHayQueCodificar 'h' ['h', 'h' ,'o','l','a'] [('h', 'o')] ~?= 2
    ]

test3 = test [
    "caso 1" ~: laQueMasHayQueCodificar ['h', 'o','l','a'] [('h', 'o')] ~?= 'h',
    "aparece una vez" ~: laQueMasHayQueCodificar ['h','h','o','l','a'] [('h', 'o')] ~?= 'h', -- > Tiene que dar Hola pq es su primer elemento
    "no coincide" ~: laQueMasHayQueCodificar ['h','o','o','l','a'] [('h', 'o')] ~?= 'h', -- > Da hola pq "como" no esta en el mapeo
    "coincide" ~: laQueMasHayQueCodificar ['h','o','o','l','a'] [('o', 'o')] ~?= 'o',
    "varias coicidencias" ~: laQueMasHayQueCodificar ['h','o','o','l','a'] [('h', 'o'),('o', 'o')] ~?= 'o', -- > Pq es el q mas se repite
    "varias coicidencias al reves" ~: laQueMasHayQueCodificar ['h','o','o','l','a'] [('o', 'o'),('h', 'o')] ~?= 'o'
    ]

testEj4 = test [
    "caso 1" ~: codificarFrase ['h', 'o','l','a'] [('h', 'o')] ~?= ['o', 'o','l','a'],
    "multiples valores" ~: codificarFrase ['h', 'o','l','a'] [('h', 'o'), ('l', 'm')] ~?= ['o', 'o','m','a'],
    "ningun valor" ~: codificarFrase ['h', 'o','l','a'] [('f', 'o'), ('g', 'm')] ~?= ['h', 'o','l','a'],
    "cambio toda la frase" ~: codificarFrase ['h', 'o','l','a'] [('h', 'o'), ('l', 'm'), ('o', 'k'), ('a', 'z')] ~?= ['o', 'k','m','z'],
    "mapea espacios" ~: codificarFrase "un gran poder blabla" [(' ', '*')] ~?= "un*gran*poder*blabla",
    "caso al reves" ~: codificarFrase "america manda" [('a', 'j')] ~?= "jmericj mjndj",
    "solo la priemra" ~: codificarFrase "cel bebe" [('c', 'z')] ~?= "zel bebe",
    "nada mapeable" ~: codificarFrase "un gran poder" [('m', 'h')] ~?= "un gran poder",
    "mapeo vacio" ~: codificarFrase "un gran poder" [] ~?= "un gran poder"
    ]

