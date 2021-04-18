import pgzrun
import pygame

WIDTH = 1280
HEIGHT = 720

huvudruta = Rect(0, 0, 820, 240)
timerruta = Rect(0, 0, 240, 240)
svarsruta1 = Rect(0, 0, 495, 165)
svarsruta2 = Rect(0, 0, 495, 165)
svarsruta3 = Rect(0, 0, 495, 165)
svarsruta4 = Rect(0, 0, 495, 165)

huvudruta.move_ip(50, 40)
timerruta.move_ip(990, 40)
svarsruta1.move_ip(50, 358)
svarsruta2.move_ip(735, 358)
svarsruta3.move_ip(50, 538)
svarsruta4.move_ip(735, 538)
svarsrutor = [svarsruta1, svarsruta2, svarsruta3, svarsruta4]

summa = 0
tid_kvar = 20

f1 = ["Vad heter Argentinas huvudstad?",
      "Colombo", "Bangui", "Pretoria", "Buenos Aires", 4]

f2 = ["Vad är 34 * 36?",
      "1224", "973", "924", "1345", 1]

f3 = ["Vilken planet ligger längst bort från solen?",
      "Jupiter", "Pluto", "Mars", "Neptunus", 4]

f4 = ["Vilken veckodag föddes Manzhou?",
      "tisdag", "fredag", "lördag", "torsdag", 2]

f5 = ["Hur många år har Mandi spelat på pokemon go?",
      "1", "3", "4", "5", 2]

fragor = [f1, f2, f3, f4, f5]
fraga = fragor.pop(0)

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(huvudruta, "sky blue")
    screen.draw.filled_rect(timerruta, "sky blue")

    for ruta in svarsrutor:
        screen.draw.filled_rect(ruta, "orange")

    screen.draw.textbox(str(tid_kvar), timerruta, color=("black"))
    screen.draw.textbox(fraga[0], huvudruta, color=("black"))

    index = 1
    for ruta in svarsrutor:
        screen.draw.textbox(fraga[index], ruta, color=("black"))
        index = index + 1

def spelet_slut():
    global fraga, tid_kvar
    meddelande = "Slutspelat. Du fick %s korrekta svar" % str(summa)
    fraga = [meddelande, "-", "-", "-", "-", 5]
    tid_kvar = 0

def ratt_svar():
    global fraga, summa, tid_kvar

    summa = summa + 1
    if fragor:
        fraga = fragor.pop(0)
        tid_kvar = 20
    else:
        print("Slutspelat.")
        spelet_slut()
        
def on_mouse_down(pos):
    index = 1
    for ruta in svarsrutor:
        if ruta.collidepoint(pos):
            print("Du har valt alternativ " + str(index))
            if index == fraga[5]:
                print("Bra jobbat!")
                ratt_svar()
            else:
                spelet_slut()
        index = index + 1

def on_key_up(key):
    global summa

    if key == keys.SPACE:
        summa = summa - 1
        ratt_svar()

def uppdatera_tid_kvar():
    global tid_kvar

    if tid_kvar:
        tid_kvar = tid_kvar - 1
    else:
        spelet_slut()

clock.schedule_interval(uppdatera_tid_kvar, 1.0)

pgzrun.go()

