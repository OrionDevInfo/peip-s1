# Auteur: Orion
# Date: 6/10/2022 & 11/10/22
# Objet: TP 04 - Niveau intermédiaire
# État: Terminé + Exo du 421
#       

# Saison
def saison(j,m) :
    ''' 
    j in [1,31],m in [1,12]: int
    Renvoie la saison sous forme de str
    j et m doivent former une date valide
    >>> saison(19,3)
    'hiver'
    >>> saison(20,3)
    'printemps'
    >>> saison(31,7)
    'été'
    >>> saison(31,12)
    'hiver'
    '''
    r= 'hiver'
    if ((j>=20 and m==3) or m==4 or m==5 or (j<=20 and m==6)) : r='printemps'
    elif ((j>=21 and m==6) or m==7 or m==8 or (j<=21 and m==9)) : r='été'
    elif ((j>=22 and m==9) or m==10 or m==11 or (j<=20 and m==12)) : r='automne'
    return r

# Dans l'ordre
# 1
from tp04_debutant import minimum, maximum3_v2,mediane
def ordre1(a, b, c):
    """Renvoie le triplet (a, b, c) trié dans l'ordre croissant
    Paramètres : - a (int)
                 - b (int)
                 - c (int)
    Valeur de retour ( (int, int, int) )
    Contraintes : aucune
    Exemples :
    >>> ordre1(4, 2, 1)
    (1, 2, 4)
    >>> ordre1(0, 7, 0)
    (0, 0, 7)
    """
    # l=[a,b,c]
    # l.sort()
    # i = l[0]
    # j = l[1]
    # k = l[2]
    i=minimum(minimum(a,b),c)
    j=mediane(a,b,c)
    k=maximum3_v2(a,b,c)
    return i, j, k
def ordre2(a, b, c):
    """Renvoie le triplet (a, b, c) trié dans l'ordre croissant
    Paramètres : - a (int)
                 - b (int)
                 - c (int)
    Valeur de retour ( (int, int, int) )
    Contraintes : aucune
    Exemples :
    >>> ordre2(4, 2, 1)
    (1, 2, 4)
    >>> ordre2(0, 7, 0)
    (0, 0, 7)
    """
    # remplacer ces 4 lignes par plusieurs lignes de code
    # vous n'avez le droit d'utiliser 0 ou 1 variable
    # en plus des paramètres a, b, et c
    # Au minimum, vous devriez avoir 6 if
    if b<a : a,b = b,a
    if c<a : a,c = c,a
    if c<b : b,c = c,b
    return a, b, c
def ordre3(a,b,c,d) :
    """Renvoie le quatuor (a, b, c,d) trié dans l'ordre croissant
    Paramètres : - a (int)
                 - b (int)
                 - c (int)
                 - d (int)
    Valeur de retour ( (int, int, int, int) )
    Contraintes : aucune
    Exemples :
    >>> ordre3(4, 2, 1, 0)
    (0, 1, 2, 4)
    >>> ordre3(0, 7, 0,6)
    (0, 0, 6, 7)
    """
    l=[a,b,c,d]
    l.sort()
    return l[0], l[1], l[2], l[3]

# Retour sur le 421
# 5
def f421(d1,d2,d3) :
    '''
    d1,d2,d3 dans [1,6] -int-
    retourne True si 421
    >>> f421(4,2,1)
    True
    >>> f421(1,2,4)
    True
    >>> f421(2,4,1)
    True
    >>> f421(4,2,5)
    False
    '''
    return True if ((d1==4 and ((d2==2 and d3==1) or (d2==1 and d3==2))) or (d1==2 and ((d2==4 and d3==1) or (d2==1 and d3==4))) or (d1==1 and ((d2==2 and d3==4) or (d2==4 and d3==2)))) else False
# 6
def ff421(d1,d2,d3) :
    '''
    d1,d2,d3 dans [1,6] -int-
    retourne True si 421
    >>> ff421(4,2,1)
    True
    >>> ff421(1,2,4)
    True
    >>> ff421(2,4,1)
    True
    >>> ff421(4,2,5)
    False
    '''
    return True if(ordre2(d1,d2,d3) == (1,2,4)) else False

