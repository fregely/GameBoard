import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QSizePolicy\
 ,QMessageBox
from PyQt6.QtGui import QPixmap, QColor, QPalette, QFont
#creates the window for the application
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        #Names the window, ontop of the page
        self.setWindowTitle('Tic-Tac-toe')
        #sets size of the window
        self.setGeometry(0, 0, 500, 500)
        #Opens the window
        self.show()
        #Calls class function
        self.peices()

    def peices(self):
        #Creates a grid the widgets can be placed on
        board = QGridLayout()
        #places a widget on 3 by 3 grid
        for j in range(0,3):
            for k in range(0,3):
                board.addWidget(x_o(j,k), j , k)
        #Makes the layout of the window the grid
        self.setLayout(board)

#This Class can be improved a lot 
class checkWin:
    board = [[0,0,0],[0,0,0],[0,0,0]]
    def __init__(self, location, types):
        checkWin.board[location[0]][location[1]] = types
        self.check = []
        self.checkRows()      
    #decieded to seperate all these out so I know which is which. Could combine
    def checkRows(self):
        for j in range(3):
            self.check = set(checkWin.board[j])
            self.check = list(self.check)
            self.winCheck()
        self.checkColumns()
    
    def checkColumns(self):
        for j in range(3):
            self.check = []
            for k in range(3):
              self.check.append(checkWin.board[k][j])
            self.check = set(self.check)
            self.check = list(self.check)
            self.winCheck()  
        self.checkDiagnoal()
    #I feel like I should be able to do this in one for loop, but i'm not sure how
    def checkDiagnoal(self):
        self.check = []
        for j in range(3):
            self.check.append(checkWin.board[j][j])
        self.check = set(self.check)
        self.check = list(self.check)
        self.winCheck() 
        self.check = []
        for j in range(3):
            self.check.append(checkWin.board[2-j][j])
            print(self.check)
        self.check = set(self.check)
        self.check = list(self.check)
        self.winCheck()  


    def winCheck(self):
        if len(self.check) == 1 and self.check[0] != 0:
            text = f"\n{self.check[0]}'s Have Won!"
            msg = QMessageBox(text = "Victory!" + text)
            msg.StandardButton.Ok
            msg.exec()
            msg.buttonClicked.connect(self.exit())
    def exit(self):
        sys.exit()

#Class for making the buttons, and giving them value, Uses QPushButtom to make the buttons
class x_o(QPushButton):
    go = 1
    def __init__(self, x, y):
        super().__init__()
        #Makes each button the same size, first is x, 2nd is y
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        self.setFont(QFont('Times New Roman', 50))
        #Could also used .clicked, does same thing, just with pressed its on click and can have
        #it does something on release fo the click using .released
        self.pressed.connect(self.choice)
        self.location = [x,y]
        self.type = None
    def choice(self):
        if self.go == 1:
            self.setText('x')
            x_o.go = 0
            self.type = 'x'
        elif self.go == 0: 
            self.setText('o')
            x_o.go = 1
            self.type = 'o'
        checkWin(self.location, self.type)
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())