# QLineEdit
# QLineEdit widget is a simple single-line text editing box, 
# into which users can type input. These are used for form fields, 
# or settings where there is no restricted list of valid inputs. 
# For example, when entering an email address, or computer name:

# The QLineEdit has a number of signals available for different editing
# events including when return is pressed (by the user), when the user 
# selection is changed. There are also two edit signals, one for when 
# the text in the box has been edited and one for when it has been changed. 
# The distinction here is between user edits and programmatic changes. 
# The textEdited signal is only sent when the user edits text.


import sys
from PyQt6.QtWidgets import (QApplication, QLineEdit, QMainWindow)


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("QListWidget Example");

        widget = QLineEdit();
        # You can set a maximum length for the text in a line edit.
        widget.setMaxLength(20);

        widget.setPlaceholderText("Enter your suggestions here.,");
        # widget.setReadOnly(True) # uncomment this to make readonly

        # Triggered when you hit enter., 
        widget.returnPressed.connect   (self.return_pressed);

        # When you select text from the line edit., each char. selected will generate this event
        # if you select control + A, only one event is generated for entire text selected.,
        # or if you select range of text with control + mouse, it will generate one event for 
        # the selected text.
        widget.selectionChanged.connect(self.selection_changed);

        # When text is chagned!, 
        # (Enen entering text will generate one event for each character)
        widget.textChanged.connect     (self.text_changed);

        # When "USER" chagnes the text., 
        widget.textEdited.connect      (self.text_edited);


        # Additionally, it is possible to perform input validation using an input mask
        # to define which characters are supported and where.
        # This can be applied to the field as follows:
        # widget.setInputMask('000.000.000.000;_') # Enable this line to test filter
        # The above would allow a series of 3-digit numbers separated with periods, 
        # and could therefore be used to validate IPv4 addresses.
        # TODO: Find more practical examples., 

        # Trying for mbile number
        # widget.setInputMask('+xx xxxxxxxxxx;_')
        self.setCentralWidget(widget);


    # Event handlers
    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed!");
        print(self.centralWidget().selectedText())
    
    def text_changed(self, s):
        print("Text changed : {}".format(s));

    def text_edited(self, s):
        print("Text edited: {}".format(s));
        

app = QApplication(sys.argv)

window = MainWindow();

window.show();

app.exec();

