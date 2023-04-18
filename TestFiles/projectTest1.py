from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor
import sys

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layout = QVBoxLayout()
        board = QGridLayout()

        
        color = 'back'
        for j in range(7):
            if color == 'black':
                board.addWidget(Color('black'), j, 0)
                color = 'white'
            elif color == "white":
                board.addWidget(Color('white'), j, 0)
                color = 'white'
        layout.addWidget(QPushButton('hi'))
        layout.addLayout(board)
        widget = QWidget()
        widget.setLayout(board)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()