import pygame

class PlanetaInfo(pygame.sprite.Sprite):
    # INICIALIZACION
    def __init__(self):
        super().__init__()
        self.image_or = pygame.image.load("resources/tablet.png").convert()
        self.image = pygame.transform.scale(self.image_or, (400, 710))
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font("resources/Font/Eight-Bit-Madness.ttf", 30)
        self.rect.centerx = 650
        self.rect.centery = 380

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def lines(self, text, pos, screen):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        max_width = 830
        x, y = pos
        for line in words:
            for word in line:
                word_surface = self.font.render(word, False, (255, 255, 255))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def saturn(self, screen):
        str = "             Planeta Saturno\n\n" \
        "No. en el sistema solar: 6.\n" \
        "Distancia estelar: 1 195 000 000 km.\n" \
        "Elementos: 93% de H, 5% de He y 2% de compuestos de carbono.\n" \
        "Masa: 5,688 × 10^26 kg.\n" \
        "Volumen: 8,27 × 10^23 m3.\n\n" \
        "Saturno tiene 82 lunas.\n" \
        "Las nubes superiores esten formadas por cristales de amoniaco.\n\n" \
        "La lluvia es de diamantes.\n" \
        "Se cree que en su atmosfera se producen 10 millones de toneladas de ellas cada anio.\n" \
        "Este fenomeno ocurre gracias a la combinacion del gas metano (CH4) con las tormentas.\n\n" \
        "Los dias duran 10.7 hrs y su anio es igual a 29 anios terrestres.\n"
        self.lines(str, (480, 100), screen)
        #info = self.font.render(str, False, (255, 255, 255))
        #screen.blit(info, (650, 380))


    def mars(self, screen):
        str = "             Planeta Marte\n\n" \
        "No. en el sistema solar: 4.\n" \
        "Distancia estelar: 54 600 000 km.\n" \
        "Elementos: 95.3% de CO2, 2.7% de H, 2% de Ar y otros compuestos.\n" \
        "Masa: 6,4185 × 10^23 kg.\n" \
        "Volumen: 1,6318 × 10^11 km3.\n\n" \
        "La fuerza gravitacional es 0,375 veces la de la Tierra.\n" \
        "Si una persona pesa 100 kg en la Tierra, en Marte pesaria alrededor de 38 kg.\n\n" \
        "Un dia dura 24,6 horas.\n\n" \
        "Un anio equivale a 687 dias en la Tierra.\n" \
        "Tiene dos lunas: Fobos y Deimos.\n" \
        "Se calcula que Fobos comenzara a desintegrarse en 70 millones de anios y en 100 millones de anios se formara un nuevo anillo.\n"
        self.lines(str, (480, 100), screen)
        #info = self.font.render(str, False, (255, 255, 255))
        #screen.blit(info, (650, 380))

    def venus(self, screen):
        str = "             Planeta Venus\n\n" \
        "No. de sistema solar: 2.\n" \
        "Distancia estelar: 261 000 000 km.\n" \
        "Elementos: 96% de CO2, 3% de N, 1% de otros compuestos.\n" \
        "Masa: 4,869 × 10^24 kg\n" \
        "Volumen: 9,28 x 10^11 km3.\n\n" \
        "Su atmosfera es densa: Atrapa el calor y esto provoca el calor extremo.\n" \
        "Es el planeta mas brillante siendo visible en las noches, se debe por el alto CO2 que contiene su atmosfera.\n\n" \
        "Tiene una superficie activa e incluye volcanes.\n\n" \
        "Gira en direccion contraria a la Tierra y la mayoria de los planetas.\n\n" \
        "No tiene lunas.\n" \
        "La presion atmosferica en la superficie de Venus es 90 veces que la superficie de la Tierra.\n"
        self.lines(str, (480, 100), screen)
        #info = self.font.render(str, False, (255, 255, 255))
        #screen.blit(info, (650, 380))