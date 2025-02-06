# QTabWidget
import sys
from PyQt6.QtGui     import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        # Do try disabling this. It will not allow user to 'shuffle' the tabs if you made it False
        tabs.setMovable(True)

        # macOS tab bar looks quite different from the others -- 
        # by default on macOS tabs take on a pill or bubble style. 
        # On macOS, this is typically used for tabbed configuration panels. 
        # For documents, you can turn on document mode to give slimline tabs
        #  similar to what you see on other platforms. 
        # This option has no effect on other platforms:
        # tabs.setDocumentMode(True)


        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()