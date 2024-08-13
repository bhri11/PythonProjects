import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First PyQt Window")
        self.setGeometry(0, 0, 400, 400)

        label = QLabel(self)
        label.setText("Hello World!")
        label.move(50,50)


        with open("car.png"):
            image_label = QLabel(self)
            pixmap = QPixmap("car.png")
            image_label.setPixmap(pixmap)
            image_label.move(50,0)

        #car name
        name_label = QLabel(self)
        name_label.setText("My Car")
        name_label.setFont(QFont("Arial",20))
        name_label.move(170,170)

        # Engine specs
        engine_label = QLabel(self)
        engine_label.setText("Engine Capacity: 4L TFSI")
        engine_label.setFont(QFont("Arial", 16))
        engine_label.move(20, 210)

        # Features
        features_label = QLabel(self)
        features_label.setText("Features: ABS, EBD, ADAS")
        features_label.setFont(QFont("Arial", 16))
        features_label.move(20, 240)

        # Models
        models_label = QLabel(self)
        models_label.setText("Models: 2.2 Petrol, 1.8 Diesel")
        models_label.setFont(QFont("Arial", 16))
        models_label.move(20, 270)

        # Pricing
        Pricing_label = QLabel(self)
        Pricing_label.setText("$80.000")
        Pricing_label.setFont(QFont("Arial", 16))
        Pricing_label.move(20, 300)


app = QApplication(sys.argv)
window = Window()
window.show()



sys.exit(app.exec())


