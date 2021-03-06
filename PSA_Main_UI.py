import os
import sys
import pandas as pd
from Regen_UI import regen_ui               # Load the function which runs a batch to regen the UI each time code runs.
# This is used for Development
from Read_Master import (Read_Master, Read_AnalyserStatus, Read_PeakControl, Read_VersionNumbers, Read_AnalyserIO, Read_A_08_Analyse, Read_PeakExtract,
                         Read_TempExtract)  # import the function which reads from the Master PSA file
# from PyQt5.QtGui import (QPixmap)
import datetime
import json
import base64
import glob
from PSA_Home import Ui_PSAHome
from PSA_Page1 import Ui_PSAPage1
from PSA_Page2 import Ui_PSAPage2
from PSA_Page3 import Ui_PSAPage3
from PSA_Page4 import Ui_PSAPage4
from PSA_Page5 import Ui_PSAPage5
from PSA_Page6 import Ui_PSAPage6
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QTableWidgetItem)
from PyQt5 import (QtCore, QtGui)
from PyQt5.QtCore import QDir



import matplotlib.pyplot as plt

# regen_ui()                  # Regenerate the UI. This is used to update the UI file after changes

# Define a function which reads in the data from the relevant files. This may be called in a few different places.
# this function takes 1 folder location and uses the PSA Master default location
class ReadInData:
    PSAMaster = "C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Master_List.xlsx"
    defaultpath = "C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\"
    resourcepath = "C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\"
    defaultanalyser = "OBA-040"
    PSAMasterData = Read_Master(PSAMaster)                                          # Read in master file data from PSA Master file.
    AnalyserStatus = Read_AnalyserStatus(defaultpath)                               # Read in PSA Report file data from PSA Report file.
    PeakControl = Read_PeakControl(defaultpath)                                     # Read in Analyser Peak Control Data
    VersionNumbers = Read_VersionNumbers(defaultpath)                               # Read in version numbers data
    AnalyserIO = Read_AnalyserIO(defaultpath)                                       # Read in Analyser IO Data
    AnalyserA08 = Read_A_08_Analyse(defaultpath)          # Read in Analysis Data
    PeakExtract = Read_PeakExtract(defaultpath)                                     # Readi in Peak Stability Data
    TempExtract = Read_TempExtract(defaultpath)                                     # Read in Temp Stability Data
    # print(" Initial Default Path: \n" + defaultpath)
    # print(" Initial PSA Master Data: \n" + str(PSAMasterData))
    # print(" Initial Analayser Status: \n" + str(AnalyserStatus))
    # print(" Initial Peak Control: \n" + str(PeakControl))
    # print(" Initial Version Number: \n" + str(VersionNumbers))
    # print(" Initial Analyser IO: \n" + str(AnalyserIO))
    # print(" Initial Analsyer Results: \n" + str(AnalyserA08))
    # print(" Initial Peak Satbility: \n" + str(PeakExtract))
    # print(" Initial Temp data: \n" + str(TempExtract))

# Read in master file data from PSA Master file. This is run at the start of the program to ensure data is loaded prior to the UI starting up.
ReadInData()

AnalyserToProcess = 0
open_window = 0

# open the data interchange file as a global variable which can be accessed throughout the program.
# This will be accessed multiple times by various functions within the functions.

with open("ReportData.json") as f:
    reportdata = json.load(f)


