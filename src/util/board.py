import pygame, random

from shapes import *
from util.color import Color
from util.game import Game
from util.window import Window


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

        Window().displayWindow()

        # left vertical line
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.columnX[0], 0), (self.columnX[0], Window.WINDOWHEIGHT), 5)
        # right vertical line
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.columnX[1], 0), (self.columnX[1], Window.WINDOWHEIGHT), 5)
        # top row
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.rowX[0], self.rowY[0]), (self.rowX[1], self.rowY[0]), 5)
        # bottom row
        pygame.draw.line(Window.DISPLAYSURF, Color.BLACK, (self.rowX[0], self.rowY[1]), (self.rowX[1], self.rowY[1]), 5)

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

    def checkMousePosition(self, mousePos):
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[y])):
                if self.boardTiles[y][x].collidepoint(mousePos):
                    if self.isClickable(self.board[y][x]):
                        return self.boardTiles[y][x]
        return None

    def highlightTile(self, tile):
        if tile is None:
            return
        highlightSurface = pygame.Surface((tile.width, tile.height))
        highlightSurface = highlightSurface.convert_alpha()
        highlightSurface.fill(Color.GREEN)
        Window.DISPLAYSURF.blit(highlightSurface, tile.topleft)

    def updateBoard(self):
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[y])):
                tile = self.boardTiles[y][x]
                tilesymb = self.board[y][x]
                if tilesymb == "X":
                    ShapeX().draw(Window.DISPLAYSURF, Color.BLACK, tile.center, tile.width, tile.height)
                if tilesymb == "O":
                    ShapeO().draw(Window.DISPLAYSURF, Color.BLACK, tile.center, tile.width)

    def resetBoard(self):

        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def isClickable(self, chosenTile):
        if chosenTile == '':
            return True
        else:
            return False

    def randomMoveFromList(self, theList):
        possibleMoves = []
        for i in theList:
            if self.isClickable(self.board[i[0]][i[1]]):
                possibleMoves.append(i)

        return random.choice(possibleMoves)