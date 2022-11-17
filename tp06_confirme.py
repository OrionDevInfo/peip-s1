# Auteurs : Orion
#
# Date : 27/10/2022
#
# État : Terminé
#
#
#
#

#1
def maj(c) :
    '''
    >>> maj('des kakis et des kiwis')
    'DES KAKIS ET DES KIWIS'
    '''
    return c.upper()
# 2
def capitales(c) : 
    '''
    >>> capitales('des kakis et des kiwis')
    'Des Kakis Et Des Kiwis'
    '''
    c2 = ''
    for l in range(len(c)) :
        if c[l-1] ==  ' ' or l==0 : c2+= c[l].upper()
        else: c2+= c[l]
    return c2
# 3
def miroir(c) :
    '''
    >>> miroir('Python')
    'nohtyP'
    '''
    return c[::-1]
# 4
def anacycliques(c1,c2) :
    '''
    >>> anacycliques('zen', 'nez')
    True
    '''
    return c1 == c2[::-1] 

from doctest import testmod
testmod(verbose=False)