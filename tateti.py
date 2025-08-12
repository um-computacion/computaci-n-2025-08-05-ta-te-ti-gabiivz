
from tablero import Tablero

class Tateti:
    def __init__(self, nombre1="Jugador 1", nombre2="Jugador 2"):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.turno = "X"
        self.tablero = Tablero()

    def obtener_nombre_actual(self):
        if self.turno == "X":
            return self.nombre1
        else:
            return self.nombre2

    def ocupar_una_de_las_casillas(self, fil, col):
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.turno)
        # condicion para ganar
        # cambia turno... va a suceder solo si se pudo poner la ficha

        if self.turno == "X":
            self.turno = "0"
        else:
            self.turno = "X"
        
     
    def verificar_ganador(self, fil, col)  :
        # verificar si hay un ganador
        return self.tablero.ganar_juego(self.turno, fil, col)
    
        
    
    