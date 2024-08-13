import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQt Window")
        self.setGeometry(0, 0, 400, 400)

        button = QPushButton("Show Messagebox",self)
        button.setGeometry(150,80,200,40)
        button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box title")
        msg.setText("This is a simple message box")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok )
        result = msg.exec()

        if result == QMessageBox.StandardButton.Ok:
            print("Ok button is clicked")
        elif result == QMessageBox.StandardButton.Cancel:
            print("Cancel button is clicked")


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())


