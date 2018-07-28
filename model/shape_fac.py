from random import randint
from .shape import *


class ShapeFac:
    ALL = [SquareShape, ZShape1, ZShape2, IShape, LShape1, LShape2, TShape]

    def __init__(self):
        self.cur = ShapeFac.ALL[randint(0, 6)]()
        self.next = None

    def getCur(self):
        self.next = ShapeFac.ALL[randint(0, 6)]()
        return self.cur

    def getNext(self):
        self.cur = self.next
        return self.next


ShapeFactory = ShapeFac()
