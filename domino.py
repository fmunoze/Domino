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
contador = [7,7,7,7]
while True:
    bloqueo=0
    for player in Player.players:
        sleep(0.5)

        print('-------------------------------------------------------------')
        
        if player.jugadas_disponibles()==[]:
            bloqueo+=1

        if player!=player1:
            
            if player == player2:
                cuenta = player.jugada_automatica(1)
                contador[player.turno-1]-=cuenta
                print(f'{player.name} tiene {contador[player.turno-1]}')
                if player.fichas==set():
                    ganador=player
                    break
                continue
            elif player == player3:
                cuenta = player.jugada_automatica(2)
                contador[player.turno-1]-=cuenta
                print(f'{player.name} tiene {contador[player.turno-1]}')
                if player.fichas==set():
                    ganador=player
                    break
                continue

            elif player == player4:
                cuenta =player.jugada_automatica(3)
                contador[player.turno-1]-=cuenta
                print(f'{player.name} tiene {contador[player.turno-1]} fichas.')
                if player.fichas==set():
                    ganador=player
                    break
                continue


        jugada_valida=False
        print(f'Turno de {player.name}\n     Tablero: {player.tablero.fichas}\n     Mano: {player.fichas}\n     Jugadas disponibles: {player.jugadas_disponibles()}\n')
        
        
        while not jugada_valida:
            
            try:
                ficha=list(map(int,input('ingrese la ficha a jugar de la forma \'n m\', para pasar 7 7: ').split()))
                if len(ficha) == 4:

                    tuples = [(int(ficha[i]), int(ficha[i+1])) for i in range(0, 4, 2)]

                elif len(ficha) == 2:
                    tuples = [(int(ficha[0]), int(ficha[1]))]
            except:
                print('Jugada invalida, ingrese de nuevo la ficha')
                continue
            
            for ficha in tuples:
               jugada_valida=False    
               if ficha in player.jugadas_disponibles() or ficha==(7,7):
                jugada_valida=True     

            if jugada_valida==False:
                print('Jugada invalida, ingrese de nuevo la ficha')
        tupleTamano = len(tuples)
        if tupleTamano == 1:
            player.jugar_ficha(ficha)
        elif tupleTamano == 2 and tuples[0][1]==tuples[0][0] and tuples[1][1]==tuples[1][0]:
             player.jugar_ficha(tuples[0])
             player.jugar_ficha(tuples[1])
        
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
