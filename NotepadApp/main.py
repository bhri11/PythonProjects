import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 800, 600)


        self.setWindowIcon(QIcon('notepad_icon.png'))

        self.current_file = None
        self.recent_files = []


        self.edit_field = QTextEdit(self)
        self.edit_field.setStyleSheet("font: 16px 'Courier New'; color: #f5f5f5; background-color: #2c3e50; padding: 10px;")
        self.setCentralWidget(self.edit_field)


        menubar = QMenuBar(self)
        menubar.setStyleSheet("background-color: #34495e; color: #ecf0f1; font: 14px 'Segoe UI';")
        menubar.setNativeMenuBar(False)
        self.setMenuBar(menubar)


        fileMenu = QMenu("File", self)
        menubar.addMenu(fileMenu)


        new_action = QAction("New", self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction("Save as", self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_as_file)

        recent_files_menu = fileMenu.addMenu("Recent Files")
        self.recent_files_actions = []
        self.update_recent_files_menu()


        editmenu = QMenu("Edit", self)
        menubar.addMenu(editmenu)


        undo_action = QAction("Undo", self)
        editmenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo", self)
        editmenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction("Cut", self)
        editmenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        paste_action = QAction("Paste", self)
        editmenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        copy_action = QAction("Copy", self)
        editmenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        find_action = QAction("Find", self)
        editmenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)


        formatmenu = QMenu("Format", self)
        menubar.addMenu(formatmenu)

        bold_action = QAction("Bold", self)
        formatmenu.addAction(bold_action)
        bold_action.triggered.connect(self.make_bold)

        italic_action = QAction("Italic", self)
        formatmenu.addAction(italic_action)
        italic_action.triggered.connect(self.make_italic)

        underline_action = QAction("Underline", self)
        formatmenu.addAction(underline_action)
        underline_action.triggered.connect(self.make_underline)


        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


        word_count_action = QAction("Word Count", self)
        editmenu.addAction(word_count_action)
        word_count_action.triggered.connect(self.word_count)

    def new_file(self):
        self.edit_field.clear()
        self.current_file = None
        self.statusBar.showMessage("New file created", 2000)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);; Python File (*.py)")
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.edit_field.setText(text)
                self.current_file = file_path

    def save_as_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);; Python File (*.py)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.edit_field.toPlainText())
            self.current_file = file_path

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.edit_field.toPlainText())
            self.statusBar.showMessage(f"File saved: {self.current_file}", 2000)
        else:
            self.save_as_file()

    def find_text(self):
        search_text, ok = QInputDialog.getText(self, "Find text", "Search for:")
        if ok:
            all_words = []
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = QColor(Qt.GlobalColor.yellow)

            while self.edit_field.find(search_text):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)
                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)
            self.edit_field.setExtraSelections(all_words)
            self.statusBar.showMessage(f"Found {len(all_words)} occurrence(s) of '{search_text}'", 2000)

    def make_bold(self):
        fmt = self.edit_field.currentCharFormat()
        fmt.setFontWeight(QFont.Weight.Bold if not fmt.font().bold() else QFont.Weight.Normal)
        self.edit_field.setCurrentCharFormat(fmt)

    def make_italic(self):
        fmt = self.edit_field.currentCharFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        self.edit_field.setCurrentCharFormat(fmt)

    def make_underline(self):
        fmt = self.edit_field.currentCharFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        self.edit_field.setCurrentCharFormat(fmt)

    def word_count(self):
        text = self.edit_field.toPlainText()
        words = text.split()
        num_words = len(words)
        self.statusBar.showMessage(f"Word Count: {num_words}", 2000)

    def add_to_recent_files(self, file_path):
        if file_path not in self.recent_files:
            self.recent_files.append(file_path)
            if len(self.recent_files) > 5:
                self.recent_files.pop(0)
        self.update_recent_files_menu()

    def update_recent_files_menu(self):
        for action in self.recent_files_actions:
            self.sender().menu().removeAction(action)
        self.recent_files_actions.clear()

        for file_path in self.recent_files:
            action = QAction(file_path, self)
            action.triggered.connect(lambda _, path=file_path: self.open_recent_file(path))
            self.recent_files_actions.append(action)
            self.sender().menu().addAction(action)

    def open_recent_file(self, file_path):
        with open(file_path, "r") as file:
            text = file.read()
            self.edit_field.setText(text)
            self.current_file = file_path
        self.statusBar.showMessage(f"Opened recent file: {file_path}", 2000)


app = QApplication(sys.argv)


app.setStyle('Fusion')
dark_palette = QPalette()
dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
dark_palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
app.setPalette(dark_palette)

window = Window()
window.show()

sys.exit(app.exec())
