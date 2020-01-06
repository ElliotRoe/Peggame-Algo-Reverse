from BoardState import BoardState as BS, BoardState
from graphics import *
from Peg import Peg
import time
import numpy as np
from Node import Node



class GM:

    file = open('solutions.txt', 'w')

    def __init__(self, win, board):
        self.backgroundColor = color_rgb(207, 155, 242)
        self.win = win
        self.win.setBackground(self.backgroundColor)
        self.board = board
        self.pegs = [Peg(win.getWidth() / 2, 50, False),  # Top Row
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
        self.setBoardState(self.board)
        self.currentNode = Node(self.board)
        self.parentNode = self.currentNode.copy()
        self.originalNode = self.currentNode.copy()

    def jumpBack(self, jumpCoors):
        startCoor = jumpCoors[0]
        endCoor = jumpCoors[2]
        # Start coor is peg before jump back
        startIndex = BS.coorToIndex(startCoor)
        endIndex = BS.coorToIndex(endCoor)
        middleCoor = jumpCoors[1]
        middleIndex = BS.coorToIndex(middleCoor)

        self.parentNode = self.currentNode

        self.board.setPeg(startIndex, False)
        self.board.setPeg(endIndex, True)
        self.board.setPeg(middleIndex, True)

        # most important part of the whole process sets a new child node of the current one
        self.currentNode = Node(self.board.copy(), self.parentNode, jumpCoors)
        self.parentNode.removeJump(jumpCoors)

        self.setBoardState(self.board)

    def getCurrentNode(self):
        return self.currentNode

    def setCurrentNode(self, node):
        self.currentNode = node
        self.board = self.currentNode.getBoardState()
        self.setBoardState(self.board)
        self.displayBoard()
        if node.getParentNode() is not None:
            self.parentNode = node.getParentNode()

    def getParentNode(self):
        return self.parentNode

    def getOriginalNode(self):
        return self.originalNode

    def setBoardState(self, board):
        self.board = board
        i = 0
        for peg in self.pegs:
            peg.setActive(self.board.getPeg(i))
            i = i+1

    def displayBoard(self):
        for peg in self.pegs:
            peg.undraw()
            peg.draw(self.win)

    @staticmethod
    def printPath(path):
        for coor in path:
            print(coor, file=GM.file)
            print(BS.coorToIndex(coor[0]) + ' ---> ' + BS.coorToIndex(coor[2]), file=GM.file)
            print()


def main():
    win = GraphWin("Peg Board", 500, 500)
    initBoard = BoardState([True, False, False, False, False, False, False, False, False, False, False, False, False, False, False])

    game = GM(win, initBoard)
    game.displayBoard()

    i = 1
    stepCount = 0

    while not game.getOriginalNode().getNodeState():
        while True:
            #time.sleep(0.01)
            posJumps = game.getCurrentNode().getPossibleJumps()
            if len(posJumps) == 0:
                #if (stepCount >= 13) and (not game.getCurrentNode().getBoardState().getBoard()[0]):
                GM.printPath(game.getCurrentNode().getPath())
                print('Step back ::', i)
                break
            game.jumpBack(posJumps[0])
            stepCount = stepCount + 1

        game.getCurrentNode().setNodeState(True)
        game.setCurrentNode(game.getParentNode())
        stepCount = stepCount - 1
        i = i + 1

    win.getMouse()
    win.close()


main()
