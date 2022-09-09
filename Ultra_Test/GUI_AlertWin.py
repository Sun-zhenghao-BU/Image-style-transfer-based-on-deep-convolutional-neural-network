from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''
Set alert window
'''


class AlertWin(QWidget):
    def __init__(self):
        super(AlertWin, self).__init__()
        self.initUI()
        self.resize(150, 150)

    def initUI(self):
        self.setWindowTitle('Warning')
        # initialize Label
        label1 = QLabel(self)

        # initialize Button
        button1 = QPushButton(self)
        button2 = QPushButton(self)

        vbox = QVBoxLayout()
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont('Arial', 16))
        label1.setText("Warning：You have not chosen the needed pictures")
        vbox.addWidget(label1)

        hbox = QHBoxLayout()
        button1.setText("Back")
        button1.clicked.connect(self.onClick_Back_Button)
        hbox.addWidget(button1)

        # Set text and size//Binding the button2 and function
        button2.setText("Quit")
        button2.clicked.connect(self.onClick_Quit_Button)
        hbox.addStretch(1)
        hbox.addWidget(button2)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def onClick_Back_Button(self):
        self.hide()

    def onClick_Quit_Button(self):
        sender = self.sender()
        print((sender.text() + 'Pushed!'))
        app = QApplication.instance()
        app.quit()
