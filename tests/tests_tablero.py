
import unittest
from tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_tablero_vacio_al_inicio(self):
        for i in range(3):
            for j in range(3):
                self.assertEqual(self.tablero.contenedor[i][j], "")
    
    def test_poner_ficha(self):
        self.tablero.poner_la_ficha(1, 1, "X")
        self.assertEqual(self.tablero.contenedor[1][1], "X")
    
    def test_posicion_ocupada(self):
        self.tablero.poner_la_ficha(1, 1, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, "O")
    
    def test_ganador_fila_horizontal(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.poner_la_ficha(0, 1, "X")
        self.tablero.poner_la_ficha(0, 2, "X")
        
        self.assertTrue(self.tablero.ganar_juego("X", 0, 2))
    
    def test_ganador_columna_vertical(self):
        self.tablero.poner_la_ficha(0, 0, "O")
        self.tablero.poner_la_ficha(1, 0, "O")
        self.tablero.poner_la_ficha(2, 0, "O")
        
        self.assertTrue(self.tablero.ganar_juego("O", 2, 0))
        
    
    def test_ganador_diagonal_principal(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.poner_la_ficha(1, 1, "X")  
        self.tablero.poner_la_ficha(2, 2, "X")

        self.assertTrue(self.tablero.ganar_juego("X", 2, 2))
        

    def test_ganador_diagonal_secundaria(self):
        self.tablero.poner_la_ficha(0, 2, "X")
        self.tablero.poner_la_ficha(1, 1, "X")
        self.tablero.poner_la_ficha(2, 0, "X")
        
        self.assertTrue(self.tablero.ganar_juego("X", 2, 0))
    
    def test_no_hay_ganador(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.poner_la_ficha(0, 1, "X")
        self.tablero.poner_la_ficha(0, 2, "O")  
        
        self.assertFalse(self.tablero.ganar_juego("X", 0, 1))
    
    def test_tablero_lleno(self):
        fichas = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        contador = 0
        for i in range(3):
            for j in range(3):
                self.tablero.poner_la_ficha(i, j, fichas[contador])
                contador += 1
        
        self.assertTrue(self.tablero.tablero_lleno())
    

if __name__ == '__main__':
    unittest.main()