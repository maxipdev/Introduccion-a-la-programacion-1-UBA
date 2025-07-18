import unittest
from buscaminas import *


'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

# Ejercicio 1
class colocar_minasTest(unittest.TestCase):
    def test_dimensiones_correctas(self): 
        filas = 3
        columnas = 3
        minas = 1
        tablero = colocar_minas(filas, columnas, minas)

       
        self.assertEqual(len(tablero), filas)
      
        cantidad_col= len(tablero[0])

        for i in tablero: 
            self.assertEqual(len(i), cantidad_col)

        # controlo que haya la caantidad pedida de bombas: 
        cant_bombas = 0
        for i in range(len(tablero)): 
            for j in range(len(tablero[0])):
                if tablero[i][j] == -1: 
                    cant_bombas += 1
        self.assertEqual(cant_bombas, minas) 

    def test_grande(self):
        filasG = 8
        columnasG = 9
        minasG = 6
        tableroG = colocar_minas(filasG, columnasG, minasG)

        # controlo que tengan la longitud pedidda:
        self.assertEqual(len(tableroG), filasG)
        
        cantidad_columnas = len(tableroG[0])
        for i in tableroG: 
            self.assertEqual(len(i), cantidad_columnas)

        # controlo que haya la caantidad pedida de bombas: 
        cant_bombas = 0
        for i in range(len(tableroG)): 
            for j in range(len(tableroG[0])):
                if tableroG[i][j] == -1: 
                    cant_bombas += 1
        self.assertEqual(cant_bombas, minasG) 

    def test_sin_minas(self):
        filas1 = 4
        columnas1 = 4 
        minas1 = 0 
        tablero1 = colocar_minas(filas1,columnas1,minas1)

        # controlo que haya 0 bombas
        cant_bombas = 0
        for i in range(len(tablero1)): 
            for j in range(len(tablero1[0])):
                if tablero1[i][j] == -1: 
                    cant_bombas += 1
        self.assertEqual(cant_bombas, minas1) 
 
    def test_tablero_lleno_de_minas(self) :
        filas2 = 2
        columnas2 = 2
        minas2 = 4 
        tablero2 = colocar_minas(filas2,columnas2,minas2)

        # todos tienen q ser minas 
        tablero_minado = True 
        for i in range(len(tablero2)): 
            for j in range(len(tablero2[0])):
                if tablero2[i][j] != -1: 
                    tablero_minado = False
            
        self.assertTrue(tablero_minado) 
 


# Ejercicio 2
class calcular_numerosTest(unittest.TestCase):
    def test_verifico_adyacentes(self): 
        tablero1 = [
            [0,0,0],
            [0,0,0],
            [0,-1,0],
            [0,0,0],
        ]

        tablero2 = [
            [-1,0,0],
            [0,0,0],
            [0,-1,0],
        ]

        calcular_numeros(tablero1)

        self.assertEqual(tablero1, [
             [0,0,0],
             [1,1,1],
             [1,-1,1],
             [1,1,1],
         ])

        calcular_numeros(tablero2)

        self.assertEqual(tablero2, [
            [-1,1,0],
            [2,2,1],
            [1,-1,1],
        ])

    def test_ninguna_mina_adyacente(self):
        tablero3 = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        calcular_numeros(tablero3)

        self.assertEqual(tablero3, [
             [0,0,0],
             [0,0,0],
             [0,0,0],
             [0,0,0],
         ])


    def test_todas_adyacentes(self):
        tablero4 = [
            [-1,-1,-1],
            [-1,0,-1],
            [-1,-1,-1],
        ]

        calcular_numeros(tablero4)

        self.assertEqual(tablero4, [
            [-1,-1,-1],
            [-1,8,-1],
            [-1,-1,-1],
         ])


