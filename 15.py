# QListWidget
# This widget is similar to QComboBox, except options are presented 
# as a scrollable list of items. It also supports selection of multiple 
# items at once. A QListWidget offers an currentItemChanged signal which 
# sends the QListWidgetItem (the element of the list widget), and a 
# currentTextChanged signal which sends the text of the current item

import sys
from PyQt6.QtWidgets import (QApplication, QListWidget, QMainWindow)


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("QListWidget Example");

        widget = QListWidget();
        widget.addItems(["First", "Second", "Third"]);

        # Index changed (New item is selected from the drop down)
        widget.currentItemChanged.connect(self.index_changed);

        # Alternatively
        widget.currentTextChanged.connect(self.text_changed);

        self.setCentralWidget(widget);

    def index_changed(self, i):
        print("Item changed to {}".format(i.text()));

    def text_changed(self, s):
        print("Text changed to : {}".format(s));


app = QApplication(sys.argv)

window = MainWindow();

window.show();

app.exec();

