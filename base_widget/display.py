from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSignal, Qt

from model.shape_fac import ShapeFactory


ROW = 20
COL = 10


class DisplayWidget(QWidget):
    signalScore = pyqtSignal()
    signalShape = pyqtSignal()

    def __init__(self):
        super(DisplayWidget, self).__init__()
        self.interval = 1000
        self.cur_shape = None
        # self.score = 0

        self.setFixedSize(460, 900)
        self.pixmap = QPixmap(self.size())
        self.initWidget()

    def initWidget(self):
        
        self.pixmap.fill(Qt.white)
        self.matrix = [[0]*COL for i in range(ROW)]
        self.timer_id = self.startTimer(self.interval)
        # self.signalShape.connect(NextShape.drawShape)
        # self.signalScore.connect(ScoreBoard.changeScore)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

    def keyPress(self, key):
        if self.cur_shape is None:
            return
        if key == Qt.Key_Up:
            if self.turn_blocked():
                return
            self.cur_shape.turn()
            self.clearOldShape(turn=True)
            self.drawShape()
        elif key == Qt.Key_Left:
            if self.left_blocked():
                return
            self.cur_shape.left()
            self.clearOldShape()
            self.drawShape()
        elif key == Qt.Key_Right:
            if self.right_blocked():
                return
            self.cur_shape.right()
            self.clearOldShape()
            self.drawShape()
        elif key == Qt.Key_Down:
            if self.cur_shape is None:
                self.cur_shape = ShapeFactory.getCur()
                if self.is_blocked():
                    self.killTimer(self.timer_id)
                self.signalShape.emit()
            if not self.is_blocked():
                self.cur_shape.down()
                self.clearOldShape()
                self.drawShape()
            else:
                x, y = self.cur_shape.getOffset()
                for coor in self.cur_shape.getVirCoor():
                    self.matrix[coor.y + y][coor.x + x] = 1
                self.cur_shape = None
                self.updateMat()
        self.update()

    def timerEvent(self, *args, **kwargs):
        if self.cur_shape is None:
            self.cur_shape = ShapeFactory.getCur()
            if self.is_blocked():
                self.killTimer(self.timer_id)
            self.signalShape.emit()
        if not self.is_blocked():
            self.cur_shape.down()
            self.clearOldShape()
            self.drawShape()
        else:
            x, y = self.cur_shape.getOffset()
            for coor in self.cur_shape.getVirCoor():
                self.matrix[coor.y+y][coor.x+x] = 1
            self.cur_shape = None
            self.updateMat()
        self.update()

    def updateMat(self):
        destroyed = []
        for i in range(ROW):
            if self.checkOnes(self.matrix[i]):
                destroyed.append(i)
        for j in destroyed:
            self.destroyRow(j)
        self.drawMatrix()

    def destroyRow(self, row):
        self.signalScore.emit()
        for i in range(row, 0, -1):
            for j in range(COL):
                self.matrix[i][j] = self.matrix[i-1][j]
        for j in range(COL):
            self.matrix[0][j] = 0

    def checkOnes(self, m):
        result = True
        for i in m:
            if i == 0:
                result = False
        return result

    def drawShape(self):
        painter = QPainter()
        pen = QPen()
        pen.setColor(self.cur_shape.color)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(self.cur_shape.color)
        painter.begin(self.pixmap)
        painter.setBrush(brush)
        painter.setPen(pen)
        offset_x, offset_y = self.cur_shape.getOffset()
        for coor in self.cur_shape.getVirCoor():
            painter.drawRect((coor.x+offset_x)*45, (coor.y+offset_y)*45, 42, 42)
        painter.end()

    def clearOldShape(self, turn=False):
        painter = QPainter()
        pen = QPen()
        pen.setColor(Qt.white)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(Qt.white)
        painter.begin(self.pixmap)
        painter.setBrush(brush)
        painter.setPen(pen)
        old_x, old_y = self.cur_shape.getOldOffset()
        if turn:
            coor = self.cur_shape.getOldShape()
        else:
            coor = self.cur_shape.getVirCoor()
        for coor in coor:
            painter.drawRect((coor.x + old_x) * 45, (coor.y + old_y) * 45, 42, 42)
        painter.end()

    def drawMatrix(self):
        self.pixmap.fill(Qt.white)
        painter = QPainter()
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(Qt.black)
        painter.begin(self.pixmap)
        painter.setBrush(brush)
        for x in range(COL):
            for y in range(ROW):
                if self.matrix[y][x] == 1:
                    painter.drawRect(x*45, y*45, 42, 42)
        painter.end()
        self.update()

    def is_blocked(self):
        if self.cur_shape:
            x, y = self.cur_shape.getOffset()
            for coor in self.cur_shape.getVirCoor():
                if coor.y + y == 19:
                    return True
                if self.matrix[coor.y+y+1][coor.x+x] == 1:
                    return True
        return False

    def right_blocked(self):
        if self.cur_shape:
            x, y = self.cur_shape.getOffset()
            for coor in self.cur_shape.getVirCoor():
                if coor.x + x == 9:
                    return True
                if self.matrix[coor.y+y][coor.x+x+1] == 1:
                    return True
        return False

    def left_blocked(self):
        if self.cur_shape:
            x, y = self.cur_shape.getOffset()
            for coor in self.cur_shape.getVirCoor():
                if coor.x + x == 0:
                    return True
                if self.matrix[coor.y+y][coor.x+x-1] == 1:
                    return True
        return False

    def turn_blocked(self):
        if self.cur_shape:
            x, y = self.cur_shape.getOffset()
            for coor in self.cur_shape.getNextShape():
                if coor.y + y == 19:
                    return True
                if coor.x + x == 9:
                    return True
                if coor.x + x == 0:
                    return True
                if self.matrix[coor.y+y+1][coor.x+x] == 1:
                    return True
                if self.matrix[coor.y+y][coor.x+x+1] == 1:
                    return True
                if self.matrix[coor.y+y][coor.x+x-1] == 1:
                    return True
        return False