# Ejercicio 3
class crear_juegoTest(unittest.TestCase):
    def test_juego (self):
        estado = crear_juego(3,4,2)

        #verifico valores
        self.assertEqual(estado['filas'], 3)
        self.assertEqual(estado['columnas'], 4)
        self.assertEqual(estado['minas'], 2)
        self.assertFalse(estado['juego_terminado'])


    def test_tablero_visible_vacio(self):
        estado1 = crear_juego(2,3,2)

        # chequeo que el tablero_visible este lleno de VACIO .

        tablero_test = estado1['tablero_visible'] 

        tablero_vacio = True 

        for i in range(len(tablero_test)):
            for j in range(len(tablero_test[0])):
                if tablero_test[i][j] != VACIO:
                    tablero_vacio = False
        
        self.assertTrue(tablero_vacio) 


    def test_cantidad_correcta_minas_tablero(self):
        estado2 = crear_juego(2,2,2)
        tablero_minas = estado2['tablero']
        contador_minas_tablero = 0

        for i in range(len(tablero_minas)):
            for j in range(len(tablero_minas[0])):
                if tablero_minas[i][j] == -1:
                    contador_minas_tablero += 1
        
        self.assertEqual(contador_minas_tablero,2)

    def test_dimensiones_correctas_tableros(self):
        filas3 = 3 
        columnas3 = 4
        minas3 = 4

        juego = crear_juego(filas3,columnas3,minas3)

        tablero_visible3 = juego['tablero_visible']
        tablero3 = juego['tablero']

        filas_tablero_visible3 = len(tablero_visible3)
        filas_tablero3 = len(tablero3)

        columnas_tablero_visible3 = len(tablero_visible3[0])
        columnas_tablero3 = len(tablero3[0])

        self.assertEqual(filas_tablero_visible3,filas3)
        self.assertEqual(filas_tablero3,filas3)

        self.assertEqual(columnas_tablero_visible3,columnas3)
        self.assertEqual(columnas_tablero3,columnas3) 

    def test_numeros_bien_calculados(self):
        filas5 = 3
        columnas5= 3
        minas5 = 1

        juego2 = crear_juego(filas5,columnas5,minas5)

        tablero5 = juego2['tablero']

        # como hay 1 mina, deberia haber calculado algunas celdas con 1, que son las que van a tener la unica mina adyacente a ellas 
        # como maximo van a haber 8 celdas = 1 y minimo 
        contador_minas = 0
        contador_unos = 0
        cantidad_otros_valores = 0

        for i in range(len(tablero5)):
            for j in range(len(tablero5[0])):
                if tablero5[i][j] == -1 : 
                    contador_minas += 1
                
                elif tablero5[i][j] == 1:
                    contador_unos += 1 

        self.assertEqual(contador_minas,1)
        self.assertIn(contador_unos,[3,5,8])
       
# Ejercicio 4
class obtener_estado_tablero_visibleTest(unittest.TestCase):
    def test_copia_tablero_visible(self):
        estado = { 'filas' : 3,
                   'columnas' : 3,
                   'minas' : 1,
                   'tablero' : [[1,-1,1],[1,1,1],[0,0,0]],
                   'tablero_visible' : [['1',VACIO,VACIO],['1',VACIO,VACIO],[VACIO,VACIO,'0']],
                   'juego_terminado' : False 
        }
        
        res = obtener_estado_tablero_visible(estado)

        self.assertEqual(res, [['1',VACIO,VACIO],['1',VACIO,VACIO],[VACIO,VACIO,'0']])


# Ejercicio 5
class marcar_celdaTest(unittest.TestCase):
    # Este es el caso de que haya un numero ahi --> No tendria que hacer nada
    def test_valor_completo(self): 
        estado = {
            "filas": 2,
            "columnas": 2,
            "minas": 1,
            "juego_terminado": False,
            "tablero": [
                [1, -1],
                [1, 1]
            ],
            "tablero_visible": [
                ["1", VACIO],
                [VACIO, VACIO]
            ]
        }

        # Ejecuto la funcion: 
        marcar_celda(estado, 0, 0)

        # Verifico valores: 
        #tienen que quedar igual: 
        self.assertFalse(estado["juego_terminado"])
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado["tablero_visible"], [
                ["1", VACIO],
                [VACIO, VACIO]
        ])

    def test_pongo_una_bandera(self):
        estado = {
            "filas": 2,
            "columnas": 2,
            "minas": 1,
            "juego_terminado": False,
            "tablero": [
                [1, -1],
                [1, 1]
            ],
            "tablero_visible": [
                ["1", VACIO],
                [VACIO, VACIO]
            ]
        }

        # Ejecuto la funcion: 
        marcar_celda(estado, 1, 0)

        # Verifico valores: 
        #tienen que quedar igual: 
        self.assertFalse(estado["juego_terminado"])
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado["tablero_visible"], [
            ["1", VACIO],
            [BANDERA, VACIO]
        ])

    def test_saco_una_bandera(self): 
        estado = {
            "filas": 2,
            "columnas": 2,
            "minas": 1,
            "juego_terminado": False,
            "tablero": [
                [1, -1],
                [1, 1]
            ],
            "tablero_visible": [
                ["1", VACIO],
                [BANDERA, VACIO]
            ]
        }

        # Ejecuto la funcion: 
        marcar_celda(estado, 1, 0)

        # Verifico valores: 
        #tienen que quedar igual: 
        self.assertFalse(estado["juego_terminado"])
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado["tablero_visible"], [
            ["1", VACIO],
            [VACIO, VACIO]
        ])


