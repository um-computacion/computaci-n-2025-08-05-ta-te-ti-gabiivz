from tablero import Tablero

class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_ficha(self, ficha):
        self.ficha = ficha

    def jugador_ganador(self, fil, col):
        return Tablero.ganar_juego(self.ficha, fil, col)
    