import sys;
from PyQt6.QtWidgets import QApplication;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QPushButton;

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")

app = QApplication(sys.argv);

win = MainWindow();
win.show();

app.exec();