# Auteur : Orion
#
# Date : 24/11/2022
#
# État : Terminé
#
#
#
#

# Test de primalité naïf
# 1
def premier_naif(n) :
    '''
    >>> premier_naif(1)
    False
    >>> premier_naif(13)
    True
    >>> premier_naif(2020)
    False
    '''
    i=2
    while i < n and n%i != 0 : i+=1
    return i == n
# 2
def auMoinsUnPremier(r=range(0)) :
    '''
    >>> auMoinsUnPremier(range(12))
    True
    >>> auMoinsUnPremier(range(8,11))
    False
    >>> auMoinsUnPremier(range(8,12))
    True
    '''
    i=r[0]
    while i in r and not premier_naif(i) : i+=1
    return i <= r[-1]

# Ecriture décimale d'un nombre
# 3
def somme_chiffres(n) :
    '''
    >>> somme_chiffres(2022)
    6
    '''
    s, r = 0, n
    while r > 0 :
        s += r%10
        r //= 10
    return s
# 4
def miroir_chiffres(n) :
    '''
    >>> miroir_chiffres(2022)
    2202
    >>> miroir_chiffres(10)
    10
    >>> miroir_chiffres(5)
    5
    '''
    s, r = 0, n
    while r > 10 :
        s = (s + r%10)*10
        r = (r - r%10)//10
    s+=r
    return s

# Sous chaines
# 5
def estPrefixe(p, s) :
    '''
    >>> estPrefixe("bon", "bonjour")
    True
    >>> estPrefixe("bonjour", "bon")
    False
    >>> estPrefixe("cuba", "cacao")
    False
    >>> estPrefixe("bon", "bon")
    True
    '''
    return p == s[:len(p)] and len(p) <= len(s)
# 5
def estSousChaine(sub, s) :
    '''
    >>> estSousChaine("lit", "ponctualité")
    True
    >>> estSousChaine("pilote", "avion")
    False
    >>> estSousChaine("fin", "Début de la fin")
    True
    '''
    i= 0
    while i < len(s) and not s[i:i+len(sub)] == sub : i += 1
    return 0 < i < len(s)

# Mots de Dyck
# 7, 8
def motsDeDyck(s) :
    '''
    >>> motsDeDyck('())(()')
    False
    >>> motsDeDyck('(()())')
    True
    >>> motsDeDyck('()(')
    False
    >>> motsDeDyck('(()')
    False
    '''
    i, j, k = 0, 0, 0
    while k < len(s) and i >= j :
        if s[k] == '(' : i+=1
        elif s[k] == ')' : j+=1
        k+=1
    return k == len(s) and i == j


# Anagrammes
# 9
def occurrences_caractere(c, carac):
    '''
    >>> occurrences_caractere("Test.", 't')
    1
    >>> occurrences_caractere("Un autre test ! Pour voir.", 't')
    3
    >>> occurrences_caractere('', 't')
    0
    '''
    o=0
    for l in c:
        if l==carac : o+=1
    return o
# 10
def delC(s, c) :
    return ''.join(i if (i!=c) else '' for i in s)
def sont_anagrammes(s1,s2) :
    '''
    >>> sont_anagrammes('chien', 'niche')
    True
    >>> sont_anagrammes('chien', 'nicher')
    False
    >>> sont_anagrammes('abba', 'baaa')
    False
    '''
    while 0 < len(s1) and occurrences_caractere(s1[0],s1) == occurrences_caractere(s1[0],s2) :
        s1, s2 = delC(s1, s1[0]), delC(s2, s1[0])
    return s1 == s2

from doctest import testmod
testmod(verbose=False)