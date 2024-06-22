import pygame
import sys, os
from classes import Personagem, Peixe, Passaro, Sol, Lua, Anzol, Nuvem, Gato
from imgs_import import FUNDOS, COVER, BARCO, BALDES, BALAO
from utils import escalar_img, mapear_sol_alpha
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 1000, 750
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sophieshing Game")

FONT = pygame.font.SysFont('comicsansms', 50, True, False)
FONT2 = pygame.font.SysFont('comicsansms', 40, True, False)

def main():
    sol = True
    chuva = False
    noite = False

    sun = Sol()
    moon = Lua()
    anzol = Anzol()
    gato = Gato()

    clock = pygame.time.Clock()
    sophie = Personagem()
    peixes = []
    nuvens = []

    anzol_ocupado = False
    peixes_pescados = 0

    for i in range(4):
        peixes.append(Peixe())
    passaros = []
    for i in range(3):
        passaros.append(Passaro())
    for i in range(5):
        nuvens.append(Nuvem())

    barcox = 930   

    RUN = True
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                RUN = False

        key = pygame.key.get_pressed()

        if key[K_DOWN]:
            anzol.y += 2
        elif key[K_UP]:
            anzol.y -= 2

        TELA.fill((0, 0, 0))

        FUNDOS[0].convert_alpha()
        
        alpha = (mapear_sol_alpha(sun.x, WIDTH/2, 255, WIDTH+100) * 5)
        
        if alpha >= 255:
            alpha = 255

        FUNDOS[0].set_alpha(alpha)

        TELA.blit(FUNDOS[2], (0, 0))
        TELA.blit(FUNDOS[0], (0, 0))

        TELA.blit(escalar_img(BARCO, .1), (barcox, 325))
        barcox -= .02
        if barcox <= 700:
            barcox = 700

        pescados_txt = FONT.render(f"{peixes_pescados}", True, (255, 50, 50))
        sophie_txt = FONT2.render("Sophie", True, (255, 255, 255))
        
        for i, peixe in enumerate(peixes):

            if peixes[i].x > WIDTH + 50 or peixes[i].x < -50:
                peixes.pop(i)
                peixes.append(Peixe())

            if anzol_ocupado == False:
                if anzol.rect.colliderect(peixes[i].rect):
                    anzol_ocupado = True
                    peixes[i].fisgado = True

            if anzol_ocupado == True:
                gato.senta()
            elif anzol_ocupado == False and noite is True:
                gato.dorme()
            elif anzol_ocupado == True and noite is True:
                gato.senta()
            else:
                gato.idle()

            if peixes[i].fisgado == True:
                if peixes[i].randtam == 3:
                    peixes[i].y = anzol.y - 5
                    peixes[i].x = anzol.x - 30
                elif peixes[i].randtam == 4:
                    peixes[i].y = anzol.y - 15
                    peixes[i].x = anzol.x - 50
                else:
                    peixes[i].y = anzol.y - 17
                    peixes[i].x = anzol.x - 65

                if peixes[i].y <= 330:
                    peixes[i].fisgado = False
                    peixes.pop(i)
                    peixes.append(Peixe())
                    peixes_pescados += 1
                    print(f"pegou {peixes_pescados} até agora")
                    anzol_ocupado = False

                if peixes[i].randtam == 5 and anzol.y >= 640:
                    anzol.y = 640
                elif peixes[i].randtam == 4 and anzol.y >= 670:
                    anzol.y = 670
                elif peixes[i].randtam == 3 and anzol.y >= 690:
                    anzol.y = 690
                else:
                    pass

        if sol == True:
            for i, passaro in enumerate(passaros):
                if passaros[i].x > WIDTH + 50 or passaros[i].y > HEIGHT + 16:
                    passaros.pop(i)
                    passaros.append(Passaro())


        sophie.draw(TELA)

        anzol.update()
        anzol.draw(TELA)
        
        gato.draw(TELA)

        if anzol.y >= 720:
            anzol.y = 720
        
        if anzol.y <= 330:
            anzol.y = 330

        for peixe in peixes:
            peixe.update()
            peixe.draw(TELA)

        if sol:
            sun.update()
            sun.draw(TELA)

            if sun.x >= WIDTH:
                sol = False
                noite = True
                sun.reset()   
        
        elif noite:
            moon.update()
            moon.draw(TELA)

            if moon.x >= WIDTH:
                sol = True
                noite = False
                moon.reset()
                for passaro in passaros:
                    passaro.reset()

        for i, nuvem in enumerate(nuvens):
            if nuvens[i].x >= WIDTH:
                nuvens.pop(i)
                nuvens.append(Nuvem(x=-150))
            nuvens[i].update()
            nuvens[i].draw(TELA)

        if sol:
            for passaro in passaros:
                passaro.update()
                passaro.draw(TELA)

        escala_balde = .125
        baldex = 430
        baldey = 310
        if peixes_pescados >= 1:
            TELA.blit(escalar_img(BALDES[1], escala_balde), (baldex, baldey))
        else:
            TELA.blit(escalar_img(BALDES[0], escala_balde), (baldex, baldey))

        COVER.convert_alpha()
        COVER.set_alpha(140)
        TELA.blit(COVER, (0, HEIGHT-373))

        TELA.blit(escalar_img(BALAO, .4), (480, 205))
        TELA.blit(pescados_txt, (530, 237))
        TELA.blit(sophie_txt, (10, 10))

        pygame.display.flip()
        clock.tick(60)

main()
        