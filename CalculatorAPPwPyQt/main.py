import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import math

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 500)

        self.setStyleSheet("background-color: #2C3E50; color: white;")

        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.ans = "0"

        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("font: 24px Arial; padding: 15px; background-color: #34495E; border: none;")
        layout.addWidget(self.display, 0, 0, 1, 6)


        operators = ["+", "-", "*", "/", "%", "(", ")"]
        operator_buttons = [QPushButton(str(op)) for op in operators]
        for button in operator_buttons:
            button.setStyleSheet("font: 18px Arial; padding: 20px; background-color: #E74C3C; border-radius: 10px;")
            button.clicked.connect(self.operator_button_clicked)

        functions = ["sin", "cos", "tan", "ln", "log", "√", "x^y", "!", "π", "e", "EXP", "Ans"]
        function_buttons = [QPushButton(str(func)) for func in functions]
        for button in function_buttons:
            button.setStyleSheet("font: 18px Arial; padding: 20px; background-color: #BDC3C7; border-radius: 10px;")
            button.clicked.connect(self.function_button_clicked)

        buttons = [QPushButton(str(i)) for i in range(0, 10)]
        for button in buttons:
            button.setStyleSheet("font: 18px Arial; padding: 20px; background-color: #1ABC9C; border-radius: 10px;")
            button.clicked.connect(self.number_button_clicked)

        decimal_button = QPushButton(".")
        decimal_button.setStyleSheet("font: 18px Arial; padding: 20px; background-color: #1ABC9C; border-radius: 10px;")
        decimal_button.clicked.connect(self.number_button_clicked)

        self.equal_button = QPushButton("=")
        self.equal_button.setStyleSheet("font: 18px Arial; padding: 20px; background-color: #F39C12; border-radius: 10px;")
        self.equal_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("AC")
        self.clear_button.setStyleSheet("font: 18px Arial; padding: 20px; background-color: #95A5A6; border-radius: 10px;")
        self.clear_button.clicked.connect(self.clear)

        layout.addWidget(self.clear_button, 1, 6)   # AC
        layout.addWidget(function_buttons[0], 2, 1)  # sin
        layout.addWidget(function_buttons[1], 3, 1)  # cos
        layout.addWidget(function_buttons[2], 4, 1)  # tan
        layout.addWidget(function_buttons[3], 2, 2)  # ln
        layout.addWidget(function_buttons[4], 3, 2)  # log

        layout.addWidget(function_buttons[5], 4, 2)  # √
        layout.addWidget(function_buttons[6], 5, 2)  # x^y
        layout.addWidget(function_buttons[7], 1, 2)  # !
        layout.addWidget(function_buttons[8], 3, 0)  # π
        layout.addWidget(function_buttons[9], 4, 0)  # e
        layout.addWidget(function_buttons[10], 5, 1)  # EXP

        layout.addWidget(operator_buttons[4], 1, 5)  # %
        layout.addWidget(operator_buttons[5], 1, 3)  # (
        layout.addWidget(operator_buttons[6], 1, 4)  # )
        layout.addWidget(buttons[7], 2, 3)  # 7
        layout.addWidget(buttons[8], 2, 4)  # 8
        layout.addWidget(buttons[9], 2, 5)  # 9
        layout.addWidget(operator_buttons[0], 5, 6)  # +

        layout.addWidget(buttons[4], 3, 3)  # 4
        layout.addWidget(buttons[5], 3, 4)  # 5
        layout.addWidget(buttons[6], 3, 5)  # 6
        layout.addWidget(operator_buttons[1], 4, 6)  # -

        layout.addWidget(buttons[1], 4, 3)  # 1
        layout.addWidget(buttons[2], 4, 4)  # 2
        layout.addWidget(buttons[3], 4, 5)  # 3
        layout.addWidget(operator_buttons[2], 3, 6)  # *

        layout.addWidget(buttons[0], 5, 3)  # 0
        layout.addWidget(decimal_button, 5, 4)  # .
        layout.addWidget(operator_buttons[3], 2, 6)  # /
        layout.addWidget(self.equal_button, 5, 5)  # =
        layout.addWidget(function_buttons[11], 5, 0)  # Ans

    def number_button_clicked(self):
        digit = self.sender().text()

        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit

        self.display.setText(self.current_input)

    def operator_button_clicked(self):
        operator = self.sender().text()
        if operator in ["+", "-", "*", "/", "%", "(", ")"]:
            if self.current_operator == "":
                self.current_operator = operator
                self.previous_input = self.current_input
                self.current_input = "0"
            else:
                self.calculate()
                self.current_operator = operator
                self.previous_input = self.current_input
                self.current_input = "0"

    def function_button_clicked(self):
        func = self.sender().text()
        try:
            if func == "sin":
                result = math.sin(math.radians(float(self.current_input)))
            elif func == "cos":
                result = math.cos(math.radians(float(self.current_input)))
            elif func == "tan":
                result = math.tan(math.radians(float(self.current_input)))
            elif func == "ln":
                result = math.log(float(self.current_input))
            elif func == "log":
                result = math.log10(float(self.current_input))
            elif func == "√":
                result = math.sqrt(float(self.current_input))
            elif func == "x^y":
                self.previous_input = self.current_input
                self.current_operator = "**"
                self.current_input = "0"
                return
            elif func == "!":
                result = math.factorial(int(self.current_input))
            elif func == "π":
                result = math.pi
            elif func == "e":
                result = math.e
            elif func == "EXP":
                result = math.exp(float(self.current_input))
            elif func == "Ans":
                result = self.ans

            self.current_input = str(result)
            self.display.setText(self.current_input)
        except Exception as e:
            self.display.setText("Error")
            self.current_input = "0"

    def calculate(self):
        try:
            if self.current_operator == "+":
                result = float(self.previous_input) + float(self.current_input)
            elif self.current_operator == "-":
                result = float(self.previous_input) - float(self.current_input)
            elif self.current_operator == "*":
                result = float(self.previous_input) * float(self.current_input)
            elif self.current_operator == "/":
                if self.current_input == "0":
                    result = "Error"
                else:
                    result = float(self.previous_input) / float(self.current_input)
            elif self.current_operator == "%":
                result = float(self.previous_input) % float(self.current_input)
            elif self.current_operator == "**":
                result = float(self.previous_input) ** float(self.current_input)
            else:
                result = self.current_input

            self.display.setText(str(result))
            self.ans = str(result)
            self.current_input = str(result)
            self.current_operator = ""
        except Exception as e:
            self.display.setText("Error")
            self.current_input = "0"
            self.current_operator = ""

    def clear(self):
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.display.setText(self.current_input)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
