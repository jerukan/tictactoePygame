import pygame, sys
from pygame.locals import *

class Game:

    mousePos = (0, 0)
    clicked = False

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                self.clicked = True
            if event.type == MOUSEBUTTONUP:
                self.clicked = False

    def isClicked(self):
        return self.clicked

    def waitForInput(self):
        while not self.clicked:
            self.getEvent()
            if self.clicked:
                self.clicked = False
                return

    def checkWinner(self, board, playerSymbol):
        return ((board[0][0] == playerSymbol and board[0][1] == playerSymbol and board[0][2] == playerSymbol) or  # across the top
                (board[1][0] == playerSymbol and board[1][1] == playerSymbol and board[1][2] == playerSymbol) or  # across the midde
                (board[2][0] == playerSymbol and board[2][1] == playerSymbol and board[2][2] == playerSymbol) or  # across the bottom
                (board[0][0] == playerSymbol and board[1][0] == playerSymbol and board[2][0] == playerSymbol) or  # down the left side
                (board[0][1] == playerSymbol and board[1][1] == playerSymbol and board[2][1] == playerSymbol) or  # down the midde
                (board[0][2] == playerSymbol and board[1][2] == playerSymbol and board[2][2] == playerSymbol) or  # down the right side
                (board[0][0] == playerSymbol and board[1][1] == playerSymbol and board[2][2] == playerSymbol) or  # diagonal
                (board[0][2] == playerSymbol and board[1][1] == playerSymbol and board[2][0] == playerSymbol))  # diagonal