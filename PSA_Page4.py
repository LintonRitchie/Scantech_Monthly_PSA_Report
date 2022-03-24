# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page4.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage4(object):
    def setupUi(self, PSAPage4):
        PSAPage4.setObjectName("PSAPage4")
        PSAPage4.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage4.sizePolicy().hasHeightForWidth())
        PSAPage4.setSizePolicy(sizePolicy)
        PSAPage4.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage4)
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
        self.Results1 = QtWidgets.QLabel(self.centralwidget)
        self.Results1.setGeometry(QtCore.QRect(100, 225, 600, 725))
        self.Results1.setText("")
        self.Results1.setPixmap(QtGui.QPixmap(":/Resources/Results1.png"))
        self.Results1.setScaledContents(True)
        self.Results1.setObjectName("Results1")
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
        PSAPage4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage4)
        self.statusbar.setObjectName("statusbar")
        PSAPage4.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage4)
        QtCore.QMetaObject.connectSlotsByName(PSAPage4)

    def retranslateUi(self, PSAPage4):
        _translate = QtCore.QCoreApplication.translate
        PSAPage4.setWindowTitle(_translate("PSAPage4", "PSA Report Page 4"))
        self.psa_report_title.setText(_translate("PSAPage4", "PSA Report"))
        self.psa_report_title_2.setText(_translate("PSAPage4", "Page 4"))
        self.groupBox.setTitle(_translate("PSAPage4", "Page Control"))
        self.NextPage_2.setText(_translate("PSAPage4", "Close"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage4 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage4()
    ui.setupUi(PSAPage4)
    PSAPage4.show()
    sys.exit(app.exec_())
