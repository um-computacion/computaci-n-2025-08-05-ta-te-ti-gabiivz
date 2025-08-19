from tablero import Tablero

class Jugador:
    def __init__(self, nombre1="Jugador 1", nombre2="Jugador 2"):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def get_nombre1(self):
        return self.nombre1
    
    def get_nombre2(self):
        return self.nombre2
    
    def set_nombre1(self, nombre):
        self.nombre1 = nombre
    
    def set_nombre2(self, nombre):
        self.nombre2 = nombre

    