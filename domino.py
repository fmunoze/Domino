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

random.shuffle(fichas)  #Mezcla de las fichas

#Inicializacion de variables y asignacion de fichas (7 por jugador)
tablero=Tablero()
#persona
player1 = Player('Humano',set(fichas[0:7]),tablero)
#bots
player2 = Player('Novato',set(fichas[7:14]),tablero)
player3 = Player('Promedio',set(fichas[14:21]),tablero)
player4 = Player('Experto',set(fichas[21:28]),tablero)


Player.designacion_turnos() #designacion de turnos

ganador=None
contador = [7,7,7,7]

bloqueo=0 #para hallar si hay un loop en el que nadie mas puede jugar, y finalizar el juego "juego cerrado"

while True:
    
    for player in Player.players:
        #sleep(0.5) Descomentar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        print('-------------------------------------------------------------')
        
        #if player.jugadas_disponibles()==[]: #si no tiene jugadas disponibles, agrega al contador de bloqueo
        #    bloqueo+=1

        if player!=player1: #juega la IA
            
            if player == player2: #Juega la IA novata
                cuenta = player.jugada_automatica(1)
                contador[player.turno-1]-=cuenta
                


                if cuenta == 1:
                    bloqueo = 0
                else: bloqueo += 1
                
                print(f'{player.name} tiene {contador[player.turno-1]} fichas.')
                if player.fichas==set():
                    ganador=player
                    break
                continue

            elif player == player3: #juega la IA medio
                cuenta = player.jugada_automatica(2)
                contador[player.turno-1]-=cuenta




                if cuenta == 1:
                    bloqueo = 0
                else: bloqueo += 1
                
                print(f'{player.name} tiene {contador[player.turno-1]} fichas.')
                if player.fichas==set():
                    ganador=player
                    break
                continue

            elif player == player4: #Juega la IA avanzada
                cuenta =player.jugada_automatica(3)
                contador[player.turno-1]-=cuenta


                if cuenta == 1:
                    bloqueo = 0
                else: bloqueo += 1
                
                print(f'{player.name} tiene {contador[player.turno-1]} fichas.')
                if player.fichas==set():
                    ganador=player
                    break
                continue



        #Si no jugó la IA, ahora es el turno del jugador  y muestra turno, tablero, fichas y jugadas que puede hacer:
        print(f'Turno de {player.name}\n     Tablero: {player.tablero.fichas}\n     Mano: {player.fichas}\n     Jugadas disponibles: {player.jugadas_disponibles()}\n')
        
        jugada_valida=False

        while not jugada_valida:
            
            try:
                ficha=list(map(int,input('ingrese la ficha a jugar de la forma \'n m\'. Para pasar ingrese \'7 7\': ').split()))  #jugador ingresa ficha a jugar
               
                if len(ficha) == 2: #verifica formato de ficha
                    tuples = [(int(ficha[0]), int(ficha[1]))]
                else:               #para formato inválido
                    tuples = [(int(ficha[i]), int(ficha[i+1])) for i in range(0, 4, 2)]
                    if tuples[0][1]!=tuples[0][0] and tuples[1][1]!=tuples[1][0]:
                        print('Jugada invalida, ingrese de nuevo la ficha')
                        continue
            except: 
                print('Jugada invalida, ingrese de nuevo la ficha')
                continue
            
            for ficha in tuples: 
               if  ficha==(7,7) and len(tuples)==1: #para pasar
                   jugada_valida=True

                   bloqueo += 1
                   break
                
               elif ficha not in player.jugadas_disponibles(): #para una ficha que no se puede jugar
                    jugada_valida=False
                    break
               jugada_valida=True     
                
            if jugada_valida==False:
                print('Jugada invalida, ingrese de nuevo la ficha') #si intentó jugar una ficha que no se tiene, reinicia el intento
        tupleTamano = len(tuples)
        if tupleTamano == 1:
            player.jugar_ficha(ficha)


        elif tupleTamano == 2 and tuples[0][1]==tuples[0][0] and tuples[1][1]==tuples[1][0]:
             player.jugar_ficha(tuples[0])
             player.jugar_ficha(tuples[1])
        
        if player.fichas==set():
            ganador=player
            break
    
    if ganador!=None or bloqueo >=4:
        break
        

print ("\nPartida finalizada, tablero final:")
print ('-------------------------------------------------')
for ficha in tablero.fichas:

    print (ficha, end= ' ')

print ('\n-------------------------------------------------')


for player in Player.players: #for que revisa el puntaje de los jugadores; primero setea el ganador como el humano, y luego verifica si hay otro mejor puntaje. 
    if ganador==None:ganador=player
    print(f'mano de {player.name}: {player.fichas}')
    if sum(list(map(sum,player.fichas)))<sum(list(map(sum,ganador.fichas))):
        ganador=player
print(f'\nGANADOR!:{ganador.name}')   
