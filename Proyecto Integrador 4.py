laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

import os 

def transformar_en_matriz(laberinto):
    return [list(fila) for fila in laberinto.split('\n')]

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ensenar_matriz(mapa):
    for fila in mapa:
        print(''.join(fila))

def loop_principal(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while(px, py) != posicion_final:
        mapa[px][py] = 'P'
        limpiar()
        ensenar_matriz(mapa)
        mapa[py][px] = '.'

        direccion = input('Ingresar (abajo, arriba, derecha, izquierda):').lower()

        if direccion == 'arriba' and py > 0 and mapa[py - 1][px] != '#':
            py -= 1
        elif direccion == 'abajo' and py < len(mapa) - 1 and mapa[py + 1][px] != '#':
            py += 1
        elif direccion == 'izquierda' and px > 0 and mapa[py][px - 1] != '#':
            px -= 1
        elif direccion == 'derecha' and px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
            px += 1
    
    limpiar()
    print('Enhorabuena, has llegado a tu destino.')

if __name__ == '__main__':
     laberinto = """..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################.."""
   
mapa = transformar_en_matriz(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0])) - 1, len(mapa) - 1
loop_principal(mapa, posicion_inicial, posicion_final)