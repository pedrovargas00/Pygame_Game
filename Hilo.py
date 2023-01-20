from threading import Thread
import sys, time

class Hilo(Thread):

   def __init__(self):
      Thread.__init__(self)

   def run(self):
      #Aqui el codigo del hilo
      time.sleep(2)
      sys.exit()
      
      print("Tiempo: ") #int(time.time() - self.start))
      #if int(time.time() - self.start) % 3 == 0:
      #self.backg = pygame.image.load("resources/Fondos/planeta.png")
...
# Arranque del hilo
#hilo = MiHilo()
#hilo.start()