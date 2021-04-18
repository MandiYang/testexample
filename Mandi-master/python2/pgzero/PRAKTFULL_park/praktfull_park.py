import pgzrun
from random import randint
import time

BREDD = 800
HOJD = 600
MITT_X = BREDD / 2
MITT_Y = HOJD / 2

spelet_slut = False
klart = False
parken_praktfull = True
huggblomma_krock = False

tid_som_gatt = 0
starttid = time.time()

ko = Actor("cow")
ko.pos = 100, 500

blomlista = []
vissnad_lista = []
huggblommelista = []

huggblomma_fy_lista = []
huggblomma_fx_lista = []

def draw():
    global spelet_slut, tid_som_gatt, klart
    if not spelet_slut:
        screen.clear()
        screen.blit("garden", (0, 0))
        ko.draw()
        for blomma in blomlista:
            blomma.draw()
        for huggblomma in huggblommelista:
            huggblomma.draw()
        tid_som_gatt = int(time.time() - starttid)
        screen.draw.text(
            "Parken praktfull i: " +
            str(tid_som_gatt) + " sekunder",
            topleft =(10, 10), color="black"
        )
    else:
        if not klart:
            ko.draw()
            screen.draw.text(
                "Parken praktfull i: " +
                str(tid_som_gatt) + " sekunder",
                topleft=(10, 10), color="black"
            )
            if (not parken_praktfull):
                screen.draw.text(
                    "PARKEN HAR VISSNAT - SLUTSPELAT!", color="black",
                    topleft = (10, 50)
                )
                klart = True
            else:
                screen.draw.text(
                    "HUGGBLOMMEATTACK - SLUTSPELAT!", color="black",
                    topleft = (10, 50)
                )
                klart = True
    return
                    

def ny_blomma():
    global blomlista, vissnad_lista
    blomma_ny = Actor("flower")
    blomma_ny.pos = randint(50, BREDD - 50), randint(150, HOJD - 100)
    blomlista.append(blomma_ny)
    vissnad_lista.append("praktfull")
    return

def lagg_till_blommor():
    global spelet_slut
    if not spelet_slut:
        ny_blomma()
        clock.schedule(lagg_till_blommor, 4)
    return

def kolla_antal_vissna():
    global vissnad_lista, spelet_slut, parken_praktfull
    if vissnad_lista:
        for vissnad_sedan in vissnad_lista:
            if (not vissnad_sedan == "praktfull"):
                tid_vissnad = int(time.time() - vissnad_sedan)
                if (tid_vissnad) > 15.0:
                    parken_praktfull = False
                    spelet_slut = True
                    break
    return

def vissna_blomma():
    global blomlista, vissnad_lista, spelet_slut
    if not spelet_slut:
        if blomlista:
            slump_blomma = randint(0, len(blomlista) - 1)
            if (blomlista[slump_blomma].image == "flower"):
                blomlista[slump_blomma].image = "flower-wilt"
                vissnad_lista[slump_blomma] = time.time()
            clock.schedule(vissna_blomma, 4)
    return

def kolla_blomkrock():
    global ko, blomlista, vissnad_lista
    index = 0
    for blomma in blomlista:
        if (blomma.colliderect(ko) and
                blomma.image == "flower-wilt"):
            blomma.image = "flower"
            vissnad_lista[index] = "praktfull"
            break
        index = index + 1
    return


def fart():
    slump_riktning = randint(0, 1)
    slump_fart = randint(2, 3)
    if slump_riktning == 0:
        return -slump_fart
    else:
        return slump_fart

def mutera():
    global blomlista, huggblommelista, huggblomma_fy_lista
    global huggblomma_fx_lista, spelet_slut
    if not spelet_slut and blomlista:
        slump_blomma = randint(0, len(blomlista) - 1)
        huggblomma_pos_x = blomlista[slump_blomma].x
        huggblomma_pos_y = blomlista[slump_blomma].y
        del blomlista[slump_blomma]
        huggblomma = Actor("fangflower")
        huggblomma.pos = huggblomma_pos_x, huggblomma_pos_y
        huggblomma_fx = fart()
        huggblomma_fy = fart()
        huggblomma = huggblommelista.append(huggblomma)
        huggblomma_fx_lista.append(huggblomma_fx)
        huggblomma_fy_lista.append(huggblomma_fy)
        clock.schedule(mutera, 20)
    return
 
        
def uppdatera_huggblommor():
    global huggblommelista, spelet_slut
    if not spelet_slut:
        index = 0
        for huggblomma in huggblommelista:
            huggblomma_fx = huggblomma_fx_lista[index]
            huggblomma_fy = huggblomma_fy_lista[index]
            huggblomma.x = huggblomma.x + huggblomma_fx
            huggblomma.y = huggblomma.y + huggblomma_fy
            if huggblomma.left < 0:
                huggblomma_fx_lista[index] = -huggblomma_fx
            if huggblomma.right > BREDD:
                huggblomma_fx_lista[index] = -huggblomma_fx
            if huggblomma.top < 150:
                huggblomma_fy_lista[index] = -huggblomma_fy
            if huggblomma.bottom > HOJD:
                huggblomma_fy_lista[index] = -huggblomma_fy
            index = index + 1
    return

def kolla_huggblomma_krock():
    global ko, huggblommelista, huggblomma_krock
    global spelet_slut
    for huggblomma in huggblommelista:
        if huggblomma.colliderect(ko):
            ko.image = "zap"
            spelet_slut = True
            break
    return

def ko_tillbaka():
    global spelet_slut
    if not spelet_slut:
        ko.image = "cow"
    return

lagg_till_blommor()
vissna_blomma()

def update():
    global summa, spelet_slut, huggblomma_krock
    global blomlista, huggblommelista, tid_som_gatt
    huggblomma_krock = kolla_huggblomma_krock()
    kolla_antal_vissna()
    if not spelet_slut:
        if keyboard.space:
            ko.image = "cow-water"
            clock.schedule(ko_tillbaka, 0.5)
            kolla_blomkrock()
        if keyboard.left and ko.x > 0:
            ko.x -= 5
        elif keyboard.right and ko.x < BREDD:
            ko.x += 5
        elif keyboard.up and ko.y > 150:
            ko.y -= 5
        elif keyboard.down and ko.y < HOJD:
            ko.y += 5
        if tid_som_gatt > 15 and not huggblommelista:
            mutera()
        uppdatera_huggblommor()

pgzrun.go()
