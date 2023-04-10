class Player:
    
    players=[]
    
    def __init__(self,fichas):
        
        self.fichas = fichas
        self.turno = None
        self.players.append(self)
    
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