# QComboBox
# The QComboBox is a drop down list, closed by default with an arrow to open it. 
# You can select a single item from the list, with the currently selected item 
# being shown as a label on the widget. The combo box is suited to selection of 
# a choice from a long list of options.

# You can add items to a QComboBox by passing a list of strings to .addItems().
# Items will be added in the order they are provided.


import sys
from PyQt6.QtWidgets import (QApplication, QComboBox, QMainWindow)


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("QComboBox Example");

        widget = QComboBox();
        # TODO: Pull it from GUI config XML (Multilingual?)
        widget.addItems(["First", "Second", "Third"]);

        # Index changed (New item is selected from the drop down)
        widget.currentIndexChanged.connect(self.index_changed);

        # Alternatively
        widget.currentTextChanged.connect(self.text_changed);

        # Do try this at home ;) 
        # Enable below and you should be able to add new items., 
        # TODO: find practical use case and use "edit" QPushButton
        # to enable or disable editing of the QComboBox!
        """
        QComboBox can also be editable, allowing users to enter values not currently in the list
        and either have them inserted, or simply used as a value. To make the box editable:

        python
        widget.setEditable(True)
        You can also set a flag to determine how the insert is handled. 
        These flags are stored on the QComboBox class itself and are listed below:

        PyQt6 flag (long name)	Behavior
        QComboBox.InsertPolicy.NoInsert	No insert
        QComboBox.InsertPolicy.InsertAtTop	Insert as first item
        QComboBox.InsertPolicy.InsertAtCurrent	Replace currently selected item
        QComboBox.InsertPolicy.InsertAtBottom	Insert after last item
        QComboBox.InsertPolicy.InsertAfterCurrent	Insert after current item
        QComboBox.InsertPolicy.InsertBeforeCurrent	Insert before current item
        QComboBox.InsertPolicy.InsertAlphabetically	Insert in alphabetical order
        To use these, apply the flag as follows:

        python
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        You can also limit the number of items allowed in the box by using .setMaxCount, e.g:

        python
        widget.setMaxCount(10)
        """
        widget.setEditable(True);
        widget.setMaxCount(5); # We can have max 5 items

        self.setCentralWidget(widget);

    def index_changed(self, i):
        print("Index changed to {}".format(i));

    def text_changed(self, s):
        print("Text changed to : {}".format(s));


app = QApplication(sys.argv)

window = MainWindow();

window.show();

app.exec();

