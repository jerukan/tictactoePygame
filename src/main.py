import pygame
from window import Window
from board import Board
from game import Game

surface = Window()
board = Board()
game = Game()

pygame.init()

CLOCK = pygame.time.Clock()

players = ["X", "O"]


def run():

    while True:

        playing = True
        board.resetBoard()
        game.waitForInput()
        game.mousePos = (-1, -1)

        while playing:

            for symbol in players:
                surface.displayWindow()
                board.displayBoard()
                board.updateBoard()

                while not game.isClicked():
                    game.getEvent()
                    game.clicked = board.checkClick(game.mousePos, symbol)

                game.clicked = False  # to prevent the game from freezing
                board.updateBoard()

                if game.checkWinner(board.board, symbol):
                    playing = False
                    break
                CLOCK.tick(surface.FPS)

            if not playing:
                break

if __name__ == "__main__":
    run()

