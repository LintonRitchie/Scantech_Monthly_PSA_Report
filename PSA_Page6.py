# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page6.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage6(object):
    def setupUi(self, PSAPage6):
        PSAPage6.setObjectName("PSAPage6")
        PSAPage6.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage6.sizePolicy().hasHeightForWidth())
        PSAPage6.setSizePolicy(sizePolicy)
        PSAPage6.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage6)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Resources/ScantechReportHeader.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.psa_report_title = QtWidgets.QLabel(self.centralwidget)
        self.psa_report_title.setGeometry(QtCore.QRect(300, 150, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.psa_report_title.setFont(font)
        self.psa_report_title.setAlignment(QtCore.Qt.AlignCenter)
        self.psa_report_title.setObjectName("psa_report_title")
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
        self.PlantPLCTable = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable.setGeometry(QtCore.QRect(50, 246, 700, 85))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable.setFont(font)
        self.PlantPLCTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable.setObjectName("PlantPLCTable")
        self.PlantPLCTable.setColumnCount(4)
        self.PlantPLCTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable.horizontalHeader().setCascadingSectionResizes(False)
        self.PlantPLCTable.horizontalHeader().setSortIndicatorShown(False)
        self.PlantPLCTable.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable.verticalHeader().setStretchLastSection(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 246, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setIndent(5)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 341, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setIndent(5)
        self.label_4.setObjectName("label_4")
        self.PlantPLCTable_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable_2.setGeometry(QtCore.QRect(50, 341, 700, 105))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable_2.setFont(font)
        self.PlantPLCTable_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_2.setObjectName("PlantPLCTable_2")
        self.PlantPLCTable_2.setColumnCount(4)
        self.PlantPLCTable_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_2.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable_2.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable_2.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable_2.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable_2.verticalHeader().setStretchLastSection(False)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 456, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setIndent(5)
        self.label_5.setObjectName("label_5")
        self.PlantPLCTable_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable_3.setGeometry(QtCore.QRect(50, 456, 700, 105))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable_3.setFont(font)
        self.PlantPLCTable_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_3.setObjectName("PlantPLCTable_3")
        self.PlantPLCTable_3.setColumnCount(4)
        self.PlantPLCTable_3.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_3.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable_3.horizontalHeader().setMinimumSectionSize(35)
        self.PlantPLCTable_3.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable_3.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable_3.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable_3.verticalHeader().setStretchLastSection(False)
        self.PlantPLCTable_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable_4.setGeometry(QtCore.QRect(50, 571, 700, 85))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable_4.setFont(font)
        self.PlantPLCTable_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_4.setObjectName("PlantPLCTable_4")
        self.PlantPLCTable_4.setColumnCount(4)
        self.PlantPLCTable_4.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_4.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable_4.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable_4.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable_4.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable_4.verticalHeader().setStretchLastSection(False)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 571, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setIndent(5)
        self.label_6.setObjectName("label_6")
        self.PlantPLCTable_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable_5.setGeometry(QtCore.QRect(50, 666, 700, 105))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable_5.setFont(font)
        self.PlantPLCTable_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_5.setObjectName("PlantPLCTable_5")
        self.PlantPLCTable_5.setColumnCount(4)
        self.PlantPLCTable_5.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_5.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable_5.horizontalHeader().setMinimumSectionSize(35)
        self.PlantPLCTable_5.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable_5.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable_5.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable_5.verticalHeader().setStretchLastSection(False)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 666, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setIndent(5)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 781, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setIndent(5)
        self.label_8.setObjectName("label_8")
        self.PlantPLCTable_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable_6.setGeometry(QtCore.QRect(50, 781, 700, 65))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable_6.setFont(font)
        self.PlantPLCTable_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_6.setObjectName("PlantPLCTable_6")
        self.PlantPLCTable_6.setColumnCount(4)
        self.PlantPLCTable_6.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_6.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable_6.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable_6.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable_6.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable_6.verticalHeader().setStretchLastSection(False)
        self.PlantPLCTable_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.PlantPLCTable_7.setGeometry(QtCore.QRect(50, 856, 700, 65))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.PlantPLCTable_7.setFont(font)
        self.PlantPLCTable_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlantPLCTable_7.setObjectName("PlantPLCTable_7")
        self.PlantPLCTable_7.setColumnCount(4)
        self.PlantPLCTable_7.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PlantPLCTable_7.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.PlantPLCTable_7.setHorizontalHeaderItem(3, item)
        self.PlantPLCTable_7.horizontalHeader().setStretchLastSection(True)
        self.PlantPLCTable_7.verticalHeader().setDefaultSectionSize(20)
        self.PlantPLCTable_7.verticalHeader().setMinimumSectionSize(20)
        self.PlantPLCTable_7.verticalHeader().setStretchLastSection(False)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 856, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setIndent(5)
        self.label_9.setObjectName("label_9")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(670, 150, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.NextPage_2 = QtWidgets.QPushButton(self.groupBox)
        self.NextPage_2.setGeometry(QtCore.QRect(20, 30, 75, 25))
        self.NextPage_2.setObjectName("NextPage_2")
        self.label.raise_()
        self.psa_report_title.raise_()
        self.psa_report_title_2.raise_()
        self.PlantPLCTable.raise_()
        self.label_3.raise_()
        self.PlantPLCTable_3.raise_()
        self.PlantPLCTable_4.raise_()
        self.PlantPLCTable_5.raise_()
        self.PlantPLCTable_6.raise_()
        self.PlantPLCTable_2.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.PlantPLCTable_7.raise_()
        self.label_9.raise_()
        self.groupBox.raise_()
        PSAPage6.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage6)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage6.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage6)
        self.statusbar.setObjectName("statusbar")
        PSAPage6.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage6)
        self.NextPage_2.released.connect(PSAPage6.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAPage6)

    def retranslateUi(self, PSAPage6):
        _translate = QtCore.QCoreApplication.translate
        PSAPage6.setWindowTitle(_translate("PSAPage6", "PSA Report Page 6"))
        self.psa_report_title.setText(_translate("PSAPage6", "PSA Report"))
        self.psa_report_title_2.setText(_translate("PSAPage6", "Page 6"))
        item = self.PlantPLCTable.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Belt Running"))
        item = self.PlantPLCTable.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "Force Analyse"))
        item = self.PlantPLCTable.verticalHeaderItem(2)
        item.setText(_translate("PSAPage6", "Force Standardise                                                          "))
        item = self.PlantPLCTable.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        self.label_3.setText(_translate("PSAPage6", "Plant PLC Status"))
        self.label_4.setText(_translate("PSAPage6", "Analyser Status"))
        item = self.PlantPLCTable_2.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Analyser OK"))
        item = self.PlantPLCTable_2.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "Standards OK"))
        item = self.PlantPLCTable_2.verticalHeaderItem(2)
        item.setText(_translate("PSAPage6", "I/O Control OK      "))
        item = self.PlantPLCTable_2.verticalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Spectra Stable                                                                  "))
        item = self.PlantPLCTable_2.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable_2.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable_2.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable_2.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        self.label_5.setText(_translate("PSAPage6", "PLC Analyser Results"))
        item = self.PlantPLCTable_3.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "System OK"))
        item = self.PlantPLCTable_3.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "Source Control Fault                                                    "))
        item = self.PlantPLCTable_3.verticalHeaderItem(2)
        item.setText(_translate("PSAPage6", "Source Off"))
        item = self.PlantPLCTable_3.verticalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Source On"))
        item = self.PlantPLCTable_3.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable_3.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable_3.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable_3.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        item = self.PlantPLCTable_4.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Analysis Period (Seconds)"))
        item = self.PlantPLCTable_4.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "AnalMinLoadLimit"))
        item = self.PlantPLCTable_4.verticalHeaderItem(2)
        item.setText(_translate("PSAPage6", "Standardise Period (Seconds)                                 "))
        item = self.PlantPLCTable_4.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable_4.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable_4.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable_4.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        self.label_6.setText(_translate("PSAPage6", "Analyser Configuration"))
        item = self.PlantPLCTable_5.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "First Standard Time"))
        item = self.PlantPLCTable_5.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "Most Recent Standard Time"))
        item = self.PlantPLCTable_5.verticalHeaderItem(2)
        item.setText(_translate("PSAPage6", "Number of Std Periods Since Last Cleared     "))
        item = self.PlantPLCTable_5.verticalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Number of Std Periods This Month"))
        item = self.PlantPLCTable_5.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable_5.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable_5.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable_5.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        self.label_7.setText(_translate("PSAPage6", "Standardisation"))
        self.label_8.setText(_translate("PSAPage6", "Software Versions"))
        item = self.PlantPLCTable_6.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Product"))
        item = self.PlantPLCTable_6.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "CsSchedule                                                                         "))
        item = self.PlantPLCTable_6.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable_6.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable_6.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable_6.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        item = self.PlantPLCTable_7.verticalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Disk Space"))
        item = self.PlantPLCTable_7.verticalHeaderItem(1)
        item.setText(_translate("PSAPage6", "% Disk Space                                                                       "))
        item = self.PlantPLCTable_7.horizontalHeaderItem(0)
        item.setText(_translate("PSAPage6", "Current"))
        item = self.PlantPLCTable_7.horizontalHeaderItem(1)
        item.setText(_translate("PSAPage6", "1 Report Ago"))
        item = self.PlantPLCTable_7.horizontalHeaderItem(2)
        item.setText(_translate("PSAPage6", "2 Reports Ago"))
        item = self.PlantPLCTable_7.horizontalHeaderItem(3)
        item.setText(_translate("PSAPage6", "Comment"))
        self.label_9.setText(_translate("PSAPage6", "Disk Space & Memory Remaining"))
        self.groupBox.setTitle(_translate("PSAPage6", "Page Control"))
        self.NextPage_2.setText(_translate("PSAPage6", "Close"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage6 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage6()
    ui.setupUi(PSAPage6)
    PSAPage6.show()
    sys.exit(app.exec_())
