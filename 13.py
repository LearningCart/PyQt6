# QCheckBox: presents a checkable box to the user
import sys;
from PyQt6.QtCore    import Qt;
from PyQt6.QtWidgets import (QApplication, QCheckBox, QMainWindow)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("QCheckBox");
        self.setFixedSize(720,480);
        self.setStyleSheet("background-color: teal;");

        widget = QCheckBox();
        widget.setCheckState (Qt.CheckState.Unchecked); # Or Qt.CheckState.Checked

        # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
        #           Or: widget.setTristate(True)
        # widget.setCheckState(Qt.CheckState.PartiallyChecked)
        # TODO: Find practical real world examples for partially checked box
        widget.setTristate(True);

        widget.stateChanged.connect(self.show_state);

        self.setCentralWidget(widget);

    def show_state(self, s):
        # print(s == Qt.CheckState.Checked.value);
        print("Checkbox status is : {}".format(s));


app = QApplication(sys.argv);

window = MainWindow();

window.show();

app.exec();
