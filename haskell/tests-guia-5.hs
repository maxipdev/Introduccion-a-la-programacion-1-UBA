module TestDeMisFunciones where

import Test.HUnit
import Guia5  -- <--- ESTE es el nombre del módulo que definiste en guia-5.hs5


-- Casos de test
runContarPalabras = runTestTT testContadorPalabras 
runAplanarConNBlancos = runTestTT testAplanarConNBlancos
runEnLosContactos = runTestTT testEnLosContactos
runAgregarContactos = runTestTT testAgregarContacto
runEliminarContactos = runTestTT testEliminarContacto
runOcuparLocker = runTestTT testOcuparLocker

testContadorPalabras = test [
    "sin palabras"~: contarPalabras [] ~?= 0,
    "sin espacios adelante y al final" ~: contarPalabras "hola soy maxi" ~?= 3,
    "con un espacio adelante y no al final" ~: contarPalabras " hola soy maxi" ~?= 3,
    "con un espacio atras solamente" ~: contarPalabras "hola soy maxi " ~?= 3,
    "con espacios adelante y atras" ~: contarPalabras " hola soy maxi " ~?= 3,
    "con muchos espacios" ~: contarPalabras "hola soy            maxi" ~?= 3
    ]

testAplanarConNBlancos = test [
    "sin lista de plabras" ~: aplanarConNBlancos [] 1 ~?= [],
    "con 3 espacios" ~: aplanarConNBlancos ["hola", "aguante", "independiente"] 3 ~?= "hola   aguante   independiente",
    "con un espacio" ~: aplanarConNBlancos ["hola", "aguante", "independiente"] 1 ~?= "hola aguante independiente"
    ]

testEnLosContactos = test [
    "no hay contactos" ~: enLosContactos "maximo" [] ~?= False,
    "hay 2 contactos (esta)" ~: enLosContactos "maximo" [("maria", "11"), ("maximo", "12")] ~?= True,
    "hay 2 contactos (esta)" ~: enLosContactos "maximo" [("maria", "11"), ("maximo", "12"), ("juan", "13")] ~?= True,
    "al final" ~: enLosContactos "maximo" [("maria", "11"), ("juan", "13"), ("maximo", "12")] ~?= True,
    "al incio" ~: enLosContactos "maximo" [("maximo", "12"), ("maria", "11"), ("juan", "13")] ~?= True,
    "no está" ~: enLosContactos "maximo" [("maria", "11"), ("juan", "13")] ~?= False
    ]

testAgregarContacto = test [
    "no hay contactos" ~: agregarContactos ("max", "10") [] ~?= [("max", "10")],
    "actualizo el contacto" ~: agregarContactos ("max", "10") [("max", "1"), ("carmen", "13")] ~?= [("max", "10"),("carmen", "13")],
    "creo mi contacto" ~: agregarContactos ("max", "10") [("diana", "10"), ("carmen", "13")] ~?= [("diana", "10"),("carmen", "13"), ("max", "10")]
    ]

testEliminarContacto = test [
    "no esta ese contacto" ~: eliminarContactos "max" [("diana", "10"), ("carmen", "13")] ~?= [("diana", "10"), ("carmen", "13")],
    "esta el contacto" ~: eliminarContactos "max" [("max", "1"), ("carmen", "13")] ~?= [("carmen", "13")],
    "en el medio" ~: eliminarContactos "max" [("diana", "10"), ("max", "1"), ("carmen", "13")] ~?= [("diana", "10"), ("carmen", "13")],
    "al final" ~: eliminarContactos "max" [("diana", "10") , ("carmen", "13"), ("max", "1")] ~?= [("diana", "10"), ("carmen", "13")]
    ]

testOcuparLocker = test [
    "ocupar" ~: ocuparLocker 101 [(100,(False,"ZD39I")),(101,(True,"JAH3I")),(103,(True,"IQSA9"))] ~?= [(100,(False,"ZD39I")),(101,(False,"JAH3I")),(103,(True,"IQSA9"))],
    "ocupar" ~: ocuparLocker 101 [(100,(False,"ZD39I")),(101,(False,"JAH3I")),(103,(True,"IQSA9"))] ~?= [(100,(False,"ZD39I")),(101,(False,"JAH3I")),(103,(True,"IQSA9"))]
    ]

