import pygame, time
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

    surface.displayMenu()

    while True:

        playing = True
        board.resetBoard()
        game.waitForInput()

        while playing:

            for symbol in players:
                game.clickPos = (-1, -1)
                board.displayBoard()
                board.updateBoard()

                while not game.isClicked():
                    game.getEvent()
                    board.displayBoard()
                    board.updateBoard()
                    board.highlightTile(board.checkMousePosition(game.mousePos))
                    game.clicked = board.checkClick(game.clickPos, symbol)

                game.clicked = False  # to prevent the game from freezing
                board.updateBoard()

                if game.checkWinner(board.board, symbol):
                    playing = False
                    surface.displayWinner(symbol)
                    break
                elif game.checkTie(board.board):
                    playing = False
                    surface.displayTie()
                    break

                CLOCK.tick(surface.FPS)

            if not playing:
                break

if __name__ == "__main__":
    run()

