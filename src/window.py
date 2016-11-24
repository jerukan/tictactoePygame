import pygame
from pygame.locals import *
from color import Color

class Window:

    pygame.init()

    WINDOWWIDTH = 650
    WINDOWHEIGHT = 600

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Tic tac toe')

    font = pygame.font.SysFont(None, 48)

    FPS = 60

    def displayWindow(self):
        self.DISPLAYSURF.fill(Color.WHITE)

    def drawText(self, text, x, y):
        textObj = self.font.render(text, True, Color.BLACK)
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        self.DISPLAYSURF.blit(textObj, textRect)


    def displayMenu(self):
        self.displayWindow()
        self.drawText("click anywhere to start the game", 325, 275)
        pygame.display.update()

    def displayWinner(self, winner):
        self.displayWindow()
        self.drawText(winner + " won!", 325, 200)
        self.drawText("click anywhere to play another game", 325, 300)
        pygame.display.update()