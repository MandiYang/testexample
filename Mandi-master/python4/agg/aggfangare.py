from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
import time
from pygame import mixer
mixer.init()
beep = mixer.Sound("eep.wav")


kanvasbredd = 800
kanvashöjd = 400

root = Tk()
c = Canvas(root, width=kanvasbredd, height=kanvashöjd, \
background='deep sky blue')
c.create_rectangle(-5, kanvashöjd - 100, kanvasbredd + 5, \
kanvashöjd + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0) 
c.pack()
root.update()

färgcykel = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
äggbredd = 45
ägghöjd = 50
äggsumma = 10
ägghastighet = 500
äggintervall = 4000
svårighetsfaktor = 0.95

fångarfärg = 'blue'
fångarbredd = 100
fångarhöjd = 100
fångare_start_x = kanvasbredd / 2 - fångarbredd / 2
fångare_start_y = kanvashöjd - fångarhöjd - 20
fångare_start_x2 = fångare_start_x + fångarbredd
fångare_start_y2 = fångare_start_y + fångarhöjd

fångare = c.create_arc(fångare_start_x, fångare_start_y, \
                       fångare_start_x2, fångare_start_y2, start=200, extent=140, \
                       style='arc', outline=fångarfärg, width=3)

spel_typsnitt = font.nametofont('TkFixedFont')
spel_typsnitt.config(size=18)

summa=0
summa_text = c.create_text(10, 10, anchor='nw', font=spel_typsnitt, fill='darkblue', \
                           text='Poäng: ' + str(summa))

liv_kvar = 5
liv_text = c.create_text(kanvasbredd - 10, 10, anchor='ne', font=spel_typsnitt, \
                           fill='darkblue', text='Liv ' + str(liv_kvar))
äggen = []

def skapa_ägg():
    x = randrange(10, 740)
    y = 40
    nytt_ägg = c.create_oval(x, y, x + äggbredd, y + ägghöjd, fill=next(färgcykel), width=0)
    äggen.append(nytt_ägg)
    root.after(äggintervall, skapa_ägg)

def flytta_äggen():
    for ägg in äggen:
        root.update()
        (ägg_x, ägg_y, ägg_x2, ägg_y2) = c.coords(ägg)
        c.move(ägg, 0, 10)
        if ägg_y2 > kanvashöjd:
            tappat_ägg(ägg)
    root.after(ägghastighet, flytta_äggen)

def tappat_ägg(ägg):
    root.update()
    äggen.remove(ägg)
    c.delete(ägg)
    förlora_ett_liv()
    if liv_kvar == 0:
        root.update()
        messagebox.showinfo('Spelet är slut!', 'Slutpoäng: ' \
                            + str(summa))
        root.destroy()

def förlora_ett_liv():
    global liv_kvar
    liv_kvar -= 1
    beep.play()
    c.itemconfigure(liv_text, text='Liv: ' \
                    + str(liv_kvar))

def kontrollera_fångst():
    (fångare_x, fångare_y, fångare_x2, fångare_y2) = c.coords(fångare)
    for ägg in äggen:
        root.update()
        (ägg_x, ägg_y, ägg_x2, ägg_y2) = c.coords(ägg)
        if fångare_x < ägg_x and ägg_x2 < fångare_x2 and fångare_y2 - ägg_y2 < 40:
            äggen.remove(ägg)
            c.delete(ägg)
            öka_summa(äggsumma)
    root.after(100, kontrollera_fångst)

def öka_summa(poäng):
    global summa, ägghastighet, äggintervall
    summa += poäng
    ägghastighet = int(ägghastighet * svårighetsfaktor)
    äggintervall = int(äggintervall * svårighetsfaktor)
    c.itemconfigure(summa_text, text='Poäng: ' + str(summa))

def flytta_vänster(händelse):
    (x1, y1, x2, y2) = c.coords(fångare)
    if x1 > 0:
        c.move(fångare, -25, 0)

def flytta_höger(händelse):
    (x1, y1, x2, y2) = c.coords(fångare)
    if x2 < kanvasbredd:
        c.move(fångare, 25, 0)

c.bind('<Left>', flytta_vänster)
c.bind('<Right>', flytta_höger)
c.focus_set()

root.after(1000, skapa_ägg)
root.after(1000, flytta_äggen)
root.after(1000, kontrollera_fångst)
root.mainloop()
