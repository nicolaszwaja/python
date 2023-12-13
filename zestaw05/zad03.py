# przestudiowaniu i uruchomieniu kodu zadanie będzie polegać na takim jego zmodyfikowaniu, żeby: 
# (a) rakietka była tylko jedna, poruszająca się w poziomie na dole ekranu (w lewo i prawo, strzałkami), 
# (b) piłeczka uruchamiana losowo z góry, punkty mają być naliczane za poprawne odbicie od rakietki, 
# (c) gra ma się zakończyć jeśli piłeczka minie rakietkę i zderzy się ze ścianą – wtedy powinien się wyświetlić wynik 
# końcowy oraz dotychczasowy najwyższy wynik. Najlepszy wynik zapisywać do i odczytywać z pliku. 

import pygame
from random import randint

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

class Rakietka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([height, width])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, height, width])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 690:
            self.rect.x = 690

class Pilka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-4, 4)

# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietka = Rakietka(BIALY, 10, 100)
rakietka.rect.x = 345
rakietka.rect.y = 400

pileczka = Pilka(BIALY, 10, 10)
pileczka.rect.x = randint(0, 690)
pileczka.rect.y = 0

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(rakietka)
all_sprites_list.add(pileczka)

kontynuuj = True
clock = pygame.time.Clock()

score = 0
high_score = 0

while kontynuuj:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kontynuuj = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rakietka.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        rakietka.moveRight(10)

    all_sprites_list.update()

    if pileczka.rect.x >= 690 or pileczka.rect.x <= 0:
        pileczka.velocity[0] = -pileczka.velocity[0]

    if pileczka.rect.y > 490:
        if score > high_score:
            high_score = score
        score = 0
        pileczka.rect.y = 0
        pileczka.rect.x = randint(0, 690)

    if pygame.sprite.collide_mask(pileczka, rakietka):
        pileczka.bounce()
        score += 1

    if pileczka.rect.y < 0:
        pileczka.rect.y = 0
        pileczka.velocity[1] = -pileczka.velocity[1]

    if pileczka.rect.y > 500:
        kontynuuj = False

    screen.fill(CZARNY)
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render("current score: {}".format(score), 1, BIALY)
    screen.blit(text, (180, 10))
    text = font.render("best score: {}".format(high_score), 1, BIALY)
    screen.blit(text, (200, 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
