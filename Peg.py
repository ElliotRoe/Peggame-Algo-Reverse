from graphics import *

class Peg:
    def __init__(self, coorX, coorY, state, radius=20,weight=10):
        self.coor = [coorX,coorY]
        self.radius = radius
        self.state = state
        self.activeColor = color_rgb(7, 140, 3)
        self.emptyColor = color_rgb(242, 5, 5)
        self.outlineColor = color_rgb(242, 226, 5)
    def setActive(self, state):
        self.state = state
    def draw(self,win):
        peg = Circle(Point(self.coor[0],self.coor[1]))
        if self.state:
            peg.setFill(self.activeColor)
            peg.setOutline(self.activeColor)
        else:
            peg.setFill(self.emptyColor)
            peg.setOutline(self.emptyColor)
        peg.setWidth(10)
