import pgzrun
import math
import random

BREDD = 800
HOJD = 600
MITT_X = BREDD / 2
MITT_Y = HOJD / 2
MITT = (MITT_X, MITT_Y)
TECKENFARG = (0, 0, 0)
AGGSUMMA = 25
RIDDARE_START = (200, 300)
ATTACK_DISTANS = 260
DRAKE_VAKENTID = 2
AGG_DOLD_TID = 2
FLYTTA_DISTANS = 6

liv = 3
samlade_agg = 0
spelet_slut = False
spelet_klart = False
omstart_behovs = False

enkelt_bo = {
    "drake": Actor("dragon-asleep", pos=(620, 100)),
    "agg": Actor("one-egg", pos=(400, 100)),
    "antal_agg": 1,
    "agg_dolt": False,
    "agg_dolt_raknare": 0,
    "sovtid": 8,
    "sovklocka": 0,
    "vakenklocka": 0
}

medel_bo = {
    "drake": Actor("dragon-asleep", pos=(620, 300)),
    "agg": Actor("two-eggs", pos=(400, 300)),
    "antal_agg": 2,
    "agg_dolt": False,
    "agg_dolt_raknare": 0,
    "sovtid": 6,
    "sovklocka": 0,
    "vakenklocka": 0
}

svart_bo = {
    "drake": Actor("dragon-asleep", pos=(620, 500)),
    "agg": Actor("three-eggs", pos=(400, 500)),
    "antal_agg": 3,
    "agg_dolt": False,
    "agg_dolt_raknare": 0,
    "sovtid": 4,
    "sovklocka": 0,
    "vakenklocka": 0
}

bon = [enkelt_bo, medel_bo, svart_bo]
riddare = Actor("hero", pos=RIDDARE_START)

def draw():
    global bon, samlade_agg, liv, spelet_klart
    screen.clear()
    screen.blit("dungeon", (0, 0))
    if spelet_slut:
        screen.draw.text("SLUTSPELAT!", fontsize=60, center=MITT, color=TECKENFARG)
    elif spelet_klart:
        screen.draw.text("DU VANN!", fontsize=60, center=MITT, color=TECKENFARG)
    else:
        riddare.draw()
        rita_bon(bon)
        rita_raknare(samlade_agg, liv)

def rita_bon(bon_att_rita):
    for bo in bon_att_rita:
        bo["drake"].draw()
        if bo["agg_dolt"] is False:
            bo["agg"].draw()

def rita_raknare(samlade_agg, liv):
    screen.blit("egg-count", (0, HOJD - 30))
    screen.draw.text(str(samlade_agg),
                     fontsize=40,
                     pos=(30, HOJD - 30),
                     color=TECKENFARG)
    screen.blit("life-count", (60, HOJD - 30))
    screen.draw.text(str(liv),
                     fontsize=40,
                     pos=(90, HOJD - 30),
                     color=TECKENFARG)

def update():
    if keyboard.right:
        riddare.x += FLYTTA_DISTANS
        if riddare.x > BREDD:
            riddare.x = BREDD
    elif keyboard.left:
        riddare.x -= FLYTTA_DISTANS
        if riddare.x < 0:
            riddare.x = 0
    elif keyboard.down:
        riddare.y += FLYTTA_DISTANS
        if riddare.y > HOJD:
            riddare.y = HOJD
    elif keyboard.up:
        riddare.y -= FLYTTA_DISTANS
        if riddare.y < 0:
            riddare.y = 0
    kolla_krock()

def uppdatera_bon():
    global bon, riddare, liv
    for bo in bon:
        if bo["drake"].image == "dragon-asleep":
            uppdatera_sovande_drake(bo)
        elif bo["drake"].image == "dragon-awake":
            uppdatera_vaken_drake(bo)
        uppdatera_agg(bo)

clock.schedule_interval(uppdatera_bon, 1)

def uppdatera_sovande_drake(bo):
    if bo["sovklocka"] >= bo["sovtid"]:
        if random.choice([True, False]):
            bo["drake"].image = "dragon-awake"
            bo["sovklocka"] = 0
    else:
        bo["sovklocka"] += 1

def uppdatera_vaken_drake(bo):
    if bo["vakenklocka"] >= DRAKE_VAKENTID:
        bo["drake"].image = "dragon-asleep"
        bo["vakenklocka"] = 0
    else:
        bo["vakenklocka"] += 1

def uppdatera_agg(bo):
    if bo["agg_dolt"] is True:
        if bo["agg_dolt_raknare"] >= AGG_DOLD_TID:
            bo["agg_dolt"] = False
            bo["agg_dolt_raknare"] = 0
        else:
            bo["agg_dolt_raknare"] += 1

def kolla_krock():
    global bon, samlade_agg, liv, omstart_behovs, spelet_klart
    for bo in bon:
        if bo["agg_dolt"] is False:
            kolla_aggkrock(bo)
        if bo["drake"].image == "dragon-awake" and omstart_behovs is False:
            kolla_drakkrock(bo)

def kolla_drakkrock(bo):
    x_distans = riddare.x - bo["drake"].x
    y_distans = riddare.y - bo["drake"].y
    distans = math.hypot(x_distans, y_distans)
    if distans < ATTACK_DISTANS:
        hantera_drakkrock()

def hantera_drakkrock():
    global omstart_behovs
    omstart_behovs = True
    animate(riddare, pos=RIDDARE_START, on_finished=ta_bort_liv)

def kolla_aggkrock(bo):
    global samlade_agg, spelet_klart
    if riddare.colliderect(bo["agg"]):
        bo["agg_dolt"] = True
        samlade_agg += bo["antal_agg"]
        if samlade_agg >= AGGSUMMA:
            spelet_klart = True

def ta_bort_liv():
    global liv, omstart_behovs, spelet_slut
    liv -= 1
    if liv == 0:
        spelet_slut = True
    omstart_behovs = False
    
pgzrun.go()
    
    
