import random
from player import Player
from tablero import Tablero
from time import sleep


"""#por ahora sigue funcionan con listas, porque ajá
fichas = {(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)}

"""
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
    n_p=0
    for player in Player.players:
        #sleep(2)

        print('-------------------------------------------------------------')
        
        if player.jugadas_disponibles()==[]:
            n_p+=1
            print(f'\n{player.name} no tiene jugadas dispobibles\n')
            if n_p==4:
                ganador=player
                for _player in Player.players:
                    print(f'mano de {_player.name}: {_player.fichas}')
                    if sum(list(map(sum,_player.fichas)))<sum(list(map(sum,ganador.fichas))):
                        ganador=_player
                print(f'\nGANADOR POR PUNTOS!:{ganador.name}')
                game=False
                break
            continue
        
        if player!=player1:

            if player == player2:
                player.jugada_automatica(1)
                continue
            elif player == player3:
                player.jugada_automatica(2)
                continue

            elif player == player4:
                player.jugada_automatica(3)
                continue


        jugada_valida=False
        print(f'Turno de {player.name}\n     Tablero: {player.tablero.fichas}\n     Mano: {player.fichas}\n     Jugadas disponibles: {player.jugadas_disponibles()}\n')
        
        while not jugada_valida:
            
            try:
                ficha=tuple(map(int,input('ingrese la ficha a jugar de la forma \'n m\', para pasar 7 7: ').split()))
            except:
                print('Jugada invalida, ingrese de nuevo la ficha')
                continue
            
            if ficha==(7,7):
                print(f'{player.name} pasó')
                jugada_valida=True  

            elif ficha in player.jugadas_disponibles():
                jugada_valida=True     
            else:
                print('Jugada invalida, ingrese de nuevo la ficha')
        
        
        if ficha==(7,7):continue
        
        player.jugar_ficha(ficha)
        
        if player.fichas==[]:
            print(f'GANADOR!: {player.name}')
            game=False
            break
