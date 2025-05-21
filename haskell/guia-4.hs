factorial :: Integer -> Integer
factorial n
    | n > 0 = n * factorial (n -1)
    | n == 0 = 1

-- Ejercicio 1
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2) 

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

-- Ejercicio 4
{--tengo que crear una funcion que me devuleva los primeros 3 numeros impares--}
sumaImpares :: Int -> Int
sumaImpares n 
    | n == 1 = 1
    | n == 0 = 0
    | otherwise = 2*n-1 + sumaImpares (n-1)

-- Ejercicio 5
medioFact :: Int -> Int
medioFact n 
    | n < 1 = 1 
    | otherwise = n*(medioFact (n-2))

-- Ejercicio 6
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n = verificar (primeros n) (ultimo n) -- Miro los primeros numeros y miro el utimo para la comparacion
   -- en este caso y es el ultimo numero e X los primeros terminos
    where 
        ultimo x = mod x 10 
        primeros x = div x 10
        verificar x y = x == 0 || ((ultimo x == y) && (verificar (primeros x) y))

-- Ejercicio 7
{--
los numeros de i tiene que ser =< a la cantidadDeDigitos de n
--}
cantDigitos :: Int -> Int 
cantDigitos n 
    | n < 10 = 1 
    | otherwise = 1 + cantDigitos(div n 10)


--Ejercicio 8
sumaDigitos :: Int -> Int
sumaDigitos 0 = 0
sumaDigitos x
    | x < 10 = x
    | otherwise = (ultimo x) + sumaDigitos(primeros x)
    where 
        primeros n = div n 10 -- > Debuelve los primeros números, es decir quita el ultimo
        ultimo n = mod n 10 -- > Debuelve el ultimo numero

--- Ejercicio 9
esCapicua:: Int -> Bool -- > Si invierto el número tendria que ser igual al que me dieron si es capicua
esCapicua x 
    | x < 10 = True
    | x == (invertir x) = True
    | otherwise = False
    where 
        invertir x = invertir_aux x 0 -- > Recibe 0 pq es con lo que inicai el nuevo numero
        ultimo n = mod n 10
        primeros n = div n 10
        invertir_aux 0 nuevo_num = nuevo_num -- > Pattern mattching
        invertir_aux b nuevo_num = invertir_aux (primeros b) (nuevo_num * 10 + (ultimo b)) -- > Multiplico a nuevo_num para que tenga un 0 atras y lo que me permita que la suma no afecte a los otros números, sino que le agrege ese núm al final

-- Ejericio 10
-- A)
{-- es la sumatora desde i = 0 hasta n de las potencias i de 2, con n >= 0
Pero tambien esto es la forma de la geometrica, es decir se puede escribir de esta manera: 
Para q !== 1: 
(q^(n+1) - 1 )/ (q -1)
Y Para q == 1
n + 1
como en el ejericio q !== 1 se aplica la priemra formula
--}
f1 :: Int -> Int
f1 n = div (2^(n+1) - 1) (2 - 1) -- > Remplace el valor de q == 2

-- B)
{--Es Exactamnete lo mismo que la anterior pero con la diferencia que a esta se tiene que dividir en casos la q ya que pertenece a los Reales--}
f2 :: Int -> Float -> Float
f2 n q 
     | q /= 1 = (q ** fromIntegral(n+1) - 1) /(q - 1) -- > con fromIntegralpaso de Int a Float
     | otherwise = fromIntegral (n+1) -- > Pq me da un Int y yo digo que devuelve Float

-- C) 
{--Es la sumatoria desde i == 1 hasta 2n lo que quiere decir esto por algebra que tenemos la sumatoria de q^i pero como está el 2 
lo puedo escribir con una multipliaccion sacandolo hacia afuera, esto hace que en lugar de la i se remplace por la n
pero le tengo que hacer -1 pq esta empezando con i = 1--}
f3:: Int -> Float -> Float
f3 n q 
    | q == 1 = fromIntegral (n + 1)
    | otherwise = ((q**(fromIntegral n)) * (q ** fromIntegral(n+1) - 1) /(q - 1)) -1


