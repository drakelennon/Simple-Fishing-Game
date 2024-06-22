import pygame
import os, sys

# Fundo
FUNDOS = [pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "fundo.png")),
          pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "fundo_chuva.png")),
          pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "fundo_noite.png"))]

# Cobertura Agua
COVER = pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "cover.png"))

# Personagem
WALK = []
for i in range(16):
    WALK.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/char/walk", f"walk{i+1}.png")))

PESCANDO = []
for i in range(16):
    PESCANDO.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/char/pescando", f"pescando{i+1}.png")))

BIKE = []
for i in range(16):
    BIKE.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/char/bike", f"Bike{i+1}.png")))

# Peixes

FISHES = []

FISH1 = []
for i in range(12):
    FISH1.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"am{i+1}.png")))

FISH2 = []
for i in range(12):
    FISH2.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"az{i+1}.png")))

FISH3 = []
for i in range(12):
    FISH3.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"azb{i+1}.png")))

FISH4 = []
for i in range(12):
    FISH4.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"ci{i+1}.png")))

FISH5 = []
for i in range(12):
    FISH5.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"marr{i+1}.png")))

FISH6 = []
for i in range(12):
    FISH6.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"ve{i+1}.png")))

FISH7 = []
for i in range(12):
    FISH7.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"veb{i+1}.png")))

FISH8 = []
for i in range(12):
    FISH8.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/fishes", f"verm{i+1}.png")))

FISHES = [FISH1, FISH2, FISH3, FISH4, FISH5, FISH6, FISH7, FISH8]

# Passaro

PASSARO_BRANCO = [pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/birds", "bird1.png")),
                  pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/birds", "bird2.png")),
                  pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/birds", "bird3.png"))]

# Clima

CLIMA = [pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/clima", "sun.png")),
         pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/clima", "moon.png")),
         pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/clima", "drop.png")),
         pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/clima", "splash.png"))]

# Anzol

ANZOL = pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "Anzol.png"))

# Barco

BARCO = pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "sail.png"))

# Nuvem

NUVEM = pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "nuvem.png"))

# cats

BALDES = [pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/balde", "balde_vazio.png")),
          pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/balde", "balde_cheio.png"))]

# Cat

GATO = []
for i in range(32):
    GATO.append(pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs/cat", f"cat{i+1}.png")))

# Balao Dialogo

BALAO = pygame.image.load(os.path.join("PythonProjects/Sophieshing/imgs", "balao.png"))
BALAO = pygame.transform.flip(BALAO, True, False)