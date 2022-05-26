from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''
设置告警弹窗
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
        label1.setText("注意：您还没有选择所要的图像")
        vbox.addWidget(label1)

        hbox = QHBoxLayout()
        button1.setText("返回以选择")
        button1.clicked.connect(self.onClick_Back_Button)
        hbox.addWidget(button1)

        # Set text and size//Binding the button2 and function
        button2.setText("我要退出")
        button2.clicked.connect(self.onClick_Quit_Button)
        hbox.addStretch(1)
        hbox.addWidget(button2)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def onClick_Back_Button(self):
        self.hide()

    def onClick_Quit_Button(self):
        sender = self.sender()
        print((sender.text() + '按钮被按下'))
        app = QApplication.instance()
        # 退出应用程序
        app.quit()
