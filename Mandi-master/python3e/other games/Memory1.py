from __future__ import unicode_literals
import random
import time
from tkinter import Tk, Button, DISABLED, messagebox
from emoji import emojize 
#terminal3!!
from tkinter import Tk, messagebox
#s = ''.join([c for c in s if ord(c)<65535])
#print(s)
print('\u23F9')

def visa_symbol(x, y):
    global först
    global föregåendeX, föregåendeY
    global drag, par
    knappar[x, y]['text'] = knappsymboler[x, y]
    knappar[x, y].update_idletasks()

    if först:
        föregåendeX = x
        föregåendeY = y
        först = False
        drag = drag + 1
    elif föregåendeX != x or föregåendeY != y:
        if knappar[föregåendeX, föregåendeY]['text'] != knappar[x, y]['text']:
            time.sleep(0.5)
            knappar[föregåendeX, föregåendeY]['text'] = ''
            knappar[x, y]['text'] = ''
        else:
            knappar[föregåendeX, föregåendeY]['command'] = DISABLED
            knappar[x, y]['command'] = DISABLED
            par = par + 1
            if par == len(knappar)/2:
                messagebox.showinfo('Matchning', 'Antal drag: ' +
                                    str(drag), command=root.destroy())
        först = True

root = Tk()
root.tk.call('encoding', 'system', 'UTF-8')
root.title('Memory') 
root.resizable(width=False, height=False)
knappar = {}
först = True
föregåendeX = 0
föregåendeY = 0
drag = 0
par = 0
knappsymboler = {}
symboler = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
           u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
           u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728',
           u'\u2733', u'\u2733', u'\u2734', u'\u2734', emojize(":thumbs_down:"),
            emojize(":thumbs_down:")]
random.shuffle(symboler)

for x in range(6):
    for y in range(5):
        knapp = Button(command=lambda x=x, y=y: visa_symbol(x, y), width=3, height=3)
        knapp.grid(column=x, row=y)
        knappar[x, y] = knapp
        knappsymboler[x, y] = symboler.pop()

root.mainloop()

