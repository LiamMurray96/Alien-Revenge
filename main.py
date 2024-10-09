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
menubg = pygame.image.load("image/alienisolation.jpg")
menubg = pygame.transform.scale(menubg, (800, 600))

orologio = pygame.time.Clock()
frame_rate = 60
speedScrl = 4

game_state = "start_menu"

def draw_start_menu():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont(None, 40)
   font2 = pygame.font.SysFont(None, 100)
   font3 = pygame.font.SysFont(None, 40)
   title = font2.render('Alien Revenge', True, (255, 255, 255))
   start_button = font.render('>>Premi Spazio<<', True, (255, 255, 255))
   change_ship = font3.render('Seleziona Nave', True, (255, 255, 255))
   screen.blit(title, (150, 100))
   screen.blit(start_button, (260, 400))
   screen.blit(change_ship, (280, 300))
   pygame.display.update()

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
          game_state = "game"
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
        redrawGameWindow()
        pygame.display.update()
