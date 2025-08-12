import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):
    
    def test_inicializacion(self):
        jugador = Jugador("Juan", "X")
        self.assertEqual(jugador.nombre, "Juan")
        self.assertEqual(jugador.ficha, "X")
    
    def test_set_nombre(self):
        jugador = Jugador("Juan", "X")
        jugador.set_nombre("Carlos")
        self.assertEqual(jugador.nombre, "Carlos")
    
    def test_set_ficha(self):
        jugador = Jugador("Juan", "X")
        jugador.set_ficha("O")
        self.assertEqual(jugador.ficha, "O")

if __name__ == '__main__':
    unittest.main()