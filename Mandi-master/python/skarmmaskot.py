from tkinter import HIDDEN, NORMAL, Tk, Canvas

print('HELLO')

def växla_ögon():
    aktuell_färg = c.itemcget(öga_vänster, 'fill')
    ny_färg = c.kroppsfärg if aktuell_färg == 'white' else 'white'
    aktuell_state = c.itemcget(pupill_vänster, 'state')
    ny_state = NORMAL if aktuell_state == HIDDEN else HIDDEN
    c.itemconfigure(pupill_vänster, state=ny_state)
    c.itemconfigure(pupill_höger, state=ny_state)
    c.itemconfigure(öga_vänster, fill=ny_färg)
    c.itemconfigure(öga_höger, fill=ny_färg)

def blinka():
    växla_ögon()
    root.after(250, växla_ögon)
    root.after(3000, blinka)

def växla_pupiller():
    if not c.ögon_skelar:
        c.move(pupill_vänster, 10, -5)
        c.move(pupill_höger, -10, -5)
        c.ögon_skelar = True
    else:
        c.move(pupill_vänster, -10, 5)
        c.move(pupill_höger, 10, 5)
        c.ögon_skelar = False

def växla_tunga():
    if not c.tunga_ute:
        c.itemconfigure(tungspets, state=NORMAL)
        c.itemconfigure(tungrot, state=NORMAL)
        c.tunga_ute = True
    else:
        c.itemconfigure(tungspets, state=HIDDEN)
        c.itemconfigure(tungrot, state=HIDDEN)
        c.tunga_ute = False

def busig(händelse):
    växla_tunga()
    växla_pupiller()
    dölj_glad(händelse)
    root.after(1000, växla_tunga)
    root.after(1000, växla_pupiller)
    return

def visa_glad(händelse):
    if (20 <= händelse.x <= 350) and (20 <= händelse.y <= 350):
        c.itemconfigure(kind_vänster, state=NORMAL)
        c.itemconfigure(kind_höger, state=NORMAL)
        c.itemconfigure(mun_glad, state=NORMAL)
        c.itemconfigure(mun_normal, state=HIDDEN)
        c.itemconfigure(mun_ledsen, state=HIDDEN)
        c.lyckonivå = 10
    return

def dölj_glad(händelse):
    c.itemconfigure(kind_vänster, state=HIDDEN)
    c.itemconfigure(kind_höger, state=HIDDEN)
    c.itemconfigure(mun_glad, state=HIDDEN)
    c.itemconfigure(mun_normal, state=NORMAL)
    c.itemconfigure(mun_ledsen, state=HIDDEN)
    return

def ledsen():
    if c.lyckonivå == 0:
        c.itemconfigure(mun_glad, state=HIDDEN)
        c.itemconfigure(mun_normal, state=HIDDEN)
        c.itemconfigure(mun_ledsen, state=NORMAL)
    else:
        c.lyckonivå -= 1
    root.after(5000, ledsen)
        
root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)
c.kroppsfärg = 'SkyBlue1'
kropp = c.create_oval(35, 20, 365, 350, outline=c.kroppsfärg, fill=c.kroppsfärg)
öra_vänster = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.kroppsfärg, fill=c.kroppsfärg)
öra_höger = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.kroppsfärg, fill=c.kroppsfärg)

fot_vänster = c.create_oval(65, 320, 145, 360, outline=c.kroppsfärg, fill=c.kroppsfärg)
fot_höger= c.create_oval(250, 320, 330, 360, outline=c.kroppsfärg, fill=c.kroppsfärg)

öga_vänster = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupill_vänster = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
öga_höger = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupill_höger = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

mun_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mun_glad = c.create_line(170, 250, 200, 282, 230, 250,  smooth=1, width=2, state=HIDDEN)
mun_ledsen = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tungrot = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tungspets = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

kind_vänster = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
kind_höger = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

c.pack()

c.bind('<Motion>', visa_glad)
c.bind('<Leave>', dölj_glad)
c.bind('<Double-1>', busig)

c.lyckonivå = 14
c.ögon_skelar = False
c.tunga_ute = False

root.after(1000, blinka)
root.after(7000, ledsen)
root.mainloop()
