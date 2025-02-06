# QDialog
import sys
from PyQt6.QtWidgets import (QVBoxLayout);
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QLabel, QDialogButtonBox

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();

        self.setWindowTitle("My App");
        self.setFixedSize(720,480);
        button = QPushButton("Press me for a dialog!");
        button.clicked.connect(self.button_clicked);
        self.setCentralWidget(button);

    # def button_clicked(self, s):
    #     print("click", s);

    #     dlg = QDialog(self);
    #     dlg.setWindowTitle("Hollow World!");
    #     dlg.exec();

    def button_clicked(self, s):
        print("click", s)
        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
