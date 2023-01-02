import random
from doctest import testmod


def extrema(l):
    """Renvoie la valeur des plus petits et des plus grands éléments de l.
    Paramètres :
    - l (list) : une liste (ne doit pas être vide)
    Valeur de retour (list) : les plus petite et plus grande valeurs dans l
    Exemples :
    >>> extrema(["cheval", "autruche", "tigre", "zèbre", "fourmi"])
    ['autruche', 'zèbre']
    """
    assert l, "l ne doit pas être vide"

    min_value = l[0]
    max_value = l[0]
    for value in l:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value

    return [min_value, max_value]


def sommes_prefixes(l):
    """Renvoie une liste contenant les sommes préfixes de l.
    Paramètres :
    - l (list) : une liste de nombres
    Valeur de retour (list) : les sommes préfixes de l
    Exemples :
    >>> sommes_prefixes([2, 4, 3, 1])
    [2, 6, 9, 10]
    """
    sommes_prefixes = []
    total = 0
    for value in l:
        total += value
        sommes_prefixes.append(total)
    return sommes_prefixes


def moyenne_ponderee(mesures, coefficients):
    """Renvoie la moyenne pondérée des mesures par les coefficients.
    Paramètres :
    - mesures (list) : une liste de nombres
    - coefficients (list) : une liste de nombres
    Valeur de retour (float) : la moyenne pondérée des mesures par les coefficients
    Exemples :
    >>> moyenne_ponderee([14.0, 15.0, 11.0], [2, 1, 2])
    13.0
    """
    assert len(mesures) == len(
        coefficients), "les listes mesures et coefficients doivent avoir la même longueur"
    assert all(isinstance(x, (int, float))
               for x in mesures), "mesures doit être une liste de nombres"
    assert all(isinstance(x, (int, float))
               for x in coefficients), "coefficients doit être une liste de nombres"

    total_ponderation = 0
    total_mesure = 0
    for i in range(len(mesures)):
        total_ponderation += coefficients[i]
        total_mesure += mesures[i] * coefficients[i]
    return total_mesure / total_ponderation


def prefixes(s):
    """Renvoie la liste des préfixes de s.
    Paramètres :
    - s (str) : une chaîne de caractères
    Valeur de retour (list) : les préfixes de s
    Exemples :
    >>> prefixes('motus')
    ['', 'm', 'mo', 'mot', 'motu', 'motus']
    """
    prefixes = []
    for i in range(len(s) + 1):
        prefixes.append(s[:i])
    return prefixes


def suffixes(s):
    """Renvoie la liste des suffixes de s.
    Paramètres :
    - s (str) : une chaîne de caractères
    Valeur de retour (list) : les suffixes de s
    Exemples :
    >>> suffixes('fin')
    ['', 'n', 'in', 'fin']
    """
    suffixes = []
    for i in range(len(s), -1, -1):
        suffixes.append(s[i:])
    return suffixes


def facteurs(s):
    """Renvoie la liste des facteurs de s.
    Paramètres :
    - s (str) : une chaîne de caractères
    Valeur de retour (list) : les facteurs de s
    Exemples :
    >>> facteurs('tot')
    ['', 't', 'to', 'tot', 'o', 'ot', 't']
    """
    facteurs = ['']
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            facteurs.append(s[i:j])
    return facteurs


def melange(n):
    """Renvoie une permutation aléatoire des entiers de range(n).
    Paramètres :
    - n (int) : un entier
    Valeur de retour (list) : une permutation aléatoire des entiers de range(n)
    Exemples :
    >>> melange(5)
    [2, 1, 4, 0, 3]
    # Réponse aléatoire, il faut juste que les chiffres soient de 0 à 4 une fois chacun.
    """
    a_vider = list(range(n))
    permutation = []
    while a_vider:
        i = random.randint(0, len(a_vider) - 1)
        permutation.append(a_vider[i])
        del a_vider[i]
    return permutation


def gather(values, indices):
    """Renvoie une liste de valeurs sélectionnées par les indices.
    Paramètres :
    - values (list) : une liste de valeurs
    - indices (list) : une liste d'indices
    Valeur de retour (list) : une liste de valeurs sélectionnées par les indices
    Exemples :
    >>> gather(list(range(5, 12)), [2, 3, 0, 6])
    [7, 8, 5, 11]
    >>> gather(["William", "Jack", "Rantanplan", "Joe", "Averell"], [3, 0, 1, 4])
    ['Joe', 'William', 'Jack', 'Averell']
    """
    assert all(0 <= i < len(values)
               for i in indices), "tous les indices doivent être valides"
    return [values[i] for i in indices]


def liste_melangee(model):
    """Renvoie une nouvelle liste dont les éléments sont ceux de model, dans un ordre aléatoire.
    Paramètres :
    - model (list) : une liste de valeurs
    Valeur de retour (list) : une nouvelle liste avec les éléments de model dans un ordre aléatoire
    Exemples :
    >>> liste_melangee([5, 6, 7, 8])
    [8, 6, 7, 5]
    # Réponse aléatoire !!
    >>> liste_melangee(["chat", "chien", "oiseau", "lapin"])
    ['lapin', 'chien', 'chat', 'oiseau']
    # Réponse aléatoire !!
    """
    indices = list(range(len(model)))  # liste des indices de model
    random.shuffle(indices)  # mélange aléatoire des indices
    return [model[i] for i in indices]  # construction de la liste mélangée


def range_a_trous(maximum, absents):
    """Renvoie une liste de valeurs entières inférieures à maximum qui ne sont pas dans la liste absents.
    Paramètres :
    - maximum (int) : valeur maximale de la liste
    - absents (list) : liste des valeurs à exclure de la liste
    Valeur de retour (list) : une liste de valeurs entières inférieures à maximum qui ne sont pas dans la liste absents
    Exemples :
    >>> range_a_trous(12, [3, 6, 7, 9])
    [0, 1, 2, 4, 5, 8, 10, 11]
    >>> range_a_trous(18, list(range(12)))
    [12, 13, 14, 15, 16, 17]
    >>> range_a_trous(18, list(range(12)) + [15])
    [12, 13, 14, 16, 17]
    """
    values = []
    i = 0
    for n in range(maximum):
        if i < len(absents) and absents[i] == n:
            i += 1
        else:
            values.append(n)
    return values


testmod(verbose=False)
