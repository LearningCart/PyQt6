import sys;
from PyQt6.QtCore import Qt;
from PyQt6.QtCore import QSize;
from PyQt6.QtWidgets import QApplication;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QPushButton;


class FirstPage(QMainWindow):
    def __init__(self, name = "Dummy Window", buttonname = "default button"):
        super().__init__();
        self.setWindowTitle(name);
        self.setFixedSize(720,480);
        # self.setMinimumSize(720,480);
        # self.setMaximumSize(1920,1080);
        button = QPushButton(buttonname);
        self.setCentralWidget(button);


app = QApplication(sys.argv)


param_acquisition = FirstPage("parameter acquisition", "Acquire Param");
bno086 = FirstPage("BNO 086 Sensor", "Plot Sensor Data");

param_acquisition.show();
bno086.show();

app.exec();


