# Auteur: Orion
# Date: 13/10/2022
# Objet: TP 05 - Niveau débutant
# État: Terminé
#       

# Jeu du 421
from random import randint
def de(): return randint(1,6)
def est421(d1,d2,d3) :
    return ((d1==4 and ((d2==2 and d3==1) or (d2==1 and d3==2))) or (d1==2 and ((d2==4 and d3==1) or (d2==1 and d3==4))) or (d1==1 and ((d2==2 and d3==4) or (d2==4 and d3==2))))
def identification() : return input('Nom ? ')
def presentation(n) :
    '''presentation(indentification())'''
    print(f'Bienvenue {n}\nPour gagner au 421, vos 3 dés doivent former ce nombre.')
def poursuivre() :
    value=input('Jouer ? ').lower()
    return (value=='yes' or value=='oui' or value=='y')
def afficherLancer(d1,d2,d3) :
    '''
    >>> afficherLancer(4,3,5)
    +---+   +---+   +---+
    | 4 |   | 3 |   | 5 |
    +---+   +---+   +---+
    '''
    p = '+---+' # pattern
    l = f'{p}   {p}   {p}' # lignes 1&3
    print(f'{l}\n| {d1} |   | {d2} |   | {d3} |\n{l}')
def afficherRes(d1,d2,d3) :
    afficherLancer(d1,d2,d3)
    print('Bravo!') if (est421(d1,d2,d3)) else print('Dommage')
def main421() :
    presentation(identification())
    while poursuivre() :
        afficherRes(de(),de(),de())

if __name__ == '__main__':
    main421()
    from doctest import testmod
    testmod(verbose=False)
