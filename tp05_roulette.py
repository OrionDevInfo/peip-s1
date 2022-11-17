def est_manque(n) : return 1 <= n <= 18
def est_impair(n) : return not (n%2 == 0)
from random  import randint
def lancer() : return randint(0,36)
def demande_montant() : return int(input('Montant: '))
def demande_mise() : return input('Sur quoi miser vous ? Numéro / Manqué / Passé / Pair / Impair\n')

from math import ceil, floor
def calculGain(n, montant, mise) :
    '''
    >>> calculGain(6, 21, "Pair")
    42
    >>> calculGain(36, 21,  "Passé")
    42
    >>> calculGain(6, 21,  "Impair")
    0
    >>> calculGain(5, 20,  "5")
    720
    >>> calculGain(5, 21,  "6")
    31
    >>> calculGain(5, 21,  "31")
    32
    '''
    m=est_manque(n)
    i=est_impair(n)
    if mise == 'Impair' : return 2*montant if (i) else 0
    if mise == 'Pair' : return 2*montant if (not i) else 0
    if mise == 'Manqué' : return 2*montant if (m) else 0
    if mise == 'Passé' : return 2*montant if (not m) else 0
    if int(mise) == n : return 36*montant
    if (est_impair(int(mise)) and i) or (not est_impair(int(mise)) and not i) : return ceil(1.5*montant)
    if (est_manque(int(mise)) and m) or (not est_manque(int(mise)) and not m) : return floor(1.5*montant)
    else : return 0

def chaine_differentiel(m,g): 
    '''
    >>> chaine_differentiel(100,500)
    '+400'
    >>> chaine_differentiel(100,0)
    '-100'
    '''
    return f'+{g-m}' if (g-m > 0) else f'{g-m}'

def identification() : return input('Nom ? ')
def presentation(n) :
    '''presentation(indentification())'''
    print(f"Bienvenue {n}\nSi le numéro misé est celui de la roulette, vous remportez 36 fois votre mise.\nSi le type misé est celui de la roulette, vous remportez 2 fois votre mise.\nSi le numéro misé et celui de la roulette sont tous les deux Pair/Impair, vous remportez 1.5 fois votre mise. (Arrondi supérieur)\nSi le numéro misé et celui de la roulette sont tous les deux Manqué/Passé, vous remportez 1.5 fois votre mise. (Arrondi inférieur)\nSinon, vous perdez!")

def afficherGain(g) :
    print(f'Bravo! Vous avez gagné {g}€.') if (g>0) else print('Aucun gain. Pas de chance!')
def afficheBilan(m,g) :
    print(f'Par rapport à votre mise, le différentiel est de: {chaine_differentiel(m,g)}€.')

def afficherLancer(n) :
    '''
    >>> afficherLancer(23)
    23 Impair Passé
    >>> afficherLancer(32)
    32 Pair Passé
    >>> afficherLancer(0)
    0 Tout le monde perd!
    '''
    print(n, 'Impair' if (est_impair(n)) else 'Pair', 'Manqué' if (est_manque(n)) else 'Passé') if (1 <= n <= 36) else print(n,'Tout le monde perd!')

def mainRoulette() :
    presentation(identification())
    global mT,gT
    mT, gT = 0, 0
    def partie() :
        m=int(input('Votre mise ? '))
        prono=input('Votre pronostic ? ')
        global mT, gT
        mT += m
        l=lancer()
        g=calculGain(l,m,prono)
        gT += g
        afficherLancer(l)
        afficherGain(g)
    def jouer() :
        value=input('Jouer ? ').lower()
        return (value=='yes' or value=='oui' or value=='y')
    while jouer() :
        partie()
    afficheBilan(mT,gT)
    # Légère modification par rapport à la fonction demandée pour afficher un bilan total après avoir joué plusieurs fois

if __name__ == '__main__':
    mainRoulette()
    from doctest import testmod
    testmod(verbose=False)
