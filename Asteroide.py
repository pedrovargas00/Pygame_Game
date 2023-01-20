'''
    PROYECTO FINAL - SISTEMAS EMPOTRADOS
    FECHA: 18/10/2021
    Elaboro: Equipo Powerbits
'''
import pygame

class Asteroide(pygame.sprite.Sprite):
    # INICIALIZACION
    def __init__(self, posY):
        super().__init__()
        self.image = pygame.image.load("resources/Obstaculos/Asteroides/asteroid_2.png").convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.velocidad = 1
        self.rect.left = 1270
        self.rect.top = posY

    # ACTUALIZACION
    def track(self):
        self.rect.left -= self.velocidad
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)