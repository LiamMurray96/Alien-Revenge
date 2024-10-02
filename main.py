import pygame
import sys
pygame.init()









screen = pygame.display.set_mode((800,600))
orologio = pygame.time.Clock()
frame_rate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    







    screen.fill("white")
    orologio.tick(frame_rate) 

    pygame.display.update()  