-- D)
f4:: Int -> Float -> Float
f4 n q 
    | q == 1 = fromIntegral (n + 1)
    | n == 1 = ((q**(fromIntegral n)) * (q ** fromIntegral(n+1) - 1) /(q - 1)) -1
    | otherwise = (q**(fromIntegral n)) * (q ** fromIntegral(n+1) - 1) /(q - 1)

-- Ejercicio 11
-- A) 
{--Es una sumatoria que va desde i == 0 hsta n en donde aplica 1/i!, por lo tento se define el factorial y se calula desde ahi
sabiendo que en el caso n == 0 se tiene que sumar 1 ya que la i empieza con un valoir de 0--}
eAprox :: Int -> Float
eAprox 0 = 1 -- > Pq empieza con i == 0
eAprox n =  (1 / (fromIntegral (factorial n))) + eAprox (n-1)
    where 
        factorial 0 = 1
        factorial n = n * factorial (n-1)

-- B)
e :: Float 
e = eAprox 10

-- -- Ejercicio 12
raizDe2Aprox :: Int -> Float 
raizDe2Aprox 1 = 1 -- > segun el ejemplo de la raiz
raizDe2Aprox n = (aux n) -1 -- > Definicion de raiz de 2 == An -1
    where 
        aux 1 = 2 -- > valor dado por A1
        aux n = 2 + (1 / (aux (n-1))) -- > es con "/" pq la funcion da como salida un Float entonces hay que dividir como floats

-- Ejercicio 13
multiSumatoria :: Int -> Int -> Int
multiSumatoria 0 _ = 0
multiSumatoria n m =( sumatoria n m n) + multiSumatoria (n-1) m -- > Le paso n de nuevo pq quiero que inicie con q == n y dpues se le va restando por funcionamiento normal de la funcion, ya que cuando se llama de nuevo a n-1 => entonces el valor de n es el que le paso como i
    where 
        sumatoria :: Int -> Int -> Int -> Int
        sumatoria n m i 
            | i == 1 = m -- > NO LE AGREGO EL +1 PQ LA SUMATORIA VA DESDE i == 1 Y COMO NO EMPIEZA DESDE i == 0 HAY QUE RESTARLE 1 PARA LA FORMULA SEA VALIDA (LA GEOMETRICA) ==> N + 1 - 1 = N
            | otherwise = (div (i^(m+1)-1) (i-1)) -1 -- > Esto simula ser la sumatoria desde j == 0 hasta m con i un numeor fijo, pero despeus este cambia pero gracias a la otra funcion

-- Ejericio 14
{--Quiero hacer una sumatoria de todas las posibles convinaciones de potencias de la forma q^(a+b)
en donde los valores de son 1 =< a =< n y 1 =< b =< m
eso ultimno me dice q es una sumatoia que va desde i == 1 hasta n/m--}

sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = aux q n m + sumaPotencias q (n-1) m
    where
        formula q a b = q^(a+b)
        aux _ _ 0 = 0
        aux q n m = (formula q n m) + (aux q n (m-1)) 

-- Ejercicio 15
sumaRacionales:: Int -> Int -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = aux n m + sumaRacionales (n-1) m
    where 
        formula p q = (fromIntegral (p)) / (fromIntegral (q)) -- > Tiene que ser en Float esta division pq con Div no devuelve nada para ya que 1/2 = 0.5 y con div == 0
        aux _ 0 = 0
        aux n m = formula n m + aux n (m-1)

-- Ejercicio 16
esPrimo :: Int -> Bool
esPrimo x 
    | x < 2 = False
    |otherwise = not (tieneDivisores x 2) -- > Se pone el 2 pq el 1 es divisior de todos y se quiere ver si desde 2 hsta x-1 hay algun divisor más, se le poone el not por un tema de escritura, ya que es lo contrario a lo que devuleve tieneDivisaores lo que necesitamos para que sea primo
    where
        tieneDivisores n d 
            | d * d > n = False -- > Pq dice que si es mayor a eso ya no hay mas divisiores, siempre un numero es divor si es mas grande, Por Ej: si n> d significa q todavia hay mas divisores
            | mod n d == 0 = True
            | otherwise = tieneDivisores n (d+1)

