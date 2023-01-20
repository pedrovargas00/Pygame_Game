import pygame, time, sys
from pygame.locals import *

import Principal

class Levels(pygame.sprite.Sprite):

   def __init__(self):
      pygame.init()
      self.WIDTH = 1280
      self.HEIGHT = 720
      pygame.display.set_caption("Powerbits")
      self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
      self.backg = pygame.image.load('resources/Fondos/Negro.jpg').convert()
      self.im = pygame.image.load('resources/Items/Saturno.png')
      self.image = pygame.transform.scale(self.im, (100, 75))
      self.rect = self.image.get_rect()
      self.backg.set_colorkey((0, 0, 0))
      self.font = pygame.font.Font("resources/Font/Eight-Bit-Madness.ttf", 100)
      self.font1 = pygame.font.Font("resources/Font/Eight-Bit-Madness.ttf", 50)
      #self.start = time.time() + 1
      self.start = 0
      self.level1 = Principal.Principal(0, 10)
      self.level2 = Principal.Principal(5, 15)
      self.level3 = Principal.Principal(10, 20)

   def convert(self, imgPlanet, scaleX, scaleY):
      self.im = pygame.image.load('resources/Items/' + imgPlanet + '.png')
      self.image = pygame.transform.scale(self.im, (scaleX, scaleY))
      #self.image = pygame.transform.scale(self.im, (150, 150)) #Mars & Venus
      #self.image = pygame.transform.scale(self.im, (125, 100)) Saturn
      self.rect = self.image.get_rect()

   def transition(self, level, planet, imgPlanet, scaleX, scaleY, posX, posY):
      
      self.start = time.time() - 1
      running = True
      self.convert(imgPlanet, scaleX, scaleY)
      self.rect.x = posX
      self.rect.y = posY
      #Mars & Venus
      #self.rect.x = 675
      #self.rect.y = 340
      #Saturn
      #self.rect.x = 675
      #self.rect.y = 360
      #print("Start ", self.start)
      while running: #int(time.time() - star) % 10 == 0:
         pygame.time.Clock().tick(60) #FPS
         self.screen.blit(self.backg, (0, 0))
         #print("Dibuja - ", int(time.time() - self.start), " -- ", int(time.time() - self.start) % 15)
         if int(time.time() - self.start) % 8 == 0:
            running = False
         title = self.font.render(level, False, (255, 255, 255))
         namePlanet = self.font1.render(planet, False, (255, 255, 255))
         self.screen.blit(title, (480, 200))
         self.screen.blit(namePlanet, (475, 400))
         self.screen.blit(self.image, self.rect)
         pygame.display.flip()

   def screenEnd(self, text):

      running = True
      self.start = time.time() - 1

      while running: #int(time.time() - star) % 10 == 0:
         pygame.time.Clock().tick(60) #FPS
         self.screen.blit(self.backg, (0, 0))
         #print("Dibuja - ", int(time.time() - self.start), " -- ", int(time.time() - self.start) % 15)
         if int(time.time() - self.start) % 5 == 0:
            running = False
         end = self.font.render(text, False, (255, 255, 255))
         self.screen.blit(end, (480, 200))
         pygame.display.flip()

   def level1Init(self):
      self.level1.init(5, 10, 8, 20, 15, 30, 1, 200, 50, "Jefe_1", 15, 910, 660, 1.05)
      if self.level1.gameOverFlag:
         star = time.time() - 1
         while int(time.time() - star) % 3 != 0:
            #print("Star: ", star, " -- ", int(time.time() - star))
            self.level1.gameOverFunc()
         sys.exit()

   def level2Init(self):
      self.level2.init(4.5, 10, 10, 25, 20, 40, 2, 300, 70, "Jefe_2", 20, 850, 660, 1.03)
      if self.level2.gameOverFlag:
         star = time.time() - 1
         while int(time.time() - star) % 3 != 0:
            #print("Star: ", star, " -- ", int(time.time() - star))
            self.level2.gameOverFunc()
         sys.exit()

   def level3Init(self):
      self.level3.init(4, 20, 12, 12, 30, 25, 3, 500, 90, "Jefe_3", 25, 680, 660, 1.01)
      if self.level3.gameOverFlag:
         star = time.time() - 1
         while int(time.time() - star) % 3 != 0:
            #print("Star: ", star, " -- ", int(time.time() - star))
            self.level3.gameOverFunc()
         sys.exit()

   def init(self):
      print("Inicia nivel 1")
      self.transition("Level 1", "Saturn", "Saturno", 125, 100, 675, 360)
      self.level1Init()
      print("Inicia nivel 2")
      self.transition("Level 2", "Venus", "Venus", 150, 150, 675, 340)
      self.level2Init()
      print("Inicia nivel 3")
      self.transition("Level 3", "Mars", "Marte", 150, 150, 675, 340)
      self.level3Init()
      self.screenEnd("End")

#if __name__ == "__main__":
#   l = Levels()
#   l.transition("Level 1", "Saturn", "Saturno", 125, 100, 675, 360)