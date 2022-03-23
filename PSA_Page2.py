# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage2(object):
    def setupUi(self, PSAPage2):
        PSAPage2.setObjectName("PSAPage2")
        PSAPage2.setEnabled(True)
        PSAPage2.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage2.sizePolicy().hasHeightForWidth())
        PSAPage2.setSizePolicy(sizePolicy)
        PSAPage2.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Resources/ScantechReportHeader.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.psa_report_title = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title.setGeometry(QtCore.QRect(300, 150, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.psa_report_title.setFont(font)
        self.psa_report_title.setAlignment(QtCore.Qt.AlignCenter)
        self.psa_report_title.setObjectName("psa_report_title")
        self.NextPage = QtWidgets.QPushButton(self.centralwidget)
        self.NextPage.setGeometry(QtCore.QRect(700, 180, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.NextPage.setFont(font)
        self.NextPage.setObjectName("NextPage")
        self.Regenerate = QtWidgets.QPushButton(self.centralwidget)
        self.Regenerate.setGeometry(QtCore.QRect(10, 160, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.Regenerate.setFont(font)
        self.Regenerate.setObjectName("Regenerate")
        self.psa_report_title_2 = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title_2.setGeometry(QtCore.QRect(350, 195, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.psa_report_title_2.setFont(font)
        self.psa_report_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.psa_report_title_2.setObjectName("psa_report_title_2")
        self.PreviousPage = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousPage.setGeometry(QtCore.QRect(610, 180, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.PreviousPage.setFont(font)
        self.PreviousPage.setObjectName("PreviousPage")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(645, 150, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(110, 230, 561, 151))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 50, 251, 71))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.ElecCabTempcomboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ElecCabTempcomboBox.setFont(font)
        self.ElecCabTempcomboBox.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.ElecCabTempcomboBox.setObjectName("ElecCabTempcomboBox")
        self.ElecCabTempcomboBox.addItem("")
        self.ElecCabTempcomboBox.addItem("")
        self.ElecCabTempcomboBox.addItem("")
        self.gridLayout.addWidget(self.ElecCabTempcomboBox, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.DetTempcomboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DetTempcomboBox.setFont(font)
        self.DetTempcomboBox.setAcceptDrops(True)
        self.DetTempcomboBox.setAutoFillBackground(False)
        self.DetTempcomboBox.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.DetTempcomboBox.setObjectName("DetTempcomboBox")
        self.DetTempcomboBox.addItem("")
        self.DetTempcomboBox.addItem("")
        self.DetTempcomboBox.addItem("")
        self.gridLayout.addWidget(self.DetTempcomboBox, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_5.setGeometry(QtCore.QRect(290, 40, 251, 95))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_5.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget_5.setItem(2, 0, item)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget_5.verticalHeader().setMinimumSectionSize(20)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 410, 801, 541))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(5, 30, 790, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(15, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(46)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 650, 421))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Resources/Detector_Stability.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.psa_report_title.raise_()
        self.NextPage.raise_()
        self.Regenerate.raise_()
        self.psa_report_title_2.raise_()
        self.PreviousPage.raise_()
        self.label_2.raise_()
        self.DetTempcomboBox.raise_()
        self.ElecCabTempcomboBox.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        PSAPage2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage2)
        self.statusbar.setObjectName("statusbar")
        PSAPage2.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage2)
        self.NextPage.released.connect(PSAPage2.close) # type: ignore
        self.DetTempcomboBox.currentTextChanged['QString'].connect(self.DetTempcomboBox.setStyleSheet) # type: ignore
        self.ElecCabTempcomboBox.currentTextChanged['QString'].connect(self.ElecCabTempcomboBox.setStyleSheet) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAPage2)

    def retranslateUi(self, PSAPage2):
        _translate = QtCore.QCoreApplication.translate
        PSAPage2.setWindowTitle(_translate("PSAPage2", "PSA Report Page 2"))
        self.psa_report_title.setText(_translate("PSAPage2", "PSA Report"))
        self.NextPage.setText(_translate("PSAPage2", "Next"))
        self.Regenerate.setText(_translate("PSAPage2", "Regenerate Report"))
        self.psa_report_title_2.setText(_translate("PSAPage2", "Page 2"))
        self.PreviousPage.setText(_translate("PSAPage2", "Previous"))
        self.label_2.setText(_translate("PSAPage2", "Page Control"))
        self.groupBox.setTitle(_translate("PSAPage2", "Temperature Control"))
        self.label_4.setText(_translate("PSAPage2", "Detector Enclosure"))
        self.ElecCabTempcomboBox.setItemText(0, _translate("PSAPage2", " "))
        self.ElecCabTempcomboBox.setItemText(1, _translate("PSAPage2", "Yes"))
        self.ElecCabTempcomboBox.setItemText(2, _translate("PSAPage2", "No"))
        self.label_5.setText(_translate("PSAPage2", "Electronics Cabinet"))
        self.DetTempcomboBox.setItemText(0, _translate("PSAPage2", " "))
        self.DetTempcomboBox.setItemText(1, _translate("PSAPage2", "Yes"))
        self.DetTempcomboBox.setItemText(2, _translate("PSAPage2", "No"))
        self.label_6.setText(_translate("PSAPage2", "Stable?"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Normal"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Situation Flagged"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("PSAPage2", "Requires Urgent Attention"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Legend"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.item(0, 0)
        item.setText(_translate("PSAPage2", "yt"))
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("PSAPage2", "Detector Stability (at the time the report was compiled)"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Enabled"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Stable"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage2", "Det 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage2", "Det 2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage2", "Det 3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage2", "Det 4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PSAPage2", "Det 5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PSAPage2", "Det 6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("PSAPage2", "Det 7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("PSAPage2", "Det 8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("PSAPage2", "Det 9"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("PSAPage2", "Det 10"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("PSAPage2", "Det 11"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("PSAPage2", "Det 12"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("PSAPage2", "Det 13"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("PSAPage2", "Det 14"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("PSAPage2", "Det 15"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("PSAPage2", "Det 16"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage2 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage2()
    ui.setupUi(PSAPage2)
    PSAPage2.show()
    sys.exit(app.exec_())
