import os.path

from PyQt6.QtWidgets import *
import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(600, 600)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)
        self.drawing = False
        self.last_mouse_position = QPoint()
        self.status_label = QLabel()

        self.eraser = False
        self.pen_color = Qt.GlobalColor.black
        self.pen_width = 2
        self.undo_stack = []
        self.redo_stack = []

    def mouseMoveEvent(self, event):
        mouse_position = event.pos()
        status_text = f"Mouse coordinates: {mouse_position.x()}, {mouse_position.y()}"
        self.status_label.setText(status_text)
        self.parent.statusBar.addWidget(self.status_label)
        if event.buttons() & Qt.MouseButton.LeftButton and self.drawing:
            self.draw(mouse_position)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_mouse_position = event.pos()
            self.drawing = True
            self.undo_stack.append(self.pixmap.copy())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def draw(self, points):
        painter = QPainter(self.pixmap)
        if not self.eraser:
            pen = QPen(self.pen_color, self.pen_width)
            painter.setPen(pen)
            painter.drawLine(self.last_mouse_position, points)
            self.last_mouse_position = points
        else:
            eraser = QRect(points.x(), points.y(), 12, 12)
            painter.eraseRect(eraser)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        target_rect = event.rect()
        painter.drawPixmap(target_rect, self.pixmap, target_rect)
        painter.end()

    def selectTool(self, tool):
        if tool == "pencil":
            self.pen_width = 2
            self.eraser = False
        elif tool == "marker":
            self.pen_width = 4
            self.eraser = False
        elif tool == "color":
            self.eraser = False
            color = QColorDialog.getColor()
            if color.isValid():
                self.pen_color = color
        elif tool == "eraser":
            self.eraser = True

    def new(self):
        self.pixmap.fill(Qt.GlobalColor.white)
        self.update()

    def save(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", "", "PNG Files (*.png);;JPEG Files (*.jpg)", options=options)
        if file_name:
            self.pixmap.save(file_name)

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.pixmap.copy())
            self.pixmap = self.undo_stack.pop()
            self.update()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.pixmap.copy())
            self.pixmap = self.redo_stack.pop()
            self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Enhanced Paint App")

        # Creating canvas
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Adding toolbar
        tool_bar = QToolBar("Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)
        tool_bar.setMovable(False)

        pencil_act = QAction(QIcon("icons/pencil.png"), "Pencil", tool_bar)
        pencil_act.triggered.connect(lambda: self.canvas.selectTool("pencil"))
        marker_act = QAction(QIcon("icons/brush.png"), "Marker", tool_bar)
        marker_act.triggered.connect(lambda: self.canvas.selectTool("marker"))
        eraser_act = QAction(QIcon("icons/eraser.png"), "Eraser", tool_bar)
        eraser_act.triggered.connect(lambda: self.canvas.selectTool("eraser"))
        color_act = QAction(QIcon("icons/colors.png"), "Colors", tool_bar)
        color_act.triggered.connect(lambda: self.canvas.selectTool("color"))
        undo_act = QAction(QIcon("icons/undo.png"), "Undo", tool_bar)
        undo_act.triggered.connect(self.canvas.undo)
        redo_act = QAction(QIcon("icons/redo.png"), "Redo", tool_bar)
        redo_act.triggered.connect(self.canvas.redo)

        tool_bar.addAction(pencil_act)
        tool_bar.addAction(marker_act)
        tool_bar.addAction(eraser_act)
        tool_bar.addAction(color_act)
        tool_bar.addAction(undo_act)
        tool_bar.addAction(redo_act)

        self.new_act = QAction("New")
        self.new_act.triggered.connect(self.canvas.new)
        self.save_file_act = QAction("Save")
        self.save_file_act.triggered.connect(self.canvas.save)
        self.quit_act = QAction("Exit")
        self.quit_act.triggered.connect(self.close)

        self.menuBar().setNativeMenuBar(False)
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_act)
        file_menu.addAction(self.save_file_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        settings_menu = self.menuBar().addMenu("Settings")
        resize_act = QAction("Resize Canvas", self)
        resize_act.triggered.connect(self.resize_canvas)
        settings_menu.addAction(resize_act)

    def resize_canvas(self):
        size, ok = QInputDialog.getInt(self, "Resize Canvas", "Enter new canvas size (width = height):", 600, 100, 2000, 50)
        if ok:
            self.canvas.pixmap = QPixmap(size, size)
            self.canvas.pixmap.fill(Qt.GlobalColor.white)
            self.canvas.update()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