# Impression à tarif dégressif
#7
def nombre_exemplaires(nb):
    """Renvoie le nombre d'exemplaires minimum à commander pour
    en avoir au moins `nb`.
    Paramètres : - nb (int) nombre d'exemplaires souhaité
    Valeur de retour (int) : nombre d'exemplaires à commander
    Contraintes : nb ≥ 0
    Exemples :
    >>> nombre_exemplaires(5)
    100
    >>> nombre_exemplaires(300)
    500
    >>> nombre_exemplaires(500)
    500
    >>> nombre_exemplaires(2022)
    3000
    >>> nombre_exemplaires(6666)
    7000
    """
    l=[100,250,500,750,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
    i,n=0,100
    while nb > l[i] :
        i+=1
        n=l[i]
    return n
#8
def montant_facture(nb):
    """Renvoie le montant minimum à payer pour recevoir au moins
    `nb` flyers.
    Paramètres : - nb (int) nombre d'exemplaires souhaité
    Valeur de retour (float) : montant de la commande
    Contraintes : nb ≥ 0
    Exemples :
    >>> montant_facture(400)
    45.0
    """
    n=nombre_exemplaires(nb)
    return .3*n if (n<=100) else .14*n if(n<=250) else .09*n if(n<=500) else .06*n if(n<=750) else .05*n if(n<=1000) else .03*n if(n<=2000) else .02*n

# Année bissextile
#9
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
    return (annee%4==0 and not annee%100==0) or annee%400==0

# Validité d'une date
def est_mois_valide(m):
    """
    Test de validité d'un numéro de mois
    Paramètre :
    - m : entier 
    Valeur de retour : booléen
    - True si m représente un mois valide, ie est compris entre 1 et 12
    - False sinon
    Contraintes : aucune
    Exemples : 
    >>> est_mois_valide(-1)
    False
    >>> est_mois_valide(15)
    False
    >>> import random
    >>> est_mois_valide(random.randint(1, 12))
    True
    """
    return 1 <= m <= 12
# 11
def nombre_jours(mois, annee):
    """
    Nombre de jours d'un mois donné d'une année donnée
    Paramètres :
    - mois, annee : entiers - le mois et l'année
    Valeur de retour :
    - entier - le nombre de jours dans le mois mois de l'année annee.
    Contrainte : 
    - mois est un mois valide
    Exemples :
    >>> nombre_jours(1, 2020)
    31
    >>> nombre_jours(2, 2018)
    28
    >>> nombre_jours(2, 2020)
    29
    """
    l1 = [1,3,5,7,8,10,12]
    l2 = [4,6,9,11]
    return 31 if (mois in l1) else 30 if (mois in l2) else 29 if (est_bissextile(annee)) else 28
# 12
def est_jour_valide(j, mois, annee):
    """
    Validité d'un numéro de jour pour un mois et une année donnée
    Paramètres :
    - j : entier - le jour à tester
    - mois, annee : entier - les mois et année 
    Valeur de retour : booléen
    - True si j est un jour valide pour le mois mois de l'année annee
    - False sinon
    Contraintes :
    - mois et annee valides
    Exemples :
    >>> est_jour_valide(-1, 1, 2020)
    False
    >>> est_jour_valide(32, 1, 2020)
    False
    >>> est_jour_valide(29, 2, 2018)
    False
    >>> est_jour_valide(29, 2, 2020)
    True
    """
    return True if ((1 <= j <= nombre_jours(mois, annee))) else False
# 13
def dateOK(j,m,a) :
    '''
    (bool) tel que j,m,a forment une date valide du calendrier grégorien
    j,m,a des entiers
    >>> dateOK(14,10,1582)
    False
    >>> dateOK(-1,10,2020)
    False
    >>> dateOK(11,10,2022)
    True
    >>> dateOK(29,2,2020)
    True
    '''
    return False if (a < 1582 or (a==1582 and j<15 and m<=10) or not est_mois_valide(m) or not est_jour_valide(j,m,a)) else True

# Nom du jour d'une date
# 14
def nom_jour(njour):
    """
    Le nom d'un jour de numéro de jour donné
    Paramètre :
    - njour : entier - numéro d'un jour, 0 pour dimanche, 1 pour lundi, ...
      6 pour samedi, 7 pour dimanche
    Valeur de retour :
    - chaîne de caractères - le nom du jour
    Contraintes :
    - njour compris entre 0 et 7
    Exemples :
    >>> nom_jour(0)
    'dimanche'
    >>> nom_jour(1)
    'lundi'
    >>> nom_jour(6)
    'samedi'
    >>> nom_jour(7)
    'dimanche'
    """
    l = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
    return l[njour]
# 15
def num_jour(jour, mois, annee):
    """
    Numéro du jour dans la semaine d'une date donnée 
    Paramètre :
    - jour : entier - le numéro du jour dans le mois
    - mois : entier - le numéro du mois dans l'année 
    - annee : entier - l'année
    Valeur de retour :
    - un entier, numéro du jour dans la semaine, de 0 (dimanche)
      à 6 (samedi)
    Contrainte :
    - le triplet (jour, mois, annee) doit être une date valide
    Exemples :
    >>> num_jour(1, 1, 2019)
    2
    >>> num_jour(1, 1, 2100)
    5
    >>> num_jour(25, 6, 2004)
    5
    >>> num_jour(13, 10, 2022)
    4
    """
    return (jour + annee - (1 if (mois==1 or mois==2) else 0) + annee//4 - annee//100 + (annee//100)//4 + (31*(mois + 12*(1 if (mois==1 or mois==2) else 0) - 2))//12)%7
# 16
def final(j,m,a) :
    '''
    jour de le semaine (str) si date valide (sinon False)
    j,m,a des entiers
    >>> final(1, 1, 2019)
    'mardi'
    >>> final(1, 1, 2100)
    'vendredi'
    >>> final(13, 10, 2022)
    'jeudi'
    >>> final(10, 13, 2022)
    False
    '''
    return nom_jour(num_jour(j,m,a)) if (dateOK(j,m,a)) else False


import doctest
doctest.testmod(verbose=False)