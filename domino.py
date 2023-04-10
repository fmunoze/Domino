
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

game=True
while game:
    for player in Player.players:
        if player.jugadas_disponibles()==[]:
            print(f'{player.name} no tiene jugadas dispobibles')
            continue
        jugada_valida=False
        print(f'Turno de {player.name}\n     Tablero: {player.tablero.fichas}\n     Mano: {player.fichas}\n     Jugadas disponibles: {player.jugadas_disponibles()}\n')
        while not jugada_valida:
            ficha=tuple(map(int,input('ingrese la ficha a jugar de la forma \'n m\': ').split()))
            if ficha in player.jugadas_disponibles():
                jugada_valida=True
            else:
                print('Jugada invalida, ingrese de nuevo la ficha')
                
        player.jugar_ficha(ficha)
        if player.fichas==[]:
            print(f'GANADOR!: {player.name}')
            game=False
            break