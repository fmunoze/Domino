import random
from player import Player
from tablero import Tablero
from time import sleep


"""#por ahora sigue funcionan con listas, porque ajá

fichas = {(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)}
manos = [[],[],[],[]]


for i in range (4):
    muestra = random.sample(list(fichas), 7)
    manos[i] = muestra
    fichas -= set(muestra)


#Inicializacion de variables y asignacion de fichas (7 por jugador)
tablero=Tablero()
#persona
player1 = Player('Humano',manos(0),tablero)
#bots
player2 = Player('Novato',manos(1),tablero)
player3 = Player('Promedio',manos(2),tablero)
player4 = Player('Experto',manos(3),tablero)

"""
fichas=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)]
#Mezcla de las fichas
random.shuffle(fichas)

#Inicializacion de variables y asignacion de fichas (7 por jugador)
tablero=Tablero()
#persona
player1 = Player('Humano',set(fichas[0:7]),tablero)
#bots
player2 = Player('Novato',set(fichas[7:14]),tablero)
player3 = Player('Promedio',set(fichas[14:21]),tablero)
player4 = Player('Experto',set(fichas[21:28]),tablero)


#designacion de turnos
Player.designacion_turnos()

ganador=None
while True:
    bloqueo=0
    for player in Player.players:
        sleep(0.5)

        print('-------------------------------------------------------------')
        
        if player.jugadas_disponibles()==[]:
            bloqueo+=1

        if player!=player1:
            
            if player == player2:
                player.jugada_automatica(1)
                if player.fichas==set():
                    ganador=player
                    break
                continue
            elif player == player3:
                player.jugada_automatica(2)
                if player.fichas==set():
                    ganador=player
                    break
                continue

            elif player == player4:
                player.jugada_automatica(3)
                if player.fichas==set():
                    ganador=player
                    break
                continue


        jugada_valida=False
        print(f'Turno de {player.name}\n     Tablero: {player.tablero.fichas}\n     Mano: {player.fichas}\n     Jugadas disponibles: {player.jugadas_disponibles()}\n')
        
        
        while not jugada_valida:
            
            try:
                ficha=tuple(map(int,input('ingrese la ficha a jugar de la forma \'n m\', para pasar 7 7: ').split()))
            except:
                print('Jugada invalida, ingrese de nuevo la ficha')
                continue
            
            if ficha in player.jugadas_disponibles() or ficha==(7,7):
                jugada_valida=True     
            else:
                print('Jugada invalida, ingrese de nuevo la ficha')
        
        player.jugar_ficha(ficha)
        
        if player.fichas==set():
            ganador=player
            break
    
    if ganador!=None or bloqueo==4:
        break
        

for player in Player.players:
    if ganador==None:ganador=player
    print(f'mano de {player.name}: {player.fichas}')
    if sum(list(map(sum,player.fichas)))<sum(list(map(sum,ganador.fichas))):
        ganador=player
print(f'\nGANADOR!:{ganador.name}')   
