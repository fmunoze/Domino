
import random
from player import Player
from tablero import Tablero


fichas=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)]
#Mezcla de las fichas
random.shuffle(fichas)


#Inicializacion de variables y asignacion de fichas (7 por jugador)
tablero=Tablero()
#persona
player1 = Player('Julian',fichas[0:7],tablero)
#bots
player2 = Player('Felipe',fichas[7:14],tablero)
player3 = Player('Daniel',fichas[14:21],tablero)
player4 = Player('Luis',fichas[21:28],tablero)


#designacion de turnos
Player.designacion_turnos()

while True:
    for player in Player.players:
        ficha=None
        if (6,6) in player.fichas:
            ficha=(6,6)
            player.jugar_ficha(ficha)
        else:
            print(player.jugadas_disponibles())
    break