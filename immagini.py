import pygame
#from immagini import Nave, Nemico, Ostacolo, Sparo
import sys

width, heigth = 800, 600
pygame.init()
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()
running = True
dt = 0

class Nave(pygame.sprite.Sprite):
    #costruttore classe
    def __init__(self, x, y):
        #chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        #carichiamo immagine personaggio
        self.image = pygame.image.load("image/nave.png")
        self.image = pygame.Surface.convert_alpha(self.image)
        #ridimensioniamo il personaggio
        self.image = pygame.transform.scale(self.image, (100, 50))

        #rettangolo di posizione e collegamento
        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self, self.image)

    def update(self):
            self.rect.x += self.velocita_x
            self.rect.y += self.velocita_y
            #controllo limiti dello schermo
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > heigth:
                self.rect.bottom = heigth

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

class Nemico(pygame.sprite.Sprite):
    #costruttore classe
    def __init__(self, x, y):
        #chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        #carichiamo immagine personaggio
        self.image = pygame.image.load("image/nemico.png")
        self.image = pygame.Surface.convert_alpha(self.image)
        #ridimensioniamo il personaggio
        self.image = pygame.transform.scale(self.image, (100, 50))

        #rettangolo di posizione e collegamento
        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self, self.image)

    def update(self):
            self.rect.x += self.velocita_x
            self.rect.y += self.velocita_y
            #controllo limiti dello schermo
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > heigth:
                self.rect.bottom = heigth

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

class Ostacolo(pygame.sprite.Sprite):
    #costruttore classe
    def __init__(self, x, y):
        #chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        #carichiamo immagine personaggio
        self.image = pygame.image.load("image/asteroide.png")
        self.image = pygame.Surface.convert_alpha(self.image)
        #ridimensioniamo il personaggio
        self.image = pygame.transform.scale(self.image, (210, 200))

        #rettangolo di posizione e collegamento
        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self, self.image)

    def update(self):
            self.rect.x += self.velocita_x
            self.rect.y += self.velocita_y
            #controllo limiti dello schermo
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > heigth:
                self.rect.bottom = heigth

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

class Sparo(pygame.sprite.Sprite):
    #costruttore classe
    def __init__(self, x, y):
        #chiamiamo il costruttore della super classe, in questo caso Sprite
        super().__init__()
        #carichiamo immagine personaggio
        self.image = pygame.image.load("image/bullet.png")
        self.image = pygame.Surface.convert_alpha(self.image)
        #ridimensioniamo il personaggio
        self.image = pygame.transform.scale(self.image, (100, 50))

        #rettangolo di posizione e collegamento
        self.rect = self.image.get_rect()

        self.rect.topleft = (x,y)
        self.velocita_x = 0
        self.velocita_y = 0

        #self.mask = pygame.mask.from_surface(self, self.image)

    def update(self):
            self.rect.x += self.velocita_x
            self.rect.y += self.velocita_y
            #controllo limiti dello schermo
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > heigth:
                self.rect.bottom = heigth

    def cambia_velocita(self, x, y):
        self.velocita_x += x
        self.velocita_y += y

#creazione dello sprite personaggio
nave = Nave(100, 100)
nemico = Nemico(400, 400)
ostacolo = Ostacolo(250, 250)
sparo = Sparo(50, 50)

if nave.rect.colliderect(nemico.rect):
    screen.fill("red")
if nave.rect.colliderect(ostacolo.rect):
    screen.fill("green")

#gruppo di sprite per gestione facilitata
gruppo_di_personaggi = pygame.sprite.Group()
gruppo_di_personaggi.add(nave)
gruppo_di_personaggi.add(nemico)
gruppo_di_personaggi.add(ostacolo)
gruppo_di_personaggi.add(sparo)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                nave.cambia_velocita(-5, 0)
            if event.key == pygame.K_RIGHT:
                nave.cambia_velocita(5, 0)
            if event.key == pygame.K_UP:
                nave.cambia_velocita(0, -5)
            if event.key == pygame.K_DOWN:
                nave.cambia_velocita(0, 5)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                nave.cambia_velocita(5, 0)
            if event.key == pygame.K_RIGHT:
                nave.cambia_velocita(-5, 0)
            if event.key == pygame.K_UP:
                nave.cambia_velocita(0, 5)
            if event.key == pygame.K_DOWN:
                nave.cambia_velocita(0, -5)

    gruppo_di_personaggi.update()

    screen.fill("purple")

    gruppo_di_personaggi.draw(screen)

    dt = clock.tick(60) / 1000

    pygame.display.update()

pygame.quit()