from collections import deque

class Tablero:
    
    
    def __init__(self):
        
        self.cabeza=6
        self.cola=6
        self.fichas=deque()
    
    
    def agregar_ficha(self,tupla):
        
        tupla=list(tupla)
        if self.cabeza in tupla:
            tupla.remove(self.cabeza)
            self.fichas.append((self.cabeza,tupla[0]))
            self.cabeza=tupla[0]
        else:
            tupla.remove(self.cola)
            self.fichas.appendleft((tupla[0],self.cola))
            self.cola=tupla[0]