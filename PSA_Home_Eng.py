# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Home_Eng.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSAHome(object):
    def setupUi(self, PSAHome):
        PSAHome.setObjectName("PSAHome")
        PSAHome.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PSAHome)
        self.centralwidget.setObjectName("centralwidget")
        self.ScantechLogo = QtWidgets.QLabel(self.centralwidget)
        self.ScantechLogo.setGeometry(QtCore.QRect(600, 0, 200, 50))
        self.ScantechLogo.setText("")
        self.ScantechLogo.setPixmap(QtGui.QPixmap(":/Resources/ScantechFullLogo.png"))
        self.ScantechLogo.setScaledContents(True)
        self.ScantechLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.ScantechLogo.setObjectName("ScantechLogo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 41, 354, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setIndent(5)
        self.label.setObjectName("label")
        self.CloseReportPB = QtWidgets.QPushButton(self.centralwidget)
        self.CloseReportPB.setGeometry(QtCore.QRect(640, 510, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.CloseReportPB.setFont(font)
        self.CloseReportPB.setObjectName("CloseReportPB")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(610, 130, 161, 281))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(42, 54, 77, 194))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PB_pg = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_pg.setEnabled(False)
        self.PB_pg.setObjectName("PB_pg")
        self.verticalLayout.addWidget(self.PB_pg)
        self.PB_pg_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_pg_2.setEnabled(False)
        self.PB_pg_2.setObjectName("PB_pg_2")
        self.verticalLayout.addWidget(self.PB_pg_2)
        self.PB_pg_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_pg_3.setEnabled(False)
        self.PB_pg_3.setObjectName("PB_pg_3")
        self.verticalLayout.addWidget(self.PB_pg_3)
        self.PB_pg_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_pg_4.setEnabled(False)
        self.PB_pg_4.setObjectName("PB_pg_4")
        self.verticalLayout.addWidget(self.PB_pg_4)
        self.PB_pg_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_pg_5.setEnabled(False)
        self.PB_pg_5.setObjectName("PB_pg_5")
        self.verticalLayout.addWidget(self.PB_pg_5)
        self.PB_pg_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.PB_pg_6.setEnabled(False)
        self.PB_pg_6.setObjectName("PB_pg_6")
        self.verticalLayout.addWidget(self.PB_pg_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 200, 320, 180))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.ImportReportPB = QtWidgets.QPushButton(self.groupBox_2)
        self.ImportReportPB.setGeometry(QtCore.QRect(60, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ImportReportPB.setFont(font)
        self.ImportReportPB.setObjectName("ImportReportPB")
        self.PreviewReportPB = QtWidgets.QPushButton(self.groupBox_2)
        self.PreviewReportPB.setEnabled(False)
        self.PreviewReportPB.setGeometry(QtCore.QRect(60, 70, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.PreviewReportPB.setFont(font)
        self.PreviewReportPB.setObjectName("PreviewReportPB")
        self.ExportReportPB = QtWidgets.QPushButton(self.groupBox_2)
        self.ExportReportPB.setEnabled(False)
        self.ExportReportPB.setGeometry(QtCore.QRect(60, 110, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ExportReportPB.setFont(font)
        self.ExportReportPB.setObjectName("ExportReportPB")
        PSAHome.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSAHome)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        PSAHome.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSAHome)
        self.statusbar.setObjectName("statusbar")
        PSAHome.setStatusBar(self.statusbar)
        self.actionNew_Report = QtWidgets.QAction(PSAHome)
        self.actionNew_Report.setObjectName("actionNew_Report")
        self.actionEdit_Exisiting_Report = QtWidgets.QAction(PSAHome)
        self.actionEdit_Exisiting_Report.setObjectName("actionEdit_Exisiting_Report")
        self.actionAbout = QtWidgets.QAction(PSAHome)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_Report = QtWidgets.QAction(PSAHome)
        self.actionOpen_Report.setObjectName("actionOpen_Report")
        self.menuFile.addAction(self.actionNew_Report)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Report)
        self.menuEdit.addAction(self.actionEdit_Exisiting_Report)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(PSAHome)
        self.ImportReportPB.released.connect(PSAHome.show) # type: ignore
        self.CloseReportPB.released.connect(PSAHome.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PSAHome)

    def retranslateUi(self, PSAHome):
        _translate = QtCore.QCoreApplication.translate
        PSAHome.setWindowTitle(_translate("PSAHome", "PSA Report Home Page"))
        self.label.setText(_translate("PSAHome", "Monthly PSA Report Generator"))
        self.CloseReportPB.setText(_translate("PSAHome", "Close"))
        self.groupBox.setTitle(_translate("PSAHome", "Page Control"))
        self.PB_pg.setText(_translate("PSAHome", "Page 1"))
        self.PB_pg_2.setText(_translate("PSAHome", "Page 2"))
        self.PB_pg_3.setText(_translate("PSAHome", "Page 3"))
        self.PB_pg_4.setText(_translate("PSAHome", "Page 4"))
        self.PB_pg_5.setText(_translate("PSAHome", "Page 5"))
        self.PB_pg_6.setText(_translate("PSAHome", "Page 6"))
        self.groupBox_2.setTitle(_translate("PSAHome", "Report Control"))
        self.ImportReportPB.setText(_translate("PSAHome", "Import Report Data"))
        self.PreviewReportPB.setText(_translate("PSAHome", "Preview Report"))
        self.ExportReportPB.setText(_translate("PSAHome", "Export Report"))
        self.menuFile.setTitle(_translate("PSAHome", "File"))
        self.menuEdit.setTitle(_translate("PSAHome", "Edit"))
        self.menuAbout.setTitle(_translate("PSAHome", "Help"))
        self.actionNew_Report.setText(_translate("PSAHome", "New Report"))
        self.actionNew_Report.setToolTip(_translate("PSAHome", "Generate New Monthly PSA Report"))
        self.actionNew_Report.setShortcut(_translate("PSAHome", "Ctrl+N"))
        self.actionEdit_Exisiting_Report.setText(_translate("PSAHome", "Edit Exisiting Report"))
        self.actionAbout.setText(_translate("PSAHome", "About"))
        self.actionOpen_Report.setText(_translate("PSAHome", "Open Report"))
        self.actionOpen_Report.setShortcut(_translate("PSAHome", "Ctrl+O"))
import PSAReportResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSAHome = QtWidgets.QMainWindow()
    ui = Ui_PSAHome()
    ui.setupUi(PSAHome)
    PSAHome.show()
    sys.exit(app.exec_())
