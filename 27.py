# Multiple window
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys
from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        self.label.setFixedSize(720,480);
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 480);
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    # However, what happens if you click the button again? 
    # The window will be re-created! This new window will 
    # replace the old in the self.w variable, and – because 
    # there is now no reference to it – the previous window 
    # will be destroyed.

    def show_new_window(self, checked):
        # Note: These are local variables, it will be distroyed as soon as 
        # function is over hence, the second window will appear just for a fraction of seconds
        # Fixing it reequires making w persistent  
        # w = AnotherWindow()
        # w.show()
        self.w = AnotherWindow();
        self.w.show();


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
