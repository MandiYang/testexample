from tkinter import Tk, simpledialog, messagebox

def läs_från_fil():
    with open('landents_H.txt', encoding="utf-8") as fil:
        for rad in fil:
            rad = rad.rstrip('\n')
            land, stad = rad.split('/')
            världen[stad] = land

def skriv_till_fil(namn_på_land, namn_på_stad):
    with open('landents_H.txt', 'a', encoding="utf-8") as fil:
        fil.write(namn_på_land + '/' + namn_på_stad + '\n') 

print('Fråga experten - Huvudstäder i världen')
root = Tk()
root.withdraw()
världen = {}

läs_från_fil()

while True:
    fråga_stad = simpledialog.askstring('Land', 'Skriv namnet på ett stad:')
    fråga_stad = fråga_stad.capitalize()

    if fråga_stad in världen:
        resultat = världen[fråga_stad]
        messagebox.showinfo('Svar',
                            'Landets som har huvudstaden ' + fråga_stad + ' heter ' + resultat + '!')
    else:
        ny_land = simpledialog.askstring('Lär mig',
                                          'Jag vet inte! ' +
                                          'Vad heter landet som har huvdstaden ' + fråga_stad + '?')
        världen[fråga_stad] = ny_land
        skriv_till_fil(ny_land, fråga_stad)

root.mainloop()
