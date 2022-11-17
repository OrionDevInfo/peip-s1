# Auteurs : Orion
#
# Date : 20/10/2022
#
# État : Terminé
#
#
#
#

#1
def sequence_10_20():
    """Affiche dans la console la séquence des nombres entiers compris
    entre 10 et 20 inclus."""
    for i in range(10,21) : print(i)
# 2
def sequence_0_20():
    """Affiche dans la console la séquence des nombres entiers compris
    entre 0 et 20 inclus."""
    for i in range(21) : print(i)
# 3 / 4 / 5 / 6
# range(10) peut s'écrire sous la forme range( 0, 10, 1 ).
# range(x,y,z) : 
# x: le début de l'intervalle compris, default: 0
# y: la fin de l'intervalle exclu, required
# z: le pas dans l'intervalle, sens inverse si négatif (x>y pour fonctionner), default: 1

# Minuscules
# 7
from curses.ascii import islower
def sont_minuscules(chaine):
    """Renvoie True si tous les caractères de `chaine` sont des lettres
    minuscules ou des espaces.
    Paramètres : - chaine (str)
    Valeur de retour (bool)
    Contraintes : aucune
    Exemples :
    >>> sont_minuscules('des kakis et des kiwis')
    True
    >>> sont_minuscules('des kakis et des kiwis !')
    False
    >>> sont_minuscules('des Kakis et des Kiwis')
    False
    >>> sont_minuscules('')
    True
    """
    b=True
    for l in chaine:
        if not islower(l) and l!=' ' : b=False
    return b

# Sommes
# 8
def somme_entiers(n):
    """Renvoie la somme des entiers de 1 à n
    Paramètres : - n (int)
    Valeur de retour (int) 1 + 2 + ... + (n-1) + n
    Contraintes : n > 0
    Exemples :
    >>> somme_entiers(3)
    6
    >>> somme_entiers(10)
    55
    """
    s = 0
    for i in range(n+1) : s+=i
    return s

# 9
def somme_carres(n):
    """Renvoie la somme des carrés des entiers de 1 à n
    Paramètres : - n (int)
    Valeur de retour (int) 1² + 2² + ... + (n-1)² + n²
    Contraintes : n > 0
    Exemples :
    >>> somme_carres(3)
    14
    >>> somme_carres(10)
    385
    """
    s=0
    for i in range(1,n+1) : s+=i**2
    return s
    # return sum(i**2 for i in range(1,n+1)) 

# 10
def somme_impairs(n):
    """Renvoie la somme des n premiers entiers impairs
    Paramètres : - n (int)
    Valeur de retour (int) 1 + 3 + ... + (2n-1)
    Contraintes : n > 0
    Exemples :
    >>> somme_impairs(3)
    9
    >>> somme_impairs(10)
    100
    """
    s=0
    for i in range(1,2*n+1,2) : s+=i
    return s

# 11
def somme_alternee(n):
    """Renvoie le n-ième terme de la série harmonique alternée
    Paramètres : - n (int)
    Valeur de retour (float) -1/1 + 1/2 - 1/3 + ... + (-1)^n/n
    Contraintes : n > 0
    Exemples :
    >>> from math import isclose, log
    >>> isclose(somme_alternee(10) - somme_alternee(9), 1/10)
    True
    """
    return ((-1)**n)/n + somme_alternee(n-1) if (n>1) else ((-1)**n)/n

# Produits
# 12
def factorielle(n):
    """Renvoie n!
    Paramètres : - n (int)
    Valeur de retour (int) n! = 1 × 2 x 3 × ... × (n-1) × n
    Contraintes : n ≥ 0
    Exemples :
    >>> factorielle(5)
    120
    >>> factorielle(0)
    1
    """
    f=1
    for i in range(1,n+1) : f*=i
    return f

# 13
def puissance(n, p):
    """Renvoie n puissance p
    Paramètres : - n (int)
                 - p (int)
    Valeur de retour (int) n^p = n × n × ... × n (p fois)
    Contraintes : p ≥ 0
    Exemples :
    >>> puissance(3, 0)
    1
    >>> puissance(4, 1)
    4
    >>> puissance(1, 5)
    1
    >>> puissance(2, 3)
    8
    """
    return n**p

# Comptages
# 14
def nombre_caracteres(s):
    """
    Renvoie le nombre de caractères d'une chaîne donnée, sans utiliser
    la fonction prédéfinie len(). 
    Parametre : s - chaîne de caractères 
    Valeur de retour : entier - le nombre de caractères de s
    Contrainte : aucune
    Exemples :
    >>> nombre_caracteres("Test")
    4
    >>> nombre_caracteres("Un autre test. ")
    15
    >>> nombre_caracteres('')
    0
    """
    return len(s)

# 15
def nombre_espaces(c):
    """
    Renvoie le nombre d'espaces présents dans une chaîne donnée
    Paramètre : c - chaîne de cractères 
    Valeur de retour : entier - le nombre d'espaces
    Contrainte : aucune
    Exemples :
    >>> nombre_espaces("Test")
    0
    >>> nombre_espaces("Un autre test. ")
    3
    >>> nombre_espaces('')
    0
    """
    s=0
    for l in c :
        if l==' ': s+=1
    return s
    
# 16
def nombre_ponctuations(c):
    """
    Renvoie le nombre de caractères  ".", "?", "!" présents dans une chaîne donnée
    Paramètre : c - chaîne de cractères 
    Valeur de retour : entier - le nombre de caractères ".", "?", "!" 
    Contrainte : aucune
    Exemples :
    >>> nombre_ponctuations("Test.")
    1
    >>> nombre_ponctuations("Un autre test ! Pour voir.")
    2
    >>> nombre_ponctuations('')
    0
    """
    p = ['.','?','!']
    s=0
    for l in c:
        if l in p: s+=1
    return s

# 17
def occurrences_caractere(c, carac):
    """
    Renvoie le nombre d'occurence d'un caractère donné dans une chaîne
    Paramètres :
    - c : chaîne de caractères 
    - carac : chaîne de (un) caractère
    Valeur de retour : entier - le nombre d'occurrences de carac dans s
    Contrainte : len(carac) == 1
    Exemples :
    >>> occurrences_caractere("Test.", 't')
    1
    >>> occurrences_caractere("Un autre test ! Pour voir.", 't')
    3
    >>> occurrences_caractere('', 't')
    0
    """
    o=0
    for l in c:
        if l==carac : o+=1
    return o

# def occurences(chaine) :
#         o = {k:0 for k in '$%#~&'}
#         for i in chaine :
#             o[i]+=1
#         return o 
# Retourne un dictionnaire avec les occurences de tous les caractères de la chaine.

from doctest import testmod
testmod(verbose=False)