class HomeWindow(QMainWindow,Ui_PSAHome):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.page1 = PSA_pg1()
        self.page2 = PSA_pg2()
        self.page3 = PSA_pg3()
        self.page4 = PSA_pg4()
        self.page5 = PSA_pg5()
        self.page6 = PSA_pg6()
        self.connectSignalsSlots()
        self.popanalysers()

    # Setup Signals and Slots for Pushbuttons
    def connectSignalsSlots(self):
        self.NewReportPB.released.connect(self.show_page_1)
        self.NewReportPB.clicked.connect(self.updateReport)
        # self.NewReportPB.clicked.connect(self.RepEmail)
        self.PB_pg.released.connect(self.show_page_1)
        self.PB_pg_2.released.connect(self.show_page_2)
        self.PB_pg_3.released.connect(self.show_page_3)
        self.PB_pg_4.released.connect(self.show_page_4)
        self.PB_pg_5.released.connect(self.show_page_5)
        self.PB_pg_6.released.connect(self.show_page_6)
        self.OpenReportPB.released.connect(self.openReport)
        self.CalibratorListComboBox.currentTextChanged.connect(self.updatehome)
        # self.AnalyserListComboBox.currentTextChanged.connect(self.updatehome)
        self.AnalyserListComboBox.activated.connect(self.GetFolder)
        self.page1.NextPage.released.connect(self.UpdateJSON)
        self.page2.NextPage.released.connect(self.UpdateJSON)
        self.page6.RepAgo1.released.connect(self.UpdatePg6_1RepAgo)
        self.page6.RepAgo2.released.connect(self.UpdatePg6_2RepAgo)
        self.page6.NextPage.released.connect(self.UpdateJSON)

    def updatereadindata(self):
        ReadInData.AnalyserStatus = Read_AnalyserStatus(ReadInData.defaultpath)     # Read in PSA Report file data from PSA Report file.
        ReadInData.PeakControl = Read_PeakControl(ReadInData.defaultpath)           # Read in Analyser Peak Control Data
        ReadInData.VersionNumbers = Read_VersionNumbers(ReadInData.defaultpath)     # Read in version numbers data
        ReadInData.AnalyserIO = Read_AnalyserIO(ReadInData.defaultpath)             # Read in Analyser IO Data
        ReadInData.AnalyserA08 = Read_A_08_Analyse(ReadInData.defaultpath)          # Read in Analysis Data
        ReadInData.PeakExtract = Read_PeakExtract(ReadInData.defaultpath)           # Readi in Peak Stability Data
        ReadInData.TempExtract = Read_TempExtract(ReadInData.defaultpath)           # Read in Temp Stability Data

    def GetFolder(self):
        anal = self.AnalyserListComboBox.currentText()
        # Switches default folder based on which analyser is selected.
        if anal[0:3] == "C15":
            fname = QFileDialog.getExistingDirectory(self,"Open PSA File in PSA Folder","J:\\Client Analysers\\NG-1500")
        elif anal[0:3] == "C21":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\CS-2100")
        elif anal[0:3] == "CMM":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\CMM-100")
        elif anal[0:3] == "OBA":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\On Belt Analyser")
        elif anal[0:3] == "TBM":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\TBM-210")
        else:
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\TBM-230")

        # ensures the file separators are correct for operating system
        if fname:
            fname = QDir.toNativeSeparators(fname)

        # if user presses cancel, return control to calling function
        if not fname:
            return

        # Update the default path vairable in the ReadINData Class
        ReadInData.defaultpath = fname

        # Update the data in the Data Variables in Use
        self.updatereadindata()

    def UpdateJSON(self):
        print("Entering UpdateJSON")
        # Update JSON File
        reportdata['Summary'][0]['SiteName'] = self.page1.site_name.text()
        reportdata['Summary'][0]['ReportDate'] = self.page1.rep_date_data.text()
        reportdata['Summary'][0]['AnalyserNo'] = self.page1.rep_analyser_data.text()
        reportdata['Summary'][0]['ServEng'] = self.page1.rep_serv_eng_data.text()
        reportdata['Summary'][0]['Application'] = self.page1.rep_app_data.text()
        reportdata['Summary'][0]['Period'] = self.page1.period_data.text()
        reportdata['Summary'][0]['Email'] = self.page1.email_data.text()
        reportdata['Summary'][0]['NextPSA'] = str(self.page1.NextPSAMnth.currentText() + " " + self.page1.NextPSAYear.currentText())
        reportdata['Summary'][0]['TopUpDue'] = str(self.page1.TopUpMonth.currentText() + " " + self.page1.TopUpYear.currentText())
        print("Entering Action taken section")

        # this loop populates the JSON by looking to see if any data exists in the first cell of the row. If not then it skips. If is does, the data is pulled into the JSON
        # pull the data from the Action Taken table row 1 to fill the JSON
        for i in range(0,4):
            print(i)
            it = self.page1.ActionTakenTable.item(i, 0)
            if it and it.text():
                jsonid = "Action" + str(i+1)
                print(jsonid)
                reportdata['ActionTaken'][0][jsonid][0]['Date']=str(self.page1.ActionTakenTable.item(i, 0).text())
                reportdata['ActionTaken'][0][jsonid][0]['Time'] = str(self.page1.ActionTakenTable.item(i, 1).text())
                reportdata['ActionTaken'][0][jsonid][0]['Action'] = str(self.page1.ActionTakenTable.item(i, 2).text())
                reportdata['ActionTaken'][0][jsonid][0]['Description'] = str(self.page1.ActionTakenTable.item(i, 3).text())
            else:
                print("passing by")

        # this loop populates the JSON by looking to see if any data exists in the first cell of the row. If not then it skips. If is does, the data is pulled into the JSON
        # Populating the Action required section of the JSON file
        for i in range(0,4):
            print(i)
            it = self.page1.ActionTakenTable.item(i, 0)
            if it and it.text():
                jsonid = "ActionReq" + str(i+1)
                print(jsonid)
                reportdata['ActionRequired'][0][jsonid][0]['Action'] = str(self.page1.ActionRequiredTable.item(i, 0).text())
                reportdata['ActionRequired'][0][jsonid][0]['ByWhom'] = str(self.page1.ActionRequiredTable.item(i, 1).text())
                reportdata['ActionRequired'][0][jsonid][0]['ByWhen'] = str(self.page1.ActionRequiredTable.item(i, 2).text())
            else:
                print("passing by")


        # populating JSON with Detector stability info
        for i in range(0,15):
            print(i)
            it = self.page2.tableWidget.item(0, i)
            if it and it.text():
                jsonid = "Detector" + str(i+1)
                print(jsonid)
                reportdata['DetectorStability'][0][jsonid][0]['Enabled'] = str(self.page2.tableWidget.item(0, i).text())
                reportdata['DetectorStability'][0][jsonid][0]['Stable'] = str(self.page2.tableWidget.item(1, i).text())

        # pull stability question data from the Temperature stability combo boxes
        reportdata['Temperatures'][0]['StableDetTemp'] = str(self.page2.DetTempStable.currentText())
        reportdata['Temperatures'][0]['StableElecTemp'] = str(self.page2.ElecCabTempStable.currentText())

        # this section dumps data from page 6 into the JSON.
        # PlantPLC Table dump to JSON
        it = self.page6.PlantPLCTable.item(0, 0)
        if it and it.text():
            reportdata['PLCStatus'][0]['BeltRunning'][0]['Current'] = str(self.page6.PlantPLCTable.item(0, 0).text())
            reportdata['PLCStatus'][0]['BeltRunning'][0]['1RepAgo'] = str(self.page6.PlantPLCTable.item(0, 1).text())
            reportdata['PLCStatus'][0]['BeltRunning'][0]['2RepAgo'] = str(self.page6.PlantPLCTable.item(0, 2).text())
            reportdata['PLCStatus'][0]['BeltRunning'][0]['Comment'] = str(self.page6.PlantPLCTable.item(0, 3).text())
            reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Current'] = str(self.page6.PlantPLCTable.item(1, 0).text())
            reportdata['PLCStatus'][0]['ForceAnalyse'][0]['1RepAgo'] = str(self.page6.PlantPLCTable.item(1, 1).text())
            reportdata['PLCStatus'][0]['ForceAnalyse'][0]['2RepAgo'] = str(self.page6.PlantPLCTable.item(1, 2).text())
            reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Comment'] = str(self.page6.PlantPLCTable.item(1, 3).text())
            reportdata['PLCStatus'][0]['ForceStandardise'][0]['Current'] = str(self.page6.PlantPLCTable.item(2, 0).text())
            reportdata['PLCStatus'][0]['ForceStandardise'][0]['1RepAgo'] = str(self.page6.PlantPLCTable.item(2, 1).text())
            reportdata['PLCStatus'][0]['ForceStandardise'][0]['2RepAgo'] = str(self.page6.PlantPLCTable.item(2, 2).text())
            reportdata['PLCStatus'][0]['ForceStandardise'][0]['Comment'] = str(self.page6.PlantPLCTable.item(2, 3).text())
        else:
            print("passing by")

        # AnalyserStatus Table dump to JSON
        it = self.page6.PlantPLCTable_2.item(0, 0)
        if it and it.text():
            reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(0, 0).text())
            reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(0, 1).text())
            reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(0, 2).text())
            reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(0, 3).text())
            reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(1, 0).text())
            reportdata['AnalyserStatus'][0]['StandardsOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(1, 1).text())
            reportdata['AnalyserStatus'][0]['StandardsOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(1, 2).text())
            reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(1, 3).text())
            reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(2, 0).text())
            reportdata['AnalyserStatus'][0]['IOControlOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(2, 1).text())
            reportdata['AnalyserStatus'][0]['IOControlOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(2, 2).text())
            reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(2, 3).text())
            reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(3, 0).text())
            reportdata['AnalyserStatus'][0]['SpectraStable'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(3, 1).text())
            reportdata['AnalyserStatus'][0]['SpectraStable'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(3, 2).text())
            reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(3, 3).text())
        else:
            print("passing by")

        # PLC Analyser Results Table dump to JSON
        it = self.page6.PlantPLCTable_3.item(0, 0)
        if it and it.text():
            reportdata['PLCResults'][0]['SystemOK'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(0, 0).text())
            reportdata['PLCResults'][0]['SystemOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(0, 1).text())
            reportdata['PLCResults'][0]['SystemOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(0, 2).text())
            reportdata['PLCResults'][0]['SystemOK'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(0, 3).text())
            reportdata['PLCResults'][0]['SourceControlFault'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(1, 0).text())
            reportdata['PLCResults'][0]['SourceControlFault'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(1, 1).text())
            reportdata['PLCResults'][0]['SourceControlFault'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(1, 2).text())
            reportdata['PLCResults'][0]['SourceControlFault'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(1, 3).text())
            reportdata['PLCResults'][0]['SourceOff'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(2, 0).text())
            reportdata['PLCResults'][0]['SourceOff'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(2, 1).text())
            reportdata['PLCResults'][0]['SourceOff'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(2, 2).text())
            reportdata['PLCResults'][0]['SourceOff'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(2, 3).text())
            reportdata['PLCResults'][0]['SourceOn'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(3, 0).text())
            reportdata['PLCResults'][0]['SourceOn'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(3, 1).text())
            reportdata['PLCResults'][0]['SourceOn'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(3, 2).text())
            reportdata['PLCResults'][0]['SourceOn'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(3, 3).text())
        else:
            print("passing by")

        # Analyser Configuration Table dump to JSON
        it = self.page6.PlantPLCTable_4.item(0, 0)
        if it and it.text():
            reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Current'] = str(self.page6.PlantPLCTable_4.item(0, 0).text())
            reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_4.item(0, 1).text())
            reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_4.item(0, 2).text())
            reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Comment'] = str(self.page6.PlantPLCTable_4.item(0, 3).text())
            reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Current'] = str(self.page6.PlantPLCTable_4.item(1, 0).text())
            reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_4.item(1, 1).text())
            reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_4.item(1, 2).text())
            reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Comment'] = str(self.page6.PlantPLCTable_4.item(1, 3).text())
            reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Current'] = str(self.page6.PlantPLCTable_4.item(2, 0).text())
            reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_4.item(2, 1).text())
            reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_4.item(2, 2).text())
            reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Comment'] = str(self.page6.PlantPLCTable_4.item(2, 3).text())
        else:
            print("passing by")

        # Standardisation Table dump to JSON
        it = self.page6.PlantPLCTable_5.item(0, 0)
        if it and it.text():
            reportdata['Standardisation'][0]['FirstStandardTime'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(0, 0).text())
            reportdata['Standardisation'][0]['FirstStandardTime'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(0, 1).text())
            reportdata['Standardisation'][0]['FirstStandardTime'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(0, 2).text())
            reportdata['Standardisation'][0]['FirstStandardTime'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(0, 3).text())
            reportdata['Standardisation'][0]['MostRecentStandard'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(1, 0).text())
            reportdata['Standardisation'][0]['MostRecentStandard'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(1, 1).text())
            reportdata['Standardisation'][0]['MostRecentStandard'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(1, 2).text())
            reportdata['Standardisation'][0]['MostRecentStandard'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(1, 3).text())
            reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(2, 0).text())
            reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(2, 1).text())
            reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(2, 2).text())
            reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(2, 3).text())
            reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(3, 0).text())
            reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(3, 1).text())
            reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(3, 2).text())
            reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(3, 3).text())
        else:
            print("passing by")

        # SSoftware Versions Table dump to JSON
        it = self.page6.PlantPLCTable_6.item(0, 0)
        if it and it.text():
            reportdata['SoftwareVersions'][0]['Product'][0]['Current'] = str(self.page6.PlantPLCTable_6.item(0, 0).text())
            reportdata['SoftwareVersions'][0]['Product'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_6.item(0, 1).text())
            reportdata['SoftwareVersions'][0]['Product'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_6.item(0, 2).text())
            reportdata['SoftwareVersions'][0]['Product'][0]['Comment'] = str(self.page6.PlantPLCTable_6.item(0, 3).text())
            reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Current'] = str(self.page6.PlantPLCTable_6.item(1, 0).text())
            reportdata['SoftwareVersions'][0]['CsSchedule'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_6.item(1, 1).text())
            reportdata['SoftwareVersions'][0]['CsSchedule'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_6.item(1, 2).text())
            reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Comment'] = str(self.page6.PlantPLCTable_6.item(1, 3).text())
        else:
            print("passing by")

        it = self.page6.PlantPLCTable_7.item(0, 0)
        if it and it.text():
            reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Current'] = str(self.page6.PlantPLCTable_7.item(0, 0).text())
            reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_7.item(0, 1).text())
            reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_7.item(0, 2).text())
            reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Comment'] = str(self.page6.PlantPLCTable_7.item(0, 3).text())
            reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Current'] = str(self.page6.PlantPLCTable_7.item(1, 0).text())
            reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_7.item(1, 1).text())
            reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_7.item(1, 2).text())
            reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Comment'] = str(self.page6.PlantPLCTable_7.item(1, 3).text())
        else:
            print("passing by")

        # This section encodes the plots into the JSON File for transmission to engineer
        # encode Temperature Plot for storage in JSON
        with open(ReadInData.resourcepath + "\\Temperatures.png", mode="rb") as tf:
             data = base64.b64encode(tf.read()).decode("utf-8")
        reportdata['Plots'][0]['TempPlot'] = data
        with open("ReportData.json",'w') as file:
            json.dump(reportdata, file, indent=1)

        # Decode Temperature plot data and produce image
        imgfile = ReadInData.resourcepath + "\\Temperatures_output.png"
        print(imgfile)
        imgdata = reportdata['Plots'][0]['TempPlot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()

        # encode Detector Stability Plot for storage in JSON
        with open(ReadInData.resourcepath + "\\Detector_Stability.png", mode="rb") as tf:
            data = base64.b64encode(tf.read()).decode("utf-8")
        reportdata['Plots'][0]['DetStabPlot'] = data
        with open("ReportData.json", 'w') as file:
            json.dump(reportdata, file, indent=1)

        # Decode Detector Stability plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = ReadInData.resourcepath + "\\Detector Stability_output.png"
        print(imgfile)
        imgdata = reportdata['Plots'][0]['DetStabPlot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()

        # encode Daily Tonnes Plot for storage in JSON
        with open(ReadInData.resourcepath + "\\Daily_Tonnes.png", mode="rb") as tf:
            data = base64.b64encode(tf.read()).decode("utf-8")
        reportdata['Plots'][0]['DailyTonsPlot'] = data
        with open("ReportData.json", 'w') as file:
            json.dump(reportdata, file, indent=1)

        # Decode Daily Tonnes plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = ReadInData.resourcepath + "\\Daily_Tonnes_output.png"
        print(imgfile)
        imgdata = reportdata['Plots'][0]['DailyTonsPlot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()

        # encode Results 1 Plot for storage in JSON
        with open(ReadInData.resourcepath + "\\Results1.png", mode="rb") as tf:
            data = base64.b64encode(tf.read()).decode("utf-8")
        reportdata['Plots'][0]['Results1Plot'] = data
        with open("ReportData.json", 'w') as file:
            json.dump(reportdata, file, indent=1)

        # Decode Results 1 plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = ReadInData.resourcepath + "\\Results1_output.png"
        print(imgfile)
        imgdata = reportdata['Plots'][0]['Results1Plot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()

        # encode Results 2 Plot for storage in JSON
        with open(ReadInData.resourcepath + "\\Results2.png", mode="rb") as tf:
            data = base64.b64encode(tf.read()).decode("utf-8")
        reportdata['Plots'][0]['Results2Plot'] = data
        with open("ReportData.json", 'w') as file:
            json.dump(reportdata, file, indent=1)

        # Decode Results 2 plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = ReadInData.resourcepath + "\\Results2_output.png"
        print(imgfile)
        imgdata = reportdata['Plots'][0]['Results2Plot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()



        print("Exit JSON")

    def updatehome(self):
        anal = self.AnalyserListComboBox.currentText()

        # Updates labels on Home Screen
        anallabel = 'Do you wish to process ' + str(anal) + "?"
        self.AnalyserToBeProcessed.setText(anallabel)
        calibrator = self.CalibratorListComboBox.currentText()
        callabel = "Welcome " + calibrator
        self.WelcomeText.setText(callabel)

    # Only called when the New Report button Pressed
    def updateReport(self):
        print ("Entering Update report")
        # Update data accordingly
        anal = self.AnalyserListComboBox.currentText()
        repdate = str(datetime.date.today()) # egt todays date
        serveng = ReadInData.PSAMasterData.loc[ReadInData.PSAMasterData["Analyser Number"] == anal, "Service Engineer"].to_string(index=False) #get the service engineer as a string without dataframe nonsense
        application = ReadInData.PSAMasterData.loc[ReadInData.PSAMasterData["Analyser Number"] == anal, "Application"].to_string(index=False) #get the service engineer as a string without dataframe nonsense
        customer = ReadInData.PSAMasterData.loc[ReadInData.PSAMasterData["Analyser Number"] == anal, "Customer Name"].to_string(index=False) #get the service engineer as a string without dataframe nonsense

        # Update UI
        self.page1.rep_analyser_data.setText(anal)
        self.page1.rep_date_data.setText(repdate)
        self.page1.rep_serv_eng_data.setText(serveng)
        self.page1.rep_app_data.setText(application)
        self.page1.site_name.setText(customer)
        self.page1.period_data.setText(self.RepPeriod())
        self.page1.email_data.setText(self.RepEmail())
        self.page1.disp_stduptodate.setText(self.StdDate())
        self.page1.disp_endiskspc.setText(self.DiskSpaceOK())
        self.UpdateDetStab()
        self.UpdatePg6()
        self.UpdateFigs()

    def EnabledYes(self):
        enabled = "Yes"
        enableditem = QTableWidgetItem(enabled)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        enableditem.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        enableditem.setForeground(brush)
        return enableditem

    def EnabledNo(self):
        enabled = "No"
        enableditem = QTableWidgetItem(enabled)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        enableditem.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        enableditem.setForeground(brush)
        return enableditem

    def ClearTable(self):
        enabled = ""
        enableditem = QTableWidgetItem(enabled)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        enableditem.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        enableditem.setForeground(brush)
        return enableditem

    def UpdatePg6(self):

        # Update PLC Status Table
        BeltRunning = QTableWidgetItem(ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "BeltRunning","Value"].to_string(index=False))
        ForceAnalyse = QTableWidgetItem(ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "ForceAnalyse", "Value"].to_string(index=False))
        ForceStandardise = QTableWidgetItem(ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "ForceStandardise", "Value"].to_string(index=False))

        self.page6.PlantPLCTable.setItem(0, 0, BeltRunning)
        self.page6.PlantPLCTable.setItem(1, 0, ForceAnalyse)
        self.page6.PlantPLCTable.setItem(2, 0, ForceStandardise)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable.setItem(0, 1, QTableWidgetItem(str(reportdata['PLCStatus'][0]['BeltRunning'][0]['1RepAgo'])))
        self.page6.PlantPLCTable.setItem(1, 1, QTableWidgetItem(str(reportdata['PLCStatus'][0]['ForceAnalyse'][0]['1RepAgo'])))
        self.page6.PlantPLCTable.setItem(2, 1, QTableWidgetItem(str(reportdata['PLCStatus'][0]['ForceStandardise'][0]['1RepAgo'])))
        self.page6.PlantPLCTable.setItem(0, 2, QTableWidgetItem(str(reportdata['PLCStatus'][0]['BeltRunning'][0]['2RepAgo'])))
        self.page6.PlantPLCTable.setItem(1, 2, QTableWidgetItem(str(reportdata['PLCStatus'][0]['ForceAnalyse'][0]['2RepAgo'])))
        self.page6.PlantPLCTable.setItem(2, 2, QTableWidgetItem(str(reportdata['PLCStatus'][0]['ForceStandardise'][0]['2RepAgo'])))
        self.page6.PlantPLCTable.setItem(0, 3, QTableWidgetItem(str(reportdata['PLCStatus'][0]['BeltRunning'][0]['Comment'])))
        self.page6.PlantPLCTable.setItem(1, 3, QTableWidgetItem(str(reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Comment'])))
        self.page6.PlantPLCTable.setItem(2, 3, QTableWidgetItem(str(reportdata['PLCStatus'][0]['ForceStandardise'][0]['Comment'])))
        # Update Analyser Status Table
        AnalyserOK = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "AnalyserOK","Value"].to_string(index=False))
        StandardsOK = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "StandardsOK","Value"].to_string(index=False))
        IOControlOK = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "IOControlOK","Value"].to_string(index=False))
        SpectraStable = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "SpectraStable", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_2.setItem(0, 0, AnalyserOK)
        self.page6.PlantPLCTable_2.setItem(1, 0, StandardsOK)
        self.page6.PlantPLCTable_2.setItem(2, 0, IOControlOK)
        self.page6.PlantPLCTable_2.setItem(3, 0, SpectraStable)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable_2.setItem(0, 1, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(1, 1, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['StandardsOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(2, 1, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['IOControlOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(3, 1, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['SpectraStable'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(0, 2, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(1, 2, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['StandardsOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(2, 2, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['IOControlOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(3, 2, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['SpectraStable'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(0, 3, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Comment'])))
        self.page6.PlantPLCTable_2.setItem(1, 3, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Comment'])))
        self.page6.PlantPLCTable_2.setItem(2, 3, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Comment'])))
        self.page6.PlantPLCTable_2.setItem(3, 3, QTableWidgetItem(str(reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Comment'])))

        # Update PLC Analyser Results
        SystemOK = QTableWidgetItem(ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "SystemRunning","Value"].to_string(index=False))
        if ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "SourceControlFault", "Value"].to_string(index=False) == "   OK\nFALSE":
            SourceControlFault = QTableWidgetItem("FALSE")
        else:
            SourceControlFault = QTableWidgetItem("TRUE")
        SourceOff = QTableWidgetItem(ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "SourceOffProx", "Value"].to_string(index=False))
        SourceOn = QTableWidgetItem(ReadInData.AnalyserIO.loc[ReadInData.AnalyserIO["Parameter Name"] == "SourceOnProx", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_3.setItem(0, 0, SystemOK)
        self.page6.PlantPLCTable_3.setItem(1, 0, SourceControlFault)
        self.page6.PlantPLCTable_3.setItem(2, 0, SourceOff)
        self.page6.PlantPLCTable_3.setItem(3, 0, SourceOn)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable_3.setItem(0, 1, QTableWidgetItem(str(reportdata['PLCResults'][0]['SystemOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(1, 1, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceControlFault'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(2, 1, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceOff'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(3, 1, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceOn'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(0, 2, QTableWidgetItem(str(reportdata['PLCResults'][0]['SystemOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(1, 2, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceControlFault'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(2, 2, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceOff'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(3, 2, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceOn'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(0, 3, QTableWidgetItem(str(reportdata['PLCResults'][0]['SystemOK'][0]['Comment'])))
        self.page6.PlantPLCTable_3.setItem(1, 3, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceControlFault'][0]['Comment'])))
        self.page6.PlantPLCTable_3.setItem(2, 3, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceOff'][0]['Comment'])))
        self.page6.PlantPLCTable_3.setItem(3, 3, QTableWidgetItem(str(reportdata['PLCResults'][0]['SourceOn'][0]['Comment'])))

        # Update Analyser Config Table
        AnalysisPeriod = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "AnalysisPeriod","Value"].to_string(index=False))
        AnalMinLoadLimit = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "AnalMinLoadLimit","Value"].to_string(index=False))
        StandardisePeriod = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "StandardisePeriod","Value"].to_string(index=False))
        self.page6.PlantPLCTable_4.setItem(0, 0, AnalysisPeriod)
        self.page6.PlantPLCTable_4.setItem(1, 0, AnalMinLoadLimit)
        self.page6.PlantPLCTable_4.setItem(2, 0, StandardisePeriod)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable_4.setItem(0, 1, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(1, 1, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(2, 1, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(0, 2, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(1, 2, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(2, 2, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(0, 3, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Comment'])))
        self.page6.PlantPLCTable_4.setItem(1, 3, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Comment'])))
        self.page6.PlantPLCTable_4.setItem(2, 3, QTableWidgetItem(str(reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Comment'])))

        # Update Standardisation Table
        FirstStandard = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "FirstStandardTime","Value"].to_string(index=False))
        LastStandard = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "LastStandardiseTime","Value"].to_string(index=False))
        NumStandard = QTableWidgetItem(ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "PeriodCount","Value"].to_string(index=False))
        NumStandardMonth = QTableWidgetItem("PlaceHolder")
        self.page6.PlantPLCTable_5.setItem(0, 0, FirstStandard)
        self.page6.PlantPLCTable_5.setItem(1, 0, LastStandard)
        self.page6.PlantPLCTable_5.setItem(2, 0, NumStandard)
        self.page6.PlantPLCTable_5.setItem(3, 0, NumStandardMonth)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable_5.setItem(0, 1, QTableWidgetItem(str(reportdata['Standardisation'][0]['FirstStandardTime'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(1, 1, QTableWidgetItem(str(reportdata['Standardisation'][0]['MostRecentStandard'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(2, 1, QTableWidgetItem(str(reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(3, 1, QTableWidgetItem(str(reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(0, 2, QTableWidgetItem(str(reportdata['Standardisation'][0]['FirstStandardTime'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(1, 2, QTableWidgetItem(str(reportdata['Standardisation'][0]['MostRecentStandard'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(2, 2, QTableWidgetItem(str(reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(3, 2, QTableWidgetItem(str(reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(0, 3, QTableWidgetItem(str(reportdata['Standardisation'][0]['FirstStandardTime'][0]['Comment'])))
        self.page6.PlantPLCTable_5.setItem(1, 3, QTableWidgetItem(str(reportdata['Standardisation'][0]['MostRecentStandard'][0]['Comment'])))
        self.page6.PlantPLCTable_5.setItem(2, 3, QTableWidgetItem(str(reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Comment'])))
        self.page6.PlantPLCTable_5.setItem(3, 3, QTableWidgetItem(str(reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Comment'])))


        # Update Software Versions Table
        Product = QTableWidgetItem(ReadInData.VersionNumbers.loc[ReadInData.VersionNumbers["Module"] == "Product","Version"].to_string(index=False))
        CsSchedule = QTableWidgetItem(ReadInData.VersionNumbers.loc[ReadInData.VersionNumbers["Module"] == "CsSchedule","Version"].to_string(index=False))
        self.page6.PlantPLCTable_6.setItem(0, 0, Product)
        self.page6.PlantPLCTable_6.setItem(1, 0, CsSchedule)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable_6.setItem(0, 1, QTableWidgetItem(str(reportdata['SoftwareVersions'][0]['Product'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(1, 1, QTableWidgetItem(str(reportdata['SoftwareVersions'][0]['CsSchedule'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(0, 2, QTableWidgetItem(str(reportdata['SoftwareVersions'][0]['Product'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(1, 2, QTableWidgetItem(str(reportdata['SoftwareVersions'][0]['CsSchedule'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(0, 3, QTableWidgetItem(str(reportdata['SoftwareVersions'][0]['Product'][0]['Comment'])))
        self.page6.PlantPLCTable_6.setItem(1, 3, QTableWidgetItem(str(reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Comment'])))


        # Update Disk Space Table
        DiskSpace = QTableWidgetItem(ReadInData.VersionNumbers.loc[ReadInData.VersionNumbers["Module"] == "DiskSpace","Version"].to_string(index=False))
        PercDiskSpace = QTableWidgetItem(ReadInData.VersionNumbers.loc[ReadInData.VersionNumbers["Module"] == "%DiskSpace","Version"].to_string(index=False))
        self.page6.PlantPLCTable_7.setItem(0, 0, DiskSpace)
        self.page6.PlantPLCTable_7.setItem(1, 0, PercDiskSpace)
        # Creating the comment item and populating with Blanks
        self.page6.PlantPLCTable_7.setItem(0, 1, QTableWidgetItem(str(reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(1, 1, QTableWidgetItem(str(reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(0, 2, QTableWidgetItem(str(reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(1, 2, QTableWidgetItem(str(reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(0, 3, QTableWidgetItem(str(reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Comment'])))
        self.page6.PlantPLCTable_7.setItem(1, 3, QTableWidgetItem(str(reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Comment'])))

    def UpdatePg6_1RepAgo(self):
        # **********************************************************************************************************************************************
        # This section defines the filename where we need to pull the relevant PSAreport.xls file from in order to update the 1 Report Ago data
        # **********************************************************************************************************************************************
        anal = self.AnalyserListComboBox.currentText()
        # Switches default folder based on which analyser is selected.
        if anal[0:3] == "C15":
            fname = QFileDialog.getExistingDirectory(self,"Open PSA File in PSA Folder","J:\\Client Analysers\\NG-1500")
        elif anal[0:3] == "C21":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\CS-2100")
        elif anal[0:3] == "CMM":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\CMM-100")
        elif anal[0:3] == "OBA":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\On Belt Analyser")
        elif anal[0:3] == "TBM":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\TBM-210")
        else:
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\TBM-230")

        # ensures the file separators are correct for operating system
        if fname:
            fname = QDir.toNativeSeparators(fname)
            fname = glob.glob(fname + "\\*Report.xls")
            fname = fname[0]

        # if user presses cancel, return control to calling function
        if not fname:
            return

        # **************************************************************************************************************************************************
        # This section imports the relevant data into the required data frames
        # **************************************************************************************************************************************************
        print ("Filename is: " + str(fname))
        # Import the Analyser Status sheet from the PSAReport.xls file in the relevant folder defined by fname
        StatusColumns1RA = ["Result Name", "Value"]
        AnalyserStatus1RA = pd.read_excel(open(fname, 'rb'), sheet_name="Analyser Status")
        AnalyserStatusdf1RA = pd.DataFrame(AnalyserStatus1RA, columns=StatusColumns1RA)

        # Import the Analyser IO sheet from the PSAReport.xls file in the relevant folder defined by fname
        StatusColumns1RA = ["Parameter Name", "Value"]
        AnalyserIO1RA = pd.read_excel(open(fname, 'rb'), sheet_name="Analyser I_O")
        AnalyserIOdf1RA = pd.DataFrame(AnalyserIO1RA, columns=StatusColumns1RA)

        # Import the Version Numbers sheet from the PSAReport.xls file in the relevant folder defined by fname
        StatusColumns1RA = ["Module", "Version"]
        VersionNumbers1RA = pd.read_excel(open(fname, 'rb'), sheet_name="Version Numbers")
        VersionNumbersdf1RA = pd.DataFrame(VersionNumbers1RA, columns=StatusColumns1RA)

        # **************************************************************************************************************************************************
        # This section updates the 1 Report ago section of the Page 6 status tables using the dataframes defined earlier
        # **************************************************************************************************************************************************

        # Update PLC Status Table
        BeltRunning = QTableWidgetItem(AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "BeltRunning", "Value"].to_string(index=False))
        ForceAnalyse = QTableWidgetItem(AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "ForceAnalyse", "Value"].to_string(index=False))
        ForceStandardise = QTableWidgetItem(AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "ForceStandardise", "Value"].to_string(index=False))

        self.page6.PlantPLCTable.setItem(0, 1, BeltRunning)
        self.page6.PlantPLCTable.setItem(1, 1, ForceAnalyse)
        self.page6.PlantPLCTable.setItem(2, 1, ForceStandardise)

        # Update Analyser Status Table
        AnalyserOK = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "AnalyserOK", "Value"].to_string(index=False))
        StandardsOK = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "StandardsOK", "Value"].to_string(index=False))
        IOControlOK = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "IOControlOK", "Value"].to_string(index=False))
        SpectraStable = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "SpectraStable", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_2.setItem(0, 1, AnalyserOK)
        self.page6.PlantPLCTable_2.setItem(1, 1, StandardsOK)
        self.page6.PlantPLCTable_2.setItem(2, 1, IOControlOK)
        self.page6.PlantPLCTable_2.setItem(3, 1, SpectraStable)

        # Update PLC Analyser Results
        SystemOK = QTableWidgetItem(AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "SystemRunning", "Value"].to_string(index=False))
        if AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "SourceControlFault", "Value"].to_string(index=False) == "   OK\nFALSE":
            SourceControlFault = QTableWidgetItem("FALSE")
        else:
            SourceControlFault = QTableWidgetItem("TRUE")
        SourceOff = QTableWidgetItem(AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "SourceOffProx", "Value"].to_string(index=False))
        SourceOn = QTableWidgetItem(AnalyserIOdf1RA.loc[AnalyserIOdf1RA["Parameter Name"] == "SourceOnProx", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_3.setItem(0, 1, SystemOK)
        self.page6.PlantPLCTable_3.setItem(1, 1, SourceControlFault)
        self.page6.PlantPLCTable_3.setItem(2, 1, SourceOff)
        self.page6.PlantPLCTable_3.setItem(3, 1, SourceOn)

        # Update Analyser Config Table
        AnalysisPeriod = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "AnalysisPeriod", "Value"].to_string(index=False))
        AnalMinLoadLimit = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "AnalMinLoadLimit", "Value"].to_string(index=False))
        StandardisePeriod = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "StandardisePeriod", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_4.setItem(0, 1, AnalysisPeriod)
        self.page6.PlantPLCTable_4.setItem(1, 1, AnalMinLoadLimit)
        self.page6.PlantPLCTable_4.setItem(2, 1, StandardisePeriod)

        # Update Standardisation Table
        FirstStandard = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "FirstStandardTime", "Value"].to_string(index=False))
        LastStandard = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "LastStandardiseTime", "Value"].to_string(index=False))
        NumStandard = QTableWidgetItem(AnalyserStatusdf1RA.loc[AnalyserStatusdf1RA["Result Name"] == "PeriodCount", "Value"].to_string(index=False))
        NumStandardMonth = QTableWidgetItem("PlaceHolder")
        self.page6.PlantPLCTable_5.setItem(0, 1, FirstStandard)
        self.page6.PlantPLCTable_5.setItem(1, 1, LastStandard)
        self.page6.PlantPLCTable_5.setItem(2, 1, NumStandard)
        self.page6.PlantPLCTable_5.setItem(3, 1, NumStandardMonth)

        # Update Software Versions Table
        Product = QTableWidgetItem(VersionNumbersdf1RA.loc[VersionNumbersdf1RA["Module"] == "Product", "Version"].to_string(index=False))
        CsSchedule = QTableWidgetItem(VersionNumbersdf1RA.loc[VersionNumbersdf1RA["Module"] == "CsSchedule", "Version"].to_string(index=False))
        self.page6.PlantPLCTable_6.setItem(0, 1, Product)
        self.page6.PlantPLCTable_6.setItem(1, 1, CsSchedule)

        # Update Disk Space Table
        DiskSpace = QTableWidgetItem(VersionNumbersdf1RA.loc[VersionNumbersdf1RA["Module"] == "DiskSpace", "Version"].to_string(index=False))
        PercDiskSpace = QTableWidgetItem(VersionNumbersdf1RA.loc[VersionNumbersdf1RA["Module"] == "%DiskSpace", "Version"].to_string(index=False))
        self.page6.PlantPLCTable_7.setItem(0, 1, DiskSpace)
        self.page6.PlantPLCTable_7.setItem(1, 1, PercDiskSpace)

    def UpdatePg6_2RepAgo(self):
        # **********************************************************************************************************************************************
        # This section defines the filename where we need to pull the relevant PSAreport.xls file from in order to update the 1 Report Ago data
        # **********************************************************************************************************************************************
        anal = self.AnalyserListComboBox.currentText()
        # Switches default folder based on which analyser is selected.
        if anal[0:3] == "C15":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\NG-1500")
        elif anal[0:3] == "C21":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\CS-2100")
        elif anal[0:3] == "CMM":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\CMM-100")
        elif anal[0:3] == "OBA":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\On Belt Analyser")
        elif anal[0:3] == "TBM":
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\TBM-210")
        else:
            fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder", "J:\\Client Analysers\\TBM-230")

        # ensures the file separators are correct for operating system
        if fname:
            fname = QDir.toNativeSeparators(fname)
            fname = glob.glob(fname + "\\*Report.xls")
            fname = fname[0]

        # if user presses cancel, return control to calling function
        if not fname:
            return

        # **************************************************************************************************************************************************
        # This section imports the relevant data into the required data frames
        # **************************************************************************************************************************************************
        print("Filename is: " + str(fname))
        # Import the Analyser Status sheet from the PSAReport.xls file in the relevant folder defined by fname
        StatusColumns2RA = ["Result Name", "Value"]
        AnalyserStatus2RA = pd.read_excel(open(fname, 'rb'), sheet_name="Analyser Status")
        AnalyserStatusdf2RA = pd.DataFrame(AnalyserStatus2RA, columns=StatusColumns2RA)

        # Import the Analyser IO sheet from the PSAReport.xls file in the relevant folder defined by fname
        StatusColumns2RA = ["Parameter Name", "Value"]
        AnalyserIO2RA = pd.read_excel(open(fname, 'rb'), sheet_name="Analyser I_O")
        AnalyserIOdf2RA = pd.DataFrame(AnalyserIO2RA, columns=StatusColumns2RA)

        # Import the Version Numbers sheet from the PSAReport.xls file in the relevant folder defined by fname
        StatusColumns2RA = ["Module", "Version"]
        VersionNumbers2RA = pd.read_excel(open(fname, 'rb'), sheet_name="Version Numbers")
        VersionNumbersdf2RA = pd.DataFrame(VersionNumbers2RA, columns=StatusColumns2RA)

        # **************************************************************************************************************************************************
        # This section updates the 1 Report ago section of the Page 6 status tables using the dataframes defined earlier
        # **************************************************************************************************************************************************

        # Update PLC Status Table
        BeltRunning = QTableWidgetItem(AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "BeltRunning", "Value"].to_string(index=False))
        ForceAnalyse = QTableWidgetItem(AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "ForceAnalyse", "Value"].to_string(index=False))
        ForceStandardise = QTableWidgetItem(AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "ForceStandardise", "Value"].to_string(index=False))

        self.page6.PlantPLCTable.setItem(0, 2, BeltRunning)
        self.page6.PlantPLCTable.setItem(1, 2, ForceAnalyse)
        self.page6.PlantPLCTable.setItem(2, 2, ForceStandardise)

        # Update Analyser Status Table
        AnalyserOK = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "AnalyserOK", "Value"].to_string(index=False))
        StandardsOK = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "StandardsOK", "Value"].to_string(index=False))
        IOControlOK = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "IOControlOK", "Value"].to_string(index=False))
        SpectraStable = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "SpectraStable", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_2.setItem(0, 2, AnalyserOK)
        self.page6.PlantPLCTable_2.setItem(1, 2, StandardsOK)
        self.page6.PlantPLCTable_2.setItem(2, 2, IOControlOK)
        self.page6.PlantPLCTable_2.setItem(3, 2, SpectraStable)

        # Update PLC Analyser Results
        SystemOK = QTableWidgetItem(AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "SystemRunning", "Value"].to_string(index=False))
        if AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "SourceControlFault", "Value"].to_string(index=False) == "   OK\nFALSE":
            SourceControlFault = QTableWidgetItem("FALSE")
        else:
            SourceControlFault = QTableWidgetItem("TRUE")
        SourceOff = QTableWidgetItem(AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "SourceOffProx", "Value"].to_string(index=False))
        SourceOn = QTableWidgetItem(AnalyserIOdf2RA.loc[AnalyserIOdf2RA["Parameter Name"] == "SourceOnProx", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_3.setItem(0, 2, SystemOK)
        self.page6.PlantPLCTable_3.setItem(1, 2, SourceControlFault)
        self.page6.PlantPLCTable_3.setItem(2, 2, SourceOff)
        self.page6.PlantPLCTable_3.setItem(3, 2, SourceOn)

        # Update Analyser Config Table
        AnalysisPeriod = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "AnalysisPeriod", "Value"].to_string(index=False))
        AnalMinLoadLimit = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "AnalMinLoadLimit", "Value"].to_string(index=False))
        StandardisePeriod = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "StandardisePeriod", "Value"].to_string(index=False))
        self.page6.PlantPLCTable_4.setItem(0, 2, AnalysisPeriod)
        self.page6.PlantPLCTable_4.setItem(1, 2, AnalMinLoadLimit)
        self.page6.PlantPLCTable_4.setItem(2, 2, StandardisePeriod)

        # Update Standardisation Table
        FirstStandard = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "FirstStandardTime", "Value"].to_string(index=False))
        LastStandard = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "LastStandardiseTime", "Value"].to_string(index=False))
        NumStandard = QTableWidgetItem(AnalyserStatusdf2RA.loc[AnalyserStatusdf2RA["Result Name"] == "PeriodCount", "Value"].to_string(index=False))
        NumStandardMonth = QTableWidgetItem("PlaceHolder")
        self.page6.PlantPLCTable_5.setItem(0, 2, FirstStandard)
        self.page6.PlantPLCTable_5.setItem(1, 2, LastStandard)
        self.page6.PlantPLCTable_5.setItem(2, 2, NumStandard)
        self.page6.PlantPLCTable_5.setItem(3, 2, NumStandardMonth)

        # Update Software Versions Table
        Product = QTableWidgetItem(VersionNumbersdf2RA.loc[VersionNumbersdf2RA["Module"] == "Product", "Version"].to_string(index=False))
        CsSchedule = QTableWidgetItem(VersionNumbersdf2RA.loc[VersionNumbersdf2RA["Module"] == "CsSchedule", "Version"].to_string(index=False))
        self.page6.PlantPLCTable_6.setItem(0, 2, Product)
        self.page6.PlantPLCTable_6.setItem(1, 2, CsSchedule)

        # Update Disk Space Table
        DiskSpace = QTableWidgetItem(VersionNumbersdf2RA.loc[VersionNumbersdf2RA["Module"] == "DiskSpace", "Version"].to_string(index=False))
        PercDiskSpace = QTableWidgetItem(VersionNumbersdf2RA.loc[VersionNumbersdf2RA["Module"] == "%DiskSpace", "Version"].to_string(index=False))
        self.page6.PlantPLCTable_7.setItem(0, 2, DiskSpace)
        self.page6.PlantPLCTable_7.setItem(1, 2, PercDiskSpace)

    # used in Update report
    def UpdateFigs(self):
        self.page2.label_3.setPixmap(QtGui.QPixmap(ReadInData.resourcepath + "\\Detector_Stability.png"))
        self.page3.Temps.setPixmap(QtGui.QPixmap(ReadInData.resourcepath + "\\Temperatures.png"))
        self.page3.label_4.setPixmap(QtGui.QPixmap(ReadInData.resourcepath + "\\Daily_Tonnes.png"))
        self.page4.Results1.setPixmap(QtGui.QPixmap(ReadInData.resourcepath + "\\Results1.png"))
        self.page5.Results2.setPixmap(QtGui.QPixmap(ReadInData.resourcepath + "\\Results2.png"))

    # used in Update report
    def UpdateDetStab(self):
        # calculate the number of detecotrs
        Dets = ReadInData.PeakControl.shape[1]-2

        # clear the table each time the function is called.
        for i in range(16):
            self.page2.tableWidget.setItem(0, i, self.ClearTable())
            self.page2.tableWidget.setItem(1, i, self.ClearTable())

        x=0
        # update the detecotr status table based on the totoal number of detectors.
        while x < Dets:
            # read in the detector disabled status
            disabled = ReadInData.PeakControl.loc[ReadInData.PeakControl["Result Name"] == "DetectorDisabled", "Detector "+str(x+1)].to_string(index=False)
            # read in the detector Stability status
            stablity = ReadInData.PeakControl.iloc[21, x+1]

            # Choose which colour and wording to update the Detector enabled row of detecotr stability table with
            if disabled == "FALSE":
                value = self.EnabledYes()
            else:
                value = self.EnabledNo()
            # update the Enabled / Disabled row of the detector stability table with the wording chosen above
            self.page2.tableWidget.setItem(0, x, value)

            # Choose which colour and wording to update the Stability row of detecotr stability table with
            if stablity == "Stable":
                value = self.EnabledYes()
            else:
                value = self.EnabledNo()
            # update the stability row of the detector stability table with the wording chosen above
            self.page2.tableWidget.setItem(1, x, value)
            # incrment the loop counter
            x += 1


    def RepPeriod(self):
        dates = ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "LastPsaReportTime", "Value"] # get the date of the last psa report generation
        dates1 = pd.to_datetime(dates,yearfirst=True)   #setup dataframe as a date time series in the correct format
        Period = dates1.dt.month_name().to_string(index=False) + " " + dates1.dt.year.to_string(index=False) #concatenate the month name and year integer into a string called period using the to_string method to eliminate indexs
        return Period   #return Period to main

    def RepEmail(self):
        anal = self.AnalyserListComboBox.currentText()
        region = ReadInData.PSAMasterData.loc[ReadInData.PSAMasterData["Analyser Number"] == anal, "Region"].to_string(index=False) #get the service engineer as a string without dataframe nonsense
        if region == "Asia":
            email = "service.asia@scantech.com.au"
        elif region == "Australia":
            email = "service.australia@scantech.com.au"
        elif region == "China":
            email = "service.asia@scantech.com.au"
        elif region == "Europe":
            email = "service.europe@scantech.com.au"
        elif region == "India":
            email = "service.india@scantech.com.au"
        elif region == "Middle East & India":
            email = "service.middleeast@scantech.com.au"
        elif region == "New Zealand":
            email = "service.newzealand@scantech.com.au"
        elif region == "North Africa":
            email = "service.northafrica@scantech.com.au"
        elif region == "South Africa":
            email = "service.southafrica@scantech.com.au"
        elif region == "Latin America":
            email = "service.southamerica@scantech.com.au"
        elif region == "USA & Canada":
            email = "service.usa@scantech.com.au"
        else:
            email = "service.fsu@scantech.com.au"

        return email

    def StdDate(self):
        stddate = ReadInData.AnalyserStatus.loc[ReadInData.AnalyserStatus["Result Name"] == "LastStandardiseTime", "Value"] # get the date of the last psa report generation
        stddate = stddate.to_string(index=False)   #setup dataframe as a date time series in the correct format
        stddate = datetime.datetime.strptime(stddate, "%a %y/%m/%d %H:%M")
        tdate = datetime.datetime.today()
        difference = (tdate.year - stddate.year)*12 + (tdate.month-stddate.month)
        if difference > 6:
            output = "No"
        else:
            output = "Yes"

        return output

    def DiskSpaceOK(self):
        diskspace = ReadInData.VersionNumbers.loc[ReadInData.VersionNumbers["Module"] == "%DiskSpace", "Version"]
        diskspace = diskspace.to_string(index=False)
        diskspace = float(diskspace.replace("%",""))
        if diskspace > 10.00 :
            diskspaceok = "Yes"
        else:
            diskspaceok = "No"

        return diskspaceok

    def openReport(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose Report File to Open", "","csv (*.csv)",
        options=options)
        print (fileName)

    def popanalysers(self):
        analysers = ReadInData.PSAMasterData["Analyser Number"]
        analysers.dropna(inplace=True)
        #print(analysers)
        for x in analysers:
            if x == "NaN":
                pass
            elif x == "Template":
                pass
            else:
                self.AnalyserListComboBox.addItem(str(x))

    def hide_pages(self):
        self.page1.hide()
        self.page2.hide()
        self.page3.hide()
        self.page4.hide()
        self.page5.hide()
        self.page6.hide()

    def show_page_1(self):
        self.hide_pages()
        self.page1.show()

    def show_page_2(self):
        self.hide_pages()
        self.page2.show()

    def show_page_3(self):
        self.hide_pages()
        self.page3.show()

    def show_page_4(self):
        self.hide_pages()
        self.page4.show()

    def show_page_5(self):
        self.hide_pages()
        self.page5.show()

    def show_page_6(self):
        self.hide_pages()
        self.page6.show()



class PSA_pg1(QMainWindow,Ui_PSAPage1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class PSA_pg2(QMainWindow,Ui_PSAPage2):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class PSA_pg3(QMainWindow,Ui_PSAPage3):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class PSA_pg4(QMainWindow,Ui_PSAPage4):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class PSA_pg5(QMainWindow,Ui_PSAPage5):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class PSA_pg6(QMainWindow,Ui_PSAPage6):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)





app = QApplication(sys.argv)
window = HomeWindow()
window.show()

app.exec()