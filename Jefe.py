import pygame

class Jefe(pygame.sprite.Sprite):

    # INICIALIZACION
    def __init__(self, posY, life, damage, ruta):
        super().__init__()
        self.image = pygame.image.load("resources/Enemigos/" + ruta +".png")
        self.rect = self.image.get_rect()
        self.speed = 5
        self.MAX_LIFE = life
        self.speedForward = 0.2
        self.life = life
        self.damage = damage
        self.rect.left = 1170
        self.rect.top = posY
    
    def moveForward(self):
        if self.rect.centerx >= 1100:
            self.rect.centerx -= self.speedForward
            return True
        else:
            return False
    
    def impact(self, damage):
        self.life -= damage
    
    def isDead(self):
        if self.life <= 0:
            return True
        else:
            return False
    def get_max_life(self):
        return self.MAX_LIFE

    def track(self):
        if self.rect.centery >= 600:
            self.speed = -5
        if self.rect.centery <= 140:
            self.speed = 5
            
        self.rect.centery += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect) #Drawing the enemy in the screan