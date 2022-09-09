import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from GUI_FirstWin import Generator


# from GUI_ResultShowWin import ResultShowWin

class GUI_MainWin(QWidget):
    def __init__(self):
        super(GUI_MainWin, self).__init__()
        self.initUI()
        self.resize(600, 600)
        self.setWindowTitle('GUI_MainWin')
        self.FirstWin = Generator()

    def initUI(self):
        # initialize Label
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        # initialize Button
        button1 = QPushButton(self)
        button2 = QPushButton(self)

        # Set text and size//Binding the button1 and function
        button1.setText("Start")
        button1.setFixedWidth(150)
        button1.setFixedHeight(50)
        # button1.clicked.connect(self.popWindow)
        button1.clicked.connect(self.onClick_Start_Button)

        # Set text and size//Binding the button2 and function
        button2.setText("Quit")
        button2.setFixedWidth(150)
        button2.setFixedHeight(50)
        button2.clicked.connect(self.onClick_Quit_Button)

        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont('Arial', 20))
        label1.setText("Welcome to Anthony's Image Stylization Generator")

        label2.setMaximumSize(600, 400)
        label2.setAlignment(Qt.AlignCenter)
        label2.setPixmap(QPixmap("/Users/anthony/Pictures/images/image3.jpg"))
        label2.setScaledContents(True)

        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label3.setOpenExternalLinks(True)
        label3.setText(
            "<a href='https://github.com/Sun-zhenghao-BU/Image-style-transfer-based-on-deep-convolutional-neural-network'>《Visit my Github to learn more》</a>")
        label3.setAlignment(Qt.AlignRight)
        label3.setToolTip('This is a hyperlink')

        # Set 2 buttons with horizontal layout
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addStretch(1)
        hbox.addWidget(button2)

        # Set the horizontal layout and labels with vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(label3)

        self.setLayout(vbox)

    # Quit this GUI
    def onClick_Quit_Button(self):
        sender = self.sender()
        print((sender.text() + 'Button is pushed'))
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

    # Start transfering
    def onClick_Start_Button(self):
        sender = self.sender()
        print((sender.text() + 'Button is pushed'))
        self.hide()
        self.FirstWin.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GUI_MainWin()
    main.show()
    sys.exit(app.exec_())
