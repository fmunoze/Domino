class Player:
    
    players=[]
    
    def __init__(self,name,fichas):
        
        self.name = name
        self.fichas = fichas
        self.turno = None
        self.players.append(self)
    
    def jugar(self,ficha,tablero):
        if tablero.cabeza in ficha or  tablero.cola in ficha:
            tablero.agregar(ficha)
            self.fichas.remove(ficha)
        else:
            return -1
        
    
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