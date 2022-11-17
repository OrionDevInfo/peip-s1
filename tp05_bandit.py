# Auteur: Orion
# Date: 13/10/2022
# Objet: TP 0 - Niveau intermédiaire
# État: 
#       

# Bandit manchot
from random import choice
def rouleau() : return choice('$%#~&')
def calculGain(m,c1,c2,c3) :
    '''
    >>> calculGain(1,'$','$','$')
    250
    >>> calculGain(1,'%','%','%')
    150
    >>> calculGain(1,'$','$','#')
    5
    >>> calculGain(1,'$','#','#')
    2
    >>> calculGain(1,'%','~','#')
    0
    '''
    def occurences(chaine) :
        o = {k:0 for k in '$%#~&'}
        for i in chaine :
            o[i]+=1
        return o 
    occ = occurences(c1+c2+c3)
    return m*250 if (occ['$']==3) else m*150 if (occ['%']==3) else m*5 if (occ['$']==2) else m*2 if (occ['$']==1) else 0

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
    print(f"Bienvenue {n}\nSi le rouleau affiche 3'$', vous remportez 250 fois votre mise.\nSi le rouleau affiche 3'%', vous remportez 150 fois votre mise.\nSi le rouleau affiche 2'$', vous remportez 5 fois votre mise.\nSi le rouleau affiche 1'$', vous remportez 2 fois votre mise.\nSinon, vous perdez!")

def afficherRouleau(c1,c2,c3) :
    '''
    >>> afficherRouleau('$','%','&')
    Symboles tirés au sort:
    +---+   +---+   +---+
    | $ |   | % |   | & |
    +---+   +---+   +---+
    '''
    p = '+---+' # pattern
    l = f'{p}   {p}   {p}' # lignes 1&3
    print(f'Symboles tirés au sort:\n{l}\n| {c1} |   | {c2} |   | {c3} |\n{l}')

def afficherGain(g) :
    print(f'Bravo! Vous avez gagné {g}€.') if (g>0) else print('Aucun gain. Pas de chance!')
def afficheBilan(m,g) :
    print(f'Par rapport à votre mise, le différentiel est de: {chaine_differentiel(m,g)}€.')

def mainBandit() :
    presentation(identification())
    global mT,gT
    mT, gT = 0, 0
    def partie() :
        m=int(input('Votre mise ? '))
        global mT, gT
        mT += m
        r=[rouleau(),rouleau(),rouleau()]
        g=calculGain(m,r[0],r[1],r[2])
        gT += g
        afficherRouleau(r[0],r[1],r[2])
        afficherGain(g)
    def jouer() :
        value=input('Jouer ? ').lower()
        return (value=='yes' or value=='oui' or value=='y')
    while jouer() :
        partie()
    afficheBilan(mT,gT)
    # Légère modification par rapport à la fonction demandée pour afficher un bilan total après avoir joué plusieurs fois

if __name__ == '__main__':
    mainBandit()
    from doctest import testmod
    testmod(verbose=False)
