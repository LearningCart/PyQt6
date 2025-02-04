from PyQt6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv);

button = QPushButton("Press this damn button!");
button.show();

app.exec();
