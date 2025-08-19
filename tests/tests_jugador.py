import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):
    
    def test_inicializacion(self):
        jugador = Jugador()
        self.assertEqual(jugador.nombre1, "Jugador 1")
        self.assertEqual(jugador.nombre2, "Jugador 2")
    
    def test_inicializacion_con_nombres(self):
        jugador = Jugador("Ana", "Luis")
        self.assertEqual(jugador.nombre1, "Ana")
        self.assertEqual(jugador.nombre2, "Luis")
    
    def test_get_nombre1(self):
        jugador = Jugador("Ana", "Luis")
        self.assertEqual(jugador.get_nombre1(), "Ana")
    
    def test_get_nombre2(self):
        jugador = Jugador("Ana", "Luis")
        self.assertEqual(jugador.get_nombre2(), "Luis")
    
    def test_set_nombre1(self):
        jugador = Jugador()
        jugador.set_nombre1("Carlos")
        self.assertEqual(jugador.get_nombre1(), "Carlos")
    
    def test_set_nombre2(self):
        jugador = Jugador()
        jugador.set_nombre2("María")
        self.assertEqual(jugador.get_nombre2(), "María")


if __name__ == '__main__':
    unittest.main()