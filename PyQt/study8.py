import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import math

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQt Window")
        self.setGeometry(0, 0, 400, 400)

        number_label = QLabel("Enter a number",self)
        number_label.move(20,20)

        self.number_input = QLineEdit(self)
        self.number_input.move(200,20)

        calculate_button = QPushButton("Find Root",self)
        calculate_button.move(200,60)

        self.result_label = QLabel("Result: ",self)
        self.result_label.move(20,100)


        calculate_button.clicked.connect(self.calculate_sqrt)

    def calculate_sqrt(self):
        try:
            number = float(self.number_input.text())
            num_sqrt = math.sqrt(number)
            if num_sqrt.is_integer():
                self.result_label.setText(f"Result: {num_sqrt}")
            else:
                msg = QMessageBox.warning(self,"Not a perfect square", "The number is not a perfect square")
        except ValueError:
            msg = QMessageBox.warning(self, "Invalid Input", "Please enter a valid input")


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())


