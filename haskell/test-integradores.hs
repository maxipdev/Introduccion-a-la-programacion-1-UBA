module TestDeIntegradores where
import Test.HUnit
import Integradores 

runDineroEnStock = runTestTT testDineroEnStock
runTablero = runTestTT testTablero
runMasRepetidos = runTestTT testMasRepetidos
runCamino = runTestTT testValoresDelCamino


testDineroEnStock = test [
    "caso 1" ~: dineroEnStock [("martillo", 3), ("clavo", 800), ("madera", 6)] [("martillo", 100), ("clavo", 10), ("madera", 500)] ~?= 11300
    ]

testTablero = test [
    "caso 1"~: maximo [ [13,12,6,4], [1,1,32,25], [9,2,14,7], [7,3,5,16], [27,2,8,18]] ~?= 32,
    "caso 2"~: maximo [ [13,12,6,4], [1,1,32,25], [9,2,14,7], [7,3,5,16], [27,2,8,99]] ~?= 99,
    "caso 3"~: maximo [ [50,12,6,4], [1,1,32,25], [9,2,14,7], [7,3,5,16], [27,2,8,7]] ~?= 50
    ]

testMasRepetidos = test [
    "caso 1"~: masRepetido [ [13,12,6,4], [1,1,32,25], [9,2,14,7], [7,3,5,16], [27,2,8,18]] ~?= 1,
    "caso 2"~: masRepetido [ [13,12,6,4], [2,2,32,25], [9,1,14,7], [7,3,5,16], [27,1,8,18]] ~?= 2, -- > Siempre da e numero q esta primero, q se repite mas veces y esta primero
    "caso 3"~: masRepetido [ [13,12,6,4], [1,4,32,25], [9,2,14,4], [7,3,5,16], [27,2,8,18]] ~?= 4
    ]

testValoresDelCamino = test [
    "caso 1"~: valoresDeCamino [[13,12,6,4], [1,1,32,25], [9,2,14,7]] [(1,1),(2,1), (2,4), (3,4)] ~?= [13, 1, 25, 7]
    ]