import random
import copy
import tablero

class Player:
    
    
    players=[]
    
    
    def __init__(self,name,fichas,tablero):
        
        self.name = name
        self.fichas = fichas
        self.turno = None
        self.tablero= tablero
        self.players.append(self)
    
    
    def jugar_ficha(self,ficha):
        
        if ficha==(7,7): 
            print(f'\n{self.name} pasó')
        elif self.tablero.cabeza in ficha or  self.tablero.cola in ficha:
            self.tablero.agregar_ficha(ficha)
            self.fichas.remove(ficha)
            print(f'\n{self.name} jugó {ficha}\n')
        else:
            print(f'{self.name} su jugada invalida\n')
    
        
    def jugadas_disponibles(self):
        
        if (6,6) in self.fichas:
            return [(6,6)]
        jugadas_disponibles=[ficha for ficha in self.fichas if self.tablero.cabeza in ficha or self.tablero.cola in ficha]
        return jugadas_disponibles
        
    def jugada_automatica(self,nivel):
        
        if nivel==1:

            disponiblesNovato = self.jugadas_disponibles() 
            print("las jugadas disp. del Novato es:", disponiblesNovato, "borrar este print luego")
            #si no hay jugada disponible, pasa
            if disponiblesNovato == []:
                print("Novato pasó")
                print()
                return
            self.jugar_ficha(random.choice(disponiblesNovato))
            return

        elif nivel==2:
            
            disponiblesPromedio = self.jugadas_disponibles()
            print("la mano disp. del Promedio es:", disponiblesPromedio, "borrar este print luego")            
            #si no hay jugada disponible, pasa
            if disponiblesPromedio == []:
                print("Promedio pasó")
                print()
                return

            mayor=(-1,-1)
            for ficha in disponiblesPromedio:
                if sum(ficha)>sum(mayor):
                    mayor=ficha
            self.jugar_ficha(mayor)
            return
 
        elif nivel ==3:

            #Falta configurar una forma de que los dobles no sumen doble en el registro, y asi el bot pueda diferenciar cuando 
            # tiene un doble, contarlo solo como una aparicion, por ahora lo dejo con X de 8 posibles apariciones, y el doble 
            # cuenta como doble aparicion

            #tambien faltaria agregar un conteo que sume cuantas hay en el tablero, y cuantas del mismo digito en la mano, 
            #y calcule si deberia jugar o no, si se le cerrraria o no, pero ya es too much eso, solo queda ahi la idea

            elegida = (9,9)
            prioridad1 = False
            prioridad2 = False

            evaluacion = copy.deepcopy(self.tablero.fichas)

            #hacer un conteo de las fichas en el tablero, para luego verificar si hay alguna de 7 o 6 (de 8 total por dígito)
            
            registro = [0,0,0,0,0,0,0]
            for ficha in evaluacion:
                for i in ficha:
                    #conteo de las apariciones de cada digito, agregandola en el registro segun su indice correspondiente
                    registro[i] += 1

            disponiblesExperto = self.jugadas_disponibles()
            print("la mano disp. del Experto es:", disponiblesExperto, "borrar este print luego") 
            #si no hay jugada disponible, pasa
            if disponiblesExperto == []:
                print("Experto pasó")
                print()
                return

            manoExperta = [0,0,0,0,0,0,0] #para verificar el numero de apariciones de cada digito en la mano del bot Experto        
            for ficha in disponiblesExperto:
                for i in ficha:
                    manoExperta[i] += 1
                    #Todo esto lo mismo que registro, pero con las fichas disponibles para jugar no mas

            for i in range (7):

                if registro[i]==7 and manoExperta[i]!=0:
                    prioridad1 = manoExperta[i]
                    break
                elif registro[i]==6 and manoExperta[i]!=0:
                    prioridad2 = manoExperta[i]
                    break

                          

            while elegida == (9,9):

                if prioridad1:

                    for ficha in disponiblesExperto:
                        if prioridad1 in ficha:
                            elegida  = ficha
                            break
                    prioridad1 = False

                    
                elif prioridad2:
                    for ficha in disponiblesExperto:
                        if prioridad2 == ficha:
                            elegida = ficha
                            break
                    prioridad2 = False
                    
                else:
                    elegida = (-1,-1)

            if elegida == (-1,-1):

                for ficha in self.jugadas_disponibles():                    
                    if sum(ficha)>sum(elegida):
                      elegida=ficha
            
            self.jugar_ficha(elegida)
            return






         
    @classmethod
    def designacion_turnos(cls):
        
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