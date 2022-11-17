# Auteur: Orion
# Date: 29/09/2022
# Objet: TP 03 - Niveau intermédiaire
# État: Prédicats réalisés
#       Tests de fonctions réalisés

# Prédicats
#1
def impair(x) :
    ''' 
    x: float
    renvoie True si x est impair
    >>> impair(42)
    False
    >>> impair(10**200+1)
    True
    '''
    return x%2 == 1
# 2
def multiple7(x) :
    ''' 
    x: float
    renvoie true si x est multiple de 7
    >>> multiple7(42)
    True
    >>> multiple7(41)
    False
    '''
    return x%7 == 0
# 3
def empty(chaine) :
    ''' 
    chaine: str
    renvoie true si chaine est vide
    >>> empty('False')
    False
    >>> empty('')
    True
    '''
    return chaine == ''
def empty2(chaine) :
    ''' 
    chaine: str
    renvoie true si chaine est vide
    >>> empty2('False')
    False
    >>> empty2('')
    True
    '''
    return len(chaine) == 0
# 4
def sup0(x) :
    ''' 
    x: float
    renvoie true si x positif
    >>> sup0(-1561368436)
    False
    >>> sup0(1564348713456)
    True
    '''
    return x >= 0
# 5
def sup2nb(x,y) :
    ''' 
    x,y: float
    renvoie true si x et y positifs
    >>> sup2nb(-1561368436,5168)
    False
    >>> sup2nb(1564348713456,123)
    True
    '''
    return sup0(x) and sup0(y)
# 6
def memesignes(x,y) :
    ''' 
    x,y: float
    renvoie true si x et y de même signe
    >>> memesignes(-1561368436,5168)
    False
    >>> memesignes(1564348713456,0)
    True
    >>> memesignes(-1564348713456,-123)
    True
    '''
    return sup2nb(x,y) or (x<=0 and y<=0)
# 7
def signesoppo(x,y) :
    ''' 
    x,y: float
    renvoie true si x et y de signes opposés
    >>> signesoppo(-1561368436,5168)
    True
    >>> signesoppo(0,1564348713456)
    True
    >>> signesoppo(-1564348713456,-123)
    False
    '''
    return memesignes(x, -y)
# 8
def inter(x,a,b) :
    ''' 
    x,a,b: float
    renvoie true si a <= x <= b
    >>> inter(88,12,88)
    True
    >>> inter(1,5,15)
    False
    '''
    return a <= x <= b

# Etats de l'eau
#1
def est_glace(x) :
    ''' 
    x: float
    renvoie True si x est une température de l'eau à l'état solide
    >>> est_glace(42)
    False
    >>> est_glace(-20)
    True
    >>> est_glace(-342)
    False
    '''
    return -273.15 < x < 0
# 2
def est_liquide(x) :
    ''' 
    x: float
    renvoie True si x est une température de l'eau à l'état solide
    >>> est_liquide(142)
    False
    >>> est_liquide(20)
    True
    >>> est_liquide(0)
    True
    '''
    return 0 <= x <= 100

# Tolérance pour les flottants
def tolerance(a,b,t):
    ''' 
    a,b,t: float
    renvoie True si a et b sont proches avec une tolérance t
    >>> tolerance(.3,3*.1,.001)
    True
    >>> tolerance(.3,3*.1,1.e-20)
    False
    '''
    return b-t <= a <= b+t

import doctest
doctest.testmod(verbose=False)
