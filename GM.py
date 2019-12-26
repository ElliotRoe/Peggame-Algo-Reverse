from BoardState import BoardState as BS
from graphics import *


class GM:
    def __init__(self):
        self.message = "df";

    def say(self, message):
        self.message = message
        print(self.message)


def main():
    gameMaster = GM()
    gameMaster.say('hello world!')
    initBoard = BS(
        [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
    win = GraphWin()


if __name__ == "__main__":
    main()
