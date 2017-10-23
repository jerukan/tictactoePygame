import pygame, time, sys
from pygame.locals import *

from util import *
from players import *

surface = Window()
board = Board()
game = Game()

pygame.init()

CLOCK = pygame.time.Clock()

players = [Player(), Computerai()]


def run():

    surface.displayMenu()

    while True:

        playing = True
        board.resetBoard()
        game.waitForInput()

        while playing:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            for playa in players:

                playa.playTurn(board, game)

                if game.checkWinner(board.board, playa.SYMBOL):
                    playing = False
                    pygame.display.update()
                    time.sleep(1)
                    surface.displayWinner(playa.SYMBOL)
                    break
                elif game.checkTie(board.board):
                    playing = False
                    pygame.display.update()
                    time.sleep(1)
                    surface.displayTie()
                    break

                pygame.display.update()

                CLOCK.tick(surface.FPS)

            if not playing:
                break

if __name__ == "__main__":
    run()

