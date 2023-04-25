##BOSQUEJO, ignorar!
import random
from player import Player
from tablero import Tablero
from time import sleep
import pygame

fichas=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)]
#Mezcla de las fichas
random.shuffle(fichas)

#Inicializacion de variables y asignacion de fichas (7 por jugador)
tablero=Tablero()
#persona
player1 = Player('Humano',fichas[0:7],tablero)
#bots
player2 = Player('Novato',fichas[7:14],tablero)
player3 = Player('Promedio',fichas[14:21],tablero)
player4 = Player('Experto',fichas[21:28],tablero)


#designacion de turnos
Player.designacion_turnos()


##########################
###########################

import pygame
import sys


pygame .init()


#para los fps, no estoy seguro como va bien aún o si va o no
pygame.time.Clock().tick(10)

fichaColor =  255, 248, 231


ancho = 1000
alto = 700

pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Dominó")


board = pygame.image.load("marmol.png")
boardrect = board.get_rect()

pantalla.blit(board, (0, 0))


#fondoColor = (193,217,232)
#pantalla.fill(fondoColor)

celdaColor1=  (204, 224, 232)
celdaColor2 = (218, 232, 240)

tamanoCelda = 50
tableroPosX = 50
tableroPosY = 50

tableroAncho = tamanoCelda * 18
tableroAlto = tamanoCelda * 12

for fila in range (12):
    for columna in range (18):

        if (fila+columna)%2 == 0:
            color = (celdaColor1)
        else:
            color = (celdaColor2)

        pygame.draw.rect(pantalla, color, (tableroPosX + columna * tamanoCelda, tableroPosY + fila * tamanoCelda, tamanoCelda, tamanoCelda))

fichasPosX = 150
fichasPosY = 580 
fichasAncho = 700
fichasAlto = 110

pygame.draw.rect(pantalla, (200,200,200), (fichasPosX, fichasPosY, fichasAncho, fichasAlto))

#jugador izq
pygame.draw.rect(pantalla, (200,200,200), (10,200,50,300))
#jugador der
pygame.draw.rect(pantalla, (200,200,200), (940,200,50,300))
#jugador arriba
pygame.draw.rect(pantalla, (200,200,200), (350,10,300,50))


fuente = pygame.font.SysFont('Arial', 20)
pygame.draw.rect(pantalla, (fichaColor),(50*9,50*6,50,100))






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player == player1:
                clickPos = pygame.mouse.get_pos()


    pygame.display.update()

pygame.quit()
