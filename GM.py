from BoardState import BoardState as BS
from graphics import *
from Peg import Peg
import time


class GM:
    def __init__(self):
        self.message = "df"

    def say(self, message):
        self.message = message
        print(self.message)


def main():
    activeColor = color_rgb(7,140,3)
    emptyColor = color_rgb(242, 5, 5)
    outlineColor = color_rgb(242, 226, 5)

    rad = 20

    print("test")
    win = GraphWin("My Circle", 500, 500)
    win.setBackground(color_rgb(207, 155, 242))

    pt = Point(win.getHeight()/2,win.getWidth()/2)
    c = Circle(pt, rad)
    c.setFill(activeColor)
    c.setOutline(outlineColor)
    c.setWidth(10)

    pt2 = Point(pt.getX(),pt.getY()+40)
    c2 = Circle(pt2,rad)
    c2.setFill(emptyColor)
    c2.setOutline(outlineColor)
    c2.setWidth(10)

    c.draw(win)
    time.sleep(2)
    c2.draw(win)

    win.getMouse()
    win.close()


main()
