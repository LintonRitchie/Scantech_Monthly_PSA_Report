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

        widget = QCheckBox("This is a Checkbox")
        widget.setCheckState(Qt.Checked)

        #For Tristate: widget.setCheckedState(Qt.PartiallyChecked)
        #Or: widget.setTriState(True)

        widget.stateChanged.connect(self.show_state)


        self.setCentralWidget(widget)

    def show_state(self, s):
        print((s == Qt.Checked))
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
