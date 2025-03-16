from utils import *

tablero = crear_tablero()
tablero_1 = crear_tablero()
tablero_2 = crear_tablero()

print("Coloca tu barco de eslora 2")
barco_1 = tu_barco(2)
tablero_1 = colocar_barco(barco_1, tablero_1)

print("Coloca tu barco de eslora 2")
barco_2 = tu_barco(2)
tablero_1 = colocar_barco(barco_2, tablero_1)

print("Coloca tu barco de eslora 2")
barco_3 = tu_barco(2)
tablero_1 = colocar_barco(barco_3, tablero_1)

print("Coloca tu barco de eslora 3")
barco_4 = tu_barco(3)
tablero_1 = colocar_barco(barco_4, tablero_1)

print("Coloca tu barco de eslora 3")
barco_5 = tu_barco(3)
tablero_1 = colocar_barco(barco_5, tablero_1)

print("Coloca tu barco de eslora 4")
barco_6 = tu_barco(4)
tablero_1 = colocar_barco(barco_6, tablero_1)

colocar_barcos_aleatorio(tablero)

print(tablero)

for i in tablero:
    while "O" in i:
        time.sleep(1)
        print("Aúnn hay barcos, dispara!")
        disparar(tablero, tablero_2)
        time.sleep(1)
        print("Te van a disparar")
        disparo_aleatorio(tablero_1)
        print(tablero_2, end = "\n\n")
        print(tablero_1)
    else:
        print("Has ganado")
        break