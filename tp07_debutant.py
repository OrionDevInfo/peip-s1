# Auteur : Orion
#
# Date : 17/11/2022
#
# État : Terminé
#
#
#
#

# 1 
'''
s[1] # 'o'
s[len(s)] # IndexError: string index out of range
s[-1] # 'r'
s[0:3] # 'Bon'
s[3:len(s)-1] # 'jou'
'''
# 2
'''
(10)
1
100
11
@univ
Bonjour
Bonjour !
Bonjour.
[10]
bonjour
bonjour
{10}
'''
# 3
def maximum(a, b): 
    '''
    >>> maximum('(10)','1')
    '1'
    '''
    return a if (a >= b) else b
# 4
def minimum(a, b):
    '''
    >>> minimum('(10)','1')
    '(10)'
    '''
    return a if (a <= b) else b
# 5
'''
Code identique à celui de la fonction pour les entiers. Donc a & b peuvent être int ou str
'''
# 6
def miroir(s) :
    '''
    >>> miroir("! xueim tse'c ]1-::[s")
    "s[::-1] c'est mieux !"
    '''
    s2 = ''
    for i in range(len(s)-1,-1,-1) : 
        s2+=s[i]
    return s2
# 7
def un_sur_deux(s) :
    '''
    >>> un_sur_deux('ejapsùyq')
    'easy'
    '''
    s2=''
    for i in range(0,len(s)-1,2) : 
        s2+=s[i]
    return s2
# 8
def dernier_indice_caractere(s,c) :
    '''
    >>> dernier_indice_caractere("Bonjour", "r")
    6
    '''
    i=0
    for j in range(len(s)) :
        if s[j] == c : i=j
    return i
# 9
def premier_indice_caractere(s,c) :
    '''
    >>> premier_indice_caractere("Bonjour", "o")
    1
    '''
    for j in range(len(s)) :
        if s[j] == c : return j


from doctest import testmod
testmod(verbose=False)