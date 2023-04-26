import sys
from PyQt6.QtCore import Qt, QSize, QRect, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QSizePolicy\
 ,QMessageBox, QLabel, QHBoxLayout
from PyQt6.QtGui import QFont, QMovie
import random


#creates a main menu window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(450,100, 500, 500)
        self.setWindowTitle('Main Menu')
        
        #Should add some decoration to make the menu look better
        self.layout = QVBoxLayout()
        self.l1 = QLabel()
        self.l1.setText('Please Select Game')
        self.l1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.l1)
        
        # Adds the buttons
        self.TicTactToeButton = QPushButton('Play TicTacToe')
        self.TicTactToeButton.clicked.connect(self.tictactoe)
        self.RPSButton = QPushButton('Play Rock Paper Scissors')
        self.RPSButton.clicked.connect(self.RPS)
        self.exitButton = QPushButton('Exit')
        self.exitButton.clicked.connect(self.exit)
        self.layout.addWidget(self.TicTactToeButton)
        self.layout.addWidget(self.RPSButton)
        self.layout.addWidget(self.exitButton)

        self.setLayout(self.layout)
        
        
        self.show()
    def tictactoe(self):
        self.tickTackToe_window = TicTacToe()
        self.tickTackToe_window.show()
    def RPS(self):
        self.rps_window = RPS()
        self.rps_window.show()
    def exit(self):
        sys.exit()

        
#creates the TicTacToe board
class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        #Names the window, ontop of the page
        self.setWindowTitle('Tic-Tac-Toe')
        #sets size of the window
        self.setGeometry(450, 100, 500, 500)
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
    def exit(self):
        self.close()
        

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
        else:
            self.catsGame()

    def catsGame(self):
        hello = []
        for element in checkWin.board:
            for elem in element:
                if elem != 0:
                    hello.append(elem)
                    if len(hello) < 9:
                        pass
                    else:
                        msg = QMessageBox(text = "This is a cat's game, no one wins")
                        msg.StandardButton.Ok
                        msg.exec()
                        msg.buttonClicked.connect(self.exit())

    def exit(self):
        sys.exit()
        # checkWin.board =[[0,0,0],[0,0,0],[0,0,0]]

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
        if checkWin.board[self.location[0]][self.location[1]] == 0:
            if self.go == 1:
                self.setText('x')
                x_o.go = 0
                self.type = 'x'
            elif self.go == 0: 
                self.setText('o')
                x_o.go = 1
                self.type = 'o'
            checkWin.board[self.location[0]][self.location[1]] = self.type
        checkWin(self.location, self.type)

#This Makes Rock Paper Scissors game

class RPS(QWidget):
    youWin = 0
    themWin = 0
    def __init__(self):
        super().__init__()
      
        self.setWindowTitle('Rock Paper Scissors')
        
        self.setGeometry(450, 100, 500, 500)
        
        self.layout = QGridLayout() 
        self.scores = QLabel()
        #calls to update the score counter in the top
        self.changeScores()
        self.layout.addWidget(self.scores, 0, 0)

        #creating the buttons
        self.rockButton = QPushButton()
        self.paperButton = QPushButton()
        self.scissorsButton = QPushButton()
        self.rockButton.setText("Rock")
        self.rockButton.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        self.rockButton.clicked.connect(self.rock)
        self.paperButton.setText("Paper")
        self.paperButton.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        self.paperButton.clicked.connect(self.paper)
        self.scissorsButton.setText("Scissors")
        self.scissorsButton.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        self.scissorsButton.pressed.connect(self.scissors)
        
        self.pickOption = QLabel(f'Pick an Option:')
        self.pickOption.setFont(QFont('Times New Roman', 25))
        
        #Adds buttons to their spots
        self.layout.addWidget(self.pickOption,1,1)
        self.layout.addWidget(self.rockButton, 2,0)
        self.layout.addWidget(self.paperButton, 2,1)
        self.layout.addWidget(self.scissorsButton, 2,2)
        self.setLayout(self.layout)
        
    #updates the scores
    def changeScores(self):
        self.scores.setText(f'Your wins: {RPS.youWin} A.I wins: {RPS.themWin}')
        

    def scissors(self):
        self.rps_animate = RPSAnimation('scissors')
        self.rps_animate.show()
        self.changeScores()
        
    
    def rock(self):
        self.rps_animate = RPSAnimation('rock')
        self.rps_animate.show()
        self.changeScores()
        
        
    def paper(self):
        self.rps_animate = RPSAnimation('paper')
        self.rps_animate.show()
        self.changeScores()
       
    
    def exits(self):
        self.rps_animate.close()

