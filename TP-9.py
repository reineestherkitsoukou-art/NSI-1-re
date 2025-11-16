# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import annotations
import matplotlib.pyplot as plt

def syrac(n:int)->int:
    """
    Calcul le terme suivant n dans la suite de Syracuse
    3n+1 si impair n/2 sinon.
    """
    if n%2==0:
        n=n//2
    else:
        n= 3*n+1
    return n

def long_vol(n:int)->int:
    """
    Calcul la longueur dâ€™un vol de la suite de Syracuse
    en partant de lâ€™entier n.
    """
    long = 0
    while n!=1:
        n = syrac(n)
        long = long+1
    return long

def table_vol(n:int)->list[int]:
    """
    renvoie un tableau contenant toutes les valeurs successives prises par une suite de syracuse
    """
    long=long_vol(n)        
    t=[0]*(long+1)
    c=0
    while n!=1:
        t[c] = n
        c+=1
        n = syrac(n)
    return t


def plot_vol(n:int) -> None:
    """
    affiche la courbe d'un vol partant de n
    """
    plt.plot(table_vol(n))
    
def hauteur_vol(n:int)->int:
    """
    Renvoie la hauteur de vol d'une suite de Syracuse
    partant de l'entier n.
    """
    hauteur = n
    while n!=1:
        n = syrac(n)
        if n > hauteur:
            hauteur = n
    return hauteur    
    
def long_max(n:int)->None:
    """
    Affiche la longueur maximale du vole d'une suite de syracuse 
    """
    vol_max=0
    long_max=0
    for i in range(1,n+1):
        longueur = long_vol(i)
        if longueur > long_max :
            long_max = longueur
            vol_max = i
    print("maximum atteint pour : ",vol_max," avec une longueur de : ",long_max)
    
def hauteur_max(x:int) -> int:
   
    """
    renvoie la valeur de départ d'une suite de syracuse de hauteur maximale généré par un nombre inférieur à n
    """
    hauteur_maximale = 0
    valeur_depart = 1
    for k in range(1,x):
        hauteur = hauteur_vol(k)
        if hauteur > hauteur_maximale:
            hauteur_maximale = hauteur
            valeur_depart = k
    return valeur_depart



def plot_max(y:int) -> int:
    """
    affiche le vol de hauteur maximale pour un entier de départ inférieur à n et renvoie cette entier
    """
    hauteur_maximale = 0
    valeur_depart = 1
    for k in range(1,y):
        hauteur = hauteur_vol(k)
        if hauteur > hauteur_maximale:
            hauteur_maximale = hauteur
            valeur_depart = k
    plt.plot(table_vol(valeur_depart))        
    return valeur_depart