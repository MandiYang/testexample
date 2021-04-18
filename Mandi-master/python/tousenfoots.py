import random
import turtle as t

t.bgcolor('yellow')
tusenfoting =t.Turtle()
tusenfoting.shape('square')
tusenfoting.color('red')
tusenfoting.speed(0)
tusenfoting.penup()
tusenfoting.hideturtle()

blad = t.Turtle()
blad_form = ((0, 0), (14, 2), (18, 6), (20, 20), \
             (6, 18), (2, 14))
t.register_shape('blad', blad_form)
blad.shape('blad')
blad.color('green')
blad.penup()
blad.hideturtle()
blad.speed(0)

spel_startat = False
textsköldpadda = t.Turtle()
textsköldpadda.write('Tryck på MELLANSLAG för att starta', \
                   align='center', font=('Arial', 16, 'bold'))
textsköldpadda.hideturtle()
               
poängsköldpadda = t.Turtle()
poängsköldpadda.hideturtle()
poängsköldpadda.speed(0)

def utanför_fönster():
    vänster_vägg = -t.window_width() / 2
    höger_vägg = t.window_width() / 2
    övre_vägg = t.window_height() / 2
    nedre_vägg = -t.window_height() / 2
    (x, y) = tusenfoting.pos()
    utanför = \
            x< vänster_vägg or \
            x> höger_vägg or \
            y< nedre_vägg or \
            y> övre_vägg
    return utanför

def spelet_slut():
    tusenfoting.color('yellow')
    blad.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('SPELET ÄR SLUT!', align='center', font=('Arial', 30, 'normal'))

def visa_poäng(aktuell_poäng):
    poängsköldpadda.clear()
    poängsköldpadda.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    poängsköldpadda.setpos(x, y)
    poängsköldpadda.write(str(aktuell_poäng), align='right', \
                       font=('Arial', 40, 'bold'))

def placera_blad():
    blad.ht()
    blad.setx(random.randint(-200, 200))
    blad.sety(random.randint(-200, 200))
    blad.st()

def starta_spel():
    global spel_startat
    if spel_startat:
        return
    spel_startat = True

    poäng = 0
    textsköldpadda.clear()

    tusenfoting_hastighet = 1
    tusenfoting_längd = 3
    tusenfoting.shapesize(1, tusenfoting_längd, 1)
    tusenfoting.showturtle()
    visa_poäng(poäng)
    placera_blad()

    while True:
        tusenfoting.forward(tusenfoting_hastighet)
        if tusenfoting.distance(blad) < 20:
            placera_blad()
            tusenfoting_längd = tusenfoting_längd + 1
            tusenfoting.shapesize(1, tusenfoting_längd, 1)
            tusenfoting_hastighet = tusenfoting_hastighet + 1
            poäng = poäng + 10
            visa_poäng(poäng)
        if utanför_fönster():
            spelet_slut()
            break

def flytta_uppåt():
    if tusenfoting.heading() == 0 or tusenfoting.heading() == 180:
        tusenfoting.setheading(90)

def flytta_nedåt():
    if tusenfoting.heading() == 0 or tusenfoting.heading() == 180:
        tusenfoting.setheading(270)

def flytta_vänster():
    if tusenfoting.heading() == 90 or tusenfoting.heading() == 270:
        tusenfoting.setheading(180)

def flytta_höger():
    if tusenfoting.heading() == 90 or tusenfoting.heading() == 270:
        tusenfoting.setheading(0)

t.onkey(starta_spel, 'space')
t.onkey(flytta_uppåt, 'Up')
t.onkey(flytta_höger, 'Right')
t.onkey(flytta_nedåt, 'Down')
t.onkey(flytta_vänster, 'Left')
t.listen()
t.mainloop()
