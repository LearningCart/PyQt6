# QLabel
import sys

from PyQt6.QtCore    import Qt
from PyQt6.QtGui     import QPixmap
from PyQt6.QtWidgets import ( QApplication, QLabel, QMainWindow )

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")

        # Font tip: Note that if you want to change the properties of a widget font 
        # it is usually better to get the current font, update it and then apply it 
        # back. This ensures the font face remains in keeping with the desktop conventions.
        font = widget.font()
        # font.setPointSize(500); # really big size font ;-)
        font.setPointSize(50);
        widget.setFont(font)

        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)


# TODO: 
# 1) How to avoid label filling the whole screen?
# 2) PNG file with transparency?
# 3) Animated gif as label? 
# StackOverflow
# QMovie *movie = new QMovie(":/images/other/images/16x16/loading.gif");
# QLabel *processLabel = new QLabel(this);
# processLabel->setMovie(movie);
# movie->start();
# Useful to show image for label., 
# 
class MainWindowPixMap(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(720,480);
        self.setStyleSheet("background-color: orange;") 
        widget = QLabel() # .setText can be used (may be xml :) and used as) label
        dimention = 30;
        widget.setGeometry(dimention,dimention,dimention,dimention);
        #  widget.setScaledContents(True) # Try turning it on or off 

        widget.setPixmap(QPixmap('test.png')) # Icon source: www.iconarchive.com

        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)

app = QApplication(sys.argv);

w = MainWindowPixMap();

w.show();
app.exec();