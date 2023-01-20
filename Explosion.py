import pygame

class Explosion(pygame.sprite.Sprite):
    animacion = ""
    def __init__(self, centro, dimensiones, frecuencia):
        pygame.sprite.Sprite.__init__(self)
        self.dimensiones = dimensiones
        self.image = self.animacion[self.dimensiones][0]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.fotograma = 0
        self.frecuencia_fotograma = frecuencia
        self.actualizacion = pygame.time.get_ticks()

    def update(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.actualizacion > self.frecuencia_fotograma:
            self.actualizacion = ahora
            self.fotograma += 1
            if self.fotograma == len(self.animacion[self.dimensiones]):
                self.kill()
            else:
                centro = self.rect.center
                self.image = self.animacion[self.dimensiones][self.fotograma]
                self.rect = self.image.get_rect()
                self.rect.center = centro