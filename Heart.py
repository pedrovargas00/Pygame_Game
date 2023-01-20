import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, posX):
        super().__init__()
        self.image = pygame.image.load("resources/heart2.png").convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.imageResized = pygame.transform.scale(self.image, (50,7))
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = 680

    def draw(self, surface):
        surface.blit(self.imageResized, self.rect)
        