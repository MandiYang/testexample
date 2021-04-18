import pygame
import os
from pygame.locals import *


pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

player = pygame.image.load(os.path.join(image_path, 'dude.png'))

while 1:

    screen.fill(0)

    screen.blit(player, (100,100))

    pygame.display.flip()

    for event in pygame.event.get():


        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
