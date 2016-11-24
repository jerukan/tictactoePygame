import pygame
from color import Color
from window import Window
from game import Game

class Board:

    #will go from top to bottom of window completely
    #left column, right column
    columnX = [(2 * Window.WINDOWWIDTH / 5), (3 * Window.WINDOWWIDTH / 5)]

    #           left limit                      right limit
    rowX = [(Window.WINDOWWIDTH / 5), (4 * Window.WINDOWWIDTH / 5)]
    #top row, bottom row
    rowY = [(Window.WINDOWHEIGHT / 3), (2 * Window.WINDOWHEIGHT / 3)]

    tileWidth = Window.WINDOWWIDTH / 5
    tileHeight = Window.WINDOWHEIGHT / 3

    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

    boardTiles = [[pygame.Rect(rowX[0], 0, tileWidth, tileHeight), pygame.Rect(columnX[0], 0, tileWidth, tileHeight), pygame.Rect(columnX[1], 0, tileWidth, tileHeight)],
                  [pygame.Rect(rowX[0], rowY[0], tileWidth, tileHeight), pygame.Rect(columnX[0], rowY[0], tileWidth, tileHeight), pygame.Rect(columnX[1], rowY[0], tileWidth, tileHeight)],
                  [pygame.Rect(rowX[0], rowY[1], tileWidth, tileHeight), pygame.Rect(columnX[0], rowY[1], tileWidth, tileHeight), pygame.Rect(columnX[1], rowY[1], tileWidth, tileHeight)]]

    def displayBoard(self):

        # left vertical line
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.columnX[0], 0), (self.columnX[0], Window.WINDOWHEIGHT), 5)
        # right vertical line
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.columnX[1], 0), (self.columnX[1], Window.WINDOWHEIGHT), 5)
        # top row
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.rowX[0], self.rowY[0]), (self.rowX[1], self.rowY[0]), 5)
        # bottom row
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.rowX[0], self.rowY[1]), (self.rowX[1], self.rowY[1]), 5)

        pygame.display.update()

    def checkClick(self, mousePos, playpiece):
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[y])):
                if self.boardTiles[y][x].collidepoint(mousePos):
                    if self.isClickable(self.board[y][x]):
                        self.board[y][x] = playpiece
                        Game.clicked = True
                        return Game.clicked
                    else:
                        Game.clicked = False
                        return Game.clicked
                else:
                    Game.clicked = False

    def updateBoard(self):
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[y])):
                tile = self.boardTiles[y][x]
                tilesymb = self.board[y][x]
                if tilesymb == "X":
                    pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, tile.topleft, tile.bottomright, 3)
                    pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, tile.topright, tile.bottomleft, 3)
                if tilesymb == "O":
                    pygame.draw.circle(Window.DISPLAYSURF, Color.BLACK, tile.center, int(tile.width / 2))

        pygame.display.update()

    def resetBoard(self):

        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def isClickable(self, chosenTile):
        if chosenTile == '':
            return True
        else:
            return False
