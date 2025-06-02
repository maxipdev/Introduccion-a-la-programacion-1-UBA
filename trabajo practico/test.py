import unittest
from funcionesMaxi import *

# cosas generales:
BOMBA = chr(128163)  # simbolo de una mina
BANDERA = chr(128681)  # simbolo de bandera blanca
VACIO = chr(9733)  # simbolo vacio inicial

class descubrir_celdaTest(unittest.TestCase): 
    # en caso de que haya una bomba
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
            "juego-terminado": False,
            "tablero": tablero,
            "tablero-visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 0
        columna_a_evaluar: int = 1
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)

        # testo que se muestre la bomba
        self.assertEqual(estado["tablero-visible"][0][1], BOMBA)

        # testeo que se termine el juego
        self.assertTrue(estado["juego-terminado"])

        #testeo que toda quede igual que antes, es decir que el resto quede igual
        tablero_visible: list[list[int]] = estado["tablero-visible"]
        for fila in range(estado["filas"]): 
            for columna in range(estado["columnas"]): 
                # pregunto que el tablero[i][j] sea != al que se esta evaluando, pq se sabe que esa posicion tuvo que cambiar
                if (fila, columna) != (fila_a_evaluar, columna_a_evaluar): 
                    # se pone vacia pq se supone que para este ejemplo no se hizo mas cambios, o sea que perdio a la primera
                    self.assertEqual(tablero_visible[fila][columna], VACIO)

    # en caso de que sea un solo valor el que hay que mostrar
    def test_hay_un_solo_valor(self): 
        tablero = [
            [1, -1,  1,  0],
            [1,  1,  1,  0],
            [1,  1,  2,  1],
            [1, -1,  2, -1],
        ]

        tablero_visible = [
            [1,  VACIO,  VACIO,  0],
            [VACIO,  VACIO,  VACIO,  VACIO],
            [VACIO,  1,  VACIO,  VACIO],
            [VACIO,  VACIO,  2,  VACIO],
        ]

        estado: EstadoJuego = {
            "filas": 4, 
            "columnas": 4,
            "minas": 3,
            "juego-terminado": False,
            "tablero": tablero,
            "tablero-visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 1
        columna_a_evaluar: int = 1
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        
        #Verufico que las cosas siguen igual
        self.assertEqual(estado['filas'], 4)
        self.assertEqual(estado['columnas'], 4)
        self.assertFalse(estado['juego-terminado'])
        self.assertEqual(estado['tablero-visible'], [
            [1,  VACIO,  VACIO,  0],
            [VACIO,  1,  VACIO,  VACIO],
            [VACIO,  1,  VACIO,  VACIO],
            [VACIO,  VACIO,  2,  VACIO],
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
            "minas": 3,
            "juego-terminado": False,
            "tablero": tablero,
            "tablero-visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 1
        columna_a_evaluar: int = 3
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 3)
        self.assertEqual(estado['columnas'], 4)
        self.assertFalse(estado['juego-terminado'])
        self.assertEqual(estado['tablero-visible'], [
            [VACIO,  VACIO,  1,  0],
            [VACIO,  VACIO,  1,  0],
            [VACIO,  VACIO,  2,  1],
        ])

    # en caso de que haya que mostrar los adyacentes de los adyacentes
    def test_multiples_adyacentes(self): 
        tablero = [
            [1, -1,  1,  5, 5],
            [1,  1,  1,  5, 5],
            [7,  1,  4,  0, 5],
            [1,  1,  0,  1, 5],
            [1,  1,  2,  1, 5],
        ]

        tablero_visible = [
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO],
            [7,      VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO]
        ]

        estado: EstadoJuego = {
            "filas": 5, 
            "columnas": 5,
            "minas": 1,
            "juego-terminado": False,
            "tablero": tablero,
            "tablero-visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 3
        columna_a_evaluar: int = 2
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 5)
        self.assertEqual(estado['columnas'], 5)
        self.assertFalse(estado['juego-terminado'])
        self.assertEqual(estado['tablero-visible'], [
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  1,      5,     5    ],
            [7,      1,      4,      0,     5    ],
            [VACIO,  1,      0,      1,     5    ],
            [VACIO,  1,      2,      1,     VACIO],
        ])

    # en caso de que haya banderas en las posiciones adyacentes -> No las tiene que mostar
    def test_hay_banderas_en_adyacentes(self): 
        tablero = [
            [1, -1,  1,  5, 5],
            [1,  1,  1,  5, 5],
            [7,  1,  4,  0, 5],
            [1,  1,  0,  1, 5],
            [1,  1,  2,  1, 5],
        ]

        tablero_visible = [
            [BANDERA,  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  BANDERA,  VACIO, VACIO],
            [7,      VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  VACIO,  BANDERA, VACIO],
            [VACIO,  VACIO,  VACIO,  VACIO, VACIO]
        ]

        estado: EstadoJuego = {
            "filas": 5, 
            "columnas": 5,
            "minas": 1,
            "juego-terminado": False,
            "tablero": tablero,
            "tablero-visible": tablero_visible
        }

        # Ejecuto la accion: 
        fila_a_evaluar: int = 3
        columna_a_evaluar: int = 2
        descubrir_celda(estado, fila_a_evaluar, columna_a_evaluar)
        self.assertEqual(estado['filas'], 5)
        self.assertEqual(estado['columnas'], 5)
        self.assertFalse(estado['juego-terminado'])
        self.assertEqual(estado['tablero-visible'], [
            [BANDERA,  VACIO,  VACIO,  VACIO, VACIO],
            [VACIO,  VACIO,  BANDERA,      5,     5],
            [7,      1,      4,      0,     5      ],
            [VACIO,  1,      0,    BANDERA,     5  ],
            [VACIO,  1,      2,      1,     VACIO],
        ])



if __name__ == '__main__':
    unittest.main(verbosity=2)