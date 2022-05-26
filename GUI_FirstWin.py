from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtGui
import GUI_WaitingWin
import GUI_AlertWin
import os


'''
设置多线程和第一子窗口
'''


def draw_final():
    os.system("python /Users/anthony/Bachelor/华大日常/大四下/毕业设计/IST/Ultra_Test/DrawFinal.py")


# class MyThread(QThread):
#     signal1 = pyqtSignal(str)  # 括号里填写信号传递的参数
#
#     def __init__(self):
#         super(MyThread, self).__init__()
#
#     def run(self):
#         # plt.figure()
#         print("子线程已开启")  # 你的需要单独开启线程的逻辑代码
#         draw_final()
#         self.signal1.emit("转换成功！单击View Result以查看结果")  # 发出任务完成信号
#         # self.signal2.emit(value)
#         # return value


class Generator(QWidget):
    def __init__(self):
        super(Generator, self).__init__()
        self.waiting_window = None
        self.initUI()
        self.resize(600, 600)
        self.setWindowTitle('GUI_FirstWin')
        # self.thread = MyThread()
        self.AW = GUI_AlertWin.AlertWin()

    def initUI(self):

        vbox = QVBoxLayout()
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        # 图像显示区域
        self.label4 = QLabel()
        self.label5 = QLabel()

        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont('Arial', 20))
        label1.setText("请先选择您想要的风格图像和内容图像")
        vbox.addWidget(label1)
        vbox.addStretch(1)

        hbox1 = QHBoxLayout()
        label2.setAlignment(Qt.AlignLeft)
        label2.setFont(QFont('Arial', 14))
        label2.setText("选择您想要的风格图像:")
        hbox1.addWidget(label2)

        self.lineEdit1 = QLineEdit()
        hbox1.addWidget(self.lineEdit1)

        self.button1 = QPushButton()
        self.button1.setText("浏览")
        self.button1.clicked.connect(self.setFilePath1)
        hbox1.addWidget(self.button1)

        hbox2 = QHBoxLayout()
        self.label4.setText("显示图片")
        self.label4.setFixedSize(270, 180)
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setStyleSheet("QLabel{background:white;}")
        hbox2.addStretch(3)
        hbox2.addWidget(self.label4)
        hbox2.addStretch(2)

        hbox3 = QHBoxLayout()
        label3.setAlignment(Qt.AlignLeft)
        label3.setFont(QFont('Arial', 14))
        label3.setText("选择您想要的内容图像:")
        hbox3.addWidget(label3)

        self.lineEdit2 = QLineEdit()
        hbox3.addWidget(self.lineEdit2)

        self.button2 = QPushButton()
        self.button2.setText("浏览")
        self.button2.clicked.connect(self.setFilePath2)
        hbox3.addWidget(self.button2)

        hbox4 = QHBoxLayout()
        self.label5.setText("显示图片")
        self.label5.setFixedSize(270, 180)
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setStyleSheet("QLabel{background:white;}")
        hbox4.addStretch(3)
        hbox4.addWidget(self.label5)
        hbox4.addStretch(2)

        hbox5 = QHBoxLayout()
        self.button3 = QPushButton()
        self.button3.setText('Start Transfer')
        self.button3.clicked.connect(self.onClick_Start_Button)

        # self.lineEdit3 = QLineEdit()

        self.button4 = QPushButton()
        self.button4.setText('Quit')
        self.button4.clicked.connect(self.onClick_End_Button)

        hbox5.addWidget(self.button3)
        # hbox5.addWidget(self.lineEdit3)
        hbox5.addStretch(1)
        hbox5.addWidget(self.button4)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = round((screen.width() - size.width()) / 2)
        newTop = round((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)

    def onClick_Start_Button(self):
        if len(self.lineEdit1.text()) == 0 or len(self.lineEdit2.text()) == 0:
            self.AW.show()
        else:
            self.hide()
            self.waiting_window = GUI_WaitingWin.WaitingWin(style_image_address(), content_image_address())
            # value = Process.output()
            # value.clamp_(0, 1)
            # plt.figure()
            # Process.img_show(self.value, title="Output Image")
            # plt.show()

    def onClick_End_Button(self):
        sender = self.sender()
        print((sender.text() + '按钮被按下'))
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

    def setFilePath1(self):
        global style_image_path
        style_image_path, imgType = QtWidgets.QFileDialog.getOpenFileName(self, "选择图片", "",
                                                                          "*.jpg;;*.png;;All Files(*)")
        self.lineEdit1.setText(style_image_path)
        print(style_image_path)
        img = QtGui.QPixmap(style_image_path).scaled(self.label4.width(), self.label4.height())
        # 在label控件上显示选择的图片
        self.label4.setPixmap(img)

    def setFilePath2(self):
        global content_image_path
        content_image_path, imgType = QtWidgets.QFileDialog.getOpenFileName(self, "选择图片", "",
                                                                            "*.jpg;;*.png;;All Files(*)")
        self.lineEdit2.setText(content_image_path)
        print(content_image_path)
        img = QtGui.QPixmap(content_image_path).scaled(self.label5.width(), self.label5.height())
        # 在label控件上显示选择的图片
        self.label5.setPixmap(img)


def style_image_address():
    style_address = style_image_path
    return style_address


def content_image_address():
    content_address = content_image_path
    return content_address