menorDivisor:: Int -> Int -- > PAra este ejercicio no era necesesario usa esPrimo, pero como no afecta usarlo
menorDivisor n
    | esPrimo n == True = n
    | otherwise = encontarDivisor n 2 -- > Empieza con 2 pq es el primeer número > 1
    where 
        encontarDivisor n k -- > Encuentra lso divisiores
            | mod n k == 0 = k
            | otherwise = encontarDivisor n (k+1) 


divisores :: Int -> [Int]
divisores n = (aux n 2 [])
    where 
        aux a b lista 
            | a < b = lista
            | mod a b == 0 = aux a (b+1) (b : lista)
            | otherwise = aux a (b+1) lista

-- divisores :: Int -> [Int] -- > No es valido hacerlo, por lo tanto, cambio l amanera de ver los divisores
-- divisores n = [d | d <- [2 .. n], mod n d == 0] -- > quito el 1 pq ya se q es dvisor de tosos y no me sirve para mi lógica

-- Creo el lenght propio:
len:: [t] -> Int
len [] = 0
len (_:xs) = 1 + len xs 


verificarLista :: [Int] -> [Int] -> Bool
verificarLista h j 
    | h == j = False
    | otherwise = sumatoria_2 h j len_h len_j -- > datos que necesita la funcion sumatoria_2
    where 
        len_h = (len h) -1
        len_j = (len j) -1
        -- ------------
        sumatoria_2 h j len_h var_j
            | var_j < 0 = False
            | sumatoria_1 h j len_h var_j == True = True -- > Indica que hay divisores repetidos
            | otherwise = sumatoria_2 h j len_h (var_j -1)

        sumatoria_1 h j len_h var_j
            | len_h < 0 = False
            | h !! len_h == j !! var_j = True -- > Dice que tienen más de un divisor en comun ya que tyodos tienen al 1, peor aca abria mas
            | otherwise = sumatoria_1 h j (len_h -1) var_j 

sonCoprimos:: Int -> Int -> Bool -- > No tienen divisores en comun >= 1
sonCoprimos x y 
    | x == y = False -- > Pq solo tienen que tener un divisor en común y acá tienen 2 el 1 y n
    | (esPrimo x) && (esPrimo y) = True
    | verificarLista divisores_x divisores_y /= True = True -- > Pq si tienenn num repetidos no son coPrimos
    | otherwise = False
    where 
        divisores_x = divisores x 
        divisores_y = divisores y 



-- nEsimoPrimo2:: Int -> Int
-- nEsimoPrimo2 n = listaDeNumerosPrimos !! (n-1)
--     where
--         listaDeNumerosPrimos = [d | d <- [2..(definirHasta n)], esPrimo d]
--         definirHasta 1 = 10 
--         definirHasta n = n*n 


nEsimoPrimo :: Int -> Int
nEsimoPrimo n = contadorPrimos 1 n 0 -- > Es el num y la cantidad hsta la que hay que llegar y las veces son las posiciones de los primos
{--empieza desde 2 ya q es el primer primo --}

contadorPrimos :: Int -> Int -> Int -> Int
contadorPrimos numero cantidad veces
    | veces == cantidad = numero - 1 -- > Le resto porque al llamar a la función le sume un numero que no iba
    | esPrimo numero = contadorPrimos (numero + 1) cantidad (veces + 1)
    | otherwise = contadorPrimos (numero + 1) cantidad veces


-- Ejercicio 17
index:: [a] -> Int -> a 
index (x:_) 0 = x -- > Da el primer numero
index (_:xs) n = index xs (n-1) -- > Va cortando la lista, le va quitando el primer numero y cuando llega a 0 da ese numero

