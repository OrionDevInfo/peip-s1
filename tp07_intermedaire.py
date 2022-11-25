# Auteur : Orion
#
# Date : 17/11/2022
#
# État : Terminé
#
#
#
#

# Parcours de chaînes 
# 1 
def palindrome(s): 
    '''
    >>> palindrome('test')
    False
    >>> palindrome('Kayak')
    True
    '''
    return s.lower() == s[::-1].lower()
# 2
def palindrome2(s) :
    '''
    >>> palindrome2('')
    True
    >>> palindrome2('aba')
    True
    >>> palindrome2('ba')
    False
    '''
    i = 0
    while i < len(s)//2 and s[i] == s[len(s)-i-1] : 
        i+=1
    return i == len(s)//2

# Application aux séquences nucléiques
def isDNA(s) :
    '''
    >>> isDNA('ATGCGATC')
    True
    >>> isDNA('ACKT')
    False
    >>> isDNA('ACTK')
    False
    >>> isDNA('')
    True
    '''
    i=0
    while i < len(s) and s[i] in 'ACGT' : i+=1
    return i == len(s)
# 4
from random import choice
def dna(n) :
    return ''.join(choice('ACGT') for i in range(n))
# 5
def complement(c) :
    return 'A' if (c=='T') else 'T' if (c=='A') else 'G' if (c=='C') else 'C'
# 6
def sComplementReversed(s) :
    '''
    >>> sComplementReversed('ACTG')
    'CAGT'
    '''
    return ''.join(complement(c) for c in s[::-1])

# Recherche de motifs
# 7
# def occurences(sub,s) : return s.count(sub)
def occurences(sub,s) :
    o, l = 0, len(c)
    for i in range(len(s)) :
        if s[i:i+l] == sub : o += 1
    return o
# 8
def tirets(s) :
    '''
    >>> tirets('Bonjour')
    'B-o-n-j-o-u-r-'
    '''
    return ''.join(f'{c}-' for c in s)
# 9 | Chaine vide, car len(s) == 0
# 10
def tirets2(s) :
    '''
    >>> tirets2('Bonjour')
    'B-o-n-j-o-u-r'
    '''
    return ''.join(f'{c}-' for c in s[:-1])+s[-1]
#11
def delC(s, c) :
    '''
    >>> delC('valeur de la chaine', ' ') == 'valeurdelachaine'
    True
    >>> delC('test', 't') == 'es'
    True
    >>> delC('test', 'a') == 'test'
    True
    '''
    return ''.join(i if (i!=c) else '' for i in s)
# 12
def phrasePalindrome(s) :
    '''
    >>> phrasePalindrome("eh ca va la vache")
    True
    >>> phrasePalindrome("engage le jeu que je le gagne")
    True
    >>> phrasePalindrome("Engage le jeu que je le gagne.")
    False
    '''
    s = delC(s, ' ').lower()
    return s == s[::-1]

# Exploitation du code ASCII
# 13
def chiffre(c) :
    '''
    >>> chiffre('0')
    0
    >>> chiffre('4')
    4
    '''
    return ord(c)-48
# 16
def estMaj(c) : return 65 <= ord(c) <= 90
# 17
def estMin(c) : return 97 <= ord(c) <= 122
# 18
def maj(c) : return chr(ord(c)-32)
#19
def enMaj(s) :
    '''
    >>> enMaj('vive Python !')
    'VIVE PYTHON !'
    '''
    return ''.join(maj(c) if (estMin(c)) else c for c in s)

from doctest import testmod
testmod(verbose=False)