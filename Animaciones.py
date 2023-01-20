#PRUEBAS EN PYGAME - PROYECTO FINAL SISTEMAS EMPOTRADOS
import pygame, os, time
from Explosion import Explosion
from Destello import Destello
from Stars import Stars

class Animaciones(pygame.sprite.Sprite):

    def __init__(self, screen):
        #---------------------------------------------------------------
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.BLACK = (0, 0, 0)
        #-------------------------INICIALIZACION DE PYGAME-------------------------
        pygame.init()
        pygame.mixer.init()
        self.screen = screen
        pygame.display.set_caption("Powerbits")
        self.clock = pygame.time.Clock()
        self.estrellas = pygame.sprite.Group()
        self.explosiones = pygame.sprite.Group()
        self.efectos = pygame.sprite.Group()
        self.running = True
        self.acelerar = False
        self.desacelerar = False
        self.tiempo = -1
        self.pantalla_info = False
        self.tiempo_cambiar_pantalla = -1
        self.bg = pygame.image.load("resources/Fondos/fondo.jpg")

#-----------INICIALIZACION DE ESTRELLAS, EXPLOSIONES Y DESTELLOS-----------

    def setStar(self):
        self.init_stars()

    def initStars(self):
        stars_images = []
        for i in range(0, 12):
            path_image = 'resources/Estrellas/Star_' + repr(i) + '.png'
            stars_images.append(pygame.image.load(path_image).convert_alpha())
        Stars.images = stars_images

    def initExplosion(self):
        animacion_explosion = {'t1': [], 't2': [], 't3': [], 't4': []}
        for x in range(20):
            archivo_explosiones = repr(x) + '.gif'
            imagenes = pygame.image.load(os.path.join('resources/Explosion/', archivo_explosiones)).convert()
            imagenes.set_colorkey(self.BLACK)
            imagenes_t1 = pygame.transform.scale(imagenes, (32,32))
            animacion_explosion['t1'].append(imagenes_t1)
            imagenes_t1 = pygame.transform.scale(imagenes, (64, 64))
            animacion_explosion['t2'].append(imagenes_t1)
            imagenes_t1 = pygame.transform.scale(imagenes, (128, 128))
            animacion_explosion['t3'].append(imagenes_t1)
            imagenes_t1 = pygame.transform.scale(imagenes, (1000, 1000))
            animacion_explosion['t4'].append(imagenes_t1)
        Explosion.animacion = animacion_explosion

    def initFlash(self):
        animacion_destello = {'t1': [], 't2': [], 't3': [], 't4': []}
        for x in range(113):
            archivo_destello = repr(x) + '.png'
            imagenes = pygame.image.load(os.path.join('resources/Destello/', archivo_destello)).convert_alpha()
            imagenes.set_colorkey(self.BLACK)
            imagenes_t1 = pygame.transform.scale(imagenes, (32,32))
            animacion_destello['t1'].append(imagenes_t1)
            imagenes_t1 = pygame.transform.scale(imagenes, (64, 64))
            animacion_destello['t2'].append(imagenes_t1)
            imagenes_t1 = pygame.transform.scale(imagenes, (128, 128))
            animacion_destello['t3'].append(imagenes_t1)
            imagenes_t1 = pygame.transform.scale(imagenes, (1280, 720))
            animacion_destello['t4'].append(imagenes_t1)
        Destello.animacion = animacion_destello

    #-----------------------DEFINICIÓN DE FUNCIONES----------------------------

    #GENERA UNA EXPLOSION EN EL LUGAR Y DEL TAMAÑO Y FRECUENCIA INDICADOS
    def generar_explosion(self, x, y, tamano, fps):
        # tamano = 't1' o 't2' o 't3' o 't4'
        aux = Explosion((x, y), tamano, fps)
        self.explosiones.add(aux)

    #GENERA UN DESTELLO EN EL LUGAR Y DEL TAMAÑO Y FRECUENCIA INDICADOS
    def generar_destello(self, x, y, tamano, fps):
        aux = Destello((x, y), tamano, fps)
        self.efectos.add(aux)

    #EFECTO DEL CAMBIO DE PANTALLA (TRAS DERROTAR A UN JEFE)
    def efecto_cambiar_pantalla(self):
        self.generar_explosion(1000, 360, 't4', 70)
        self.generar_destello(640, 360, 't4', 35)
        self.estrellas = pygame.sprite.Group()

    #FUNCIONES UTILIZADAS PARA LOS EFECTOS
    def acelerar_estrellas(self):
        Stars.aceleracion += 1
        if Stars.aceleracion > 5:
            Stars.aceleracion = 5
        return time.time()

    def desacelerar_estrellas(self):
        Stars.aceleracion -= 1
        if Stars.aceleracion < 0:
            Stars.aceleracion = 0
        return time.time()

    #EFECTO DE ACELERACION DE ESTRELLAS (ALTA VELOCIDAD)
    def animacion_acelerar(self):
        esperar = 1
        if self.acelerar:
            if Stars.aceleracion == 4:
                esperar = 3
                self.generar_destello(640, 360, 't4', 35)
                self.estrellas = pygame.sprite.Group()
            if self.tiempo == -1:
                self.tiempo = self.acelerar_estrellas()
            if time.time() - self.tiempo > esperar:
                if Stars.aceleracion < 5:
                    self.tiempo = self.acelerar_estrellas()
                else:
                    self.acelerar = False
                    self.desacelerar = True
                    #self.bg = pygame.image.load("resources/Fondos/planeta.png")
        esperar = 1
        if self.desacelerar:
            if self.tiempo == 5:
                self.tiempo = self.desacelerar_estrellas()
            if time.time() - self.tiempo > esperar:
                if Stars.aceleracion > 1:
                    self.tiempo = self.desacelerar_estrellas()
                else:
                    self.tiempo = -1
                    self.acelerar = False
                    self.desacelerar = False
        #return acelerar, desacelerar, tiempo, estrellas, bg
        #return self.bg

    #IR A LA PANTALLA PRINCIPAL
    def pantalla_principal(self):
        main_menu = True
        main_image = pygame.image.load("resources/Fondos/Inicio.jpg")
        while main_menu:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.screen.blit(main_image, (0, 0))
            pygame.display.update()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_RETURN]:
                main_menu = False

    #INICIALIZA LAS ESTRELLAS
    def init_stars(self):
        for i in range(0, 20):
            aux = Stars()
            self.estrellas.add(aux)

    #INICIALIZA LOS EFECTOS DEL MUNDO (ESTRELLAS, FONDO, ETCETERA)
    def init_world(self):
        self.estrellas = pygame.sprite.Group()
        self.explosiones = pygame.sprite.Group()
        self.efectos = pygame.sprite.Group()
        self.init_stars()
        self.running = True
        self.acelerar = False
        self.desacelerar = False
        self.tiempo = -1
        self.pantalla_info = False
        self.tiempo_cambiar_pantalla = -1
        self.bg = pygame.image.load("resources/Fondos/fondo.jpg")

    def setAll(self):
        #self.pantalla_principal()
        self.initStars()
        self.initExplosion()
        self.initFlash()
        self.setStar()
