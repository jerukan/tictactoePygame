import pygame
from pygame.locals import *

from util.color import Color


class Window:

    pygame.init()

    WINDOWWIDTH = 750
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
        self.drawText("click anywhere to start the game", int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2))
        pygame.display.update()

    def displayWinner(self, winner):
        self.displayWindow()
        self.drawText(winner + " won!", int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2))
        self.drawText("click anywhere to play another game", int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2) + 50)
        pygame.display.update()

    def displayTie(self):
        self.displayWindow()
        self.drawText("there was a tie. no one won", int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2))
        self.drawText("click anywhere to play another game", int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2) + 50)
        pygame.display.update()