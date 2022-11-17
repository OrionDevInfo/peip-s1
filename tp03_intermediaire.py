# Auteur: Orion
# Date: 2/10/2022
# Objet: TP 03 - Niveau intermédiaire
# État: Tout le Tp terminé (fonction au cinéma incluse)

# Intervalles
# 1
def intersectionVide(a,b) :
    ''' 
    a,b: [float,float]
    renvoie True si a U b = ø
    >>> intersectionVide([1,2],[3,4])
    True
    >>> intersectionVide([1,4],[3,8])
    False
    >>> intersectionVide([3,8],[1,2])
    True
    >>> intersectionVide([4,6],[0,5])
    False
    '''
    return (a[1] <= b[0]) or (b[1] <= a[0])
# 2
def inclusdansa(a,b) :
    ''' 
    a,b: [float,float]
    renvoie True si  b € a
    >>> inclusdansa([1,2],[3,4])
    False
    >>> inclusdansa([1,8],[4,8])
    True
    >>> inclusdansa([4,8],[1,8])
    False
    '''
    return (a[0] <= b[0]) and (b[1] <= a[1])
# 3
def recouvrement(a,b) :
    ''' 
    a,b: [float,float]
    renvoie True si  b € a
    >>> recouvrement([1,2],[3,4])
    False
    >>> recouvrement([1,8],[4,8])
    True
    >>> recouvrement([4,8],[1,8])
    True
    '''
    return inclusdansa(a,b) or ((b[0] <= a[0]) and (a[1] <= b[1]))

# Quatre vingt-et-un
# 1
def est_un_42(de1, de2): 
    """
    Renvoie vrai si et seulement si deux dés forment un 42
    Paramètres :
    - de1 : entier - un lancer de dé six
    - de2 : entier - un autre lancer de dé six
    Valeur de retour : booléen
    Contraintes : de1 et de2 appartiennent à [1, 6]
    :Exemples:
    >>> est_un_42(4, 2)
    True
    >>> est_un_42(2, 4)
    True
    >>> est_un_42(4, 4)
    False
    >>> est_un_42(5, 1)
    False
    """
    return (de1 == 4 and de2 == 2) or (de1 == 2 and de2 == 4)
# 2
def est_un_421(d1,d2,d3): 
    """
    Renvoie True si et seulement si trois dés forment un 421
    d1, d2, d3: 1 <= int <= 6
    >>> est_un_421(4,2,1)
    True
    >>> est_un_421(2,1,4)
    True
    >>> est_un_421(4,4,6)
    False
    """
    return (d1==1 and est_un_42(d2,d3)) or (d2==1 and est_un_42(d1,d3)) or (d3==1 and est_un_42(d1,d2))
# 3
def est_un_421(d1,d2,d3): 
    """
    Renvoie True si et seulement si trois dés forment un 421
    d1, d2, d3: 1 <= int <= 6
    >>> est_un_421(4,2,1)
    True
    >>> est_un_421(2,1,4)
    True
    >>> est_un_421(4,4,6)
    False
    """
    d = [d1,d2,d3]
    d.sort(reverse=True)
    return d[0]==4 and d[1]==2 and d[2]==1

# En automne
# 1
def en_automne(jour, mois):
    """
    Renvoie vrai si et seulement si une date donnée est en automne.
    Paramètres :
    - jour (int) : numéro du jour
    - mois (int) : numéro du mois
    Valeur de retour :
    - bool
    Contraintes :
    - 1 <= mois <= 12 et 1 <= jour <= njour
    njour étant le nombre de jours du mois (31 pour janvier...)
    Exemples :
    >>> en_automne(1, 1)
    False
    >>> en_automne(21, 9)
    False
    >>> en_automne(22, 9)
    True
    >>> en_automne(1, 11)
    True
    """
    return (jour>=22 and mois==9) or mois in [10,11] or (jour<=20 and mois==12)

# Au cinéma
# Question non obligatoire, donc méthode utilisée différente de celle demandée pour créer la fonction
from datetime import date
def tarifreduit(y,m,d) :
    '''
    Retourne True si l'age est <26 ans (mineurs+étudiants) ou >60 ans (séniors)
    y (année de naissance),m (mois),d (jour): type int
    Contrainte: Date formée par y,m,d valdie
    Exemple:
    >>> tarifreduit(1924,11,20)
    True
    >>> tarifreduit(2007,5,28)
    True
    >>> tarifreduit(1971,2,27)
    False
    '''
    today = date.today()
    naissance = date(y,m,d)
    age = ((today-naissance).days)//365
    return age < 26 or age > 60

# Autour du calendrier
# Année bissextile
# 1
def est_divisible_par(a, b):
    """
    Test de divisibilité de deux entiers.
    Paramètres :
    - a, b : deux entiers
    Valeur de retour : booléen
    - True si a est divisible par b
    - False sinon
    Contraintes :
    - b non nul
    Exemples:
    >>> est_divisible_par(10, 2)
    True
    >>> est_divisible_par(10, 3)
    False
    """
    return a%b == 0
# 2
def est_bissextile(annee): 
    """
    Paramètres :
    - annee : entier - l'année à tester
    Valeur de retour : booléen
    - True si annee est une année bissextile
    - False sinon
    Contraintes :
    - annee > 1582, année d'établissement du calendrier grégorien
    Exemples :
    >>> est_bissextile(2019)
    False
    >>> est_bissextile(2020)
    True
    >>> est_bissextile(1900)
    False
    >>> est_bissextile(2000)
    True
    """
    return (est_divisible_par(annee,4) and not est_divisible_par(annee,100)) or est_divisible_par(annee,400)

import doctest
doctest.testmod(verbose=False)