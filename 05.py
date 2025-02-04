import sys;
from PyQt6.QtWidgets import QApplication;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QPushButton;


class MainWindow(QMainWindow):
    def __init__(self):
        self.checked = False;
        self.count = 0;
        super().__init__();
        self.setWindowTitle("Test App");
        self.setFixedSize(720,480);

        button = QPushButton("Press it!");
        button.setCheckable(True);
        button.clicked.connect(self.handleBtnPress);
        button.clicked.connect(self.handleToggle);
        self.setCentralWidget(button);

    def handleBtnPress(self):
        self.count = self.count + 1;
        self.setWindowTitle("Test App: {}".format(self.count));
        print("Button pressed!!");

    def handleToggle(self, status):
        # Store button checked status in a variable for use without accessing the widget
        self.checked = status;
        print("Button Toggled?", status);
        # print("slef.checked = {}".format(self.checked));


app = QApplication(sys.argv);

win = MainWindow();
win.show();

app.exec();