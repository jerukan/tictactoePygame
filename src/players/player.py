import pygame

class Player:

    SYMBOL = 'X'

    def playTurn(self, board, game):
        game.clickPos = (-1, -1)
        board.displayBoard()
        board.updateBoard()

        while not game.isClicked():
            game.getEvent()
            board.displayBoard()
            board.updateBoard()
            board.highlightTile(board.checkMousePosition(game.mousePos))
            game.clicked = board.checkClick(game.clickPos, self.SYMBOL)
            pygame.display.update()
        game.clicked = False  # to prevent the game from freezing
        board.updateBoard()