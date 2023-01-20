import pygame, random

WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)

class Stars(pygame.sprite.Sprite):
    images = ""
    aceleracion = 0
    def __init__(self):
        super().__init__()
        i = random.randint(0, 11)
        self.image = self.images[i].convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH+50, WIDTH+1000)
        self.rect.y = random.randrange(0, HEIGHT-10)
        self.speed_x = random.randrange(-10, -5)

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < -10:
            i = random.randint(0, 11)
            self.image = self.images[i]
            self.image.set_colorkey(BLACK)
            self.rect.x = random.randrange(WIDTH+50, WIDTH+1000)
            self.rect.y = random.randrange(0, HEIGHT - 10)
        if self.aceleracion == 5:
            self.speed_x = random.randrange(-300, -200)
        if self.aceleracion == 4:
            self.speed_x = random.randrange(-100, -75)
        if self.aceleracion == 3:
            self.speed_x = random.randrange(-75, -40)
        if self.aceleracion == 2:
            self.speed_x = random.randrange(-40, -20)
        if self.aceleracion == 1:
            self.speed_x = random.randrange(-20, -7)