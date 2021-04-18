from tkinter import Tk, Canvas
from datetime import date, datetime
def hämta_händelser():
    lista_händelser = []
    with open('handelser.txt', encoding="utf-8") as fil:
        for rad in fil:
            rad = rad.rstrip('\n')
            aktuell_händelse = rad.split(',')
            händelsedatum = datetime.strptime(aktuell_händelse[1], '%d/%m/%y').date()
            aktuell_händelse[1] = händelsedatum
            lista_händelser.append(aktuell_händelse)
    return lista_händelser

def dagar_mellan_datum(date1, date2):
    tid_mellan = str(date1 - date2)
    antal_dagar = tid_mellan.split(' ')
    return antal_dagar[0]

root = Tk()
c = Canvas(root, width=800, height=800, bg="black")
c.pack()
c.create_text(100, 50, anchor='w', fill='orange', \
font='Arial 28 bold underline', text='Min nedräkningskalender')

händelser = hämta_händelser()
idag = date.today()

vertikalt_utrymme = 100
händelser.sort(key=lambda x: x[1])
for händelse in händelser:
    händelsenamn = händelse[0]
    dagar_till = dagar_mellan_datum(händelse[1], idag)
    display = 'Det är %s dagar till %s' % (dagar_till, händelsenamn)
    if (int(dagar_till) <= 4):
        textfärg = 'red'
    else:
        textfärg = 'lightblue'
    c.create_text(100, vertikalt_utrymme, anchor='w', fill=textfärg, \
                  font='Arial 28 bold', text=display)

    vertikalt_utrymme = vertikalt_utrymme + 30
root.mainloop()