esFibonacci :: Int -> Bool -- > Verificar Ejercicio
esFibonacci n = aux n (k n)
    where
        k 1 = 10
        k n = n*n + 2
        aux n k
            | k < 0 = False -- > Significa que ya no hay mas numeros para probar
            | n == fibonacci k = True
            | otherwise = aux n (k-1)

 -- Ejercicio 18
mayorDigitoPar :: Int -> Int
mayorDigitoPar 0 = 0
mayorDigitoPar n
    | n < 10 && esPar n = n
    | n < 10 && (esPar n == False) = -1
    | otherwise = aux n 0
    where
        ultimoDigito x = mod x 10
        resto x = div x 10
        esPar n 
            | mod n 2 == 0 = True
            | otherwise = False

        aux :: Int -> Int -> Int
        aux a maxPar
            | a == 0 = maxPar -- > caso base
            | esPar (ultimoDigito a) && (ultimoDigito a > maxPar) = aux (resto a) (ultimoDigito a) -- > Pongo el mayor digito par
            | (a < 10) && (esPar a == False) && (maxPar == 0) = -1 -- > Condicion de que si el termino que sobra es impar ya esta lo descarto y verifica que si existe un maxPar > 0 no funciona ya que si hay un número
            | otherwise = aux (resto a) maxPar

-- Ejericio 19
esSumaInicialDePrimos :: Int -> Bool -- > Tambien hay otro ejemplo en la clase del 21/04/2025 (mia)
esSumaInicialDePrimos n = aux n 0 2 -- > Empieza con 2 pq es el primer primo
    where 
        aux n suma actual 
            | suma == n = True
            | suma > n = False 
            | esPrimo actual = aux n (suma + actual) (actual+1)
            | otherwise = aux n suma (actual +1)

-- Ejericicio 20
tomaValorMax:: Int -> Int -> Int
tomaValorMax n1 n2 = buscarMax n2 0 n1 0 -- > El valorActual = n1 ya que es el primer valro que tiene la función

buscarMax:: Int -> Int -> Int -> Int -> Int
buscarMax hasta mejorSuma valorActual mejorValor
    | valorActual > hasta = mejorValor -- > Da el mejor valor encontrado, es > pq tambien hay que verificar con el caso de que valorActual == hasta
    | (division) > mejorSuma = buscarMax hasta (division) (valorActual +1) valorActual-- > Se aumneto el mejor suma y aumento el valor actual
    | otherwise = buscarMax hasta mejorSuma (valorActual +1) mejorValor -- > Solo aumenta el valor actual
    where 
        division = (sumaDivisores valorActual 1)

sumaDivisores:: Int -> Int -> Int
sumaDivisores n x
    | n < x = 0 
    | mod n x == 0 = x + sumaDivisores n (x+1)
    | otherwise = sumaDivisores n (x+1)

-- Ejercicio 21
pitagoras :: Int -> Int -> Int -> Int
pitagoras m n r = buscarPares_p 0 m 0 n r 

buscarPares_p :: Int -> Int -> Int -> Int -> Int -> Int 
buscarPares_p actual_m hasta_m actual_n hasta_n r
    | p > hasta_m = 0
    | otherwise = (buscarPares_q p actual_n hasta_n r) + (buscarPares_p (p + 1) hasta_m 0 hasta_n r)
    where 
        p = actual_m
        q = actual_n

buscarPares_q :: Int -> Int -> Int -> Int -> Int
buscarPares_q actual_m actual_n hasta_n r  
    | q > hasta_n = 0
    | (p^2 + q^2) <= r^2 = 1 + (buscarPares_q p (q + 1) hasta_n r)  
    | otherwise = buscarPares_q p (q + 1) hasta_n r 
    where 
        q = actual_n
        p = actual_m 














        
-- ==> VERIFICAR EJERCICIO
iesimoDigito :: Int -> Int -> Int
iesimoDigito n i = mod (div n 10^((cantDigitos n) -i)) 10 -- ==> es una formula cerrada

iesimoDigito_2 :: Int -> Int -> Int -- ==> Realizada con recu
iesimoDigito_2 n i 
    | cantDigitos n == i = mod n 10 
    | otherwise = iesimoDigito_2 (div n 10) i





