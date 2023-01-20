'''
    PROYECTO FINAL - SISTEMAS EMPOTRADOS
    FECHA: 18/10/2021
    Elaboro: Equipo Powerbits
'''
import pygame
import Disparo

class Jugador(pygame.sprite.Sprite):
    #INICIALIZACION
    def __init__(self, speed):
        super().__init__()
        self.BLACK = (0, 0, 0)
        self.image = pygame.image.load("resources/ships/naveR.png").convert()
        self.image.set_colorkey(self.BLACK)
        #self.image = pygame.transform.rotate(self.image, 270)
        #La imagen será un rectángulo
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.centery = 340
        self.speed = speed
        self.life = 100
        self.lives = 3
        self.move = 40
        self.damage = 15

    def movement(self):
        #Si está vivo
        if self.life > 0:
            #Evita que salga de escena
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom > 720:
                self.rect.bottom = 720

    def increaseLive(self):
        self.lives += 1

    def changeLiveImage(self, x, y):
        if self.lives == 3:
            self.image = pygame.image.load("resources/ships/naveR.png")
        if self.lives == 2:
            self.image = pygame.image.load("resources/ships/nave2R.png")
        if self.lives == 1:
            self.image = pygame.image.load("resources/ships/nave3R.png")
        self.image.set_colorkey(self.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def impact(self, damage):
        self.life -= damage

    def impactBoss(self, damage):
        self.life -= damage
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