class RPSAnimation(QWidget):
    def __init__(self, choice):
        super().__init__()
        self.setGeometry(950,100, 500, 500)
        self.setWindowTitle('Animation')
        
        self.player_label = QLabel()
        self.ai_label = QLabel()
        self.player = choice
        self.aiChoice_num = random.randint(1,3)

        self.describe()

        #Puts the size of the GIFs
        self.player_label.setGeometry(QRect(25, 25, 200, 200))
        self.player_label.setMinimumSize(QSize(200, 200))
        self.player_label.setMaximumSize(QSize(200, 200))
        self.player_label.setObjectName("Player Choice")

        self.ai_label.setGeometry(QRect(25, 25, 200, 200))
        self.ai_label.setMinimumSize(QSize(200, 200))
        self.ai_label.setMaximumSize(QSize(200, 200))
        self.ai_label.setObjectName("Ai Choice")

        self.player_label.setMovie(self.player_movie) 
        self.ai_label.setMovie(self.ai_movie)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.player_label)
        self.layout.addWidget(self.ai_label)
        self.setLayout(self.layout)
        
        #Makes a timer so it tells use who one after gif plays out
        self.timer = QTimer()
        self.timer.timeout.connect(self.winMSG)
        self.timer.start(3000)

        self.player_movie.start()
        self.ai_movie.start()
        
        #defining what everyone picked
    def describe(self):
        #Picks the other person choice and gives them a gif
        if self.aiChoice_num == 1:
            self.aiChoice = 'scissors'
            self.ai_movie = QMovie(r'Pictures\rock-paper-scissors-scissors.gif')
        elif self.aiChoice_num == 2:
            self.aiChoice = 'rock'
            self.ai_movie = QMovie(r'Pictures\rock-paper-scissors-rock.gif')
        elif self.aiChoice_num == 3:
            self.aiChoice = 'paper'
            self.ai_movie = QMovie(r'Pictures\rock-paper-scissors-paper.gif')
        
        

        #Seeing who one and giving the their gifs
        if self.player == 'scissors':
             self.player_movie = QMovie(r'Pictures\rock-paper-scissors-scissors.gif')
             if self.player == self.aiChoice:
                self.who_won = "Tie"
             elif self.aiChoice == 'rock':
                self.who_won = "A.I won"
                RPS.themWin = RPS.themWin + 1
             elif self.aiChoice == 'paper':
                self.who_won = "You won"
                RPS.youWin += 1
        elif self.player == 'rock':
             self.player_movie = QMovie(r'Pictures\rock-paper-scissors-rock.gif')
             if self.player == self.aiChoice:
                self.who_won = "Tie"
             elif self.aiChoice == 'paper':
                self.who_won = "A.I won"
                RPS.themWin = RPS.themWin + 1
             elif self.aiChoice == 'scissors':
                self.who_won = "You won"
                RPS.youWin += 1
        elif self.player == 'paper':
             self.player_movie = QMovie(r'Pictures\rock-paper-scissors-paper.gif')
             if self.player == self.aiChoice:
                self.who_won = "Tie"
             elif self.aiChoice == 'scissors':
                self.who_won = "A.I won"
                RPS.themWin = RPS.themWin + 1
             elif self.aiChoice == 'rock':
                self.who_won = "You won"
                RPS.youWin += 1
    #Adds the win message
    def winMSG(self):
        self.timer.stop()
        msg = QMessageBox(text = self.who_won)
        msg.StandardButton.Ok
        msg.exec()
        msg.buttonClicked.connect(self.exit)
    def exit(self):
        RPS.exits()
        

        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()