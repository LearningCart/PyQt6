# QSpinBox and QDoubleSpinBox 
# QSpinBox provides a small numerical input box with arrows to 
# increase and decrease the value.
# QSpinBox supports integers while the related widget 
# QDoubleSpinBox supports floats.



import sys
from PyQt6.QtWidgets import (QApplication, QSpinBox, QMainWindow)

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("QSpinBox Example");
        self.setFixedSize(720,480);

        widget = QSpinBox();
        
        widget.setMinimum(0);
        widget.setMaximum(+100);

        # widget.setPrefix("₹") # Add prefix optional?
        # widget.setSuffix(" ₹"); # Add suffix optional?
        widget.setSuffix(" $"); # could not print ₹, using $
        widget.setSingleStep(5)  # Or e.g. 3.0 for QDoubleSpinBox

        # Enbale below you don't want user to manually change it.
        # After enabling it, It will change as per range set by 
        # set<Mini/Maxi>mum or setRange
        # and step size only setSingleStep( step size)
        widget.lineEdit().setReadOnly(True);

        # Connect signals to respective slots in this class
        widget.valueChanged.connect(self.value_changed);
        widget.textChanged.connect (self.text_changed);

        self.setCentralWidget(widget);
    
        

    # Event handlers
    # NOTE: Both QSpinBox and QDoubleSpinBox have a .valueChanged signal 
    # that fires whenever their value is altered. The raw .valueChanged signal 
    # sends the numeric value (either an int or a float), while .textChanged 
    # sends the value as a string, including both the prefix and suffix characters.

    def value_changed(self, i):
        print("Value changed: {}".format(i));

    def text_changed(self, s):
        print("Text changed: {}".format(s));

app = QApplication(sys.argv)

window = MainWindow();

window.show();

app.exec();

