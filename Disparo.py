import pygame

class Disparo(pygame.sprite.Sprite):

    def __init__(self, posX, posY, angle = 270, speed = 5, damage = 10):
        super().__init__()
        self.image = pygame.image.load("resources/misil.png").convert()
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.damage = damage
        self.rect.centerx = posX
        self.rect.centery = posY

    def track_ally(self):
        self.rect.right += self.speed

    def track_enemy(self):
        self.rect.right -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
