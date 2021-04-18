from tkinter import Tk, simpledialog, messagebox

def läs_från_fil():
    with open('huvudstad.txt', encoding="UTF-8") as fil:
        for rad in fil:
            rad = rad.rstrip('\n')
            land, stad = rad.split('/')
            världen[land] = stad

def skriv_till_fil(namn_på_land, namn_på_stad):
    with open('huvudstad.txt', 'a', encoding="UTF-8") as fil:
        fil.write(namn_på_land + '/' + namn_på_stad + '\n')

print('Fråga experten - Huvudstäder i världen')
root = Tk()
root.withdraw()
världen = {}

läs_från_fil()

while True:
    try:
        fråga_land = simpledialog.askstring('Land', 'Skriv namnet på ett land:')
        fråga_land = fråga_land.capitalize()
    except:
        print('goodbye')
        exit()

    if fråga_land in världen:
        resultat = världen[fråga_land]
        messagebox.showinfo('Svar',
                            'Huvudstaden i ' + fråga_land + ' är ' + resultat + '!')
    else:
        try:
            ny_stad = simpledialog.askstring('Lär mig',
                                              'Jag vet inte! ' +
                                              'Vad är huvdstaden i ' + fråga_land + '?')
            världen[fråga_land] = ny_stad
            skriv_till_fil(fråga_land, ny_stad)
        except:
            print('goodbye')
            exit()
           
root.mainloop()
