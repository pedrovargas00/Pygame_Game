import pygame, sys, time
from pygame.locals import *

import Levels

class Menu(pygame.sprite.Sprite):
   # INICIALIZACION

   def __init__(self):
      super().__init__()
      pygame.init()
      self.WIDTH = 1280
      self.HEIGHT = 720
      pygame.display.set_caption("Powerbits")
      self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
      self.backg = pygame.image.load('resources/Fondos/Inicio.jpg').convert()
      self.backg.set_colorkey((0, 0, 0))
      self.state = "Start"
      self.levels = Levels.Levels()

   def drawText(self, text, nFont, x, y, color):
      font = pygame.font.Font("resources/Font/Eight-Bit-Madness.ttf", nFont)
      text_surface = font.render(text, True, color)
      self.screen.blit(text_surface, (x, y))

   def displayMenu(self):
      #print("Entra a displayMenu")
      
      self.drawText("Start game", 50, 515, 450, (92, 187, 241))
      self.drawText("Credits", 50, 555, 510, (255, 255, 255))
      self.drawText("Exit", 50, 590, 590, (255, 255, 255))
      while True:
         pygame.time.Clock().tick(60) #FPS
         self.screen.blit(self.backg, (0, 0))
         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
            elif event.type == pygame.KEYDOWN:
               self.events(event)
               self.input(event)
         self.drawText("POWERBITS", 100, 430, 100, (255, 255, 255))
         #self.drawText("=> ", 30, self.cursor.x, self.cursor.y)
         #print("X: ", self.cursor.x, " Y: ", self.cursor.y)
         pygame.display.flip()

   def events(self, event):
      #print("Entra a events")
      if event.key == K_DOWN:
         if self.state == 'Start':
            #print("Estado: ", self.state)
            self.drawText("Start game", 50, 515, 450, (255, 255, 255))
            self.drawText("Credits", 50, 555, 510, (92, 187, 241))
            self.state = 'Credits'
            #print("Estado: ", self.state)
         elif self.state == 'Credits':
            #print("Estado: ", self.state)
            self.drawText("Credits", 50, 555, 510, (255, 255, 255))
            self.drawText("Exit", 50, 590, 590, (92, 187, 241))
            self.state = 'Exit'
            #print("Estado: ", self.state)
         elif self.state == 'Exit':
            #print("Estado: ", self.state)
            self.drawText("Exit", 50, 590, 590, (255, 255, 255))
            self.drawText("Start game", 50, 515, 450, (92, 187, 241))
            self.state = 'Start'
            #print("Estado: ", self.state)
      elif event.key == K_UP:
         if self.state == 'Start':
            self.drawText("Start game", 50, 515, 450, (255, 255, 255))
            self.drawText("Exit", 50, 590, 590, (92, 187, 241))
            self.state = 'Exit'
         elif self.state == 'Exit':
            self.drawText("Exit", 50, 590, 590, (255, 255, 255))
            self.drawText("Credits", 50, 555, 510, (92, 187, 241))
            self.state = 'Credits'
         elif self.state == 'Credits':
            self.drawText("Credits", 50, 555, 510, (255, 255, 255))
            self.drawText("Start game", 50, 515, 450, (92, 187, 241))
            self.state = 'Start'

   def input(self, event):
      #print("Entra a input")
      if event.key == K_RETURN:
         if self.state == 'Start':
            #self.game.playing = True
            print("Ejecuta juego")
            self.levels.init()
         elif self.state == 'Credits':
            #self.game.curr_menu = self.game.options
            print("Creditos")
            self.creditsDisplay(event)
         elif self.state == 'Exit':
            pygame.quit()
            sys.exit()

   def creditsDisplay(self, event):
      
      '''pygame.time.Clock().tick(60) #FPS
      #self.screen.blit(self.backg, (0, 0))
      if event.key == K_ESCAPE:
         self.displayMenu()
         self.run_display = False
      self.backg.blit(self.backg, (0, 0))
      #self.drawText('Equipo Powerbits', 70, 430, 100, (255, 255, 255))
      self.drawText('Marti Galdino Castillo Avila', 50, 350, 170, (255, 255, 255))
      self.drawText('Maria Fernanda Merlo Simoni', 50, 350, 230, (255, 255, 255))
      self.drawText('Pedro Vargas Arenas', 50, 350, 280, (255, 255, 255))
      self.drawText('Damian Eli Garcia Corte', 50, 340, 170, (255, 255, 255))
      self.drawText('Julio Papaqui Cortes', 50, 350, 400, (255, 255, 255))
      self.screen.blit(self.screen, (0, 0))'''
      pygame.display.flip()
   
   

#Llamada a init
if __name__ == "__main__":
    principal = Menu()
    principal.displayMenu()