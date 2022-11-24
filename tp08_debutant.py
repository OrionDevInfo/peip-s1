from re import A

# Quotient et reste dans la division euclidienne
def divmod_verbeux(a, b):
    """Affiche les calculs qu'un élève de CE1 ferait pour
    obtenir le quotient et le reste de la division euclidienne
    de a par b.
    Contraintes : a >= 0 et b > 0
    """
    reste = a
    nb_soustractions = 0
    print("Au début, on a fait", nb_soustractions, "soustractions,",
          "et le reste est", reste)
    # début de la boucle
    while reste >= b:
        nb_soustractions = nb_soustractions + 1
        reste = reste - b
        print("Après", nb_soustractions, "soustractions, le reste vaut", reste)
    # fin de la boucle
    print("Au final, on a fait", nb_soustractions, "soustractions,",
          "et le reste est", reste)
# 1
def main() :
    divmod_verbeux(100,12)
    divmod_verbeux(15,1)
    divmod_verbeux(145,12)
# 2
def reste(divid,divis) :
    '''
    >>> reste(10,3)
    1
    '''
    r=divid
    while r >= divis :
        r-=divis
    return r
# 3
def quotient(divid,divis) :
    '''
    >>> quotient(10,3)
    3
    '''
    q, r = 0, divid
    while r >= divis :
        r-= divis
        q+=1
    return q

# Blob
# 4
def croissance_blob(m) :
    '''
    >>> croissance_blob(.5)
    1
    >>> croissance_blob(.33)
    2
    '''
    d, s = 0, m
    while s < 1. : 
        s*=2
        d+=1
    return d

# Période radioactive
# 5
def nb_periodes_rad(p) :
    '''
    >>> nb_periodes_rad(.75)
    2
    '''
    n, t = 1, 0
    while n > 1-p :
        n/=2
        t+=1
    return t 

# Racine carrée entière
# 6
def racine_carree_entiere(n) :
    '''
    >>> racine_carree_entiere(9)
    3
    >>> racine_carree_entiere(8)
    2
    >>> racine_carree_entiere(10)
    3
    '''
    x=0
    while (x+1)**2 <= n :
        x+= 1
    return x

# Retour sur des exercices précédents
# 7
# from curses.ascii import islower
# def sont_minuscules(s) :
#     '''
#     >>> sont_minuscules('abcdefg')
#     True
#     >>> sont_minuscules('adcdZefg')
#     False
#     >>> sont_minuscules(' A')
#     False
#     '''
#     i=0
#     while (islower(s[i]) or s[i] == ' ') and len(s)-1>i :
#         i+=1
#     return 
# sont_minuscules('abcdefg')
# 8
def palindrome(s) :
    '''
    >>> palindrome('')
    True
    >>> palindrome('aba')
    True
    >>> palindrome('ba')
    False
    '''
    i = 0
    while i < len(s)//2 and s[i] == s[len(s)-i-1] : 
        i+=1
    return i == len(s)//2
# 9
def est_ADN() :
    '''
    '''
    return

from doctest import testmod
testmod(verbose=False)