# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 11:57:08 2025

@author: reine
t=[[11,12,13], [21,22,23]]

t[0][1]=666
t[1][0]=667

print(t)

grille_1 = [[" "]*3]*3
grille_1[1][1] = "X"
#print(grille)

grille1 = [[" "]*3, [" "]*3, [" "]*3]
#g[1][1] = "X"
print(grille1)

grille1[0][2]="X"
grille1[1][0]= "O"

# Fonction pour la question 4.a. tapez dans la console print_grille(g)
def print_grille(grille:list[list[str]]) -> None:
    """
    affiche le contenu de la grille à la manère d'un morpion
    """
    for i in range(3):
        print(grille[i][0] + " | " + grille[i][1] + " | " + grille[i][2])
        if i < 2:
            print("---------")

# III Jouer des coups
from random import randint

def coup_ordi(grille:list[list[str]]) -> None:
    """
    choisi une case au hasard tant que la case choisi et déjà occupé elle en choisi une autre si la case est vide elle inscri un rond dedans
    """
    i = randint(0,2)
    j = randint(0,2)
    while grille[i][j] != " ":
        i = randint(0, 2)
        j = randint(0, 2)
    grille[i][j] = "O"
    print_grille(grille)
    
def coup_humain(grille:list[list[str]]) -> None:
    i = int(input("Choisir le numéro de ligne de 0 à 1 : "))
    j = int(input("Choisir le numéro de la colonne de 0 à 1 : "))
    while grille[i][j] != " ":
        print("Cette case est déjà occupée, choisissez une autre case")
        i = int(input("Choisir le numéro de ligne de 0 à 1 : "))
        j = int(input("Choisir le numéro de la colonne de 0 à 1 : "))
    grille[i][j] = "X"
    print_grille(grille)
    
# IV Jouer une partie

grille2 = [[" "]*3, [" "]*3, [" "]*3]
def partie() -> None:
    for tour in range(9):  
        if tour % 2 == 0:
            coup_ordi(grille2)
        else:
            coup_humain(grille2)




