# File for all the programs releated to layout.,
import sys
from PyQt6.QtWidgets import QHBoxLayout;
from PyQt6.QtGui     import QColor, QPalette;
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit);


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)



# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#         widget = Color("red")
#         self.setCentralWidget(widget);

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QHBoxLayout()

        # layout.addWidget(Color("black"))
        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("orange"))
        # layout.addWidget(Color("blue"))

        # Create empty list and keep appending QLineEdit widget in list.
        lines = [];
        for i in range (5):
            lines.append(QLineEdit());
            # You can set a maximum length for the text in a line edit.
            lines[i].setMaxLength(20);
            lines[i].setPlaceholderText("Your Text {}".format(i));
            # Triggered when you hit enter., 
            lines[i].returnPressed.connect (self.line_edited);
        
        # Lets add them to layout., 
        for i in range(5):
            layout.addWidget(lines[i]);

        # Lets add layout to dummy widget so that layout becomes 
        # central widget of QMainWindow
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def line_edited(self):
        print("Return pressed!");

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

