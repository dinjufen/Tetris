from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Button(QPushButton):

    def __init__(self, name):
        super(Button, self).__init__()
        self.setFixedSize(100, 40)
        self.setText(name)
        self.setFont(QFont("Microsoft YaHei", 12))
        self.setFocusPolicy(Qt.NoFocus)