from tateti import Tateti

def main():
    print("Bienvenidos al Tateti")

    nombre1 = input("Nombre del Jugador 1 (X): ")
    nombre2 = input("Nombre del Jugador 2 (0): ")
    juego = Tateti(nombre1, nombre2)  
    
    while True:
        print("Tablero: ")
        print(juego.tablero.contenedor)
        print("Turno: ")
        print(f"{juego.obtener_nombre_actual()} ({juego.turno})")


        try:
            fil = int(input("Ingrese fila(de 0 a 2): "))
            col = int(input("Ingrese columna(de 0 a 2): " ))
        
            jugador_actual = juego.turno
            nombre_actual = juego.obtener_nombre_actual()
            juego.ocupar_una_de_las_casillas(fil, col)
            
            if juego.tablero.ganar_juego(jugador_actual, fil, col):
                print(f"El jugador {nombre_actual} ha ganado!")
                break
                    
            if juego.tablero.tablero_lleno():
                print("El tablero está lleno, es un empate!")
                break
        except Exception as e:
            print(e)



        


if __name__ == '__main__':
    main()
