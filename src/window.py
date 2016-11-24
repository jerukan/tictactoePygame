import pygame
from pygame import *
from color import Color

class Window:

    WINDOWWIDTH = 650
    WINDOWHEIGHT = 600

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Tic tac toe')

    FPS = 60

    def displayWindow(self):
        self.DISPLAYSURF.fill(Color.WHITE)