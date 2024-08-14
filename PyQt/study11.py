import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 400, 300)

        # combo_box = QComboBox()
        # combo_box.addItems(["Label","Form"])
        # combo_box.activated.connect(self.change_page)
        #
        # label = QLabel("This is the label page")
        #
        # form = QFormLayout()
        # form.addRow("", QLabel("This is a form page"))
        # page2_container = QWidget()
        # page2_container.setLayout(form)
        #
        # self.stacked_layout = QStackedLayout()
        # self.stacked_layout.addWidget(label)
        # self.stacked_layout.addWidget(page2_container)
        #
        #
        # main_layout = QVBoxLayout()
        # main_layout.addWidget(combo_box)
        # main_layout.addLayout(self.stacked_layout)
        #
        # self.setLayout(main_layout)

        # #Step 1: Create a menubar
        # menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        #
        #
        # #creating the menu icons
        # file_menu = menubar.addMenu("File")
        #
        # #creating an action
        # self.new_action = QAction("New")
        #
        # #adding action to the menu
        # file_menu.addAction(self.new_action)
        #
        # file_menu.addSeparator()
        #
        # self.exit_action = QAction("Exit")
        # file_menu.addAction(self.exit_action)
        #
        # edit_menu = menubar.addMenu("Edit")
        #
        # self.cut_action = QAction("Cut")
        # edit_menu.addAction(self.cut_action)
        #
        # self.copy_action = QAction("Copy")
        # edit_menu.addAction(self.copy_action)
        #
        # self.paste_action = QAction("Paste")
        # edit_menu.addAction(self.paste_action)


        toolbar = self.addToolBar("Main Toolbar")
        self.new_action = QAction(QIcon("icons/new.png"), "New")
        toolbar.addAction(self.new_action)

        self.open_action = QAction(QIcon("icons/open.png"), "Open")
        toolbar.addAction(self.open_action)

        toolbar.addSeparator()

        self.save_action = QAction(QIcon("icons/save.png"), "Save")
        toolbar.addAction(self.save_action)





    def change_page(self,index):
        self.stacked_layout.setCurrentIndex(index)





app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())


