import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.size = 0
        self.x = 0
        self.y = 0
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.paint_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paint_circle(self, qp):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 560)
        self.size = random.randint(0, 560)
        qp.setPen(QColor("yellow"))
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(self.x, self.y, self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())