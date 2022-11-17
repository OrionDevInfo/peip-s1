# Auteur: Orion
# Date: 6/10/2022
# Objet: TP 04 - Niveau débutant
# État: 
#       

# Minimum, maximum, valeur absolue
#1
def maximum(a,b) :
    ''' 
    a,b: float
    renvoie le plus grand des deux
    >>> maximum(2,5)
    5
    >>> maximum(4,1)
    4
    >>> maximum(9,9)
    9
    '''
    return a if (a>=b) else b
# 2
def minimum(a,b) :
    ''' 
    a,b: float
    renvoie le plus petit des deux
    >>> minimum(2,5)
    2
    >>> minimum(4,1)
    1
    >>> minimum(9,9)
    9
    '''
    return a if (a<=b) else b
# 3
def v_abs(x) :
    ''' 
    x: float
    renvoie la valeur absolue de x
    >>> v_abs(2)
    2
    >>> v_abs(-2)
    2
    >>> v_abs(0)
    0
    '''
    return x if (x>=0) else -x

# Pair et signe
# 4
def parite(x):
    '''
    x: int
    Retourne 'pair' si x pair, 'impair' si x impair
    >>> parite(2)
    'pair'
    >>> parite(3)
    'impair'
    >>> parite(0)
    'pair'
    '''
    return 'pair' if(x%2 == 0) else 'impair'
# 5
def signe(x):
    '''
    x: int
    Retourne 'positif' si x positif, 'négatif' si x négatif ou 'nul' si x nul
    >>> signe(2)
    'positif'
    >>> signe(-3)
    'négatif'
    >>> signe(0)
    'nul'
    '''
    return 'positif' if(x>0) else 'négatif' if(x<0) else 'nul'

# Pile ou face
# 6
from random import randint
def pileface() :
    '''
    Retourne 'pile' ou 'face' de façon aléatoire.
    '''
    return 'pile' if(randint(0,1)==1) else 'face'

# Pour aller plus loin
# 8
def maximum3(x, y, z):
    """Renvoie le maximum des nombres x, y et z
    Paramètres : - x (int ou float)
                 - y (int ou float)
                 - z (int ou float)
    Valeur de retour (int ou float) : max {x, y, z}
    Contraintes : aucune
    Exemples :
    >>> maximum3(1, 4, 2)
    4
    >>> maximum3(4, 1, 2)
    4
    >>> maximum3(0, 0, 7)
    7
    >>> maximum3(7, 7, 0)
    7
    """
    return maximum(maximum(x,y),z)
def maximum3_v2(x, y, z):
    """Renvoie le maximum des nombres x, y et z
    Paramètres : - x (int ou float)
                 - y (int ou float)
                 - z (int ou float)
    Valeur de retour (int ou float) : max {x, y, z}
    Contraintes : aucune
    Exemples :
    >>> maximum3_v2(1, 4, 2)
    4
    >>> maximum3_v2(4, 1, 2)
    4
    >>> maximum3_v2(0, 0, 7)
    7
    >>> maximum3_v2(7, 7, 0)
    7
    """
    return x if(x>=y and x>=z) else y if(y>=x and y>=z) else z

def mediane(x, y, z):
    """Renvoie la médiane des nombres x, y et z
    Paramètres : - x (int ou float)
                 - y (int ou float)
                 - z (int ou float)
    Valeur de retour (int ou float) : med {x, y, z}
    Contraintes : aucune
    Exemples :
    >>> mediane(1, 4, 2)
    2
    >>> mediane(4, 1, 2)
    2
    >>> mediane(0, 0, 7)
    0
    >>> mediane(7, 7, 0)
    7
    """
    return x+y+z - maximum3(x,y,z) - (minimum(minimum(x,y),z))
    
import doctest
doctest.testmod(verbose=False)