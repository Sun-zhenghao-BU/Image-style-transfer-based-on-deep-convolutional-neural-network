from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import ImageQt
import GUI_FirstWin

'''
设置结果显示窗口
'''


class ResultShowWin(QWidget):
    def __init__(self):
        super(ResultShowWin, self).__init__()
        self.FirstWin = None
        self.setWindowTitle('GUI_ResultShowWin')
        self.resize(700, 700)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.label1 = QLabel()
        self.label2 = QLabel()
        label3 = QLabel(self)
        label4 = QLabel(self)
        label5 = QLabel(self)
        label6 = QLabel(self)

        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()

        # 输出的风格化图片
        self.label1.setFixedSize(480, 320)
        self.label1.setStyleSheet("QLabel{background:white;}")
        figure1_path = "./result_figure/final_figure.jpg"
        img = QPixmap(figure1_path).scaled(self.label1.width(), self.label1.height())
        self.label1.setPixmap(img)

        label5.setText('风格化输出图像显示')
        label5.setAlignment(Qt.AlignCenter)

        vbox1.addWidget(self.label1)
        vbox1.addWidget(label5)

        vbox2 = QVBoxLayout()
        # 绘制折线堆叠损失曲线
        self.label2.setFixedSize(480, 320)
        self.label2.setStyleSheet("QLabel{background:white;}")
        figure2_path = "./result_figure/loss_figure.jpg"
        img = QPixmap(figure2_path).scaled(self.label2.width(), self.label2.height())
        self.label2.setPixmap(img)
        label6.setText('损失函数折线图')
        label6.setAlignment(Qt.AlignCenter)

        vbox2.addWidget(self.label2)
        vbox2.addWidget(label6)

        hbox1.addLayout(vbox1)
        hbox1.addStretch(1)
        hbox1.addLayout(vbox2)

        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(QFont('Arial', 20))
        label3.setText('最终转换结果')

        label4.setOpenExternalLinks(True)
        label4.setText(
            "<a href='https://github.com/Sun-zhenghao-BU/Image-style-transfer-based-on-deep-convolutional-neural-network'>《访问我的Github以了解更多》</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        label6.setText('损失函数折线图')

        hbox2 = QHBoxLayout()
        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()

        self.button1.setText('Save Output Image')
        self.button1.resize(200,100)
        self.button1.clicked.connect(self.onClick_Save_Button)
        '''
        文件命名及即保存
        '''

        self.button2.setText('Transfer Again')
        self.button2.resize(200, 1000)
        self.button2.clicked.connect(self.onClick_Again_Button)

        self.button3.setText('Quit')
        self.button3.resize(200, 100)
        self.button3.clicked.connect(self.onClick_Quit_Button)

        hbox2.addWidget(self.button1)

        hbox2.addWidget(self.button2)

        hbox2.addWidget(self.button3)

        vbox.addWidget(label3)
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addStretch(3)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addWidget(label4)

        self.setLayout(vbox)

    def onClick_Save_Button(self):
        # 提取Qlabel中的图片
        img1 = ImageQt.fromqpixmap(self.label1.pixmap())
        img2 = ImageQt.fromqpixmap(self.label2.pixmap())
        fpath= QFileDialog.getExistingDirectory(self, 'Select Folder')
        img1.save(f"{fpath}/final_figure.jpg")
        img2.save(f"{fpath}/loss_figure.jpg")

    def onClick_Again_Button(self):
        self.hide()
        self.FirstWin = GUI_FirstWin.Generator()
        self.FirstWin.show()

    def onClick_Quit_Button(self):
        app = QApplication.instance()
        app.quit()

