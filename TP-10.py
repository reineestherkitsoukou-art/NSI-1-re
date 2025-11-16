# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 11:57:08 2025

@author: reine
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:36:05 2025

@author: r.kitsoukou
"""
t=[[11,12,13], [21,22,23]]

t[0][1]=666
t[1][0]=667

print(t)

grille_1 = [[" "]*3]*3
grille_1[1][1] = "X"
#print(grille)

g = [[" "]*3, [" "]*3, [" "]*3]
#g[1][1] = "X"
print(g)

g[0][2]="X"
g[1][0]= "O"
def print_grille(grille:list[list[str]]) -> None:
    for i in range(3):
        print(grille[i][0] + " | " + grille[i][1] + " | " + grille[i][2])
        if i < 2:
            print("---------")



