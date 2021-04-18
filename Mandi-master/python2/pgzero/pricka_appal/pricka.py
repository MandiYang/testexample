import pygame
import pgzrun
from random import randint
apple = Actor("apple")
orange = Actor("orange")
annanas = Actor("pineapple")

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    annanas.draw()

def placera_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Snyggt skott!")
        placera_apple()
    else:
        print("Du missade!")
        exit()
        
placera_apple()
pgzrun.go()

