import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication;
from PyQt6.QtWidgets import QLabel;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QTextEdit;


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        print("mouseMoveEvent");

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
        print("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
        print("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
        print("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

