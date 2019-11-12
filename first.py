import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor


class KiK(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = randint(1, 200)
        self.y = randint(1, 200)
        self.d = randint(10, 100)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Кнопка и круги")

        self.btn1 = QPushButton("Создать", self)
        self.btn1.clicked.connect(self.new)
        self.btn1.move(100, 100)

    def new(self):
        self.x = randint(1, 200)
        self.y = randint(1, 200)
        self.d = randint(10, 100)
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x, self.y, self.x + self.d, self.y + self.d)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = KiK()
    w.show()
    sys.exit(app.exec())
