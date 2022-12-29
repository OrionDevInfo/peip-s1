from doctest import testmod


def maximum(l):  # max()
    """Renvoie la valeur des plus grands éléments de l.
    Paramètres :
    - l (list) : une liste de nombres (ne doit pas être vide)
    Valeur de retour (int ou float) : la plus grande valeur dans l
    Exemples :
    >>> maximum([4, 4, 3, 1, 2, 1, 1, 3])
    4
    """
    assert l, "l ne doit pas être vide"
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste de nombres"
    vmax = l[0]
    for e in l:
        if e > vmax:
            vmax = e
    return vmax


def minimum(l):  # min()
    """Renvoie la valeur des plus petits éléments de l.
    Paramètres :
    - l (list) : une liste de nombres (ne doit pas être vide)
    Valeur de retour (int ou float) : la plus petite valeur dans l
    Exemples :
    >>> minimum([4, 4, 3, 1, 2, 1, 1, 3])
    1
    """
    assert l, "l ne doit pas être vide"
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste de nombres"
    vmin = l[0]
    for e in l:
        if e < vmin:
            vmin = e
    return vmin


def nombre_occurrences(v, l):  # l.count(v)
    """Renvoie le nombre d'occurrences de la valeur v parmi les éléments de l.
    Paramètres :
    - v : la valeur à rechercher (peut être de n'importe quel type)
    - l (list) : la liste dans laquelle chercher (peut être de n'importe quel type)
    Valeur de retour : le nombre d'occurrences de v dans l (int)
    Exemples :
    >>> nombre_occurrences(2, [4, 2, 6, 2, 2, 5, 4])
    3
    >>> nombre_occurrences(4, [4, 2, 6, 2, 2, 5, 4])
    2
    """
    compteur = 0
    for e in l:
        if e == v:
            compteur += 1
    return compteur


def somme(l):  # sum(l)
    """Renvoie la somme des valeurs des éléments de l.
    Paramètres :
    - l (list) : une liste de nombres (int ou float)
    Valeur de retour (int ou float) : la somme des éléments de l
    Exemples :
    >>> somme([1, 2, 3, 4])
    10
    """
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste de nombres"
    s = 0
    for e in l:
        s += e
    return s


def moyenne(l):
    """Renvoie la moyenne arithmétique des valeurs des éléments de l.
    Paramètres :
    - l (list) : une liste de nombres (int ou float)
    Valeur de retour (float) : la moyenne des éléments de l
    Exemples :
    >>> moyenne([1, 2, 3, 4])
    2.5
    """
    assert l, "l ne doit pas être vide"
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste de nombres"
    s = somme(l)
    return s / len(l)


def variance(l):
    """Renvoie la variance des valeurs des éléments de l.
    Paramètres :
    - l (list) : une liste de nombres (int ou float)
    Valeur de retour (float) : la variance des éléments de l
    Exemples :
    >>> variance([1, 2, 3, 4, 5])
    2.5
    >>> variance([1, 2, 3, 4, 5, 6, 7])
    4.666666666666666
    """
    assert l, "l ne doit pas être vide"
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste de nombres"
    m = moyenne(l)
    variance = (1 / (len(l) - 1)) * sum((x - m)**2 for x in l)
    return variance


def tous_positifs(l):
    """Renvoie True si et seulement si la liste l ne contient que des éléments positifs ou nuls.
    Paramètres :
    - l (list) : une liste d'entiers ou de nombres à virgule flottante
    Valeur de retour (bool) : True si et seulement si la liste l ne contient que des éléments positifs ou nuls
    Exemples :
    >>> tous_positifs([1, 2, 3])
    True
    >>> tous_positifs([0, 1, 2])
    True
    >>> tous_positifs([1, -2, 3])
    False
    """
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste d'entiers ou de nombres à virgule flottante"
    for x in l:
        if x < 0:
            return False
    return True


def au_moins_un_positif(l):
    """Renvoie True si et seulement si la liste l contient au moins un élément positif ou nul.
    Paramètres :
    - l (list) : une liste d'entiers ou de nombres à virgule flottante
    Valeur de retour (bool) : True si et seulement si la liste l contient au moins un élément positif ou nul
    Exemples :
    >>> au_moins_un_positif([1, 2, 3])
    True
    >>> au_moins_un_positif([0, -1, -2])
    True
    >>> au_moins_un_positif([-1, -2, -3])
    False
    """
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste d'entiers ou de nombres à virgule flottante"
    for x in l:
        if x >= 0:
            return True
    return False


def nombre_positifs(l):
    """Renvoie le nombre d'éléments positifs ou nuls de la liste l.
    Paramètres :
    - l (list) : une liste d'entiers ou de nombres à virgule flottante
    Valeur de retour (int) : le nombre d'éléments positifs ou nuls de la liste l
    Exemples :
    >>> nombre_positifs([1, 2, 3])
    3
    >>> nombre_positifs([0, -1, -2])
    1
    >>> nombre_positifs([-1, -2, -3])
    0
    """
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste d'entiers ou de nombres à virgule flottante"
    compteur = 0
    for x in l:
        if x >= 0:
            compteur += 1
    return compteur


def filtre_positifs(l):
    """Renvoie la liste des éléments positifs ou nuls de la liste l.
    Paramètres :
    - l (list) : une liste d'entiers ou de nombres à virgule flottante
    Valeur de retour (list) : la liste des éléments positifs ou nuls de la liste l
    Exemples :
    >>> filtre_positifs([1, 2, 3])
    [1, 2, 3]
    >>> filtre_positifs([0, -1, -2])
    [0]
    >>> filtre_positifs([-1, -2, -3])
    []
    >>> filtre_positifs([0, -1, -5, 2, 8, -13])
    [0, 2, 8]
    """
    assert all(isinstance(x, (int, float))
               for x in l), "l doit être une liste d'entiers ou de nombres à virgule flottante"
    resultat = []
    for x in l:
        if x >= 0:
            resultat.append(x)
    return resultat


def est_croissante(l):
    """Renvoie True si et seulement si la liste l est croissante.
    Paramètres :
    - l (list) : une liste d'éléments comparables
    Valeur de retour (bool) : True si la liste l est croissante, False sinon
    Exemples :
    >>> est_croissante([1, 2, 4])
    True
    >>> est_croissante(["un", "deux", "quatre"])
    False
    >>> est_croissante([])
    True
    """
    if not l:
        return True
    for i in range(1, len(l)):
        if l[i] <= l[i - 1]:
            return False
    return True


def suite_partielle(n):
    """Renvoie la liste des n+1 premiers termes de la suite u.
    Paramètres :
    - n (int) : un entier strictement positif
    Valeur de retour (list) : la liste des n+1 premiers termes de la suite u
    Exemples :
    >>> suite_partielle(3)
    [1, 5, 13, 29]
    >>> suite_partielle(1)
    [1, 5]
    >>> suite_partielle(2)
    [1, 5, 13]
    >>> suite_partielle(0)
    [1]
    """
    assert isinstance(
        n, int) and n >= 0, "n doit être un entier strictement positif"
    u = [1]
    for i in range(1, n+1):
        u.append(2*u[i-1] + 3)
    return u


testmod(verbose=False)
