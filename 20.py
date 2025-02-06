# File for all the programs releated to layout.,
import sys
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout);
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QDial, QPushButton, QCheckBox);

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
        
        # You can set the spacing around the layout using .setContentMargins
        # or set the spacing between elements using .setSpacing:
        masterlayout.setContentsMargins(40,20,20,20)
        masterlayout.setSpacing(30)

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


class MainWindowGridLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QGridLayout()
        
        widget = QPushButton("Press it!");
        layout.addWidget(widget, 0, 3);

        widget = QDial();
        widget.setRange(0, 100);
        widget.setSingleStep(1);
        layout.addWidget(widget, 1, 1);

        widget = QCheckBox();
        layout.addWidget(widget, 2, 0);

        widget = QLineEdit();
        widget.setMaxLength(20);
        widget.setPlaceholderText("Enter Your Text Here");
        layout.addWidget(widget, 3, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainWindowStackedLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QStackedLayout()

        btn = QPushButton("Press it!");

        dial = QDial();
        dial.setRange(0, 100);
        dial.setSingleStep(1);

        chkbx = QCheckBox();

        line = QLineEdit();
        line.setMaxLength(20);
        line.setPlaceholderText("Enter Your Text Here");

        layout.addWidget(btn);
        layout.addWidget(dial);
        layout.addWidget(chkbx);
        layout.addWidget(line);

        # Changing index will change the stacking order
        # Different widget will be on the top.
        layout.setCurrentIndex(1) 

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindowStackedLayout()
window.show()
app.exec()

