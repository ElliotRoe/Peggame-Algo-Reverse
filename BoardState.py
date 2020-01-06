import numpy as np

class BoardState:
    coors = [np.array([4, 4]),
             np.array([3, 3]), np.array([5, 3]),
             np.array([2, 2]), np.array([4, 2]), np.array([6, 2]),
             np.array([1, 1]), np.array([3, 1]), np.array([5, 1]), np.array([7, 1]),
             np.array([0, 0]), np.array([2, 0]), np.array([4, 0]), np.array([6, 0]), np.array([8, 0])]

    def __init__(self, pegs):
        self.pegs = pegs

    def __str__(self):
        return str(BoardState.coors)

    def copy(self):
        return BoardState(self.getBoard())

    def getBoard(self):
        return self.pegs.copy()

    def getPeg(self, i):
        return self.pegs[i]

    def setPeg(self, i, state):
        self.pegs[i] = state

    @staticmethod
    def coorToIndex(c):
        i = 0
        for coor in BoardState.coors:
            if np.array_equal(BoardState.coors[i], c):
                return i
            i = i + 1
        return len(BoardState.coors)

    @staticmethod
    def indexToCoor(i):
        return BoardState.coors[i]