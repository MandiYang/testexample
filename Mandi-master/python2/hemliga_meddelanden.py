from tkinter import messagebox, simpledialog, Tk

def är_jämn(tal):
    return tal % 2 == 0

def hämta_jämna_bokstäver(meddelande):
    jämna_bokstäver = []
    for räknare in range(0, len(meddelande)):
        if är_jämn(räknare):
            jämna_bokstäver.append(meddelande[räknare])
    return jämna_bokstäver

def hämta_ojämna_bokstäver(meddelande):
    ojämna_bokstäver = []
    for räknare in range(0, len(meddelande)):
        if not är_jämn(räknare):
            ojämna_bokstäver.append(meddelande[räknare])
    return ojämna_bokstäver

def byt_bokstäver(meddelande):
    bokstavslista = []
    if not är_jämn(len(meddelande)):
        meddelande = meddelande + 'x'
    jämna_bokstäver = hämta_jämna_bokstäver(meddelande)
    ojämna_bokstäver = hämta_ojämna_bokstäver(meddelande)
    for räknare in range(0, int(len(meddelande)/2)):
        bokstavslista.append(ojämna_bokstäver[räknare])
        bokstavslista.append(jämna_bokstäver[räknare])
    nytt_meddelande = ''.join(bokstavslista)
    return nytt_meddelande

def kryptera(meddelande):
    omkastat_meddelande = byt_bokstäver(meddelande)
    krypterat_meddelande = ''.join(reversed(omkastat_meddelande))
    return krypterat_meddelande

def dekryptera(meddelande):
    ej_omkastat_meddelande = ''.join(reversed(meddelande))
    dekrypterat_meddelande = byt_bokstäver(ej_omkastat_meddelande)
    return dekrypterat_meddelande

def hämta_uppgift():
    uppgift = simpledialog.askstring('Uppgift', 'Vill du kryptera eller dekryptera?')
    return uppgift

def hämta_meddelande():
    meddelande = simpledialog.askstring('Meddelande', 'Skriv det det hemliga meddelandet: ')
    return meddelande

root = Tk()
root.withdraw()
while True:
    uppgift = hämta_uppgift()
    if uppgift == 'kryptera':
        meddelande = hämta_meddelande()
        krypterad = kryptera(meddelande)
        messagebox.showinfo('Chiffertexten i det hemliga meddelandet är:', krypterad)
    elif uppgift == 'dekryptera':
        meddelande = hämta_meddelande()
        dekrypterad = dekryptera(meddelande)
        messagebox.showinfo('Klartext för det hemliga meddelandet är:', dekrypterad)
    else:
        root.destroy()
        break

root.mainloop()


    
    
