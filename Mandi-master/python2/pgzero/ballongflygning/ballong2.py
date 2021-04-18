'Det finns tre lufthinder och tre markhiner, du är ballongen som ska styra dig förbi alla hinder'
'utan att krascha i dom.'

import pgzrun
from random import randint
import pygame

WIDTH = 800
HEIGHT = 600

ballong = Actor("balloon")
ballong.pos = 400, 300

fagel = Actor("bird-up")
fagel.pos = randint(800, 1600), randint(5, 80)

fagel2 = Actor("bird-up")
fagel2.pos = randint(800, 1600), randint(10, 170)

fagel3 = Actor("bird-up")
fagel3.pos = randint(800, 1600), randint(150, 470)

hus = Actor("house")
hus.pos = randint(800, 1600), 460

hus2 = Actor("house")
hus2.pos = randint(800, 1600), 460

trad = Actor("tree")
trad.pos = randint(800, 1600), 450

fagel_upp = True
upp = False
spelet_slut = False
summa = 0
antal_uppdateringar = 0

summor = []

def uppdatera_rekord():
    global summa, summor
    filnamn = r"/home/mandi/Desktop/Mandi-master/python2/pgzero/ballongflygning/rekord2.txt"
    summor = []
    with open(filnamn, "r") as fil:
        rad = fil.readline()
        rekorden = rad.split()
        for rekord in rekorden:
            if (summa > int(rekord)):
                summor.append(str(summa) + " ")
                summa = int(rekord)
            else:
                summor.append(str(rekord) + " ")
    with open(filnamn, "w") as fil:
        for rekord in summor:
            fil.write(rekord)
        

def visa_rekord():
    screen.draw.text("REKORD", (350, 150), color="black")
    y = 175
    position = 1
    for rekord in summor:
        screen.draw.text(str(position) + ". " + rekord, (350, y), color="black")
        y += 25
        position += 1
    
def draw():
    screen.blit("background", (0,0))
    if not spelet_slut:
        ballong.draw()
        fagel.draw()
        fagel2.draw()
        fagel3.draw()
        hus.draw()
        hus2.draw()
        trad.draw()
        screen.draw.text("Summa: " + str(summa), (700, 5), color="black")
    else:
        visa_rekord()

def on_mouse_down():
    global upp
    upp = True
    ballong.y -= 55

def on_mouse_up():
    global upp
    upp = False

def flaxa():
    global fagel_upp
    if fagel_upp:   
        fagel.image = "bird-down"
        fagel2.image = "bird-down"
        fagel3.image = "bird-down"
        fagel_upp = False
    else:
        fagel.image = "bird-up"
        fagel2.image = "bird-up"
        fagel3.image = "bird-up"
        fagel_upp = True
   
def update():
    global spelet_slut, summa, antal_uppdateringar
    if not upp:
        ballong.y += 1

    if fagel.x > 0 or fagel2.x > 0 or fagel3.x > 0:
        fagel.x -= 4
        fagel2.x -= 4
        fagel3.x -= 4
        if antal_uppdateringar == 9:
            flaxa()
            antal_uppdateringar = 0
        else:
            antal_uppdateringar += 1
    else:
        fagel.x = randint(800, 1600)
        fagel.y = randint(10, 350)
        fagel2.x = randint(800, 1600)
        fagel2.y = randint(10, 200)
        fagel3.x = randint(800, 1600)
        fagel3.y = randint(10, 470)
        summa += 8
        antal_uppdateringar = 0

    if hus.right > 0 or hus2.right > 0:
        hus.x -= 2
        hus2.x -= 2
    else:
        hus.x = randint(800, 1600)
        hus2.x = randint(800, 1600)
        summa += 2

    if trad.right > 0:
        trad.x -= 2
    else:
        trad.x = randint(800, 1600)
        summa += 1

    if ballong.top < 5 or ballong.bottom > 560:
        spelet_slut = True
        uppdatera_rekord()

    if ballong.collidepoint(fagel.x, fagel.y) or \
       ballong.collidepoint(fagel2.x, fagel2.y) or \
       ballong.collidepoint(fagel3.x, fagel3.y) or \
       ballong.collidepoint(hus.x, hus.y) or \
       ballong.collidepoint(hus2.x, hus2.y) or \
       ballong.collidepoint(trad.x, trad.y):
        spelet_slut = True
        uppdatera_rekord()
            
pgzrun.go()
'ha en trevlig stund.'
        

