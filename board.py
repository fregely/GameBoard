import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QSizePolicy, QMessageBox
from PyQt6.QtGui import QPixmap, QColor, QPalette

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Background Image')
        self.setGeometry(100, 100, 500, 500)
        self.initUI()
        self.peices()
        
    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap(r'Pictures\Checkerboard.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        self.show()

    def peices(self):
        board = QGridLayout()
        spacer = QWidget()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        for i in range(8):
            for j in range(2):
                board.addWidget(QPushButton("hi"),j,i)
            for middle in range(3,5):
                board.addWidget(spacer, middle, i)
            for k in range(5,7):
                board.addWidget(QPushButton("bye"),k,i)
        self.setLayout(board)
            

class whiteButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setGeometry
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())