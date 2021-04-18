import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL
print('spelare1 enter q')
print('spelare2 enter p')


def nästa_form():
    global form
    global föregående_färg
    global aktuell_färg

    föregående_färg = aktuell_färg

    c.delete(form)
    if len(former) > 0:
        form = former.pop()
        c.itemconfigure(form, state=NORMAL)
        aktuell_färg = c.itemcget(form, 'fill')
        root.after(1000, nästa_form)
    else:
        c.unbind('q')
        c.unbind('p')
        if spelare1_poäng > spelare2_poäng:
            c.create_text(200, 200, text='Vinnare: Spelare1')
        elif spelare2_poäng > spelare1_poäng:
            c.create_text(200, 200, text='Vinnare: Spelare2')
        else:
            c.create_text(200, 200, text='Oavgjort')
        c.pack()

def snap(händelse):
    global form
    global spelare1_poäng
    global spelare2_poäng
    global föregående_färg
    valid = False

    c.delete(form)
    
    if föregående_färg == aktuell_färg:
        valid = True

    if valid:
        if händelse.char == 'q':
            spelare1_poäng = spelare1_poäng  + 1
            form = c.create_text(200, 200, text='SNAP! spelare1 får 1 poäng!')
        else:
            spelare2_poäng = spelare2_poäng + 1
            form = c.create_text(200, 200, text='SNAP! spelare2 får 1 poäng!')
        föregående_färg = ''
    else:
        if händelse.char == 'q':
            spelare1_poäng = spelare1_poäng - 1
            form = c.create_text(200, 200, text='FEL! spelare1 förlorar 1 poäng!')
        else:
            spelare2_poäng = spelare2_poäng - 1
            form = c.create_text(200, 200, text='FEL! spelare2 förlorar 1 poäng!')
    c.pack()
    root.update_idletasks()
    time.sleep(1)

root = Tk()
root.title('Snap')
c = Canvas(root, width = 400, height = 400)

former = []

cirkel = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
former.append(cirkel)
cirkel = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
former.append(cirkel)
cirkel = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
former.append(cirkel)
cirkel = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
former.append(cirkel)
cirkel = c.create_oval(35, 20, 365, 350, outline='yellow', fill='yellow', state=HIDDEN)
former.append(cirkel)
cirkel = c.create_oval(35, 20, 365, 350, outline='purple', fill='purple', state=HIDDEN)
former.append(cirkel)

rektangel = c.create_rectangle(35, 100, 365, 270, outline='yellow', fill='yellow', state=HIDDEN)
former.append(rektangel)
rektangel = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
former.append(rektangel)
rektangel = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
former.append(rektangel)
rektangel = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
former.append(rektangel)
rektangel = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
former.append(rektangel)
rektangel = c.create_rectangle(35, 100, 365, 270, outline='purple', fill='purple', state=HIDDEN)
former.append(rektangel)

kvadrat = c.create_rectangle(35, 20, 365, 350, outline='yellow', fill='yellow', state=HIDDEN)
former.append(kvadrat)
kvadrat = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
former.append(kvadrat)
kvadrat = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
former.append(kvadrat)
kvadrat = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
former.append(kvadrat)
kvadrat = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
former.append(kvadrat)
kvadrat = c.create_rectangle(35, 20, 365, 350, outline='purple', fill='purple', state=HIDDEN)
former.append(kvadrat)

polygon = c.create_polygon(35, 200, 365, 200, 200, 35, outline='blue', fill='blue', state=HIDDEN)
former.append(polygon)
polygon = c.create_polygon(35, 200, 365, 200, 200, 35, outline='yellow', fill='yellow', state=HIDDEN)
former.append(polygon)
polygon = c.create_polygon(35, 200, 365, 200, 200, 35, outline='red', fill='red', state=HIDDEN)
former.append(polygon)
polygon = c.create_polygon(35, 200, 365, 200, 200, 35, outline='black', fill='black', state=HIDDEN)
former.append(polygon)
polygon = c.create_polygon(35, 200, 365, 200, 200, 35, outline='green', fill='green', state=HIDDEN)
former.append(polygon)
polygon = c.create_polygon(35, 200, 365, 200, 200, 35, outline='purple', fill='purple', state=HIDDEN)
former.append(polygon)
c.pack()
random.shuffle(former)

form = None
föregående_färg = 'a'
aktuell_färg = 'b'
spelare1_poäng = 0
spelare2_poäng = 0

root.after(3000, nästa_form)
c.bind('q', snap)
c.bind('p', snap)
c.focus_set()

root.mainloop()


