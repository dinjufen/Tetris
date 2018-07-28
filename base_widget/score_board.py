from PyQt5.QtWidgets import QLabel, QFormLayout, QWidget, QVBoxLayout
from .button import Button

from .next_shape import NextShape


class ScoreBoard(QWidget):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0

        self.setFixedWidth(350)

        self.shape_widget = NextShape()

        self.lb_score = QLabel(self.tr("Score"))
        self.show_score = QLabel(self.tr('0'))

        self.lb_level = QLabel(self.tr("Level"))
        self.show_level = QLabel(self.tr('1'))

        score_layout = QFormLayout()
        score_layout.addRow(self.lb_level, self.show_level)
        score_layout.addRow(self.lb_score, self.show_score)

        self.btn_restart = Button(self.tr("Restart"))
        self.btn_restart.clicked.connect(self.restart)

        self.btn_exit    = Button(self.tr("Close"))

        layout = QVBoxLayout()
        layout.addWidget(self.shape_widget)
        layout.addLayout(score_layout)
        layout.addWidget(self.btn_restart)
        layout.addWidget(self.btn_exit)

        self.setLayout(layout)

    def restart(self):
        self.score = 0
        self.show_score.setText('0')

    def changeScore(self):
        self.score += 1
        self.show_score.setText(str(self.score))
