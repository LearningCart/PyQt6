"""
So far we've seen examples of connecting widget signals to Python methods. When a signal is fired from the widget, our Python method is called and receives the data from the signal. But you don't always need to use a Python function to handle signals -- you can also connect Qt widgets directly to one another.

In the following example, we add a QLineEdit widget and a QLabel to the window. In the \\__init__ for the window we connect our line edit .textChanged signal to the .setText method on the QLabel. Now any time the text changes in the QLineEdit the QLabel will receive that text to it's .setText method.
"""
import sys;

from PyQt6.QtWidgets import QLabel;
from PyQt6.QtWidgets import QWidget;
from PyQt6.QtWidgets import QLineEdit;
from PyQt6.QtWidgets import QVBoxLayout;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QApplication;

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
