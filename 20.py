# File for all the programs releated to layout.,
import sys
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout);
from PyQt6.QtGui     import (QColor, QPalette);
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QDial);

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        masterlayout = QHBoxLayout();
        layout = QVBoxLayout()

        # Create empty list and keep appending QLineEdit widget in list.
        lines = [];
        for i in range (3):
            lines.append(QLineEdit());
            # You can set a maximum length for the text in a line edit.
            lines[i].setMaxLength(20);
            lines[i].setPlaceholderText("Your Text {}".format(i));
            # Triggered when you hit enter., 
            lines[i].returnPressed.connect (self.line_edited);
            # Lets add widget to the layout., 
            layout.addWidget(lines[i]);
        
        # Add this layout to master layout:
        masterlayout.addLayout(layout);

        # Now create layout of verticle dials and add them to master layout
        layout2 = QVBoxLayout()
        dials = [];
        for i in range (3):
            dials.append(QDial());
            dials[i].setRange(0, 100);
            dials[i].setSingleStep(1);
            # Triggered when you hit enter., 
            dials[i].sliderMoved.connect(self.slider_position);
            # Lets add widget to the layout., 
            layout2.addWidget(dials[i]);

        # Add this layout to master layout:
        masterlayout.addLayout(layout2);

        # Lets add layout to dummy widget so that layout becomes 
        # central widget of QMainWindow
        widget = QWidget()
        widget.setLayout(masterlayout)
        self.setCentralWidget(widget)

    def line_edited(self):
        print("Return pressed!");

    def slider_position(self, p):
        print("Position changed to {}".format(p));



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

