# Auteurs : Orion
#
# Date : 27/10/2022
#
# État : Terminé
#
#
#
#
import turtle

def spiral(n) :
    turtle.pencolor("red")
    for i in range(n):
        turtle.forward(i * 10)
        turtle.right(144)
# spiral(20)

#1
def carre(c) :
    for i in range(4) :
        turtle.forward(c)
        turtle.left(90)
# carre(50)
# 2
def cinqCarre() :
    l = [i for i in range(10,60,10)]
    for i in l: carre(i)
# cinqCarre()
def cinquanteCarre() :
    l = [i for i in range(10,510,10)]
    for i in l: carre(i)
# cinquanteCarre()
# 3
def dixCarre():
    for i in range(10):
        turtle.down()
        carre(50)
        turtle.up()
        turtle.forward(55)
# dixCarre()
# 4 
def centCarre() :
    for i in range(10) :
        turtle.down()
        dixCarre()
        turtle.up()
        turtle.right(180)
        turtle.forward(550)
        turtle.left(90)
        turtle.forward(55)
        turtle.left(90)
# centCarre()
# 5
def carreTournant(n) :
    for i in range(n) :
        carre(100)
        turtle.left(360/n)
# carreTournant(12)
# 6
def carreEmboites(l) :
    for i in range(min(l,10)) : # Pour pouvoir avoir de grands carrés mais ne pas tourner à l'infini
        carre(l)
        turtle.forward(l/2)
        turtle.left(45)
        l= ((l/2)**2 + (l/2)**2)**.5
# carreEmboites(100)
# 7
def dessine(c,l,a) :
    for i in c :
        if i == ('F' or 'G') : turtle.forward(l)
        elif i == '+' : turtle.left(a)
        elif i == '-' : turtle.right(a)
# dessine('++F-F--F-F',100,45)
# 8
def carreHexa() :
    carre='F+++F+++F+++F+++'
    hexa='F++F++F++F++F++F++F'
    dessine(carre+hexa,100,30)
# carreHexa()
# 9
def polygoneRegulier(n,l) :
    c='F+'*n
    dessine(c,l,360/n)
# polygoneRegulier(5,100)
# 10
def polygones(mini,maxi,l) :
    for i in range(mini,maxi+1) :
        polygoneRegulier(i,l)
# polygones(3,5,100)
# polygones(3,12,100)
# 11
# def derive(c1,c2) : return c1.replace(c1,c2)
# def deriveN(c1,c2,n) :
#     '''
#     >>> deriveN('F', '+FF', 1)
#     '+FF'
#     '''
#     for i in range(n) : derive(c1,c2)

# from doctest import testmod
# testmod(verbose=False)