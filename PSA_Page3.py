# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAPage3(object):
    def setupUi(self, PSAPage3):
        PSAPage3.setObjectName("PSAPage3")
        PSAPage3.resize(800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSAPage3.sizePolicy().hasHeightForWidth())
        PSAPage3.setSizePolicy(sizePolicy)
        PSAPage3.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(PSAPage3)
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
        self.Temps = QtWidgets.QLabel(self.centralwidget)
        self.Temps.setGeometry(QtCore.QRect(75, 235, 650, 350))
        self.Temps.setText("")
        self.Temps.setPixmap(QtGui.QPixmap(":/Resources/Temperatures.png"))
        self.Temps.setScaledContents(True)
        self.Temps.setObjectName("Temps")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(75, 600, 650, 350))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Resources/Daily_Tonnes.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(550, 150, 235, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.NextPage = QtWidgets.QPushButton(self.groupBox)
        self.NextPage.setGeometry(QtCore.QRect(5, 20, 50, 50))
        self.NextPage.setObjectName("NextPage")
        self.pg1 = QtWidgets.QPushButton(self.groupBox)
        self.pg1.setGeometry(QtCore.QRect(60, 20, 30, 50))
        self.pg1.setObjectName("pg1")
        self.pg2 = QtWidgets.QPushButton(self.groupBox)
        self.pg2.setGeometry(QtCore.QRect(95, 20, 30, 50))
        self.pg2.setObjectName("pg2")
        self.pg4 = QtWidgets.QPushButton(self.groupBox)
        self.pg4.setGeometry(QtCore.QRect(130, 20, 30, 50))
        self.pg4.setObjectName("pg4")
        self.pg5 = QtWidgets.QPushButton(self.groupBox)
        self.pg5.setGeometry(QtCore.QRect(165, 20, 30, 50))
        self.pg5.setObjectName("pg5")
        self.pg6 = QtWidgets.QPushButton(self.groupBox)
        self.pg6.setGeometry(QtCore.QRect(200, 20, 30, 50))
        self.pg6.setObjectName("pg6")
        PSAPage3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAPage3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PSAPage3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAPage3)
        self.statusbar.setObjectName("statusbar")
        PSAPage3.setStatusBar(self.statusbar)

        self.retranslateUi(PSAPage3)
        QtCore.QMetaObject.connectSlotsByName(PSAPage3)

    def retranslateUi(self, PSAPage3):
        _translate = QtCore.QCoreApplication.translate
        PSAPage3.setWindowTitle(_translate("PSAPage3", "PSA Report Page 3"))
        self.psa_report_title.setText(_translate("PSAPage3", "PSA Report"))
        self.psa_report_title_2.setText(_translate("PSAPage3", "Page 3"))
        self.groupBox.setTitle(_translate("PSAPage3", "Page Control"))
        self.NextPage.setText(_translate("PSAPage3", "Save"))
        self.pg1.setText(_translate("PSAPage3", "PG\n"
"1"))
        self.pg2.setText(_translate("PSAPage3", "PG\n"
"2"))
        self.pg4.setText(_translate("PSAPage3", "PG\n"
"4"))
        self.pg5.setText(_translate("PSAPage3", "PG\n"
"5"))
        self.pg6.setText(_translate("PSAPage3", "PG\n"
"6"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAPage3 = QtWidgets.QMainWindow()
    ui = Ui_PSAPage3()
    ui.setupUi(PSAPage3)
    PSAPage3.show()
    sys.exit(app.exec_())
