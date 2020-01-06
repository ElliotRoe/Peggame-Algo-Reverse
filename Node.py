import numpy as np
from BoardState import BoardState as BS


class Node:
    jumps = [np.array([4, 0]), np.array([-4, 0]), np.array([2, 2]), np.array([-2, 2]), np.array([-2, -2]),
             np.array([2, -2])]

    def __init__(self, boardState, node=None, jump=None, childrenNodes=[]):
        self.parentNode = node
        if node is not None:
            self.parentNode.addChildNode(self)
        self.boardState = boardState
        self.childrenNodes = childrenNodes
        # if state is true then node has been completely fulfilled
        self.state = False
        self.possibleJumps = Node.findJumps(boardState)
        # this holds the jump that was used to get to this boardstate
        # it's only purpose is to help with path construction when a solution is found
        self.jump = jump
        # print(self.possibleJumps[0])

    def copy(self):
        return Node(self.boardState.copy(), self.parentNode, self.childrenNodes)

    @staticmethod
    def findJumps(board):
        jumps = np.array([[[0, 0], [0, 0], [0, 0]]])
        for i in range(0, len(board.getBoard()) - 1):
            # if peg is filled then find a jump
            if board.getBoard()[i]:
                startCoor = BS.indexToCoor(i)
                for jump in Node.jumps:
                    endCoor = startCoor + jump
                    midCoor = (startCoor + endCoor) / 2
                    endIndex = BS.coorToIndex(endCoor)
                    midIndex = BS.coorToIndex(midCoor)
                    if not (midIndex == len(BS.coors) or endIndex == len(BS.coors)):
                        if (not board.getBoard()[endIndex]) and (not board.getBoard()[midIndex]):
                            jumps = np.append(jumps, [[startCoor, midCoor, endCoor]], axis=0)
        return np.delete(jumps, 0, 0)

    def removeJump(self, jump):
        for i in range(0, len(self.possibleJumps)):
            # print(jump,i)
            # print(self.possibleJumps,i)
            if np.array_equal(jump, self.possibleJumps[i]):
                self.possibleJumps = np.delete(self.possibleJumps, i, 0)
                break

    def addChildNode(self, node):
        self.childrenNodes = np.append(self.childrenNodes, [node])

    def getChildNodes(self):
        return self.childrenNodes

    def getParentNode(self):
        return self.parentNode

    def getJump(self):
        return self.jump

    def getPossibleJumps(self):
        return self.possibleJumps

    def getBoardState(self):
        return self.boardState.copy()

    def getNodeState(self):
        return self.state

    def setNodeState(self, state):
        self.state = state

    def getUnfilledNodes(self):
        for child in self.childrenNodes:
            if not child.getNodeState():
                self.state = False
                return child.getNodeState()
        self.state = True
        return self

    def getPath(self):
        path = np.array([[[0, 0],[0, 0], [0, 0]]])
        currentNode = self
        while currentNode.getJump() is not None:
            path = np.append(path, [currentNode.getJump()], axis=0)
            currentNode = currentNode.getParentNode()
        return np.delete(path, 0, 0)
