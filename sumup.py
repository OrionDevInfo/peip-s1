from random import choice, randint
from math import pi, cos
nb = 1234
# unité: nb%10 | str(nb)[-1]
# nb dizaines: (nb%100-nb%10)//10 | str(nb)[:-1]
# chiffre dizaine: (nb-nb%10)//10 | str(nb)[-2]
def impair(x): return x % 2 == 1
def multiple7(x): return x % 7 == 0
def empty(chaine): return chaine == ''
def empty2(chaine): return len(chaine) == 0
def sup0(x): return x >= 0
def sup2nb(x, y): return sup0(x) and sup0(y)
def memesignes(x, y): return sup2nb(x, y) or (x <= 0 and y <= 0)
def signesoppo(x, y): return memesignes(x, -y)
def inter(x, a, b): return a <= x <= b
def est_glace(x): return -273.15 < x < 0
def est_liquide(x): return 0 <= x <= 100
def tolerance(a, b, t): return b-t <= a <= b+t
def cercle_circonference(r): return round(2*r*pi, 2)
def cercle_aire(r): return round(pi*r**2, 2)
def cote_adjacent(alpha, h): return cos(alpha)*h
def de(n): return randint(1, n)
def choisi_caractere(chaine): return choice(chaine)
def puissance(a, n): return a**n
def enluminure1(c=str): return '-'*len(c)  # '-----'
def enluminure2(c=str): return '-'*(len(c)//2)+'O'+'-'*(len(c)//2)  # '--O--'
def enluminure3(c=str):  # '-o-O-o-'
    p1 = '-o'*(len(c)//4)
    return p1+'O'+p1[::-1]
def xor(x, y): return x != y
def maximum(a, b): return a if (a >= b) else b
def minimum(a, b): return a if (a <= b) else b
def v_abs(x): return x if (x >= 0) else -x
def parite(x): return 'pair' if (x % 2 == 0) else 'impair'
def signe(x): return 'positif' if(x > 0) else 'négatif' if(x < 0) else 'nul'
def pileface(): return 'pile' if(randint(0, 1) == 1) else 'face'
def maximum3(x, y, z): return maximum(maximum(x, y), z)
def maximum3_v2(x, y, z): return x if (x >= y and x >= z) else y if(y >= x and y >= z) else z
def mediane(x, y, z): return x+y+z - maximum3(x, y, z) - (minimum(minimum(x, y), z))
def saison(j, m):
    r = 'hiver'
    if ((j >= 20 and m == 3) or m == 4 or m == 5 or (j <= 20 and m == 6)): r = 'printemps'
    elif ((j >= 21 and m == 6) or m == 7 or m == 8 or (j <= 21 and m == 9)): r = 'été'
    elif ((j >= 22 and m == 9) or m == 10 or m == 11 or (j <= 20 and m == 12)): r = 'automne'
    return r
def ordre1(a, b, c):
    i = minimum(minimum(a, b), c)
    j = mediane(a, b, c)
    k = maximum3_v2(a, b, c)
    return i, j, k
def ordre2(a, b, c):
    if b < a: a, b = b, a
    if c < a: a, c = c, a
    if c < b: b, c = c, b
    return a, b, c
def ff421(d1, d2, d3): return True if(ordre2(d1, d2, d3) == (1, 2, 4)) else False
def est_bissextile(annee): return (annee % 4 == 0 and not annee % 100 == 0) or annee % 400 == 0
def sequence_10_20():
    for i in range(10,21) : print(i)
def sequence_0_20():
    for i in range(21) : print(i)
# range(10) peut s'écrire sous la forme range( 0, 10, 1 ).
# range(x,y,z) : 
# x: le début de l'intervalle compris, default: 0
# y: la fin de l'intervalle exclu, required
# z: le pas dans l'intervalle, sens inverse si négatif (x>y pour fonctionner), default: 1
from curses.ascii import islower
def sont_minuscules(chaine):
    b=True
    for l in chaine:
        if not islower(l) and l!=' ' : b=False
    return b
def somme_entiers(n): # return sum(i for i in range(1,n+1))
    s = 0
    for i in range(n+1) : s+=i
    return s
def somme_carres(n): # return sum(i**2 for i in range(1,n+1)) 
    s=0
    for i in range(1,n+1) : s+=i**2
    return s
def somme_impairs(n):
    s=0
    for i in range(1,2*n+1,2) : s+=i
    return s
def somme_alternee(n=int):
    """     Renvoie le n-ième terme de la série harmonique alternée
    Return float: -1/1 + 1/2 - 1/3 + ... + (-1)^n/n | Contrainte: n>0   """
    return ((-1)**n)/n + somme_alternee(n-1) if (n>1) else ((-1)**n)/n
def factorielle(n):
    f=1
    for i in range(1,n+1) : f*=i
    return f
def nombre_caracteres(s): return len(s)
def nombre_espaces(c):
    s=0
    for l in c :
        if l==' ': s+=1
    return s
def nombre_ponctuations(c):
    p = ['.','?','!']
    s=0
    for l in c:
        if l in p: s+=1
    return s
def occurrences_caractere(c, carac):
    o=0
    for l in c:
        if l==carac : o+=1
    return o
def occurences(chaine) :
        o = {k:0 for k in '$%#~&'}
        for i in chaine :
            o[i]+=1
        return o 
def terme_suite(n):
    u=1
    for i in range(1,n+1) : u=2*u+3
    return u
def chaine_multiplication(a, b): return f'{a} x {b} = {a*b}'
def table_multiplication(n):
    s=''
    for i in range(11):
        s+=f' | {chaine_multiplication(i,n)}'
    return s+' | '
def paire2str(a, b): return '{'+f'{a},{b}'+'}'
def les_paires(n):
    s =''
    for i in range(1,n+1) :
        for j in range(1,n+1):
            if i<=j : s+=paire2str(i,j)+' '
    return s
def affiche_ligne(n) : print(n*'o')
def affiche_bloc(n):
    for i in range(n) : affiche_ligne(n)
def affiche_bloc2(n):
    for i in range(n) :
        l=''
        for j in range(n) :l+='o'
        print(l)
def affiche_triangle(n):
    for i in range(1,n+1) : affiche_ligne(i)
def affiche_triangle2(n):
    for i in range(1,n+1) :
        l=''
        for j in range(i) :l+='o'
        print(l)
def affiche_diago(n):
    for i in range(1,n+1) :
        l=''
        for j in range(1,n+1) :
            if i==j : l+='X'
            else: l+='o'
        print(l)
def maj(c) : return c.upper()
def capitales(c) : 
    c2 = ''
    for l in range(len(c)) :
        if c[l-1] ==  ' ' or l==0 : c2+= c[l].upper()
        else: c2+= c[l]
    return c2
def miroir(c) : return c[::-1]
def anacycliques(c1,c2) : return c1 == c2[::-1] 
