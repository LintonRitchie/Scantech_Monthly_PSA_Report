import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap)
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QFrame,


)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Widgets App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap('Scantech_Logo.PNG'))
        widget.setFixedSize(1000,200)
        widget.setFrameStyle(QFrame.Panel)
        widget.setScaledContents(True)


        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
