module TestP2023 where 

import Test.HUnit 
import Parcial2023 

runEj2 = runTestTT testEj2

testEj2 = test [
    "todo valido" ~: formulasValidas [("Mario", "Julia"), ("marcos", "esteban")] ~?= True,
    "formula interna invalida" ~: formulasValidas [("Mario", "Mario"), ("marcos", "esteban")] ~?= False,
    "todo invaldio" ~: formulasValidas [("Mario", "Mario"), ("Mario", "Mario")] ~?= False,
    "presi 2 vecs" ~: formulasValidas [("Mario", "Julia"), ("Mario", "esteban")] ~?= False,
    "el presindete aparace como vice" ~: formulasValidas [("Mario", "Julia"), ("marcos", "Mario")] ~?= False,
    "el vice aparece 2 veces" ~: formulasValidas [("Mario", "Julia"), ("esteban", "Julia")] ~?= False,
    "el vice aparece 2 veces x2" ~: formulasValidas [("Mario", "Julia"), ("Julia", "esteban")] ~?= False
    ]