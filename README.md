# Hundir la Flota

¡Bienvenido a **Hundir la Flota**! Este es un juego clásico de estrategia en el que tu objetivo es hundir todos los barcos de tu oponente antes de que él hunda los tuyos. El juego se desarrolla en dos tableros: uno para tus barcos y otro para los barcos del oponente. ¡Buena suerte, capitán Jack "Stringrrow"!

---

## Instalación

1. **Clona el repositorio** o descarga los archivos del juego.
   ```bash
   git clone https://github.com/PlazzaA/La_flota_me_ha_hundido

## Asegúrate de tener Python instalado. Este juego requiere Python 3.6 o superior. Puedes verificar tu versión de Python con:
    python --version

## Instala las dependencias. Este juego utiliza numpy para manejar los tableros. Si no lo tienes instalado, puedes instalarlo con:
    pip install numpy

## Ejecuta el juego:
    python estoy_hundido

# Cómo jugar
## 1. Coloca tus barcos
Al inicio del juego, se te pedirá que coloques tus barcos en el tablero.

Debes ingresar las coordenadas (x, y) y la orientación (Arriba, Abajo, Derecha, Izquierda) para cada barco.

Los barcos tienen diferentes esloras (tamaños):

3 barcos de eslora 2.

2 barcos de eslora 3.

1 barco de eslora 4.

## 2. Dispara al oponente
Después de colocar tus barcos, comenzará el juego.

Ingresa las coordenadas (x, y) para disparar al tablero del oponente.

Si aciertas ("O"), marcarás un impacto ("X").

Si fallas ("_"), marcarás un agua ("A").

## 3. Defiende tus barcos
Después de tu turno, el oponente disparará aleatoriamente a tu tablero.

¡Cuidado! Si el oponente acierta, perderás un barco.

## 4. Gana el juego
El juego termina cuando todos los barcos de un jugador han sido hundidos.

Si hundes todos los barcos del oponente, ¡ganas!

Si el oponente hunde todos tus barcos, pierdes.
