import pygame

class SondaInfo(pygame.sprite.Sprite):
    # ATRIBUTOS GENERALES PARA SPRITES
    

    # INICIALIZACION
    def __init__(self, posY):
        super().__init__()
        self.image = pygame.image.load("resources/.png").convert()
        self.rect = self.image.get_rect()
        self.speed = 1
        self.life = 0
        self.damage = 10
        self.rect.left = 1270
        self.rect.top = posY