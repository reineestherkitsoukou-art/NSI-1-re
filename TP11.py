# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import annotations
moi=('Reine-Esther','Kitsoukou',16)

def inscription(fiche:tuple) -> None:
    prenom, nom, age = fiche
    print('------------------------------')
    print('- Nom:',nom)
    print('- Prénom:',prenom)
    print('- Age:',age)
    print('------------------------------')
    
def viellir(fiche:tuple):
    prenom, nom, age = fiche
    age2=fiche[2]
    age2+=1
    fiche2=(prenom,nom,age2)
    return fiche2
    
inscription(moi)
moi=viellir(moi)
inscription(moi)

prenom, nom, age = moi
prenom,_,age = moi


elle = ('Maï', 'Kits', 21)
lui = ('Ash', 'Kits', 33)

personne = [moi, elle, lui]

prenom1, nom1, age1 = elle
prenom2, nom2, age2 = lui

def plus_jeune(personne1:tuple(str,str,int), personne2:tuple(str,str,int)):
    """
    renvoie l'uplet de la personne la plus jeune des deux
    """
    if personne1[2] < personne2[2]:
        return personne1
    else:
        return personne2
    
personnes = [moi, elle, lui]

def print_personnes(groupe:list[tuple]):
    """
    affiche toutes les personnes de la structure dans l'ordre
    """
    for i in range(3):
        print(groupe[i])
        

    