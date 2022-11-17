# Auteurs : Orion
#
# Date : 20/10/2022
#
# État : Terminé
#
#
#
#

# Suite
# 1
def terme_suite(n):
    """Renvoie la somme des n premiers entiers impairs
    Paramètres : - n (int)
    Valeur de retour (int) u_n
    Contraintes : n ≥ 0
    Exemples :
    >>> terme_suite(0)
    1
    >>> terme_suite(1)
    5
    >>> terme_suite(2)
    13
    """
    u=1
    for i in range(1,n+1) : u=2*u+3
    return u

# Tables de multiplications
# 2
def chaine_multiplication(a, b):
    """renvoie la chaîne de la forme « a x b = c », où c = a×b.
    Paramètres : - a (int)
                 - b (int)
    Valeur de retour (str)
    Contraintes : aucune
    Exemples :
    >>> chaine_multiplication(6, 7)
    '6 x 7 = 42'
    """
    return f'{a} x {b} = {a*b}'

# 3
def table_multiplication(n):
    """renvoie la chaîne contenant une table de multiplication par n.
    Paramètres : - n (int)
    Valeur de retour (str)
    Contraintes : aucune
    Exemples :
    >>> table_multiplication(3)
    ' | 0 x 3 = 0 | 1 x 3 = 3 | 2 x 3 = 6 | 3 x 3 = 9 | 4 x 3 = 12 | 5 x 3 = 15 | 6 x 3 = 18 | 7 x 3 = 21 | 8 x 3 = 24 | 9 x 3 = 27 | 10 x 3 = 30 | '
    """
    s=''
    for i in range(11):
        s+=f' | {chaine_multiplication(i,n)}'
    return s+' | '

# Paires
# 4
def paire2str(a, b):
    """Renvoie une écriture de la paire {a, b}
    Paramètres : 
    - a, b : entiers - composantes de la paire
    Valeur de retour : str - l'écriture de la paire
    Contraintes : aucune 
    Exemples : 
    >>> paire2str(2, 2)
    '{2,2}'
    >>> paire2str(2, 6)
    '{2,6}'
    """
    return '{'+f'{a},{b}'+'}'

# 5
def les_paires(n):
    '''
    >>> les_paires(2)
    '{1,1} {1,2} {2,2} '
    >>> les_paires(4)
    '{1,1} {1,2} {1,3} {1,4} {2,2} {2,3} {2,4} {3,3} {3,4} {4,4} '
    '''
    s =''
    for i in range(1,n+1) :
        for j in range(1,n+1):
            if i<=j : s+=paire2str(i,j)+' '
    return s

# Affichage de motifs
# 6
def affiche_ligne(n) : 
    '''
    >>> affiche_ligne(5)
    ooooo
    '''
    print(n*'o')

# 7
def affiche_bloc(n):
    '''
    >>> affiche_bloc(3)
    ooo
    ooo
    ooo
    '''
    for i in range(n) : affiche_ligne(n)

# 8
def affiche_bloc2(n):
    '''
    >>> affiche_bloc2(3)
    ooo
    ooo
    ooo
    '''
    for i in range(n) :
        l=''
        for j in range(n) :l+='o'
        print(l)

# 9
def affiche_triangle(n):
    '''
    >>> affiche_triangle(3)
    o
    oo
    ooo
    '''
    for i in range(1,n+1) :
        affiche_ligne(i)

def affiche_triangle2(n):
    '''
    >>> affiche_triangle2(3)
    o
    oo
    ooo
    '''
    # A faire
    for i in range(1,n+1) :
        l=''
        for j in range(i) :l+='o'
        print(l)

# 10
def affiche_diago(n):
    '''
    >>> affiche_diago(3)
    Xoo
    oXo
    ooX
    '''
    for i in range(1,n+1) :
        l=''
        for j in range(1,n+1) :
            if i==j : l+='X'
            else: l+='o'
        print(l)
    


from doctest import testmod
testmod(verbose=False)