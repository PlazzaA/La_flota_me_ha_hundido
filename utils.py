#!pip install numpy


import numpy as np
import random
import time


def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, '_')


def tu_barco(eslor = 1):
    tus_barcos = []

    coord_x = ""
    coord_y = ""
    posicion = ""

    coord_x = int(input("Introduzca la coordenada x (del 0 al 9) donde quiere que empiece su barco"))
    coord_y = int(input("Introduzca la coordenada y (del 0 al 9) donde quiere que empiece su barco"))
    posicion = input("¿Hacia dónde quiere que mire el barco? (Arriba, Abajo, Derecha o Izquierda)")

    if 0 > coord_x > 10 or 0 > coord_y > 10:
        print("Tus coordenadas están fuera de rango, ingreselas de nuevo")
        return tu_barco(eslor)
     
    if posicion == "Arriba" or posicion == "Abajo" or posicion == "Derecha" or posicion == "Izquierda":
        if posicion == "Arriba":
            if (coord_y - eslor) < 0:
                print("Tu barco se va a salir del tablero, ajustalo")
                return tu_barco(eslor)
            for i in range(eslor):
                if tablero_1[coord_y - i][coord_x] != "_":
                    print("Tu barco no puede ir en esa posición, revisa si las coordenadas deseadas están libres y si el barco cabe enn el tablero")
                    return tu_barco(eslor)
                else:
                    tus_barcos.append((coord_y - i, coord_x))
        elif posicion == "Abajo":
            if (coord_y + eslor) < 0:
                print("Tu barco se va a salir del tablero, ajustalo")
                return tu_barco(eslor)
            for i in range(eslor):
                if tablero_1[coord_y + i][coord_x] != "_":
                    print("Tu barco no puede ir en esa posición, revisa si las coordenadas deseadas están libres y si el barco cabe enn el tablero")
                    return tu_barco(eslor)
                else:
                    tus_barcos.append((coord_y + i, coord_x))
        elif posicion == "Izquierda":
            if (coord_x - eslor) < 0:
                print("Tu barco se va a salir del tablero, ajustalo")
                return tu_barco(eslor)
            for i in range(eslor):
                if tablero_1[coord_y][coord_x - i] != "_":
                    print("Tu barco no puede ir en esa posición, revisa si las coordenadas deseadas están libres y si el barco cabe enn el tablero")
                    return tu_barco(eslor)
                else:
                    tus_barcos.append((coord_y, coord_x - i))
        elif posicion == "Derecha":
            if (coord_x + eslor) > 9:
                print("Tu barco se va a salir del tablero, ajustalo")
                return tu_barco(eslor)
            for i in range(eslor):
                if tablero_1[coord_y][coord_x + i] != "_":
                    print("Tu barco no puede ir en esa posición, revisa si las coordenadas deseadas están libres y si el barco cabe enn el tablero")
                    return tu_barco(eslor)
                else:
                    tus_barcos.append((coord_y, coord_x + i))
    else:
        print("Por favor indica una buena posicion")
        return tu_barco(eslor)

    return tus_barcos


def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


def crear_barco_aleatorio(eslora):
    barco_aleatorio = []

    orientacion =  random.choice(["Horizontal", "Vertical"])


    if orientacion == "Horizontal":
        fila = random.randint(0, 10 - eslora)
        columna = random.randint(0,9)
        for i in range(eslora):
            if tablero[fila + i][columna] == "O" or tablero[fila + i][columna] == "X":
                return crear_barco_aleatorio(eslora)
        for h in range(eslora):
            if tablero[fila + h - 1][columna] == "_":
                barco_aleatorio.append((fila + h, columna))

    if orientacion == "Vertical":
        columna = random.randint(0, 10 - eslora)
        fila = random.randint(0,9)
        for j in range(eslora):
            if tablero[fila][columna + j - 1] == "O" or tablero[fila][columna + j] == "X":
                return crear_barco_aleatorio(eslora)
        for g in range(eslora):
            if tablero[fila][columna + g - 1] == "_":
                barco_aleatorio.append((fila, columna + g))

    return barco_aleatorio


def colocar_barcos_aleatorio(tablero):
    for i in range(3):
        for casilla in crear_barco_aleatorio(2):
            tablero[casilla] = "O"
    for j in range(2):
        for casilla in crear_barco_aleatorio(3):
            tablero[casilla] = "O"
    for casilla in crear_barco_aleatorio(4):
        tablero[casilla] = "O"
    return tablero


def disparar(tablero, tablero_2):
    coord_x = int(input("Dónde quieres disparar. (Coordenada x, valores del 0 al 9)"))
    coord_y = int(input("Dónde quieres disparar. (Coordenada y, valores del 0 al 9)"))
    if 0 > coord_x > 9 or 0 > coord_y > 9:
        print("Has introducido valores coordenadas para este tablero")
        return disparar()
    if tablero[coord_y][coord_x] == "O":
        print("Acertaste")
        tablero[coord_y][coord_x] = "X"
        tablero_2[coord_y][coord_x] = "X"
    elif tablero[coord_y][coord_x] == "_":
        print("Fallaste")
        tablero[coord_y][coord_x]  = "A"
        tablero_2[coord_y][coord_x]  = "A"
    elif tablero[coord_y][coord_x] == "X":
        print("Ahí ya has disparado")
        return disparar()
    elif tablero[coord_y][coord_x] == "A":
        print("Ahí ya has disparado")
        return disparar()
    return tablero, tablero_2


def disparo_aleatorio(tablero_1):
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
    if tablero_1[fila][columna] == "_":
        tablero_1[fila][columna] = "A"
    elif tablero_1[fila][columna] == "O":
        tablero_1[fila][columna] = "X"
    return tablero_1


tablero = crear_tablero()
tablero_1 = crear_tablero()
tablero_2 = crear_tablero()
