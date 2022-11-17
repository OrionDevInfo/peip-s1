# Auteurs : Orion MAUBERT
#
# Date : 22/09/2022
#
# Objet : description concise 
#         du travail réalisé
#
# État : description détaillée de 
#        l'état d’achèvement du travail :
#        - fonctions réalisées correctement 
#        - fonctions non achevées
#        - remarques éventuelles
#        ...

# 1
from math import pi
def cercle_circonference(r) : 
    '''
    r: le rayon du cerlce, float
    C = 2*pi*r
    r=5 => 31.42 (arrondi)'''
    return round(2*r*pi,2)
# 2
from math import pi
def cercle_aire(r) : 
    '''
    r: le rayon du cerlce, float
    A = pi * r**2
    r=6 => 113.1 (arrondi)
    '''
    return round(pi*r**2,2)
# 3
from math import cos, pi
def cote_adjacent(alpha,h) : 
    '''
    alpha: l'angle en radian, float ; h: longueur hypoténuse, float
    cos alpha = adjacent/hypoténuse => adjacent = cos alpha * hypoténuse
    Retourne la longueur de l'adjacent, type float
    '''
    return cos(alpha)*h
# 4
from random import choice, randint
def de_6() : 
    '''Retourne un élement de la liste: [i for i in range(1,7)]'''
    return randint(1,6)
def de(n) :
    '''
    n ¢ |N*, int
    Retourne un élement de la liste: [i for i in range(1,n+1)], type int
    '''
    return randint(1,n)
# 5
def choisi_caractere(chaine):
    '''
    chaine: str non vide
    Retourne un des éléments de char, type str
    '''
    return choice(chaine)
# 6
def calcule_interets(c, r, t, n) :
    '''
    c: le capital (float) ; r: le taux d'interêt: ex: 5%=>.05 (float)
    t: nombre d'années (int)
    n: nb fois par an que les interets sont ajoutés au c (int)
    Retourne A (le montant du capital final, float) = c*(1+(r/t))**(n*t)
    
    c=1000000 ; r=.05 ; t=5 ; n=2 => 1280084.54
    '''
    return c*(1+(r/n))**(n*t)
# 7
def addition(a,b) :
    '''
    a, b deux nombre float
    Retourne la somme (float) ; ex: a=-3,b=3 => 0
    '''
    return a+b
# 8
def carre(a) :
    '''
    a float
    Retourne a au carré (float) ; ex: a=-2 => 4
    '''
    return a**2
# 9
def cube(a) :
    '''
    a float
    Retourne a au cube (float) ; ex: a=3 => 9
    '''
    return a**3
# 10
def enluminure1(c=str) :
    '''
    c: str non vide
    Retourne une chaine de la forme '-----' de la même longueur que c
    'hello' => -----
    '''
    return '-'*len(c)
def enluminure2(c=str) :
    '''
    c: str non vide
    Retourne une chaine de la forme '--O--' de la même longueur que c
    '''
    return '-'*(len(c)//2)+'O'+'-'*(len(c)//2)
def enluminure3(c=str) :
    '''
    c: str non vide
    Retourne une chaine de la forme '-o-O-o-' de la même longueur que c
    '''
    p1 = '-o'*(len(c)//4)
    return p1+'O'+p1[::-1]
'''
print(enluminure1('hello'))
print(enluminure1('hello world!'))
print(enluminure2('hello'))
print(enluminure2('hello world!'))
print(enluminure3('hello'))
print(enluminure3('hello world!'))
'''