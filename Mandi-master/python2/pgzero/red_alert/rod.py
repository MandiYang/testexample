import pgzrun
import random

TECKENFARG = (255, 255, 255)
BREDD = 800
HOJD = 600
MITT_X = BREDD / 2
MITT_Y = HOJD / 2
MITT = (MITT_X, MITT_Y)
SISTA_NIVA = 6
STARTHASTIGHET = 10
FARGER = ["green", "blue"]

spelet_slut = False
spelet_klart = False
aktuell_niva = 1
stjarnor = []
animationer = []

def draw():
    global stjarnor, aktuell_niva, spelet_slut, spelet_klart
    screen.clear()
    screen.blit("space", (0, 0))
    if spelet_slut:
        visa_meddelande("SLUTSPELAT!", "Testa igen.")
    elif spelet_klart:
        visa_meddelande("DU VANN!", "Bra gjort.")
    else:
        for stjarna in stjarnor:
            stjarna.draw()

def update():
    global stjarnor
    if len(stjarnor) == 0:
        stjarnor = rita_stjarnor(aktuell_niva)

def rita_stjarnor(antal_extra_stjarnor):
    farger_att_skapa = hamta_farger_att_skapa(antal_extra_stjarnor)
    nya_stjarnor = skapa_stjarnor(farger_att_skapa)
    layouta_stjarnor(nya_stjarnor)
    animera_stjarnor(nya_stjarnor)
    return nya_stjarnor

def hamta_farger_att_skapa(antal_extra_stjarnor):
    farger_att_skapa = ["red"]
    for i in range(0, antal_extra_stjarnor):
        slump_farg = random.choice(FARGER)
        farger_att_skapa.append(slump_farg)
    return farger_att_skapa

def skapa_stjarnor(farger_att_skapa):
    nya_stjarnor = []
    for farg in farger_att_skapa:
        stjarna = Actor(farg + "-star")
        nya_stjarnor.append(stjarna)
    return nya_stjarnor

def layouta_stjarnor(stjarnor_att_layouta):
    antal_luckor = len(stjarnor_att_layouta) + 1
    luckstorlek = BREDD / antal_luckor
    random.shuffle(stjarnor_att_layouta)
    for index, stjarna in enumerate(stjarnor_att_layouta):
        nya_x_pos = (index + 1) * luckstorlek
        stjarna.x = nya_x_pos

def animera_stjarnor(stjarnor_att_animera):
    for stjarna in stjarnor_att_animera:
        duration = STARTHASTIGHET - aktuell_niva
        stjarna.anchor = ("center", "bottom")
        animation = animate(stjarna, duration=duration, on_finished=hantera_spelslut, y=HOJD)
        animationer.append(animation)

def hantera_spelslut():
    global spelet_slut
    spelet_slut = True

def on_mouse_down(pos):
    global stjarnor, aktuell_niva
    for stjarna in stjarnor:
        if stjarna.collidepoint(pos):
            if "red" in stjarna.image:
                klicka_rod_stjarna()
            else:
                hantera_spelslut()

def klicka_rod_stjarna():
    global aktuell_niva, stjarnor, animationer, spelet_klart
    stoppa_animationer(animationer)
    if aktuell_niva == SISTA_NIVA:
        spelet_klart = True
    else:
        aktuell_niva = aktuell_niva + 1
        stjarnor = []
        animationer = []

def shuffle():
    global stjarnor
    if stjarnor:
        x_varden = [stjarna.x for stjarna in stjarnor]
        random.shuffle(x_varden)
        for index, stjarna in enumerate(stjarnor):
            nya_x = x_varden[index]
            animation = animate(stjarna, duration=0.5, x=nya_x)
            animationer.append(animation)

clock.schedule_interval(shuffle, 0.7)

def stoppa_animationer(animationer_att_stoppa):
    for animation in animationer_att_stoppa:
        if animation.running:
            animation.stop()

def visa_meddelande(rubrik, underrubrik):
    screen.draw.text(rubrik, fontsize=60, center=MITT, color=TECKENFARG)
    screen.draw.text(underrubrik,
                     fontsize=30,
                     center=(MITT_X, MITT_Y + 30),
                     color=TECKENFARG)
pgzrun.go()