# Ejercicio 6
class descubrir_celdaTest(unittest.TestCase): 
    # en caso de que haya una bomba en la primera celda tocada
    def test_hay_bomba(self): 
        tablero = [
            [1, -1,  1,  0],
            [1,  1,  1,  0],
            [1,  1,  2,  1],
            [1, -1,  2, -1],
        ]

        tablero_visible = [
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO],
        ]

        estado: EstadoJuego = {
            "filas": 4, 
            "columnas": 4,
            "minas": 3,
            "juego_terminado": False,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 0
        columna_a_evaluar: int = 1
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)

        # testo que se muestre la bomba
        self.assertEqual(estado["tablero_visible"][0][1], BOMBA)

        # testeo que se termine el juego
        self.assertTrue(estado["juego_terminado"])
        self.assertEqual(estado['filas'], 4)
        self.assertEqual(estado['columnas'], 4)
        self.assertTrue(estado['juego_terminado'])

        #testeo que toda quede igual que antes, es decir que el resto quede igual
        self.assertEqual(estado['tablero_visible'], [
            [VACIO,  BOMBA,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  BOMBA,  VACIO,  BOMBA],
        ])

    # en caso de que sea un solo valor el que hay que mostrar
    def test_hay_un_solo_valor(self): 
        tablero = [
            [1, -1,  1,  0],
            [1,  1,  1,  0],
            [1,  1,  2,  1],
            [1, -1,  2, -1],
        ]

        tablero_visible = [
            ["1",  VACIO,  VACIO,  "0"],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  "1",  VACIO,  VACIO],
            [VACIO,  VACIO,  "2",  VACIO],
        ]

        estado: EstadoJuego = {
            "filas": 4, 
            "columnas": 4,
            "minas": 3,
            "juego_terminado": False,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 1
        columna_a_evaluar: int = 1
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        
        #Verufico que las cosas siguen igual
        self.assertEqual(estado['filas'], 4)
        self.assertEqual(estado['columnas'], 4)
        self.assertFalse(estado['juego_terminado'])
        self.assertEqual(estado['tablero_visible'], [
            ["1",  VACIO,  VACIO,  "0"],
            [VACIO,  "1",  VACIO,  VACIO],
            [VACIO,  "1",  VACIO,  VACIO],
            [VACIO,  VACIO,  "2",  VACIO],
        ])

    # en caso de que haya que mostrar sus adyacentes
    def test_mostrar_adyacentes(self): 
        tablero = [
            [1, -1,  1,  0],
            [1,  1,  1,  0],
            [1,  1,  2,  1]
        ]

        tablero_visible = [
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO]
        ]

        estado: EstadoJuego = {
            "filas": 3, 
            "columnas": 4,
            "minas": 1,
            "juego_terminado": False,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 1
        columna_a_evaluar: int = 3
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 3)
        self.assertEqual(estado['columnas'], 4)
        self.assertFalse(estado['juego_terminado'])
        self.assertEqual(estado['tablero_visible'], [
            [VACIO,  VACIO,  "1",  "0"],
            [VACIO,  VACIO,  "1",  "0"],
            [VACIO,  VACIO,  "2",  "1"],
        ])

    # en caso de que haya que mostrar los adyacentes de los adyacentes
    def test_multiples_adyacentes(self): 
        tablero = [
            [1, -1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],

        ]

        tablero_visible = [
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO],
            ["1",  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,      VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO]
        ]

        estado: EstadoJuego = {
            "filas": 5, 
            "columnas": 5,
            "minas": 1,
            "juego_terminado": False,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 3
        columna_a_evaluar: int = 2
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 5)
        self.assertEqual(estado['columnas'], 5)
        self.assertFalse(estado['juego_terminado'])
        self.assertEqual(estado['tablero_visible'], [
            [VACIO, VACIO, "1", "0", "0"],
            ["1",   "1",   "1", "0", "0"],
            ["0",   "0",   "0", "0", "0"],
            ["0",   "0",   "0", "0", "0"],
            ["0",   "0",   "0", "0", "0"]
        ])

    # en caso de que haya banderas en las posiciones adyacentes -> No las tiene que mostar
    def test_hay_banderas_en_adyacentes(self): 
        tablero = [
            [1, -1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        tablero_visible = [
            [BANDERA,  VACIO,  VACIO,  VACIO, VACIO],
            ["1",  VACIO,  BANDERA,  VACIO, VACIO],
            [VACIO,      VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  BANDERA, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO]
        ]

        estado: EstadoJuego = {
            "filas": 5, 
            "columnas": 5,
            "minas": 1,
            "juego_terminado": False,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 3
        columna_a_evaluar: int = 2
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 5)
        self.assertEqual(estado['columnas'], 5)
        self.assertFalse(estado['juego_terminado'])
        self.assertEqual(estado['tablero_visible'], [
            [BANDERA, VACIO, "1", "0", "0"],
            ["1",     "1",   BANDERA, "0", "0"],
            ["0",     "0",   "0",      "0", "0"],
            ["0",     "0",   "0",      BANDERA, "0"],
            ["0",     "0",   "0",      "0", "0"]
        ])

    # en caso de que el juego este terminado
    def test_juego_terminado(self): 
        tablero = [
            [1, -1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        tablero_visible = [
            ['1', VACIO, '1', '0', '0'],
            ['1', '1', '1', '0', '0'],
            ['7', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0']

        ]

        estado: EstadoJuego = {
            "filas": 5, 
            "columnas": 5,
            "minas": 1,
            "juego_terminado": True,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        fila_a_evaluar: int = 3
        columna_a_evaluar: int = 2
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 5)
        self.assertEqual(estado['columnas'], 5)
        self.assertTrue(estado['juego_terminado'])
        self.assertEqual(estado['tablero_visible'], [
            ['1', VACIO, '1', '0', '0'],
            ['1', '1', '1', '0', '0'],
            ['7', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ])

    # en caso de que al usuariole falte un valor, lo toca y gana: 
    def test_gana_al_descubrir_la_ultima(self): 
        estado = {
            "filas": 2,
            "columnas": 2,
            "minas": 1,
            "juego_terminado": False,
            "tablero": [
                [1, -1],
                [1, 1]
            ],
            "tablero_visible": [
                ["1", VACIO],
                ["1", VACIO]
            ]
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 1
        columna_a_evaluar: int = 1
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)

        #Verifico que las cosas siguen igual
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)

        # Cosas que cambian: 
        self.assertTrue(estado['juego_terminado'])
        self.assertEqual(estado["tablero_visible"], [
                ["1", VACIO],
                ["1", "1"]
        ])


# Ejercicio 7
class verificar_victoriaTest(unittest.TestCase):
    def test_todas_las_celdas_seguras_descubiertas(self): 
        tablero = [
            [1, -1,  1,  0],
            [1,  1,  1,  0],
            [1,  1,  2,  1],
            [1, -1,  2, -1],
        ]

        tablero_visible = [
            ["1",  VACIO,  "1",  "0"],
            ["1",  "1",  "1",  "0"],
            ["1",  "1",  "2",  "1"],
            ["1",  VACIO,  "2",  VACIO],
        ]

        estado: EstadoJuego = {
            "filas": 4, 
            "columnas": 4,
            "minas": 3,
            "juego_terminado": True,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la funcion: y verifco que de verdadero
        self.assertTrue(verificar_victoria(estado))

    # caso de que no esten todas descubiertas: 
    def test_hay_celdas_vacias(self):
        tablero = [
            [1, -1,  1,  0],
            [1,  1,  1,  0],
            [1,  1,  2,  1],
            [1, -1,  2, -1],
        ]

        tablero_visible = [
            ["1",  VACIO,  "1",  "0"],
            ["1",  VACIO,  "1",  "0"],
            ["1",  "1",  "2",  "1"],
            ["1",  VACIO,  "2",  VACIO],
        ]

        estado: EstadoJuego = {
            "filas": 4, 
            "columnas": 4,
            "minas": 3,
            "juego_terminado": False,
            "tablero": tablero,
            "tablero_visible": tablero_visible
        }

        # Ejecuto la funcion: y verifco que de false
        self.assertFalse(verificar_victoria(estado))


# Ejercicio 8
def leer_archivo(nombre: str) -> str:
    archivo = open(os.path.join("./", nombre), "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def escribir_archivo(nombre: str, contenido: str): 
        archivo = open(os.path.join("./", nombre), "w")
        archivo.write(contenido)
        archivo.close()
        return


class reiniciar_juego_test(unittest.TestCase):

    def test_reiniciar_partida_perdida(self):
        estado = {
            'tablero': [[1, 1, 1], [1, -1, 1],[1, 1, 1]],
            'tablero_visible': [[VACIO, VACIO, '1'], [VACIO, BOMBA, VACIO],['1', VACIO, VACIO]],
            'filas': 3,
            'columnas': 3,
            'minas': 1,
            'juego_terminado': True
        }
        tablero_previo: list[list[int]] = estado['tablero']
        reiniciar_juego(estado)

        self.assertNotEqual(estado["tablero"], tablero_previo, "test_reiniciar_partida_perdida(tablero)")
        self.assertEqual(estado['tablero_visible'], [[VACIO, VACIO, VACIO], [VACIO, VACIO, VACIO],[VACIO, VACIO, VACIO]], "test_reiniciar_partida_perdida(visible)") 
        self.assertFalse(estado['juego_terminado'], "test_reiniciar_partida_perdida(juego_terminado)")
        self.assertEqual(estado['filas'], 3, "test_reiniciar_partida_perdida(filas)")
        self.assertEqual(estado['columnas'], 3, "test_reiniciar_partida_perdida(columnas)")
        self.assertEqual(estado['minas'], 1, "test_reiniciar_partida_perdida(minas)")

    def test_reiniciar_partida_en_curso(self):
        estado = {
            'tablero': [[-1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, -1], [0, 0, 1, 1]],
            'tablero_visible': [[BANDERA, '1', VACIO, VACIO], ['1', '1', VACIO, VACIO],[VACIO, VACIO, '1', VACIO],[VACIO, VACIO, VACIO, '1']],
            'filas': 4,
            'columnas': 4,
            'minas': 2,
            'juego_terminado': False
        }
        tablero_previo: list[list[int]] = estado['tablero']
        reiniciar_juego(estado)

        self.assertNotEqual(estado["tablero"], tablero_previo, "test_reiniciar_partida_perdida(tablero)")
        self.assertEqual(estado['tablero_visible'], [[VACIO, VACIO, VACIO, VACIO], [VACIO, VACIO, VACIO, VACIO],[VACIO, VACIO, VACIO, VACIO],[VACIO, VACIO, VACIO, VACIO]], "test_reiniciar_partida_perdida(visible)")
        self.assertFalse(estado['juego_terminado'], "test_reiniciar_partida_en_curso(juego_terminado)")
        self.assertEqual(estado['filas'], 4, "test_reiniciar_partida_en_curso(filas)")
        self.assertEqual(estado['columnas'], 4, "test_reiniciar_partida_en_curso(columnas)")
        self.assertEqual(estado['minas'], 2, "test_reiniciar_partida_en_curso(minas)")


# Ejercicio 9
class guardar_estado_test(unittest.TestCase):

    def test_guardar_estado_basico(self):
        estado = {
            'tablero': [[-1, 1], [1, 1]],
            'tablero_visible': [[BANDERA, '1'], [VACIO, VACIO]],
            'filas': 2,
            'columnas': 2,
            'minas': 1,
            'juego_terminado': False
        }

        guardar_estado(estado, "./")

        contenido_tablero = leer_archivo("tablero.txt")
        contenido_visible = leer_archivo("tablero_visible.txt")

        self.assertEqual(contenido_tablero, "-1,1\n1,1\n", "test_guardar_estado_basico(tablero)")
        self.assertEqual(contenido_visible, "*,1\n?,?\n", "test_guardar_estado_basico(visible)")

    def test_guardar_estado_completo_diferente(self):
        estado = {
            'tablero': [[0, 1, -1], [0, 1, 1]],
            'tablero_visible': [[VACIO, '1', BANDERA], [VACIO, VACIO, VACIO]],
            'filas': 2,
            'columnas': 3,
            'minas': 1,
            'juego_terminado': False
        }

        guardar_estado(estado, "./")

        contenido_tablero = leer_archivo("tablero.txt")
        contenido_visible = leer_archivo("tablero_visible.txt")

        self.assertEqual(contenido_tablero, "0,1,-1\n0,1,1\n", "test_guardar_estado_completo_diferente(tablero)")
        self.assertEqual(contenido_visible, "?,1,*\n?,?,?\n", "test_guardar_estado_completo_diferente(visible)")


# Ejercicio 10
class cargar_estado_test(unittest.TestCase):
    """Para que el test de archivos inexistentes funcione no tiene que haber ningún tablero.txt ni tablero_visible.txt en la carpeta.
    En caso de que existan dichos archivos por favor eliminelos y luego podrá ejecutar sin ningún problema el test"""
    
    def test_archivos_inexistentes(self):
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_archivos_inexistentes")

    def test_un_archivo_faltante(self):
        escribir_archivo("tablero.txt", "-1,1\n1,1\n")
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_un_archivo_faltante")

    def test_lineas_diferentes(self):
        escribir_archivo("tablero.txt", "-1,1\n")
        escribir_archivo("tablero_visible.txt", "*,1\n?,?\n")
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_lineas_diferentes")

    def test_comas_diferentes(self):
        escribir_archivo("tablero.txt", "-1,1\n1,1\n")
        escribir_archivo("tablero_visible.txt", "*,1\n1,1,1\n")
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_comas_diferentes")

    def test_sin_minas(self):
        escribir_archivo("tablero.txt", "1,1\n1,1\n")
        escribir_archivo("tablero_visible.txt", "1,1\n1,1\n")
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_sin_minas")

    def test_valores_invalidos_tablero(self):
        escribir_archivo("tablero.txt", "-1,2\n1,1\n")  # 2 no válido si no hay 2 minas alrededor
        escribir_archivo("tablero_visible.txt", "*,2\n1,1\n")
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_valores_invalidos_tablero")

    def test_visible_invalido(self):
        escribir_archivo("tablero.txt", "-1,1\n1,1\n")
        escribir_archivo("tablero_visible.txt", "*,X\n1,1\n")
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_visible_invalido")

    def test_visible_no_coincide(self):
        escribir_archivo("tablero.txt", "-1,1\n1,1\n")
        escribir_archivo("tablero_visible.txt", "*,2\n1,1\n")  # 2 no coincide con tablero
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_visible_no_coincide")

    def test_no_hay_vacio_adyacente(self):
        escribir_archivo("tablero.txt", "0,0,0\n1,1,0\n-1,1,0\n")
        escribir_archivo("tablero_visible.txt", "?,?,?\n1,1,?\n?,1,?\n")  
        estado = {}
        self.assertFalse(cargar_estado(estado, "./"), "test_no_hay_vacio_adyacente")

    def test_estado_valido(self):
        escribir_archivo("tablero.txt", "-1,1\n1,1\n")
        escribir_archivo("tablero_visible.txt", "*,1\n?,?\n")
        estado = {
            'filas': 0,
            'columnas': 0,
            'minas': 0,
            'tablero': [],
            'tablero_visible': [],
            'juego_terminado': True
        }
        self.assertTrue(cargar_estado(estado, "./"), "test_estado_valido")
        self.assertEqual(estado['filas'], 2)
        self.assertEqual(estado['columnas'], 2)
        self.assertEqual(estado['minas'], 1)
        self.assertEqual(estado['tablero'], [[-1, 1], [1, 1]])
        self.assertEqual(estado['tablero_visible'], [[BANDERA, '1'], [VACIO, VACIO]])
        self.assertFalse(estado['juego_terminado'])



"""
- Agregar varios casos de prueba para cada función.
- Se debe cubrir al menos el 95% de las líneas de cada función.
- Se debe cubrir al menos el 95% de ramas de cada función.
"""

if __name__ == '__main__':
    unittest.main(verbosity=2)
