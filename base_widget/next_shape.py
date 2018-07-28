from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QBrush, QPainter, QPen
from PyQt5.QtCore import Qt

from model.shape_fac import ShapeFactory


class NextShape(QWidget):

    def __init__(self):
        super(NextShape, self).__init__()
        self.setFixedSize(250, 250)
        self.pix = QPixmap(self.size())
        self.pix.fill(Qt.white)

    def drawShape(self):
        self.pix.fill(Qt.white)
        next_shape = ShapeFactory.getNext()
        coors = next_shape.getVirCoor()
        pen = QPen()
        pen.setColor(next_shape.color)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(next_shape.color)
        painter = QPainter()
        painter.begin(self.pix)
        painter.setBrush(brush)
        painter.setPen(pen)
        for coor in coors:
            painter.drawRect(50 + coor.x * 45, 50 + coor.y * 45, 42, 42)
        painter.end()
        self.update()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

