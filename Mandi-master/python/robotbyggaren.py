import turtle as t
t.shape('turtle')
t.setheading(0)

def rektangel(vågrät, lodrät, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for x in range(1, 3):
        t.forward(vågrät)
        t.right(90)
        t.forward(lodrät)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

# fötter
t.goto(-100, -150)
rektangel(50, 20, 'blue')
t.goto(-30, -150)
rektangel(50, 20, 'blue')

# ben
t.goto(-25, -50)
rektangel(15, 100, 'grey')
t.goto(-55, -50)
rektangel(-15, 100, 'grey')

# kropp
t.goto(-90, 100)
rektangel(100, 150, 'red')

# armar
t.goto(-150, 70)
rektangel(60, 15, 'grey')
t.goto(-150, 110)
rektangel(15, 40, 'grey')

t.goto(10, 70)
rektangel(60, 15, 'grey')
t.goto(55, 110)
rektangel(15, 40, 'grey')

#hals
t.goto(-50, 120)
rektangel(15, 20, 'grey')

# huvud
t.goto(-85, 170)
rektangel(80, 50, 'red')

# ögon
t.goto(-60, 160)
rektangel(30, 10, 'white')
t.goto(-55, 155)
rektangel(5, 5, 'black')
t.goto(-40, 155)
rektangel(5, 5, 'black')

#mun
t.goto(-65, 135)
rektangel(40, 5, 'black')

t.hideturtle()





















           
    
