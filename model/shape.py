from PyQt5.Qt import Qt


class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:

    def __init__(self):
        self.cur_angle = 0
        self.offset_x = 3
        self.offset_y = 0
        self.length = 4
        self.coor = {}
        self.color = Qt.red
        self.speed = 4
        self.old_x = self.offset_x
        self.old_y = self.offset_y

    def turn(self):
        self.old_x = self.offset_x
        self.old_y = self.offset_y
        if self.cur_angle == 3:
            self.cur_angle = 0
            return
        self.cur_angle += 1

    def left(self):
        for coor in self.coor[self.cur_angle]:
            if coor.x +self.offset_x <= 0:
                return
        self.old_x = self.offset_x
        self.old_y = self.offset_y
        self.offset_x -= 1

    def right(self):
        for coor in self.coor[self.cur_angle]:
            if coor.x +self.offset_x >= 9:
                return
        self.old_x = self.offset_x
        self.old_y = self.offset_y
        self.offset_x += 1

    def down(self):
        tmp = self.coor[self.cur_angle]
        for coor in tmp:
            if coor.y + self.offset_y >= 19:
                return
        self.old_y = self.offset_y
        self.old_x = self.offset_x
        self.offset_y += 1

    def getOffset(self):
        return self.offset_x, self.offset_y

    def getVirCoor(self):
        return self.coor[self.cur_angle]

    def getOldOffset(self):

        return self.old_x, self.old_y

    def getOldShape(self):
        if self.cur_angle == 0:
            old_coor = self.coor[3]
        else:
            old_coor = self.coor[self.cur_angle-1]
        return old_coor

    def getNextShape(self):
        if self.cur_angle == 3:
            next_coor = self.coor[0]
        else:
            next_coor = self.coor[self.cur_angle+1]
        return next_coor


class SquareShape(Shape):

    def __init__(self):
        super().__init__()
        self.color = Qt.blue
        self.coor = {}
        for i in range(4):
            self.coor[i] = [Coor(0, 0), Coor(1, 0), Coor(0, 1), Coor(1, 1)]

    def __str__(self):
        return "SquareShape"


class ZShape1(Shape):

    def __init__(self):
        super().__init__()
        self.coor = {}
        self.coor[0] = [Coor(0, 0), Coor(1, 0), Coor(1, 1), Coor(2, 1)]
        self.coor[1] = [Coor(2, 0), Coor(2, 1), Coor(1, 1), Coor(1, 2)]
        self.coor[2] = [Coor(0, 0), Coor(1, 0), Coor(1, 1), Coor(2, 1)]
        self.coor[3] = [Coor(2, 0), Coor(2, 1), Coor(1, 1), Coor(1, 2)]
        self.color = Qt.green

    def __str__(self):
        return "ZShape1"


class ZShape2(Shape):

    def __init__(self):
        super().__init__()
        self.color = Qt.darkGreen
        self.coor = {}
        self.coor[0] = [Coor(0, 1), Coor(1, 1), Coor(1, 0), Coor(2, 0)]
        self.coor[1] = [Coor(0, 0), Coor(0, 1), Coor(1, 1), Coor(1, 2)]
        self.coor[2] = [Coor(0, 1), Coor(1, 1), Coor(1, 0), Coor(2, 0)]
        self.coor[3] = [Coor(0, 0), Coor(0, 1), Coor(1, 1), Coor(1, 2)]

    def __str__(self):
        return "ZShape2"


class IShape(Shape):
    '''
    __ __ __ __
    '''
    def __init__(self):
        super().__init__()
        self.color = Qt.red
        self.coor = {}
        self.coor[0] = [Coor(0, 0), Coor(1, 0), Coor(2, 0), Coor(3, 0)]
        self.coor[1] = [Coor(1, 0), Coor(1, 1), Coor(1, 2), Coor(1, 3)]
        self.coor[2] = [Coor(0, 0), Coor(1, 0), Coor(2, 0), Coor(3, 0)]
        self.coor[3] = [Coor(1, 0), Coor(1, 1), Coor(1, 2), Coor(1, 3)]

    def __str__(self):
        return "IShape"


class LShape1(Shape):
    '''
     __
    |__|______
    |__|__|__|
    '''
    def __init__(self):
        super().__init__()
        self.color = Qt.yellow
        self.coor = {}
        self.coor[0] = [Coor(0, 0), Coor(0, 1), Coor(1, 1), Coor(2, 1)]
        self.coor[1] = [Coor(1, 0), Coor(0, 0), Coor(0, 1), Coor(0, 2)]
        self.coor[2] = [Coor(0, 0), Coor(1, 0), Coor(2, 0), Coor(2, 1)]
        self.coor[3] = [Coor(0, 2), Coor(1, 2), Coor(1, 1), Coor(1, 0)]

    def __str__(self):
        return "LShape1"


class LShape2(Shape):
    '''
            |
       __ __|
    '''

    def __init__(self):
        super().__init__()
        self.color = Qt.darkYellow
        self.coor = {}
        self.coor[0] = [Coor(0, 1), Coor(1, 1), Coor(2, 1), Coor(2, 0)]
        self.coor[1] = [Coor(0, 0), Coor(0, 1), Coor(0, 2), Coor(1, 2)]
        self.coor[2] = [Coor(0, 1), Coor(0, 0), Coor(1, 0), Coor(2, 0)]
        self.coor[3] = [Coor(0, 0), Coor(1, 0), Coor(1, 1), Coor(1, 2)]

    def __str__(self):
        return "LShape2"


class TShape(Shape):
    '''
    ____
     |
     |
    '''
    def __init__(self):
        super().__init__()
        self.color = Qt.magenta
        self.coor = {}
        self.coor[0] = [Coor(0, 0), Coor(1, 0), Coor(2, 0), Coor(1, 1)]
        self.coor[1] = [Coor(1, 0), Coor(1, 1), Coor(1, 2), Coor(0, 1)]
        self.coor[2] = [Coor(0, 1), Coor(1, 1), Coor(1, 0), Coor(2, 1)]
        self.coor[3] = [Coor(0, 0), Coor(0, 1), Coor(1, 1), Coor(0, 2)]

    def __str__(self):
        return "TShape"
