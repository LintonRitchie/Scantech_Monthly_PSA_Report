import sys
from fpdf import FPDF
import pandas as pd
from Regen_UI import regen_ui_eng               # Load the function which runs a batch to regen the UI each time code runs.
# This is used for Development
from Read_Master import (Read_Master, Read_AnalyserStatus, Read_PeakControl, Read_VersionNumbers, Read_AnalyserIO, Read_A_08_Analyse, Read_PeakExtract,
                         Read_TempExtract)  # import the function which reads from the Master PSA file
# from PyQt5.QtGui import (QPixmap)
import datetime
import json
import base64
import glob
from PSA_Home_Eng import Ui_PSAHome
from PSA_Page1_Eng import Ui_PSAPage1
from PSA_Page2_Eng import Ui_PSAPage2
from PSA_Page3_Eng import Ui_PSAPage3
from PSA_Page4_Eng import Ui_PSAPage4
from PSA_Page5_Eng import Ui_PSAPage5
from PSA_Page6_Eng import Ui_PSAPage6
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QTableWidgetItem)
from PyQt5 import (QtCore, QtGui)
from PyQt5.QtCore import QDir
import GeneratePSAReportPDF as genpdf

# regen_ui_eng()                  # Regenerate the UI. This is used to update the UI file after changes