#-----------------------------CICLO PRINCIPAL----------------------------------
    def init(self):
        #Se inicializa el mundo
        #estrellas,explosiones,efectos,running,acelerar,desacelerar,tiempo,pantalla_info,tiempo_cambiar_pantalla,bg = init_world()
        self.setAll()
        while self.running:
            self.clock.tick(60)  #60 Cuadros por segundo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # ------------------ACTIVAR ANIMACIONES------------------
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                self.generar_explosion(300, 200, 't2', 60)
            if keystate[pygame.K_DOWN]:
                self.efecto_cambiar_pantalla()   #Si se presiona Abajo, se realiza el efecto cambiar pantalla
                self.pantalla_info = True
            if keystate[pygame.K_RIGHT]:
                self.acelerar = True     #Si se presiona Derecha, se realiza el efecto de alta velocidad
            if keystate[pygame.K_RETURN]:   #Reiniciar mundo
                self.init_world() #estrellas,explosiones,efectos,running,acelerar,desacelerar,tiempo,pantalla_info,tiempo_cambiar_pantalla,bg = 

            #--------------CONTROL DE ANIMACION ACELERAR ESTRELLAS--------------
            #acelerar, desacelerar, tiempo, estrellas, bg = self.animacion_acelerar(acelerar, desacelerar, tiempo, estrellas, bg)
            self.animacion_acelerar()
            # -------------------------------------------------------

            self.explosiones.update()
            self.estrellas.update()
            self.efectos.update()
            self.screen.blit(self.bg, (0, 0))
            self.explosiones.draw(self.screen)
            self.efectos.draw(self.screen)
            self.estrellas.draw(self.screen)
            pygame.display.flip()

#Llamada a init
#if __name__ == "__main__":
#    a = Animaciones(pygame.display.set_mode((1280, 720)))
#    a.init()
