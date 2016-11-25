import pygame, copy
from util import *
from players.player import Player

class Computerai():

    SYMBOL = 'O'

    def playTurn(self, board, game):

        boardCopy = copy.deepcopy(board.board)

        #first checks if it can win next turn
        for y in range(0, len(boardCopy)):
            for x in range(0, len(boardCopy[y])):
                if board.isClickable(boardCopy[y][x]):
                    boardCopy[y][x] = self.SYMBOL
                    if game.checkWinner(boardCopy, self.SYMBOL):
                        board.board[y][x] = self.SYMBOL
                        board.updateBoard()
                        pygame.display.update()
                        return

        #then checks if the player will win next turn and block it
        for y in range(0, len(boardCopy)):
            for x in range(0, len(boardCopy[y])):
                if board.isClickable(boardCopy[y][x]):
                    boardCopy[y][x] = Player.SYMBOL
                    if game.checkWinner(boardCopy, Player.SYMBOL):
                        board.board[y][x] = self.SYMBOL
                        board.updateBoard()
                        pygame.display.update()
                        return

        #take the corners
        choice = board.randomMoveFromList([[0, 0], [0, 2], [2, 0], [2, 2]])
        if choice is not None:
            board.board[choice[0]][choice[1]] = self.SYMBOL
            board.updateBoard()
            pygame.display.update()
            return

        #take the center
        if board.isClickable(board.board[1][1]):
            board.board[1][1] = self.SYMBOL
            board.updateBoard()
            pygame.display.update()
            return

        #take a side
        choice = board.randomMoveFromList([[0, 1], [1, 2], [2, 1], [1, 0]])
        if choice is not None:
            if choice is not None:
                board.board[choice[0]][choice[1]] = self.SYMBOL
                board.updateBoard()
                pygame.display.update()
                return
