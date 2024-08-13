import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import math

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("My First PyQt Window")
        self.setGeometry(0, 0, 400, 400)

        # label = QLabel("Name")
        # name = QLineEdit()
        # button = QPushButton("Add")
        #
        # layout = QVBoxLayout()
        # layout.addWidget(label)
        # layout.addWidget(name)
        # layout.addWidget(button)
        #
        # self.setLayout(layout)

        # button1 = QPushButton("button1")
        # button2 = QPushButton("button2")
        # button3 = QPushButton("button3")
        # button4 = QPushButton("button4")
        #
        # hbox1 = QHBoxLayout()
        # hbox1.addWidget(button1)
        # hbox1.addWidget(button2)
        #
        # hbox2 = QHBoxLayout()
        # hbox2.addWidget(button3)
        # hbox2.addWidget(button4)
        #
        # vbox = QVBoxLayout()
        # vbox.addLayout(hbox1)
        # vbox.addLayout(hbox2)
        #
        # self.setLayout(vbox)

        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
        button3 = QPushButton("button3")

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(label1,0,0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)
        layout.addWidget(button1, 1, 0)
        layout.addWidget(button2, 1, 1)
        layout.addWidget(button3, 1, 2)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())


