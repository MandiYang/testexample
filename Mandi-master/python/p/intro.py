import pgzrun
import time
WIDTH = 300
HEIGHT = 300

alien = Actor('alien')
alien.topright = 0, 10

score = 0

def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        set_alien_hurt()
        score += 1
    else:
        score -= 3
        print('nothing here')
    print(score)


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    print('eek')
    clock.schedule_unique(set_alien_normal, 0.3)


def set_alien_normal():
    alien.image = 'alien'

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
pgzrun.go()
