import pygame, sys, time
from pygame.locals import *
from random import randint
from pygame import mixer
from HiloAsteroides import HiloAsteroides

#Clases
import Jugador, Enemigo, Disparo, Heart, PlanetaInfo, Asteroide, Jefe, DisparoJefe, Animaciones, Hilo, HiloAsteroides, DisparoEspecialJefe
#Animaciones

class Principal(pygame.sprite.Sprite):

    def __init__(self, nAsteroids, nEnemies):
        pygame.init()
        self.start_enemy = time.time() + 1
        self.start_boss = time.time() + 1
        self.start_boss_especial = time.time() + 1
        self.start = 0  
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLACK = (0,0,0)
        self.WIDTH = 1280
        self.HEIGHT = 720
        #self.animations = Animaciones
        pygame.display.set_caption("Powerbits")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.backg = pygame.image.load('resources/Fondos/Fondo.jpg').convert()
        self.font = pygame.font.Font("resources/Font/Eight-Bit-Madness.ttf", 50)
        self.animations = Animaciones.Animaciones(self.screen)
        self.tablet = PlanetaInfo.PlanetaInfo()
        self.thread = Hilo.Hilo()
        self.threadAs = HiloAsteroides.HiloAsteroides()
        self.treadAct = True
        self.bossDeath = False
        self.gameOverFlag = False
        self.animations.setAll()
        self.HEART_DISTANCE = 90
        #self.EXTRA_LIFE_POINTS = 3
        self.contador = 0
        self.points = 0
        self.liveIndex = 420
        self.enemiesEli = 0
        self.nAsteroids = nAsteroids
        self.nEnemies = nEnemies
        self.hearts = pygame.sprite.Group()
        self.ally = pygame.sprite.Group()
        self.boss = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.shot_ally = pygame.sprite.Group()
        self.shot_boss = pygame.sprite.Group()
        self.special_shot = pygame.sprite.Group()
        self.shot_enemy = pygame.sprite.Group()
        self.planet = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.all = pygame.sprite.Group()
        self.damage = None
        self.destroySound = None
        self.shootSounfEffect = None
        self.extraLife = None
        self.game_over = None
        self.bossShootSound = None
        self.bossEspecialSound = None

    def setThreadAS(self):
        self.threadAs = HiloAsteroides.HiloAsteroides()
        self.threadAs.start()

    def setPoints(self):
        self.points += 1
    
    def gameOverFunc(self):
        fontG_O = pygame.font.Font("resources/Font/Eight-Bit-Madness.ttf", 80)
        gameOver = fontG_O.render("GAME OVER", False, (255, 255, 255)) #Creating the text to display life
        self.screen.blit(gameOver, (480, 200))
        self.gameOverFlag = True

    def initSounds(self):
        pygame.mixer.init()
        self.damage = mixer.Sound('resources/sounds/damage.wav')
        self.destroySound = mixer.Sound("resources/sounds/explosion.wav")
        self.shootSounfEffect = mixer.Sound("resources/sounds/laser2.wav")
        self.extraLife = mixer.Sound("resources/sounds/extraLife.wav")
        self.game_over = mixer.Sound("resources/sounds/gameOver.wav")
        self.bossShootSound = mixer.Sound('resources/sounds/laser.wav')
        self.bossEspecialSound = mixer.Sound('resources/sounds/especialShoot.wav')
        self.damage.set_volume(0.1)
        self.destroySound.set_volume(0.1)
        self.shootSounfEffect.set_volume(0.1)
        self.extraLife.set_volume(0.1)
        self.game_over.set_volume(0.1)
        self.bossShootSound.set_volume(0.1)
        self.bossEspecialSound.set_volume(0.1)
        mixer.music.load('resources/sounds/background.wav')
        mixer.music.set_volume(0.1)
        mixer.music.play(-1) #This line plays the background music in a loop so it never ends

    def createHearts(self): #This function creates all three hearts
        posX = 420
        aux = 0
        for i in range(3):
            heart = Heart.Heart(posX-aux)
            self.hearts.add(heart)
            self.all.add(heart)
            aux += self.HEART_DISTANCE
    
    def updateHearts(self): #This function is going to create hearts in case the nave scores a certain amount of points
        x_maximo = 0
        for heart in self.hearts:
            if heart.rect.centerx > x_maximo:
                x_maximo = heart.rect.centerx
        #if x_maximo == 420:
        #    pass
        new_heart = Heart.Heart(x_maximo+self.HEART_DISTANCE)
        self.hearts.add(new_heart)
        self.all.add(new_heart)
        #Don't forget to increase nave's lives by 1
        
    def deleteHearts(self): #This function deletes heart by heart
        aux_heart = None
        x_maximo = 0
        for heart in self.hearts:
            if heart.rect.centerx > x_maximo:
                x_maximo = heart.rect.centerx
                aux_heart = heart        
        self.hearts.remove(aux_heart)
        self.all.remove(aux_heart)

    def checknEnemies(self):
        if (self.enemiesEli + len(self.enemies)) == self.nEnemies:
            return True
        return False

    def enemy(self, y, speedEnemy, damageEnemy, speedShoot, damageShoot):
        enemigo = Enemigo.Enemigo(y, speedEnemy, damageEnemy)
        shot_en = Disparo.Disparo(enemigo.rect.centerx, enemigo.rect.centery, 90, speedShoot, damageShoot)
        self.shot_enemy.add(shot_en)
        self.all.add(shot_en)
        self.enemies.add(enemigo)
        self.all.add(enemigo)

    def bossShoots(self, jefe, nave):
        if len(self.boss) > 0:
            if int(time.time() - self.start_boss) % 3 == 0:
                self.start_boss += 1
                bossShot = DisparoJefe.DisparoJefe(jefe.rect.centerx, jefe.rect.centery, 270, 20, 70)
                self.bossShootSound.play() #Playing the bullet sound effect
                self.shot_boss.add(bossShot)
                self.all.add(bossShot)
            if int(time.time() - self.start_boss_especial) % 20 == 0:
                self.start_boss_especial += 10 
                bossShot = DisparoEspecialJefe.DisparoEspecialJefe(jefe.rect.centerx, jefe.rect.centery, 270, 20, 100)
                self.bossEspecialSound.play() #Playing the bullet sound effect
                self.shot_boss.add(bossShot)
                self.all.add(bossShot)
            if len(self.shot_boss) > 0:
                for x in self.shot_boss:
                    x.track_enemy()
                    if x.rect.right < 0: #If the bullet is out of the screen we delete it
                        self.shot_boss.remove(x)
                        self.all.remove(x)
                    elif pygame.sprite.spritecollide(x, self.ally, False): #If the bullet collides with the spaceship then we delete the bullet
                        nave.impactBoss(x.getDamage())
                        self.destroySound.play()  #Playing the sound of an explosion
                        self.shot_boss.remove(x)
                        self.all.remove(x)
    
    def checkSpaceshipHealth(self, nave):
        if nave.life <= 0:
            nave.life = 100
            nave.lives -= 1
            self.destroySound.play()  #Playing the sound of an explosion
            self.animations.generar_explosion(nave.rect.centerx, nave.rect.centery, 't2', 60)
            nave.changeLiveImage(nave.rect.centerx, nave.rect.centery) #Calling the function tha will change the image of nave
            self.deleteHearts()
            if nave.lives == 0:
                self.life = 0
                self.ally.remove(nave)
                self.all.remove(nave)
                self.game_over.play() #Game over sound effect
                self.gameOverFunc()
                return True
            else: 
                return False

    def checkEnemyDeletion(self, nave):
        if len(self.enemies) > 0:
            for x in self.enemies:
                x.track()
                if x.rect.right < 20: #If the enemy is on the other side of the screen then we delete it from all sprite groups
                    self.enemies.remove(x)
                    self.enemiesEli += 1
                    self.all.remove(x)
                elif pygame.sprite.spritecollide(x, self.ally, False):#Colisión entre enemigo y jugador
                    self.enemiesEli += 1
                    self.enemies.remove(x)
                    self.all.remove(x)
                    nave.impact(x.damage) #This function subtracks 30 to variable life
                    self.damage.play() #A sound effect is played
                    self.colisionNave(x, nave)

    def colisionNave(self, x, nave):
        #print("Tipo: ", type(x))
        if(type(x) == Disparo.Disparo):
            self.shot_enemy.remove(x)
        else:
            self.enemies.remove(x)
            self.enemiesEli += 1
        self.all.remove(x)
        nave.impact(x.damage) #This function subtracks 30 to variable life
        self.damage.play() #A sound effect is played

    def creationEnemys(self, speedEnemy, damageEnemy, speedShoot, damageShoot):#Creación de enemigos
        #print("Tiempo: ", (int(time.time() - self.start_time) % 3))
        if int(time.time() - self.start_enemy) % 3 == 0:
            self.start_enemy += 1
            self.enemy(randint(2, 650), speedEnemy, damageEnemy, speedShoot, damageShoot) #Generate an enemy at random position

    def checksExtraLife(self, nave, lifePoints):
        if self.points != 0:
            if self.points%lifePoints == 0: #self.EXTRA_LIFE_POINTS #If we reach a certain amount of points, the nave's lives increases by 1
                if nave.lives < 3:
                    self.updateHearts()
                    nave.increaseLive()
                    nave.changeLiveImage(nave.rect.centerx, nave.rect.centery)
                    self.extraLife.play()

    def shotAlly(self, nave, jefe, lifePoints):
        #Disparo Aliado
        if len(self.shot_ally) > 0:
            for x in self.shot_ally:
                x.track_ally()
                if x.rect.right > 1280: #If the bullet is out of the screen we delete it
                    self.shot_ally.remove(x)
                    self.all.remove(x)
                elif pygame.sprite.spritecollide(x, self.enemies, True): #If the bullet collides with any enemy then we delete the bullet
                    self.enemiesEli += 1
                    self.destroySound.play()  #Playing the sound of an explosion
                    self.shot_ally.remove(x)
                    self.all.remove(x)
                    self.points += 1
                    self.checksExtraLife(nave, lifePoints)
                elif pygame.sprite.spritecollide(x, self.boss, False): #If the bullet hits the final boss we execute the impact function
                    jefe.impact(nave.damage)
                    self.destroySound.play()  #Playing the sound of an explosion
                    self.shot_ally.remove(x)
                    self.all.remove(x)
                    self.points += 1
                    self.deathBoss(jefe)
                    self.checksExtraLife(nave, lifePoints)           

    def checkEventsGameOver(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def shotEnemy(self, nave, lifePoints):
        #Disparo Enemigo
        #print("Disparo: ", len(self.shot_enemy))
        #print("Enemigo: ", len(self.enemies))
        if len(self.shot_enemy) > 0:
            for x in self.shot_enemy:
                #print("Entra a disparo enemigo")
                x.track_enemy()
                if x.rect.right < 10: #If the bullet is out of the screen we delete it
                    self.shot_enemy.remove(x)
                    self.all.remove(x)
                elif pygame.sprite.spritecollide(x, self.ally, False): #If the bullet collides with any enemy then we delete the bullet
                    #self.points += 1
                    self.checksExtraLife(nave, lifePoints)
                    return self.colisionNave(x, nave)

    def asteroidsGen(self):
        #print("Crea asteriode")
        a = Asteroide.Asteroide(randint(2, 650))
        self.asteroids.add(a)
        self.all.add(a)

    def asteroidsPhy(self, nave):
        #print("Lon: ", len(enemies))
        #Acción enemiga
        if len(self.asteroids) > 0:
            for x in self.asteroids:
                x.track()
                if x.rect.right < 20: #If the enemy is on the other side of the screen then we delete it from all sprite groups
                    self.asteroids.remove(x)
                    self.all.remove(x)
                elif pygame.sprite.spritecollide(x, self.ally, False):#Colisión entre enemigo y jugador
                    self.destroySound.play()  #Playing the sound of an explosion
                    self.asteroids.remove(x)
                    self.all.remove(x)
                    nave.impact(50)
                    #Pierde vida

    def events(self, nave, flag, speed):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    if flag:
                        shot_al = Disparo.Disparo(nave.rect.centerx, nave.rect.centery, 270, speed)
                        self.shootSounfEffect.play() #Playing the bullet sound effect
                        self.shot_ally.add(shot_al)
                        self.all.add(shot_al)

                if event.key == K_RETURN:
                    print("Disparo y colisión de proyectil especial")
        keystate = pygame.key.get_pressed()
        if keystate[K_UP]:
            nave.rect.top -= nave.speed
        if keystate[K_DOWN]:
            nave.rect.bottom += nave.speed

    def setGameOver(self, nave, lifePoints):
        if self.shotEnemy(nave, lifePoints) or self.checkSpaceshipHealth(nave):
            return True
        return False

    def generateBoss(self, bossAdded, jefe, bossApper, nave):
        
        activateAB = True
        
        if not bossAdded:
            mixer.music.stop()
            mixer.music.load("resources/sounds/here-comes-the-boss.wav")
            mixer.music.play(-1) 
            self.boss.add(jefe)
            self.all.add(jefe)
            bossAdded = True
            activateAB = False
        if bossApper:
            bossApper = jefe.moveForward()
        else:
            activateAB = True
            self.bossShoots(jefe, nave)
            jefe.track()
        
        return activateAB      
    
    def createHealthBar(self, jefe,x,y,z):
      pygame.draw.rect(self.screen, self.BLACK, (x,y-7, (jefe.get_max_life()*z), 50))
      pygame.draw.rect(self.screen, self.RED, (x+5,y, (jefe.get_max_life()), 35))
      pygame.draw.rect(self.screen, self.GREEN, (x+5,y, (jefe.life), 35))


    def deathBoss(self, jefe):
        if jefe.isDead():
            #print("Entra a muerte")
            self.boss.remove(jefe)
            self.all.remove(jefe)
            if len(self.shot_boss) > 0:
                for x in self.shot_boss:
                    self.shot_boss.remove(x)
                    self.all.remove(x)
            mixer.music.stop()
            #animación
#----------------------------------------------------------------
            self.animations.efecto_cambiar_pantalla()
            if self.treadAct:
                self.thread.start()
                self.treadAct = False
                self.start = time.time() + 1
            #self.thread.join()
            #print("Tiempo: ", int(time.time() - self.start))
            if not self.thread.is_alive():
                #print("Cambio")
                self.backg = pygame.image.load("resources/Fondos/planeta.png")
                self.planet.add(self.tablet)
                self.all.add(self.planet)
                self.bossDeath = True
            #self.animations.pantalla_info = True


    def restart(self):
        self.points = 0
        self.life = 3

    def init(self, speedPlayer, speedShootAl, speedEnemy, damageEnemy, speedShoot, damageShoot, n, lifeBoss, damageBoss, ruta, lifePoints, xCoor, yCoor, barPadding):
        self.initSounds() #Initializing all sounds and pygame.mixer
        #clk = pygame.time.Clock()
        #Instancias
        nave = Jugador.Jugador(speedPlayer) #Creating the player
        #tablet = PlanetaInfo.PlanetaInfo()#-----------------------
        #self.planet.add(tablet) #-----------------------
        self.ally.add(nave)      #Adding the nave to the ally list
        self.all.add(self.ally)  #Adding the ally to all
        #self.all.add(self.planet) #-----------------------
        self.createHearts()                 #This function creates the hearts 
        self.threadAs.start()
        jefe = Jefe.Jefe(randint(100, 600), lifeBoss, damageBoss, ruta) #This line creates the boss
        gameOver = False
        #Creating variables to control the spwan of the final boss
        bossAdded = False
        bossApper = True
        activateAllyBullets = True
        #Ciclo de juego
        while not gameOver:
            pygame.time.Clock().tick(60) #FPS
            self.screen.blit(self.backg, (0, 0)) #Painting the BG
            score = self.font.render("Points   " + str(self.points), False, (255, 255, 255)) #Creating the text to display score
            life = self.font.render("Life   " + str(nave.life), False, (255, 255, 255)) #Creating the text to display life
            self.screen.blit(score, (1000, 0)) #Painting the score in the screen
            self.screen.blit(life, (100, 0)) #Painting life in the screen
            nave.movement()               #Checks if the nave can move
            if self.points >= self.nEnemies:
                if not self.bossDeath:
                    self.deathBoss(jefe)
                #activateAllyBullets = self.generateBoss(bossAdded, jefe, bossApper, nave)
                if not bossAdded:
                    mixer.music.stop()
                    mixer.music.load("resources/sounds/here-comes-the-boss.wav")
                    mixer.music.play(-1) 
                    self.boss.add(jefe)
                    self.all.add(jefe)
                    bossAdded = True
                    activateAllyBullets = False
                if bossApper:
                    bossApper = jefe.moveForward()
                    #print("Movimiento")
                else:
                    if not jefe.isDead():
                        self.createHealthBar(jefe, xCoor, yCoor, barPadding)
                    activateAllyBullets = True
                    self.bossShoots(jefe, nave)
                    jefe.track()
            else:
                self.creationEnemys(speedEnemy, damageEnemy, speedShoot, damageShoot)
            self.checkEnemyDeletion(nave)
            gameOver = self.setGameOver(nave, lifePoints)
            self.shotAlly(nave, jefe, lifePoints)
            self.asteroidsPhy(nave)
            if not self.threadAs.is_alive():
                self.asteroidsGen()
                self.setThreadAS()
            self.events(nave, activateAllyBullets, speedShootAl)
            self.all.draw(self.screen)
            if self.bossDeath:
                if n == 1:
                    self.tablet.saturn(self.screen) #------------------------------
                if n == 2:
                    self.tablet.venus(self.screen) #------------------------------
                if n == 3:
                    self.tablet.mars(self.screen) #------------------------------
                if int(time.time() - self.start) % 15 == 0:
                    gameOver = True
            #print("Enemigos: ", self.enemiesEli + len(self.enemies))
            #self.backg = self.animations.animacion_acelerar()
            #self.animations.animacion_acelerar()
            self.animations.explosiones.update()
            self.animations.estrellas.update()
            self.animations.efectos.update()
            self.animations.explosiones.draw(self.screen)
            self.animations.efectos.draw(self.screen)
            self.animations.estrellas.draw(self.screen)
            #print("N: ", time.time() - self.start ," -- ", finJuego)
            pygame.display.flip()
            #if jefe.isDead(): #En esta parte se checa si se mató al jefe final para cambiar a otro nivel
            #    break
        
        while not gameOver:
            mixer.music.stop()
            #self.events(nave)
            #self.all.draw(self.screen)
            #pygame.display.flip()
            self.checkEventsGameOver()

#Llamada a init
#if __name__ == "__main__":
#    principal = Principal(50, 50)
#    principal.init(5, 4, 20, 5, 30, 3)