#!/usr/bin/python3
#testing
import pgzrun
from random import randint
import time

WIDTH = 500
HEIGHT = 405
aplle = Actor('apple')
aplle.x = 100
aplle.y = 300
beep = tone.create('A3', 1)
    
def draw():
    screen.blit('astro_fits2', (0, 0))
    screen.draw.text('A apple and then stop', topleft=(10, 300), color=(255, 0, 0))
    aplle.draw()
def over():
    beep.play()

animate(aplle, tween='accel_decel', duration=7, on_finished=over(), pos=(400, 300))

pgzrun.go()
