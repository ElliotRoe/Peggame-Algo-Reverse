from graphics import *


class Peg:
    def __init__(self, coorX, coorY, state, radius=20, weight=10):
        self.coor = Point(coorX, coorY)
        self.radius = radius
        self.state = state
        self.activeColor = color_rgb(7, 140, 3)
        self.emptyColor = color_rgb(242, 5, 5)
        self.outlineColor = color_rgb(242, 226, 5)
        self.peg = Circle(self.coor, self.radius)
        if self.state:
            self.peg.setFill(self.activeColor)
            self.peg.setOutline(self.outlineColor)
        else:
            self.peg.setFill(self.emptyColor)
            self.peg.setOutline(self.outlineColor)
        self.peg.setWidth(10)

    def setActive(self, state):
        self.state = state
        if self.state:
            self.peg.setFill(self.activeColor)
        else:
            self.peg.setFill(self.emptyColor)

    def getState(self):
        return self.state

    def undraw(self):
        self.peg.undraw()

    def draw(self, win):
        self.peg.draw(win)
