# In Qt toolbars are created from the QToolBar class. 
# To start you create an instance of the class and then call .addToolbar 
# on the QMainWindow. Passing a string in as the first parameter to 
# QToolBar sets the toolbar's name, which will be used to identify 
# the toolbar in the UI.

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();

        self.setWindowTitle("My Awesome App");

        label = QLabel("Test");
        label.setAlignment(Qt.AlignmentFlag.AlignCenter);
        self.setCentralWidget(label);

        toolbar = QToolBar("My main toolbar");
        self.addToolBar(toolbar);

    
    def onMyToolBarButtonClick(self, s):
        print("click", s);

app = QApplication(sys.argv);
w   = MainWindow();

w  .show();
app.exec();
