##BOSQUEJO, ignorar!
import pygame

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Dominó")

jugando = True

ganador = False
turno = 0


while not ganador:
  
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      gnador = True
        
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if turno == 0:
        clickPos = pygame.mouse.get_pos()

  
  
  
  
  ventana.fill((37, 150, 190))
  pygame.display.flip()
  pygame.time.Clock().tick(10)
  pygame.quit()