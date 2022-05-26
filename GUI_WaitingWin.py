import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib import pyplot as plt

import GUI_ResultShowWin
import Process

'''
设置等待窗口
'''


class WaitingWin(QWidget):
    def __init__(self, style_addr, content_addr):
        super(WaitingWin, self).__init__()
        self.ViewResult = None
        self.initUI()
        self.resize(200, 200)
        self.setWindowTitle('GUI_WaitingWin')
        self.style_image_address = style_addr
        self.content_image_address = content_addr
        self.show()
        threading.Thread(target=self.start, daemon=True).start()

    def start(self):
        value = Process.output()
        value.clamp_(0, 1)
        Process.img_show(value, title="Output Image")
        plt.savefig("./result_figure/final_figure.jpg")
        Process.loss_figure_output()
        self.button2.setEnabled(True)
        self.label2.setText("转换成功！单击View Result以查看结果")

    def initUI(self):
        label1 = QLabel(self)
        label1.setText('转换过程可能需要花费您几分钟，请稍等')

        self.label2 = QLabel()
        self.label2.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText('Quit Transfer')
        self.button1.clicked.connect(self.onClick_Quit_Button)
        hbox.addWidget(self.button1)

        self.button2 = QPushButton()
        self.button2.setText('View Result')
        self.button2.clicked.connect(self.onClick_Continue_Button)
        self.button2.setEnabled(False)
        hbox.addWidget(self.button2)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch(1)
        vbox.addWidget(self.label2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def onClick_Continue_Button(self):
        print(self.label2.text())
        if self.label2.text() != "":
            self.ViewResult = GUI_ResultShowWin.ResultShowWin()
            self.hide()
            self.ViewResult.show()

    def onClick_Quit_Button(self):
        app = QApplication.instance()
        app.quit()
