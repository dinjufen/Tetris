import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from base_widget.display import DisplayWidget
from base_widget.score_board import ScoreBoard


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(900, 950)
        self.setWindowTitle("俄罗斯方块")

        self.main_widget = DisplayWidget()
        self.score_widget = ScoreBoard()
        self.main_widget.signalShape.connect(self.score_widget.shape_widget.drawShape)
        self.main_widget.signalScore.connect(self.score_widget.changeScore)
        self.score_widget.btn_exit.clicked.connect(self.close)


        layout = QHBoxLayout()
        layout.addWidget(self.main_widget)
        layout.addWidget(self.score_widget)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        key = event.key()
        self.main_widget.keyPress(key)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())