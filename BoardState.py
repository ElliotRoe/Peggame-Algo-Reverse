class BoardState:
    coors = [[4, 4], [3, 3], [3, 5], [2, 2], [2, 4], [2, 6], [1, 1], [1, 3], [1, 5], [1, 7], [0, 0], [0, 2], [0, 4],
             [0, 6], [0, 8]]

    def __init__(self, pegs):
        self.pegs = pegs

    def getBoard(self):
        return self.pegs

    def getPeg(self, i):
        return self.pegs[i]

    def setPeg(self, i, state):
        self.pegs[i] = state

    @staticmethod
    def coorToIndex(c):
        i = 0
        for coor in BoardState.coors:
            if BoardState.coors[i] == c:
                return i
            i = i + 1
        return -1

    @staticmethod
    def indexToCoor(i):
        return BoardState.coors[i]