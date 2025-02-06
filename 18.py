# QSlider
# QSlider provides a slide-bar widget, which functions internally 
# much like a QDoubleSpinBox. Rather than display the current value 
# numerically, it is represented by the position of the slider handle
# along the length of the widget.
# 
# This is often useful when providing adjustment between two extremes, 
# but where absolute accuracy is not required.
# The most common use of this type of widget is for volume controls.


# There is an additional .sliderMoved signal that is triggered whenever
# the slider moves position 
# and a .sliderPressed signal that emits whenever the slider is clicked

import sys;
from PyQt6.QtCore    import Qt;
from PyQt6.QtWidgets import (QApplication, QSlider, QMainWindow)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();

        self.setWindowTitle("QSlider example");
        self.setFixedSize(720, 480);

        widget = QSlider();
        widget.setFixedSize(100, 200);
        
        widget.setMinimum(10);
        widget.setMaximum(100);

        # widget.setOrientation(Qt.Orientation.Horizontal);
        widget.setOrientation(Qt.Orientation.Vertical);

        widget.valueChanged   .connect (self. value_changed  );
        widget.sliderMoved    .connect (self. slider_moved   );
        widget.sliderPressed  .connect (self. slider_pressed );
        widget.sliderReleased .connect (self. slider_released);

        self.setCentralWidget(widget);

    # Event handlers
    def value_changed(self, i):
        print("Value changed {}".format(i));

    def slider_moved (self, p):
        print("Slider moved to position: {}".format(p));

    def slider_pressed(self):
        print("Slider pressed");

    def slider_released(self):
        print("Slider released");

app = QApplication(sys.argv);

window = MainWindow();

window.show();
app.exec();