class HomeWindow(QMainWindow,Ui_PSAHome):
    reportdata = []                     # Class Variable for report data to be used throughout the report
    fname = ""                          # Root directory indicator class variable
    fname2 = ""                         # Root directory indicator class variable No.2

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

    def importReport(self):

        fname = QFileDialog.getExistingDirectory(self, "Open PSA File in PSA Folder")

        if fname:
            fname = QDir.toNativeSeparators(fname)
            fname2 = fname
            fname = glob.glob(fname + "\\ReportData.json")
            fname = fname[0]
        # if user presses cancel, return control to calling function
        if not fname:
            return

        with open(fname) as f:
            HomeWindow.reportdata = json.load(f)
        HomeWindow.fname = fname
        HomeWindow.fname2 = fname2
        self.DecodeFigs()
        self.PreviewReportPB.setEnabled(True)

    # Setup Signals and Slots for Pushbuttons
    def connectSignalsSlots(self):
        self.PreviewReportPB.released.connect(self.show_page_1)
        self.PreviewReportPB.clicked.connect(self.updateReport)
        self.PB_pg.released.connect(self.show_page_1)
        self.PB_pg_2.released.connect(self.show_page_2)
        self.PB_pg_3.released.connect(self.show_page_3)
        self.PB_pg_4.released.connect(self.show_page_4)
        self.PB_pg_5.released.connect(self.show_page_5)
        self.PB_pg_6.released.connect(self.show_page_6)
        self.ImportReportPB.released.connect(self.importReport)
        self.page1.NextPage.released.connect(self.UpdateJSON)
        self.page2.NextPage.released.connect(self.UpdateJSON)
        self.page6.NextPage.released.connect(self.UpdateJSON)
        self.ExportReportPB.released.connect(self.Generate_PDF)
        self.page1.NextPage.released.connect(self.reloadJSON)
        self.page2.NextPage.released.connect(self.reloadJSON)


    def reloadJSON(self):
        with open(HomeWindow.fname) as f:
            HomeWindow.reportdata = json.load(f)

    def UpdateJSON(self):
        print("Entering UpdateJSON")
        # Update JSON File
        HomeWindow.reportdata['Summary'][0]['SiteName'] = self.page1.site_name.text()
        HomeWindow.reportdata['Summary'][0]['ReportDate'] = self.page1.rep_date_data.text()
        HomeWindow.reportdata['Summary'][0]['AnalyserNo'] = self.page1.rep_analyser_data.text()
        HomeWindow.reportdata['Summary'][0]['ServEng'] = self.page1.rep_serv_eng_data.text()
        HomeWindow.reportdata['Summary'][0]['Application'] = self.page1.rep_app_data.text()
        HomeWindow.reportdata['Summary'][0]['Period'] = self.page1.period_data.text()
        HomeWindow.reportdata['Summary'][0]['Email'] = self.page1.email_data.text()
        HomeWindow.reportdata['Summary'][0]['NextPSA'] = str(self.page1.NextPSAMnth.currentText() + " " + self.page1.NextPSAYear.currentText())
        HomeWindow.reportdata['Summary'][0]['TopUpDue'] = str(self.page1.TopUpMonth.currentText() + " " + self.page1.TopUpYear.currentText())
        HomeWindow.reportdata['Summary'][0]['AnalyserOpCorrect'] = self.page1.AnalOpCor.currentText()
        HomeWindow.reportdata['Summary'][0]['AllDetStable'] = self.page1.EnableDetStable.currentText()
        HomeWindow.reportdata['Summary'][0]['DetTempStable'] = self.page1.DetEncTempStable.currentText()
        HomeWindow.reportdata['Summary'][0]['ElecTempStable'] = self.page1.ElecEncTempStable.currentText()
        HomeWindow.reportdata['Summary'][0]['STDUpToDate'] = self.page1.disp_stduptodate.text()
        HomeWindow.reportdata['Summary'][0]['EnoughDiskSpace'] = self.page1.disp_endiskspc.text()
        print("Entering Action taken section")

        # this loop populates the JSON by looking to see if any data exists in the first cell of the row. If not then it skips. If is does, the data is pulled into the JSON
        # pull the data from the Action Taken table row 1 to fill the JSON
        for i in range(0,5):
            it = self.page1.ActionTakenTable.item(i, 0)
            if it and it.text():
                jsonid = "Action" + str(i+1)
                HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Date']= str(self.page1.ActionTakenTable.item(i, 0).text())
                HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Time'] = str(self.page1.ActionTakenTable.item(i, 1).text())
                HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Action'] = str(self.page1.ActionTakenTable.item(i, 2).text())
                HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Description'] = str(self.page1.ActionTakenTable.item(i, 3).text())
            else:
                pass
        # this loop populates the JSON by looking to see if any data exists in the first cell of the row. If not then it skips. If is does, the data is pulled into the JSON
        # Populating the Action required section of the JSON file
        for i in range(0,5):

            it = self.page1.ActionRequiredTable.item(i, 0)
            if it and it.text():
                jsonid = "ActionReq" + str(i+1)
                HomeWindow.reportdata['ActionRequired'][0][jsonid][0]['Action'] = str(self.page1.ActionRequiredTable.item(i, 0).text())
                HomeWindow.reportdata['ActionRequired'][0][jsonid][0]['ByWhom'] = str(self.page1.ActionRequiredTable.item(i, 1).text())
                HomeWindow.reportdata['ActionRequired'][0][jsonid][0]['ByWhen'] = str(self.page1.ActionRequiredTable.item(i, 2).text())
            else:
                pass
        # populating JSON with Detector stability info
        for i in range(0,16):
            it = self.page2.tableWidget.item(0, i)
            if it and it.text():
                jsonid = "Detector" + str(i+1)
                HomeWindow.reportdata['DetectorStability'][0][jsonid][0]['Enabled'] = str(self.page2.tableWidget.item(0, i).text())
                HomeWindow.reportdata['DetectorStability'][0][jsonid][0]['Stable'] = str(self.page2.tableWidget.item(1, i).text())
        # pull stability question data from the Temperature stability combo boxes
        HomeWindow.reportdata['Temperatures'][0]['StableDetTemp'] = str(self.page2.DetTempStable.currentText())
        HomeWindow.reportdata['Temperatures'][0]['StableElecTemp'] = str(self.page2.ElecCabTempStable.currentText())
        # this section dumps data from page 6 into the JSON.
        # PlantPLC Table dump to JSON
        it = self.page6.PlantPLCTable.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['Current'] = str(self.page6.PlantPLCTable.item(0, 0).text())
            HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['1RepAgo'] = str(self.page6.PlantPLCTable.item(0, 1).text())
            HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['2RepAgo'] = str(self.page6.PlantPLCTable.item(0, 2).text())
            HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['Comment'] = str(self.page6.PlantPLCTable.item(0, 3).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Current'] = str(self.page6.PlantPLCTable.item(1, 0).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['1RepAgo'] = str(self.page6.PlantPLCTable.item(1, 1).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['2RepAgo'] = str(self.page6.PlantPLCTable.item(1, 2).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Comment'] = str(self.page6.PlantPLCTable.item(1, 3).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['Current'] = str(self.page6.PlantPLCTable.item(2, 0).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['1RepAgo'] = str(self.page6.PlantPLCTable.item(2, 1).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['2RepAgo'] = str(self.page6.PlantPLCTable.item(2, 2).text())
            HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['Comment'] = str(self.page6.PlantPLCTable.item(2, 3).text())
        else:
            print("passing by")
        # AnalyserStatus Table dump to JSON
        it = self.page6.PlantPLCTable_2.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(0, 0).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(0, 1).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(0, 2).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(0, 3).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(1, 0).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(1, 1).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(1, 2).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(1, 3).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(2, 0).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(2, 1).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(2, 2).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(2, 3).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Current'] = str(self.page6.PlantPLCTable_2.item(3, 0).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_2.item(3, 1).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_2.item(3, 2).text())
            HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Comment'] = str(self.page6.PlantPLCTable_2.item(3, 3).text())
        else:
            print("passing by")

        # PLC Analyser Results Table dump to JSON
        it = self.page6.PlantPLCTable_3.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(0, 0).text())
            HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(0, 1).text())
            HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(0, 2).text())
            HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(0, 3).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(1, 0).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(1, 1).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(1, 2).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(2, 0).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(2, 1).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(2, 2).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(2, 3).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['Current'] = str(self.page6.PlantPLCTable_3.item(3, 0).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_3.item(3, 1).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_3.item(3, 2).text())
            HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['Comment'] = str(self.page6.PlantPLCTable_3.item(3, 3).text())
        else:
            print("passing by")

        # Analyser Configuration Table dump to JSON
        it = self.page6.PlantPLCTable_4.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Current'] = str(self.page6.PlantPLCTable_4.item(0, 0).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_4.item(0, 1).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_4.item(0, 2).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Comment'] = str(self.page6.PlantPLCTable_4.item(0, 3).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Current'] = str(self.page6.PlantPLCTable_4.item(1, 0).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_4.item(1, 1).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_4.item(1, 2).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Comment'] = str(self.page6.PlantPLCTable_4.item(1, 3).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Current'] = str(self.page6.PlantPLCTable_4.item(2, 0).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_4.item(2, 1).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_4.item(2, 2).text())
            HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Comment'] = str(self.page6.PlantPLCTable_4.item(2, 3).text())
        else:
            print("passing by")

        # Standardisation Table dump to JSON
        it = self.page6.PlantPLCTable_5.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(0, 0).text())
            HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(0, 1).text())
            HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(0, 2).text())
            HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(0, 3).text())
            HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(1, 0).text())
            HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(1, 1).text())
            HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(1, 2).text())
            HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(1, 3).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(2, 0).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(2, 1).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(2, 2).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(2, 3).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Current'] = str(self.page6.PlantPLCTable_5.item(3, 0).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_5.item(3, 1).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_5.item(3, 2).text())
            HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Comment'] = str(self.page6.PlantPLCTable_5.item(3, 3).text())
        else:
            print("passing by")

        # SSoftware Versions Table dump to JSON
        it = self.page6.PlantPLCTable_6.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['Current'] = str(self.page6.PlantPLCTable_6.item(0, 0).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_6.item(0, 1).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_6.item(0, 2).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['Comment'] = str(self.page6.PlantPLCTable_6.item(0, 3).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Current'] = str(self.page6.PlantPLCTable_6.item(1, 0).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_6.item(1, 1).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_6.item(1, 2).text())
            HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Comment'] = str(self.page6.PlantPLCTable_6.item(1, 3).text())
        else:
            print("passing by")

        it = self.page6.PlantPLCTable_7.item(0, 0)
        if it and it.text():
            HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Current'] = str(self.page6.PlantPLCTable_7.item(0, 0).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_7.item(0, 1).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_7.item(0, 2).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Comment'] = str(self.page6.PlantPLCTable_7.item(0, 3).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Current'] = str(self.page6.PlantPLCTable_7.item(1, 0).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['1RepAgo'] = str(self.page6.PlantPLCTable_7.item(1, 1).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['2RepAgo'] = str(self.page6.PlantPLCTable_7.item(1, 2).text())
            HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Comment'] = str(self.page6.PlantPLCTable_7.item(1, 3).text())
        else:
            print("passing by")
        with open(HomeWindow.fname, 'w') as file:
            json.dump(HomeWindow.reportdata, file, indent=1)

    def DecodeFigs(self):
        # Decode Daily Tonnes plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = HomeWindow.fname2 + "\\ResourcesEng\\Daily_Tonnes_output.png"
        print(imgfile)
        imgdata = HomeWindow.reportdata['Plots'][0]['DailyTonsPlot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()
        # Decode Detector Stability plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = HomeWindow.fname2 + "\\ResourcesEng\\Detector_Stability_output.png"
        print(imgfile)
        imgdata = HomeWindow.reportdata['Plots'][0]['DetStabPlot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()
        # Decode Temperatures plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = HomeWindow.fname2 + "\\ResourcesEng\\Temperatures_output.png"
        print(imgfile)
        imgdata = HomeWindow.reportdata['Plots'][0]['TempPlot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()
        # Decode Results 1 plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = HomeWindow.fname2 + "\\ResourcesEng\\Results1_output.png"
        print(imgfile)
        imgdata = HomeWindow.reportdata['Plots'][0]['Results1Plot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()
        # Decode Results 2 plot data and produce image. This will be commented for testing and used in the Engineer version of the code
        imgfile = HomeWindow.fname2 + "\\ResourcesEng\\Results2_output.png"
        print(imgfile)
        imgdata = HomeWindow.reportdata['Plots'][0]['Results2Plot']
        imgplot = open(imgfile, "wb")
        imgplot.write(base64.b64decode(imgdata))
        imgplot.close()


    # Only called when the New Report button Pressed
    def updateReport(self):
        print ("Entering Update report")
        # Update data accordingly
        repdate = str(datetime.date.today()) # egt todays date
        self.ExportReportPB.setEnabled(True)
        self.PB_pg.setEnabled(True)
        self.PB_pg_2.setEnabled(True)
        self.PB_pg_3.setEnabled(True)
        self.PB_pg_4.setEnabled(True)
        self.PB_pg_5.setEnabled(True)
        self.PB_pg_6.setEnabled(True)
        # Update UI
        self.page1.rep_analyser_data.setText(str(HomeWindow.reportdata['Summary'][0]['AnalyserNo']))
        self.page1.rep_date_data.setText(repdate)
        self.page1.rep_serv_eng_data.setText(str(HomeWindow.reportdata['Summary'][0]['ServEng']))
        self.page1.rep_app_data.setText(str(HomeWindow.reportdata['Summary'][0]['Application']))
        self.page1.site_name.setText(str(HomeWindow.reportdata['Summary'][0]['SiteName']))
        self.page1.period_data.setText(str(HomeWindow.reportdata['Summary'][0]['Period']))
        self.page1.email_data.setText(str(HomeWindow.reportdata['Summary'][0]['Email']))
        self.page1.disp_stduptodate.setText(self.StdDate())
        self.page1.disp_endiskspc.setText(self.DiskSpaceOK())
        self.UpdateDetStab()
        self.UpdatePg1()
        self.UpdatePg6()



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
        self.page6.PlantPLCTable.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['Current'])))
        self.page6.PlantPLCTable.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Current'])))
        self.page6.PlantPLCTable.setItem(2, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['Current'])))
        self.page6.PlantPLCTable.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['1RepAgo'])))
        self.page6.PlantPLCTable.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['1RepAgo'])))
        self.page6.PlantPLCTable.setItem(2, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['1RepAgo'])))
        self.page6.PlantPLCTable.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['2RepAgo'])))
        self.page6.PlantPLCTable.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['2RepAgo'])))
        self.page6.PlantPLCTable.setItem(2, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['2RepAgo'])))
        self.page6.PlantPLCTable.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['BeltRunning'][0]['Comment'])))
        self.page6.PlantPLCTable.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Comment'])))
        self.page6.PlantPLCTable.setItem(2, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCStatus'][0]['ForceStandardise'][0]['Comment'])))

        # Update Analyser Status Table
        self.page6.PlantPLCTable_2.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Current'])))
        self.page6.PlantPLCTable_2.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Current'])))
        self.page6.PlantPLCTable_2.setItem(2, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Current'])))
        self.page6.PlantPLCTable_2.setItem(3, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Current'])))
        self.page6.PlantPLCTable_2.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(2, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(3, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(2, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(3, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_2.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Comment'])))
        self.page6.PlantPLCTable_2.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Comment'])))
        self.page6.PlantPLCTable_2.setItem(2, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Comment'])))
        self.page6.PlantPLCTable_2.setItem(3, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Comment'])))

        # Update PLC Analyser Results
        self.page6.PlantPLCTable_3.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['Current'])))
        self.page6.PlantPLCTable_3.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['Current'])))
        self.page6.PlantPLCTable_3.setItem(2, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['Current'])))
        self.page6.PlantPLCTable_3.setItem(3, 0, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['Current'])))
        self.page6.PlantPLCTable_3.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(2, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(3, 1, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(2, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(3, 2, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_3.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SystemOK'][0]['Comment'])))
        self.page6.PlantPLCTable_3.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceControlFault'][0]['Comment'])))
        self.page6.PlantPLCTable_3.setItem(2, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOff'][0]['Comment'])))
        self.page6.PlantPLCTable_3.setItem(3, 3, QTableWidgetItem(str(HomeWindow.reportdata['PLCResults'][0]['SourceOn'][0]['Comment'])))

        # Update Analyser Config Table
        self.page6.PlantPLCTable_4.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Current'])))
        self.page6.PlantPLCTable_4.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Current'])))
        self.page6.PlantPLCTable_4.setItem(2, 0, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Current'])))
        self.page6.PlantPLCTable_4.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(2, 1, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(2, 2, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_4.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Comment'])))
        self.page6.PlantPLCTable_4.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Comment'])))
        self.page6.PlantPLCTable_4.setItem(2, 3, QTableWidgetItem(str(HomeWindow.reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Comment'])))

        # Update Standardisation Table
        self.page6.PlantPLCTable_5.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['Current'])))
        self.page6.PlantPLCTable_5.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['Current'])))
        self.page6.PlantPLCTable_5.setItem(2, 0, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Current'])))
        self.page6.PlantPLCTable_5.setItem(3, 0, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Current'])))
        self.page6.PlantPLCTable_5.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(2, 1, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(3, 1, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(2, 2, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(3, 2, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_5.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['FirstStandardTime'][0]['Comment'])))
        self.page6.PlantPLCTable_5.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['Comment'])))
        self.page6.PlantPLCTable_5.setItem(2, 3, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Comment'])))
        self.page6.PlantPLCTable_5.setItem(3, 3, QTableWidgetItem(str(HomeWindow.reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Comment'])))


        # Update Software Versions Table
        self.page6.PlantPLCTable_6.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['Current'])))
        self.page6.PlantPLCTable_6.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Current'])))
        self.page6.PlantPLCTable_6.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_6.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['Product'][0]['Comment'])))
        self.page6.PlantPLCTable_6.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Comment'])))


        # Update Disk Space Table
        self.page6.PlantPLCTable_7.setItem(0, 0, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Current'])))
        self.page6.PlantPLCTable_7.setItem(1, 0, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Current'])))
        self.page6.PlantPLCTable_7.setItem(0, 1, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(1, 1, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['1RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(0, 2, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(1, 2, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['2RepAgo'])))
        self.page6.PlantPLCTable_7.setItem(0, 3, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Comment'])))
        self.page6.PlantPLCTable_7.setItem(1, 3, QTableWidgetItem(str(HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Comment'])))


    def UpdatePg1(self):
        print("Updating Pg1")
        psamnth = pd.Series(HomeWindow.reportdata['Summary'][0]['NextPSA'])
        psamnth = pd.to_datetime(psamnth, yearfirst=True)
        psayear = psamnth.dt.year.to_string(index=False)
        psamnth = psamnth.dt.month_name().to_string(index=False)
        topupmnth = pd.Series(HomeWindow.reportdata['Summary'][0]['TopUpDue'])
        topupmnth = pd.to_datetime(topupmnth, yearfirst=True)
        topupyear = topupmnth.dt.year.to_string(index=False)
        topupmnth = topupmnth.dt.month_name().to_string(index=False)
        # insert Next PSA Visit and Source top-up dates from previous report into this report
        self.page1.NextPSAMnth.setCurrentText(psamnth)
        self.page1.NextPSAYear.setCurrentText(psayear)
        self.page1.TopUpMonth.setCurrentText(topupmnth)
        self.page1.TopUpYear.setCurrentText(topupyear)
        # insert previous actions and requirements, from pervious report, into this report.
        for i in range(0, 5):
            jsonid = "Action" + str(i + 1)
            jsonid2 = "ActionReq" + str(i + 1)
            self.page1.ActionTakenTable.setItem(i, 0, QTableWidgetItem(str(HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Date'])))
            self.page1.ActionTakenTable.setItem(i, 1, QTableWidgetItem(str(HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Time'])))
            self.page1.ActionTakenTable.setItem(i, 2, QTableWidgetItem(str(HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Action'])))
            self.page1.ActionTakenTable.setItem(i, 3, QTableWidgetItem(str(HomeWindow.reportdata['ActionTaken'][0][jsonid][0]['Description'])))
            self.page1.ActionRequiredTable.setItem(i, 0, QTableWidgetItem(str(HomeWindow.reportdata['ActionRequired'][0][jsonid2][0]['Action'])))
            self.page1.ActionRequiredTable.setItem(i, 1, QTableWidgetItem(str(HomeWindow.reportdata['ActionRequired'][0][jsonid2][0]['ByWhom'])))
            self.page1.ActionRequiredTable.setItem(i, 2, QTableWidgetItem(str(HomeWindow.reportdata['ActionRequired'][0][jsonid2][0]['ByWhen'])))



    # used in Update report
    def UpdateFigs(self):
        self.page2.label_3.setPixmap(QtGui.QPixmap(HomeWindow.fname2 + "\\ResourcesEng\\Detector_Stability_output.png"))
        self.page3.Temps.setPixmap(QtGui.QPixmap(HomeWindow.fname2 + "\\ResourcesEng\\Temperatures_output.png"))
        self.page3.label_4.setPixmap(QtGui.QPixmap(HomeWindow.fname2 + "\\ResourcesEng\\Daily_Tonnes_output.png"))
        self.page4.Results1.setPixmap(QtGui.QPixmap(HomeWindow.fname2 + "\\ResourcesEng\\Results1_output.png"))
        self.page5.Results2.setPixmap(QtGui.QPixmap(HomeWindow.fname2 + "\\ResourcesEng\\Results2_output.png"))

    # used in Update report
    def UpdateDetStab(self):
        print("Got to here 4.1")
        # calculate the number of detecotrs

        # clear the table each time the function is called.
        for i in range(16):
            self.page2.tableWidget.setItem(0, i, self.ClearTable())
            self.page2.tableWidget.setItem(1, i, self.ClearTable())
        print("Got to here 4.2")
        for i in range(16):
            print("Got to here 4.3."+str(i))
            # read in the detector disabled status from JSON
            detnum = str('Detector'+str(i+1))
            print(detnum)
            disabled = HomeWindow.reportdata['DetectorStability'][0][detnum][0]['Enabled']
            print("Disabled = "+ str(disabled))
            # read in the detector Stability status from JSON
            stability = HomeWindow.reportdata['DetectorStability'][0][detnum][0]['Stable']
            print("Got to here 4.3." + str(i) + ".1")
            # Choose which colour and wording to update the Detector enabled row of detecotr stability table with
            if disabled == "Yes":
                value = self.EnabledYes()
            elif disabled == "No":
                value = self.EnabledNo()
            else:
                pass
            # update the Enabled / Disabled row of the detector stability table with the wording chosen above
            self.page2.tableWidget.setItem(0, i, value)

            # Choose which colour and wording to update the Stability row of detecotr stability table with
            if stability == "Yes":
                value = self.EnabledYes()
            elif stability == "No":
                value = self.EnabledNo()
            else:
                pass
            # update the stability row of the detector stability table with the wording chosen above
            self.page2.tableWidget.setItem(1, i, value)


    def StdDate(self):
        stddate = HomeWindow.reportdata['Standardisation'][0]['MostRecentStandard'][0]['Current']
        print("Got to here 2.1")
        #stddate = stddate.to_string(index=False)   # setup dataframe as a date time series in the correct format
        stddate = datetime.datetime.strptime(stddate, "%a %y/%m/%d %H:%M")
        print("Got to here 2.2")
        tdate = datetime.datetime.today()
        print("Got to here 2.3")
        difference = (tdate.year - stddate.year)*12 + (tdate.month-stddate.month)
        print("Got to here 2.4")
        if difference > 6:
            output = "No"
        else:
            output = "Yes"
        print("Got to here 2.5")
        return output

    def DiskSpaceOK(self):
        diskspace = HomeWindow.reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Current']
        #diskspace = diskspace.to_string(index=False)
        diskspace = float(diskspace.replace("%", ""))
        if diskspace > 10.00:
            diskspaceok = "Yes"
        else:
            diskspaceok = "No"

        return diskspaceok

    def Generate_PDF(self):
        print("Trying to generate a report")
        genpdf.gen_pdf.generate_pdf(self, HomeWindow.fname2)
        print("I managed to generate a report")

    def hide_pages(self):
        self.page1.hide()
        self.page2.hide()
        self.page3.hide()
        self.page4.hide()
        self.page5.hide()
        self.page6.hide()

    def close_pages(self):
        self.page1.close()
        self.page2.close()
        self.page3.close()
        self.page4.close()
        self.page5.close()
        self.page6.close()

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