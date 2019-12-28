from BoardState import BoardState as BS, BoardState
from graphics import *
from Peg import Peg
import time
import numpy as np


class GM:

    jumps = [[4,0],[-4,0],[2,2],[-2,2],[-2,-2],[2,-2]]

    def __init__(self, win):
        self.backgroundColor = color_rgb(207, 155, 242)
        self.win = win
        self.win.setBackground(self.backgroundColor)
        pegs = [Peg(win.getWidth() / 2, 50, False),  # Top Row
                Peg(win.getWidth() / 2 - 50, 50 + (400 / 4), False),
                Peg(win.getWidth() / 2 + 50, 50 + (400 / 4), False),
                Peg(win.getWidth() / 2 - (400 / 4), 50 + (400 / 4) * 2, False),
                Peg(win.getWidth() / 2, 50 + (400 / 4) * 2, False),
                Peg(win.getWidth() / 2 + (400 / 4), 50 + (400 / 4) * 2, False),
                Peg(win.getWidth() / 2 - 150, 50 + (400 / 4) * 3, False),
                Peg(win.getWidth() / 2 - 50, 50 + (400 / 4) * 3, False),
                Peg(win.getWidth() / 2 + 50, 50 + (400 / 4) * 3, False),
                Peg(win.getWidth() / 2 + 150, 50 + (400 / 4) * 3, False),
                Peg(50, 450, False), Peg(50 + (400 / 4), 450, False), Peg(50 + (400 / 4) * 2, 450, False),
                Peg(50 + (400 / 4) * 3, 450, False), Peg(50 + (400 / 4) * 4, 450, False)]  # Bottom Row

    def jumpBack(self, startCoor, endCoor):
        #Start coor is peg before jump back
        startIndex = BS.coorToIndex(startCoor)
        endIndex = BS.coorToIndex(endCoor)
        middleCoor = [(startCoor[0]+endCoor[0])/2,(startCoor[1]+endCoor[1])/2]
        middleIndex = BS.coorToIndex(middleCoor)

        self.board.setPeg(startIndex, False)
        self.board.setPeg(endIndex, True)
        self.board.setPeg(middleIndex, True)

        self.setBoardState(self.board)

    def findJumps(self):
        for i in self.board.getBoard().length:
            if self.board.getBoard()[i]:
                np.array(BS.indexToCoor(i))


    def setBoardState(self, board):
        self.board = board
        i = 0
        for peg in self.pegs:
            peg.setActive(self.board.getPeg(i))
            print(self.board.getPeg(i))
            i = i+1

    def displayBoard(self):
        for peg in self.pegs:
            peg.undraw()
            peg.draw(self.win)


def main():
    win = GraphWin("Peg Board", 500, 500)
    initBoard = BoardState([True, False, False, False, False, False, False, False, False, False, False, False, False, False, False])

    game = GM(win)
    game.displayBoard()
    game.setBoardState(initBoard)

    time.sleep(1)
    game.jumpBack([4,4],[2,2])

    win.getMouse()
    win.close()


main()
