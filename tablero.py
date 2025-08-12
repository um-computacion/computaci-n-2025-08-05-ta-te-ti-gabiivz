class PosOcupadaException(Exception):
    ...

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
        
    def ganar_juego(self, ficha, fil, col):
        for i in range(3):
            if self.contenedor[i][0] == ficha and self.contenedor[i][1] == ficha and self.contenedor[i][2] == ficha:
                return True
            if self.contenedor[0][i] == ficha and self.contenedor[1][i] == ficha and self.contenedor[2][i] == ficha:
                return True
        if self.contenedor[0][0] == ficha and self.contenedor[1][1] == ficha and self.contenedor[2][2] == ficha:
            return True
        if self.contenedor[0][2] == ficha and self.contenedor[1][1] == ficha and self.contenedor[2][0] == ficha:
            return True
        return False
    
    def tablero_lleno(self):
        for fila in self.contenedor:
            if "" in fila:
                return False
        return True