# Auteur: Orion
# Date: 19/09/2022
# Objet: TP 01 - Niveau intermédiaire
# État: Terminé - Exo 1 à 11
#       Résultats des calculs pour les exos 4 & 5 ne correspondent pas aux attentes

# Échange de valeurs
# 1
'''
n1 = 'Un'
n2 = 'Deux'
n2 = n1
n1 = n2
=> Donc n1='Un' & n2='Un'
Pour échanger les valeurs des 2 variables, plusieurs solutions sont possibles :
• Permutation
n1='Un'
n2='Deux'
n1, n2 = n2, n1
• Utilisation varaible valeur tampon
n1='Un'
n2='Deux'
n3=n1
n1=n2
n2=n3
'''
# 2
'''
• Permutation circulaire 3 variables
n1='Un'
n2='Deux'
n3='Trois'
n1, n2, n3 = n3, n1, n2
• Permutation circulaire 4 variables
n1='Un'
n2='Deux'
n3='Trois'
n4='Quatre'
n1, n2, n3, n4 = n4, n1, n2, n3
'''
# Programme de calcul
# 3
'''
nb = float(input('Nombre: '))
résultat = nb+3
résultat*=2
résultat+=nb
résultat-=12
résultat/=3
résultat+=2
'''
# Calculs d'intérêts
# 4
'''
c = 1000000
r = .05
t = 5
n = 2
a_t5_n2 = c*(1+(r/n))**(n*t)
print(a_t5_n2) #  1280084,54
'''
# 5
'''
c = 1000000
r = .05
t = 5
n = 4
a_t5_n4 = c*(1+(r/n))**(n*t)

print(a_t5_n4) #  1282037,23
'''
# Chiffres et divisions euclidiennes
# 6
'''
nb='2031'
nb[-1] # Chiffre des unités
'''
# 7
'''
nb='2031'
nb[:-1] # Nombre de dizaines
'''
# 8
'''
nb='2031'
nb[-2] # Chiffre des dizaines
'''
# 9
'''
nip = 123456789
n = 5
nième_droite = int(str(nip)[-n])
'''
# Dans l'ordre
# 10
'''
coeff = 3
str1 = 'oh '
str2 = coeff * str1
str2 = str2 + '!'
'''
# 11
'''
coeff2 = 3
coeff3 = coeff2 - 1
str1 = 'oh '
str2 = coeff2 * str1
str1 = 'oh !'
str2 = str2 + '!'
'''
