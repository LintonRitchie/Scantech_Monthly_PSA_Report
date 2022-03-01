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

        widget = QComboBox()
        widget.addItems(["One","Two","Three"])
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAtTop)

        #Send the current index (position) of the selected item
        widget.currentIndexChanged.connect(self.index_changed)

        #There is an alternate Signal to send the Text
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i): # I is an Int which displays the index of the options selected
        print(i)

    def text_changed(self, s):  # s is a string which returns the text of the list option selected.
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
