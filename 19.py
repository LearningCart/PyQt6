# QDial my favourite so far
# Finally, the QDial is a rotatable widget that functions just like 
# the slider, but appears as an analogue dial. 
# This looks nice, but from a UI perspective is not particularly 
# user friendly. However, they are often used in audio applications
# as representation of real-world analogue dials:



import sys;

from PyQt6.QtWidgets import (QApplication, QMainWindow, QDial);

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("QDial Example");
        self.setFixedSize(720, 480);

        widget = QDial();
        widget.setRange(0, 100);
        widget.setSingleStep(1);

        widget.valueChanged   .connect(self.value_changed  );
        # The signals are the same as for QSlider and retain the same names (e.g. .sliderMoved).
        widget.sliderMoved    .connect(self.slider_position);
        widget.sliderPressed  .connect(self.slider_pressed );
        widget.sliderReleased .connect(self.slider_released);

        self.setCentralWidget(widget);


    # Event handlers
    def value_changed(self, i):
        print("Value changed to : {}".format(i));

    def slider_position(self, p):
        print("Position changed to {}".format(p));

    def slider_pressed(self):
        print("Pressed!");

    def slider_released(self):
        print("Released");

app = QApplication(sys.argv);

window = MainWindow();
window.show();

app.exec();