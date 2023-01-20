'''
    PROYECTO FINAL - SISTEMAS EMPOTRADOS
    FECHA: 18/10/2021
    Elaboro: Equipo Powerbits
'''
import pygame

class Enemigo(pygame.sprite.Sprite):
    # INICIALIZACION
    def __init__(self, posY, speed, damage):
        super().__init__()
        self.image = pygame.image.load("resources/enemy/enemy1.png") #Loading the image of the enemy
        #self.image = pygame.transform.rotate(self.image, 90) #Rotating the enemy 90°
        self.rect = self.image.get_rect() #The rectangle in which the enemy is going to be drwan
        self.speed = speed
        self.damage = damage
        self.rect.left = 1270
        self.rect.top = posY

    def track(self):
        self.rect.left -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect) #Drawing the enemy in the screan

    def lifePerLevel(self, life):
        self.life = life

    def damagePerLevel(self, damage):
        self.damage = damage

    def speedPerLevel(self, speed):
        self.speed = speed