import unittest
from tateti import Tateti


class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.juego = Tateti()
    
    def test_turno_inicial(self):
        self.assertEqual(self.juego.turno, "X")
    

    def test_cambio_de_turno(self):
        self.assertEqual(self.juego.turno, "X")
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "X")
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno, "0")
    
    def test_ocupar_casilla(self):
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(self.juego.tablero.contenedor[1][1], "X")
    
    def test_verificar_ganador_funciona(self):
        self.juego.tablero.poner_la_ficha(0, 0, "X")
        self.juego.tablero.poner_la_ficha(0, 1, "X")
        self.juego.tablero.poner_la_ficha(0, 2, "X")
        resultado = self.juego.tablero.ganar_juego("X", 0, 2)
        self.assertTrue(resultado)

    def test_verificar_ganador_sin_ganador(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        resultado = self.juego.verificar_ganador(0, 1)
        self.assertFalse(resultado)

    def test_verificar_ganador_con_ganador(self):
        self.juego.tablero.poner_la_ficha(0, 0, "X")
        self.juego.tablero.poner_la_ficha(0, 1, "X") 
        self.juego.tablero.poner_la_ficha(0, 2, "X")

        self.juego.turno = "X"
    
        resultado = self.juego.verificar_ganador(0, 2)
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()