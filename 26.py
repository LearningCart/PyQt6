# QMessageBox
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

"""
Built in QMessageBox dialogs
To make things even simpler the QMessageBox has a number of methods which can be used
 to construct these types of message dialog. These methods are shown below --

python
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)
The parent parameter is the window which the dialog will be a child of. If you're 
launching your dialog from your main window, you can just pass in self.
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();

        self.setWindowTitle("My App");
        self.setFixedSize(720, 480);

        button = QPushButton("Press me for a dialog!");
        # button_clicked, button_clickedyn, button_clickedquestion, button_clickedcritical
        button.clicked.connect(self.button_clickedcritical);
        self.setCentralWidget(button);

    def button_clicked(self, s):
        dlg = QMessageBox(self);
        dlg.setWindowTitle("I have a question!");
        dlg.setText("This is a simple dialog");
        button = dlg.exec();

        if button == QMessageBox.StandardButton.Ok:
            print("OK!");

    def button_clickedyn(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")

    def button_clickedquestion(self, s):
        button = QMessageBox.question(
            self,
            "Question dialog",
            "The longer message"
        );

        if button == QMessageBox.StandardButton.Yes:
            print("Yes!");
        else:
            print("No!");

    def button_clickedcritical(self, s):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.StandardButton.Discard
            | QMessageBox.StandardButton.NoToAll
            | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )

        if button == QMessageBox.StandardButton.Discard:
            print("Discard!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
