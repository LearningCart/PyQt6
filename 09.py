"""
All mouse events in Qt are tracked with the QMouseEvent object, with information about the event 
being readable from the following event methods.

Method	Returns
.button()	Specific button that triggered this event
.buttons()	State of all mouse buttons (OR'ed flags)
.position()	Widget-relative position as a QPoint integer
You can use these methods within an event handler to respond to different events differently, 
or ignore them completely. The positional methods provide both global and local (widget-relative) 
position information as QPoint objects, while buttons are reported using the mouse button types 
from the Qt namespace.

he button identifiers are defined in the Qt namespace, as follows --

Identifier	Value (binary)	Represents
Qt.MouseButton.NoButton	0 (000)	No button pressed, or the event is not related to button press.
Qt.MouseButton.LeftButton	1 (001)	The left button is pressed
Qt.MouseButton.RightButton	2 (010)	The right button is pressed.
Qt.MouseButton.MiddleButton	4 (100)	The middle button is pressed.

"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication;
from PyQt6.QtWidgets import QLabel;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QTextEdit;


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        print("mouseMoveEvent");

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

