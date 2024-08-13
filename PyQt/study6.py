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

        #Total cost of coffe
        self.total_cost = 0

        label = QLabel(self)
        label.setText("Select you options")
        label.resize(200,20)
        label.move(20,20)

        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText("Sugar($ 0.5)")
        sugar_checkbox.move(20,40)
        sugar_checkbox.toggled.connect(self.sugar_checked)

        milk_checkbox = QCheckBox(self)
        milk_checkbox.setText("Milk($ 1)")
        milk_checkbox.move(20,60)
        milk_checkbox.toggled.connect(self.milk_checked)

        self.cost_label = QLabel(self)
        self.cost_label.setText("Total Cost os $0")
        self.cost_label.resize(200,20)
        self.cost_label.move(20,90)

    def sugar_checked(self,checked):
        if checked:
            self.total_cost += 0.5
        else:
            self.total_cost -= 0.5

        self.cost_label.setText(f"Total Cost os ${self.total_cost}")

    def milk_checked(self,checked):
        if checked:
            self.total_cost += 1
        else:
            self.total_cost -= 1

        self.cost_label.setText(f"Total Cost os ${self.total_cost}")


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())


