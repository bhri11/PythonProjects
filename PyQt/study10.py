import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("My First PyQt Window")
        self.setGeometry(100, 100, 400, 300)

        # label1 = QLabel("Name:")
        # name_edit = QLineEdit()
        #
        # label2 = QLabel("Age:")
        # age_edit = QLineEdit()
        #
        # form_layout = QFormLayout()
        # self.setLayout(form_layout)
        #
        # form_layout.addRow(label1,name_edit)
        # form_layout.addRow(label2,age_edit)

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject","Personal","Business"])

        self.message_edit = QTextEdit()

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_clicked)

        form_layout.addRow(QLabel("Name"),self.name_edit)
        form_layout.addRow(QLabel("Email"), self.email_edit)
        form_layout.addRow(QLabel("Phone Number"), self.phone_edit)
        form_layout.addRow(QLabel("Subject"), self.subject_combo)
        form_layout.addRow(QLabel("Message"), self.message_edit)
        form_layout.addRow(submit_button)


    def submit_clicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone_number = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nSubject: {subject}\nMessage: {message}")



app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())


