import sys
import random

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import QPointF, QRectF, Qt


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Suprematism")
        self.button = QPushButton(self)
        self.button.move(423, 423)
        self.button.clicked.connect(self.paintEvent)
        self.button.setText('Круг')
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.current_size = random.randint(20, 100)
        painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        painter.drawEllipse(QPointF(200, 200), self.current_size, self.current_size,)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Suprematism()
    window.show()
    sys.exit(app.exec())
