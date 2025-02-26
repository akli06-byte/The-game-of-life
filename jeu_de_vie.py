import os
import time
import random

def create(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def aupif(grille):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            grille[i][j] = random.choice([0, 1])

def alive(x, y, grille):
    voisins = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    n = len(grille)
    vivantes = sum(
        1 for dx, dy in voisins
        if 0 <= x + dx < n and 0 <= y + dy < n and grille[x + dx][y + dy] == 1
    )

    if grille[x][y] == 1:
        return 1 if vivantes in [2, 3] else 0
    else:
        return 1 if vivantes == 3 else 0

def next_grid(grille):
    n = len(grille)
    return [[alive(i, j, grille) for j in range(n)] for i in range(n)]

def affiche(grille):
    for ligne in grille:
        print("".join("X" if cell else " " for cell in ligne))

def jeu_de_la_vie(n=20, iterations=200, delay=0.2):
    grille = create(n)
    aupif(grille)

    for _ in range(iterations):
        os.system("cls" if os.name == "nt" else "clear")  # Efface la console
        affiche(grille)
        time.sleep(delay)
        grille = next_grid(grille)

jeu_de_la_vie()
