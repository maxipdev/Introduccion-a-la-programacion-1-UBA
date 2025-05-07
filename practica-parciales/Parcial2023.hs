module Parcial2023 where 


type Formulas = (String, String)
type ListaDeFormulas = [Formulas]
type Votos = [Int]

-- Ejericicio 1
votosEnBlanco :: ListaDeFormulas -> Votos -> Int -> Int
votosEnBlanco formulas votos cantidadDeVotos = cantidad
    where 
        cantidad = cantidadDeVotos - (suma votos)
        suma [] = 0
        suma (v:vs) = v + suma vs 

-- Ejericio 2
formulasValidas:: ListaDeFormulas -> Bool
formulasValidas [] = True -- > Pq no hay ninguna falsa
formulasValidas ((a,b):ls) 
    | formula == False = False -- > Pq ya hay una formula invalida
    | (formula == True) && (presidenteValido == True) && (viceValido == True) = formulasValidas ls -- > Pruebo con la siguiente formula
    | otherwise = False -- > Pq hay almenos una coidicencia
    where 
        formula = analizoFormula (a,b)
        presidenteValido = verificoPresidente a ls
        viceValido = verificoPresidente b ls

-- Verifico cada presiendete
verificoPresidente:: String -> ListaDeFormulas -> Bool 
verificoPresidente _ [] = True -- > Pq no hubo ninguna coincidencia
verificoPresidente presidente ((a,b):fs)
    | presidente /= a && presidente /= b = verificoPresidente presidente fs -- > miro si el Presidente es igual algun presiendete o vice en cada lista
    | otherwise = False -- > False pq se repite en algun caso

-- Analizo cada formula
analizoFormula :: Formulas -> Bool -- Donde a = Presidente y B = Vicepresidente
analizoFormula (a,b) 
    | a == b = False -- > Compara que no sean lo mismo 
    | otherwise = True -- > Pq cumple con la condicon de que sean formula