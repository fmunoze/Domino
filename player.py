class Player:
    
    
    players=[]
    
    
    def __init__(self,name,fichas,tablero):
        
        self.name = name
        self.fichas = fichas
        self.turno = None
        self.tablero= tablero
        self.players.append(self)
    
    
    def jugar_ficha(self,ficha):
        
        if self.tablero.cabeza in ficha or  self.tablero.cola in ficha:
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