import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600

class Personaggio(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('image/aliennave.png')
        self.image = pygame.transform.scale(self.image, (100,100))

        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.velocita_x
        self.rect.y += self.velocita_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

        
personaggio = Personaggio(50, 250)
gruppo_di_personaggi = pygame.sprite.Group()
gruppo_di_personaggi.add(personaggio)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Alien Revenge")
bg = pygame.image.load("image/nuovospace.png")
bgX = 0
bgX2 = bg.get_width()
menubg = pygame.image.load("image/alienisolation.png")
menubg = pygame.transform.scale(menubg, (800, 600))

orologio = pygame.time.Clock()
frame_rate = 60
speedScrl = 4

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def redrawGameWindow():
    for bullet in bullets:
        bullet.draw(screen)

game_state = "start_menu"

font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 100)
title = font2.render('Alien Revenge', True, (255, 0, 0))
title2 = font2.render('Scegli la tua nave', True, (255, 0, 0))
#Bottone start
button_surface = pygame.Surface((150, 50))
text = font.render(">>Click to Start<<", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
button_rect = pygame.Rect(315, 400, 150, 50) 
#Bottone prima scelta
button_surface1 = pygame.Surface((200, 200))
text1 = font.render("Nave uno", True, (0, 0, 0))
text_rect1 = text1.get_rect(center=(button_surface1.get_width()/2, 25))
button_rect1 = pygame.Rect(100, 200, 200, 200) 
scelta1 = pygame.image.load('image/aliennave.png')
scelta1 = pygame.transform.scale(scelta1, (150, 150))
#Bottone seconda scelta
button_surface2 = pygame.Surface((200, 200))
text2 = font.render("Nave due", True, (0, 0, 0))
text_rect2 = text2.get_rect(center=(button_surface2.get_width()/2, 25))
button_rect2 = pygame.Rect(310, 200, 200, 200) 
scelta2 = pygame.image.load('image/ship.png')
scelta2 = pygame.transform.scale(scelta2, (150, 150))
#Bottone terza scelta
button_surface3 = pygame.Surface((200, 200))
text3 = font.render("Nave tre", True, (0, 0, 0))
text_rect3 = text3.get_rect(center=(button_surface3.get_width()/2, 25))
button_rect3 = pygame.Rect(520, 200, 200, 200) 
scelta3 = pygame.image.load('image/bird.png')
scelta3 = pygame.transform.scale(scelta3, (150, 150))

vite = 3

score = 0
#main loop
bullets = []
while True:
    
    orologio.tick(frame_rate)

    #Tasti e Comandi
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            keys = pygame.key.get_pressed()
        for bullet in bullets:
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel # Moves the bullet by its vel
            else:
                bullets.pop(bullets.index(bullet))  # This will remove the bullet if it is off the screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
         #Comandi Navicella
            if game_state == "game":   
                if event.key == pygame.K_a:
                    personaggio.cambia_velocita(-5, 0)
                if event.key == pygame.K_d:
                    personaggio.cambia_velocita(5, 0)
                if event.key == pygame.K_w:
                    personaggio.cambia_velocita(0, -5)
                if event.key == pygame.K_s:
                    personaggio.cambia_velocita(0, 5)
                if keys[pygame.K_SPACE]:
                    if len(bullets) < 20:  # This will make sure we cannot exceed 20 bullets on the screen at once
                        bullets.append(projectile(round(personaggio.rect.x+personaggio.rect.y//2), round(personaggio.rect.x + personaggio.rect.y//2), 6, ("yellow"), 1))
        elif event.type == pygame.KEYUP:
            if game_state == "game":
                if event.key == pygame.K_a:
                    personaggio.cambia_velocita(5, 0)
                if event.key == pygame.K_d:
                    personaggio.cambia_velocita(-5, 0)
                if event.key == pygame.K_w:
                    personaggio.cambia_velocita(0, 5)
                if event.key == pygame.K_s:
                    personaggio.cambia_velocita(0, -5)


    #Menu
    if game_state == "start_menu":
      if event.type == pygame.MOUSEBUTTONDOWN:
       if button_rect.collidepoint(event.pos):  
         game_state = "scelta"
      if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (255, 0, 0), (1, 1, 148, 48))
      else:
       pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
       pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
       pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
       pygame.draw.rect(button_surface, (0, 0, 0), (1, 48, 148, 10), 2)    

      screen.blit(menubg, (0, 0))
      screen.blit(title, (150, 100))
      button_surface.blit(text, text_rect)
      screen.blit(button_surface, (button_rect.x, button_rect.y))

      pygame.display.update()
    
    #Menu Scelta
    elif game_state == "scelta":
     #Prima scelta
     if event.type == pygame.MOUSEBUTTONDOWN:
       if button_rect1.collidepoint(event.pos):  
         game_state = "game"
     if button_rect1.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface1, (255, 0, 0), (1, 1, 198, 198))
     else:
       pygame.draw.rect(button_surface1, (0, 0, 0), (0, 0, 200, 200))
       pygame.draw.rect(button_surface1, (255, 255, 255), (1, 1, 198, 198))
       pygame.draw.rect(button_surface1, (0, 0, 0), (1, 1, 198, 1), 2)
       pygame.draw.rect(button_surface1, (0, 0, 0), (1, 198, 198, 10), 2)    
     #Seconda scelta
     if event.type == pygame.MOUSEBUTTONDOWN:
       if button_rect2.collidepoint(event.pos):  
         game_state = "game"
     if button_rect2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface2, (255, 0, 0), (1, 1, 198, 198))
     else:
       pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 200, 200))
       pygame.draw.rect(button_surface2, (255, 255, 255), (1, 1, 198, 198))
       pygame.draw.rect(button_surface2, (0, 0, 0), (1, 1, 198, 1), 2)
       pygame.draw.rect(button_surface2, (0, 0, 0), (1, 198, 198, 10), 2)    
     #Terza scelta
     if event.type == pygame.MOUSEBUTTONDOWN:
       if button_rect3.collidepoint(event.pos):  
         game_state = "game"
     if button_rect3.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface3, (255, 0, 0), (1, 1, 198, 198))
     else:
       pygame.draw.rect(button_surface3, (0, 0, 0), (0, 0, 200, 200))
       pygame.draw.rect(button_surface3, (255, 255, 255), (1, 1, 198, 198))
       pygame.draw.rect(button_surface3, (0, 0, 0), (1, 1, 198, 1), 2)
       pygame.draw.rect(button_surface3, (0, 0, 0), (1, 198, 198, 10), 2)    

     screen.blit(menubg, (0, 0))
     screen.blit(title2, (110, 50))

     button_surface1.blit(text1, text_rect1)
     screen.blit(button_surface1, (button_rect1.x, button_rect1.y))
     screen.blit(scelta1, (130, 230))

     button_surface2.blit(text2, text_rect2)
     screen.blit(button_surface2, (button_rect2.x, button_rect2.y))
     screen.blit(scelta2, (330, 230))

     button_surface3.blit(text3, text_rect3)
     screen.blit(button_surface3, (button_rect3.x, button_rect3.y))
     screen.blit(scelta3, (550, 230))

     pygame.display.update()

    #Gioco
    elif game_state == "game":
        #Sfondo
        bgX -= speedScrl  
        bgX2 -= speedScrl

        if bgX < bg.get_width() * -1: 
            bgX = bg.get_width()
            
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        screen.blit(bg, (bgX, 0))  
        screen.blit(bg, (bgX2, 0))  
        gruppo_di_personaggi.update()
        gruppo_di_personaggi.draw(screen)
        score_text = font.render(f'Punteggio: {score}', True, "white")
        screen.blit(score_text, (10, 10))
        vite_text = font.render(f'vite: {vite}', True, "white")
        screen.blit(vite_text, (600, 10))


        redrawGameWindow()
        pygame.display.update()   