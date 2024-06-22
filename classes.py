import pygame
import os, sys
import random
from imgs_import import *
from utils import escalar_img

# Classes

class Personagem:
    def __init__(self):
        
        self.img = PESCANDO[4]
        self.x = 325
        self.y = 265
        self.mod = 3

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, 1.5), (self.x, self.y))

class Peixe(Personagem):
    def __init__(self):
        super().__init__()

        self.tamx = 50
        self.tamy = 40
        self.x_init = random.choice([-49, 1049])
        self.rand_fish = random.randint(0, 7)
        self.img = FISHES[self.rand_fish][4]

        if self.x_init < 0:
            self.img = pygame.transform.flip(self.img, True, False)

        self.x = self.x_init
        self.y = random.randint(340, 650)
        self.randtam = random.randint(3, 5)
        self.randvel = random.uniform(.5, 4)
        self.mod_ticks = 1
        self.rect = pygame.Rect(self.x, self.y, self.tamx, self.tamy)
        self.fisgado = False

        if self.randtam == 3:
            self.rect = pygame.Rect(self.x+25, self.y+40, self.tamx, self.tamy)
        elif self.randtam == 4:
            self.rect = pygame.Rect(self.x+25, self.y+50, self.tamx+25, self.tamy+10)
        else:
            self.rect = pygame.Rect(self.x+30, self.y+70, self.tamx+45, self.tamy+15)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        self.mod += self.mod_ticks
        if self.mod >= 62:
            self.mod_ticks = -self.mod_ticks
        elif self.mod <= 1:
            self.mod_ticks = -self.mod_ticks

        if self.fisgado == False:
            self.img = FISHES[self.rand_fish][(self.mod // 21)+3]

            if self.x_init < 0:
                self.img = pygame.transform.flip(self.img, True, False)

            if self.x_init < 0:
                self.x += self.randvel
            else:
                self.x -= self.randvel

            if self.randtam == 3:
                self.rect = pygame.Rect(self.x+25, self.y+40, self.tamx, self.tamy)
            elif self.randtam == 4:
                self.rect = pygame.Rect(self.x+25, self.y+50, self.tamx+25, self.tamy+10)
            else:
                self.rect = pygame.Rect(self.x+30, self.y+70, self.tamx+45, self.tamy+15)
        else:
            self.img = FISHES[self.rand_fish][(self.mod // 21)]
            self.randvel = 0
            self.img = pygame.transform.flip(self.img, True, True)
        

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, self.randtam), (self.x, self.y))
        # pygame.draw.rect(TELA, (255, 255, 255), self.rect, 2)
        

class Passaro(Peixe):
    def __init__(self):
        super().__init__()

        self.img = PASSARO_BRANCO[0]
        self.x = random.randint(-1000, -16)
        self.y = random.randint(0, 200)
        self.x_init = -20

    def reset(self):
        self.img = PASSARO_BRANCO[0]
        self.x = random.randint(-1000, -16)
        self.y = random.randint(0, 200)
        self.x_init = -20

    def update(self):

        self.mod += self.mod_ticks
        if self.mod >= 62:
            self.mod_ticks = -self.mod_ticks
        elif self.mod <= 1:
            self.mod_ticks = -self.mod_ticks

        self.img = PASSARO_BRANCO[(self.mod // 21)]
        if self.x_init < 0:
            self.img = pygame.transform.flip(escalar_img(self.img, .5), False, False)

        self.x += 2
        self.y -= .25

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, 2.5), (self.x, self.y))

class Sol:
    def __init__(self):
        self.img = CLIMA[0]
        self.x = -100
        self.y = 100
        self.tamx = 0
        self.tamy = 0
        self.x_init = 0
        self.rect = pygame.Rect(self.x, self.y, self.tamx, self.tamy)
        self.vel = .06
        self.invert = False

    def reset(self):
        self.x = 0
        self.y = 100
        self.x_init = 0
        self.invert = False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        self.x += .3

        if self.invert is False:
            self.y -= self.vel
        else:
            self.y += self.vel
        
        if self.y <= 0:
            self.invert = True

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, .05), (self.x, self.y))

class Lua(Sol):
    def __init__(self):
        super().__init__()

        self.img = CLIMA[1]

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, .3), (self.x, self.y))

class Anzol:
    def __init__(self):

        self.img = ANZOL
        self.x = 320
        self.y = 330
        self.tamx = 20
        self.tamy = 30
        self.rect = pygame.Rect(self.x, self.y, self.tamx, self.tamy)
        self.vel = 1

    def update(self):

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, .05), (self.x, self.y))
        # pygame.draw.rect(TELA, (255, 255, 255), (self.x+10, self.y, self.tamx, self.tamy), 2)
        pygame.draw.line(TELA, (255, 255, 255), (self.rect.centerx+10, self.rect.top), (340, 320))

class Nuvem:
    def __init__(self, x=None):
        self.img = NUVEM
        if x is None:
            self.x = random.randint(-200, 900)
        else:
            self.x = x
        self.y = random.randint(0, 150)
        self.vel = random.uniform(.05, .50)
        self.randtam = random.uniform(.1, .4)

    def update(self):
        self.x += self.vel

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, self.randtam), (self.x, self.y))

class Gato:
    def __init__(self):
        self.img = GATO[19]
        self.x = 455
        self.y = 277
        self.vel = 1
        self.mod = 1
        self.mod_ticks = 1
        self.count = 0
        self.count_ts = 5

    def senta(self):
        if self.mod >= 125:
            self.mod = 1
        self.count += 1
        if self.count >= self.count_ts:
            self.mod += self.mod_ticks
            if self.mod >= 125:
                self.mod = 1
            self.count = 0

        self.img = GATO[(self.mod // 21)+18]

    def idle(self):
        if self.mod >= 82:
            self.mod = 1
        self.count += 1
        if self.count >= self.count_ts:
            self.mod += self.mod_ticks
            if self.mod >= 82:
                self.mod = 1
            self.count = 0

        self.img = GATO[(self.mod // 21)]

    def dorme(self):
        if self.mod >= 62:
            self.mod = 22
        self.count += 1
        if self.count >= self.count_ts:
            self.mod += self.mod_ticks
            if self.mod >= 62:
                self.mod = 22
            self.count = 0

        self.img = GATO[(self.mod // 21)+27]

    def draw(self, TELA):
        TELA.blit(escalar_img(self.img, .5), (self.x, self.y))
