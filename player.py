import random
import copy
import tablero

class Player:
    
    
    players=[]
    
    
    def __init__(self,name,fichas,tablero):
        
        self.name = name
        self.fichas = fichas
        self.turno = None
        self.tablero = tablero
        self.players.append(self)
    
    
    def jugar_ficha(self,ficha):
        
        if ficha==(7,7): 
            print(f'\n{self.name} pasó')
        elif self.tablero.cabeza in ficha or  self.tablero.cola in ficha:
            self.tablero.agregar_ficha(ficha)
            self.fichas.discard(ficha)
            print(f'\n{self.name} jugó {ficha}\n')
        else:
            print(f'{self.name} su jugada invalida\n')
    
        
    def jugadas_disponibles(self): # O(n)   
        
        if (6,6) in self.fichas: 
            return [(6,6)]
        jugadas_disponibles=[ficha for ficha in self.fichas if self.tablero.cabeza in ficha or self.tablero.cola in ficha]
        return jugadas_disponibles
        




    def jugada_automatica(self,nivel):
        orden = 0
        if nivel==1:

            disponiblesNovato = self.jugadas_disponibles() 
            #print("las jugadas disp. del Novato es:", disponiblesNovato, "borrar este print luego")
            #si no hay jugada disponible, pasa
            orden = 1
            if disponiblesNovato == []:
                print("Novato pasó")
                print()
                orden = 0
                return orden
            self.jugar_ficha(random.choice(disponiblesNovato))
            return orden

        elif nivel==2:
            
            disponiblesPromedio = self.jugadas_disponibles()
            #print("la mano disp. del Promedio es:", disponiblesPromedio, "borrar este print luego")  
            orden =1          
            #si no hay jugada disponible, pasa
            if disponiblesPromedio == []:
                print("Promedio pasó")
                print()
                orden=0
                return orden

            mayor=(-1,-1)
            for ficha in disponiblesPromedio:
                if sum(ficha)>sum(mayor):
                    mayor=ficha
            self.jugar_ficha(mayor)
            return orden
 
        elif nivel ==3:


            elegida = (9,9)
            prioridad1 = False
            prioridad2 = False

            evaluacion = copy.deepcopy(self.tablero.fichas)

            #hacer un conteo de las fichas en el tablero, para luego verificar si hay alguna de 7 o 6 (de 8 total por dígito)
            
            registro = [0,0,0,0,0,0,0] #del tablero
            for ficha in evaluacion:
                for i in ficha:
                    #conteo de las apariciones de cada digito, agregandola en el registro segun su indice correspondiente
                    registro[i] += 1

            disponiblesExperto = self.jugadas_disponibles()
            #print("la mano disp. del Experto es:", disponiblesExperto, "borrar este print luego") 
            orden = 1 
            #si no hay jugada disponible, pasa
            if disponiblesExperto == []:
                print("Experto pasó")
                print()
                orden = 0
                return orden

            manoExperta = [0,0,0,0,0,0,0] #para verificar el numero de apariciones de cada digito en la mano del bot Experto        
            for ficha in disponiblesExperto:
                for i in ficha:
                    manoExperta[i] += 1
                    #Todo esto lo mismo que registro, pero con las fichas disponibles para jugar no mas

            for i in range (7):

                if registro[i]==7 and manoExperta[i]!=0: #reservarla (pues solo este jugador puede ocupar ese lado del tablero, pues tiene la última ficha que se puede poner en ese lado)
                    prioridad1 = manoExperta[i]
                    break
                elif registro[i]==6 and manoExperta[i]!=0: #jugarla inmediatamente (pues hay posiblemente otro jugador con esa ficha, y solo el primero que la ponga la podra jugar, el otro no)
                    prioridad2 = manoExperta[i]
                    break

                          

            while elegida == (9,9):

                if prioridad1: 

                    for ficha in disponiblesExperto:
                        if prioridad1 in ficha:
                            disponiblesExperto.remove(ficha) #reserva la ficha para otro turno
                            elegida = (-1,-1)
                            break
                    prioridad1 = False

                    
                elif prioridad2:
                    for ficha in disponiblesExperto:
                        if prioridad2 == ficha:
                            elegida = ficha #elige para jugar la ficha inmediatamente
                            break
                    prioridad2 = False
                    
                else:
                    elegida = (-1,-1)

            if elegida == (-1,-1): #de no suceder la prioridad 2, elige la ficha de mayor valor (sin la reservad, si sucedió la prioridad 1)

                for ficha in self.jugadas_disponibles():                    
                    if sum(ficha)>sum(elegida):
                      elegida=ficha
            
            self.jugar_ficha(elegida)
            
            return orden






         
    @classmethod
    def designacion_turnos(cls): #O(k n), k: jugadores, n: numero de fichas
        
        turno=2
        encontrado=False
        while True:
            for player in Player.players:
                if (6,6) in player.fichas and encontrado==False:
                    player.turno=1
                    encontrado=True
                elif encontrado==True and player.turno==None:
                    player.turno=turno
                    turno+=1
            if turno==5:
                break
        #ordena la lista de jugadores basado en su turno
        Player.players.sort(key=lambda player: player.turno)