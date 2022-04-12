from fpdf import FPDF
import json


def create_letterhead(pdf, WIDTH, fname):
    pdf.image(fname + "\\ScantechReportHeader.png", 0, 0, WIDTH)


def create_title(title, sitename, pdf, date, analyser, serveng, application, period, email, nextpsa, topup, TFS, SFS, GFS):
    # Add main title
    pdf.set_font('Helvetica', 'b', TFS)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    pdf.ln(1)
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SFS)
    pdf.ln(1)
    pdf.multi_cell(0, 10, sitename, border=0, align='C')
    pdf.ln(1)
    # Date of report from Data File
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(95, 5, "Date: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,date,border=0,align='L',ln=1)
    # Analyser of report from Data File
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(95, 5, "Analyser: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,analyser,border=0,align='L',ln=1)
    # Service Engineer of report from Data File
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(95, 5, "Service Engineer: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,serveng,border=0,align='L',ln=1)
    # Application of report from Data File
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(95, 5, "Application: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,application,border=0,align='L',ln=1)
    pdf.set_font('Helvetica', 'b', GFS)
    # Period covered of report from Data File
    pdf.cell(95, 5, "Period Covered: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,period,border=0,align='L',ln=1)
    pdf.set_font('Helvetica', 'b', GFS)
    # Email of report from Data File
    pdf.cell(95, 5, "Email: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,email,border=0,align='L',ln=1)
    # Next PSA Visit Date of report from Data File
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(95, 5, "Next PSA Visit: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,nextpsa,border=0,align='L',ln=1)
    pdf.set_font('Helvetica', 'b', GFS)
    # Source Top-Up Due Date of report from Data File
    pdf.cell(95, 5, "Source Top-Up Due: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(40,5,topup,border=0,align='L',ln=1)
    pdf.ln(1)


def create_summary(pdf, SFS, GFS, reportdata):
    pdf.ln(2)
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Summary ", border=0, align='L', ln=1)
    pdf.ln(2)
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(85, 5,"Is the analyser operating correctly? ",border=1,align='L')
    pdf.cell(35, 5, reportdata['Summary'][0]['AnalyserOpCorrect'], border=1, align='C', ln=1)
    pdf.cell(85, 5,"Are all enabled detectors stable? ",border=1,align='L')
    pdf.cell(35, 5, reportdata['Summary'][0]['AllDetStable'], border=1, align='C', ln=1)
    pdf.cell(85, 5,"Is the detector enclosure temperature stable? ",border=1,align='L')
    pdf.cell(35, 5, reportdata['Summary'][0]['DetTempStable'], border=1, align='C', ln=1)
    pdf.cell(85, 5,"Is the electronics enclosure temperature stable? ",border=1,align='L')
    pdf.cell(35, 5, reportdata['Summary'][0]['ElecTempStable'], border=1, align='C', ln=1)
    pdf.cell(85, 5,"Is the standardisation up to date? ",border=1,align='L')
    pdf.cell(35, 5, reportdata['Summary'][0]['STDUpToDate'], border=1, align='C', ln=1)
    pdf.cell(85, 5,"Is there enough (>10%) disk space available? ",border=1,align='L')
    pdf.cell(35, 5, reportdata['Summary'][0]['EnoughDiskSpace'], border=1, align='C', ln=1)
    pdf.ln(10)


def create_action_taken(pdf, SFS, GFS, reportdata):
    # Section Title
    pdf.ln(2)
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Action Taken ", border=0, align='L', ln=1)
    pdf.ln(2)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(25, 5, "Date", border=1, align='C')
    pdf.cell(25, 5, "Time", border=1, align='C')
    pdf.cell(35, 5, "Action", border=1, align='C')
    pdf.cell(105, 5, "Description", border=1, align='C', ln=1)
    # Table row 1
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action1'][0]["Date"], border=1, align='C')
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action1'][0]["Time"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionTaken'][0]['Action1'][0]["Action"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionTaken'][0]['Action1'][0]["Description"], border=1, align='C', ln=1)
    # Table row 2
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action2'][0]["Date"], border=1, align='C')
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action2'][0]["Time"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionTaken'][0]['Action2'][0]["Action"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionTaken'][0]['Action2'][0]["Description"], border=1, align='C', ln=1)
    # Table row 3
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action3'][0]["Date"], border=1, align='C')
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action3'][0]["Time"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionTaken'][0]['Action3'][0]["Action"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionTaken'][0]['Action3'][0]["Description"], border=1, align='C', ln=1)
    # Table row 4
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action4'][0]["Date"], border=1, align='C')
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action4'][0]["Time"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionTaken'][0]['Action4'][0]["Action"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionTaken'][0]['Action4'][0]["Description"], border=1, align='C', ln=1)
    # Table row 5
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action5'][0]["Date"], border=1, align='C')
    pdf.cell(25, 5, reportdata['ActionTaken'][0]['Action5'][0]["Time"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionTaken'][0]['Action5'][0]["Action"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionTaken'][0]['Action5'][0]["Description"], border=1, align='C', ln=1)
    pdf.ln(10)


def create_action_required(pdf, SFS, GFS, reportdata):
    # Section Title
    pdf.ln(2)
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Action Required ", border=0, align='L', ln=1)
    pdf.ln(2)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(50, 5, "By Whom", border=1, align='C')
    pdf.cell(35, 5, "By When", border=1, align='C')
    pdf.cell(105, 5, "Description", border=1, align='C', ln=1)
    # Table row 1
    pdf.set_font('Helvetica', '', GFS)
    pdf.cell(50, 5, reportdata['ActionRequired'][0]['ActionReq1'][0]["ByWhom"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionRequired'][0]['ActionReq1'][0]["ByWhen"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionRequired'][0]['ActionReq1'][0]["Action"], border=1, align='C', ln=1)
    # Table row 2
    pdf.cell(50, 5, reportdata['ActionRequired'][0]['ActionReq2'][0]["ByWhom"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionRequired'][0]['ActionReq2'][0]["ByWhen"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionRequired'][0]['ActionReq2'][0]["Action"], border=1, align='C', ln=1)
    # Table row 3
    pdf.cell(50, 5, reportdata['ActionRequired'][0]['ActionReq3'][0]["ByWhom"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionRequired'][0]['ActionReq3'][0]["ByWhen"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionRequired'][0]['ActionReq3'][0]["Action"], border=1, align='C', ln=1)
    # Table row 4
    pdf.cell(50, 5, reportdata['ActionRequired'][0]['ActionReq4'][0]["ByWhom"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionRequired'][0]['ActionReq4'][0]["ByWhen"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionRequired'][0]['ActionReq4'][0]["Action"], border=1, align='C', ln=1)
    # Table row 5
    pdf.cell(50, 5, reportdata['ActionRequired'][0]['ActionReq5'][0]["ByWhom"], border=1, align='C')
    pdf.cell(35, 5, reportdata['ActionRequired'][0]['ActionReq5'][0]["ByWhen"], border=1, align='C')
    pdf.cell(105, 5, reportdata['ActionRequired'][0]['ActionReq5'][0]["Action"], border=1, align='C', ln=1)
    pdf.ln(10)


def create_page_2(pdf, TFS, SFS, GFS, reportdata, title, sitename, analyser, fname):
    # Add main title
    pdf.set_font('Helvetica', 'b', TFS)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    pdf.ln(1)
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SFS)
    pdf.ln(1)
    pdf.multi_cell(0, 10, analyser + " at " + sitename, border=0, align='C')
    pdf.ln(1)

    # Generate Legend Table
    # Section Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Legend ", border=0, align='L', ln=1)
    pdf.ln(1)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(50, 5, "Normal", border=1, align='C')
    pdf.cell(50, 5, "Situation Flagged", border=1, align='C')
    pdf.cell(50, 5, "Requires Urgent Attention", border=1, align='C', ln=1)
    # Set Legend Colours
    pdf.set_fill_color(0, 255, 0)
    pdf.cell(50, 5, "", border=1, align='C', fill=True)
    pdf.set_fill_color(255, 165, 0)
    pdf.cell(50, 5, "", border=1, align='C', fill=True)
    pdf.set_fill_color(255, 0, 0)
    pdf.cell(50, 5, "", border=1, align='C', fill=True, ln=1)
    pdf.ln(5)

    # Temperature Control Table
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Temperature Control ", border=0, align='L', ln=1)
    pdf.ln(2)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GFS)
    pdf.cell(50, 5, "", border=1, align='C')
    pdf.cell(50, 5, "Stable?", border=1, align='C', ln=1)
    pdf.cell(50, 5, "Detector Enclosure: ", border=1, align='R')
    check = reportdata['Temperatures'][0]["StableDetTemp"]
    if check == "Yes":
        pdf.set_fill_color(0, 255, 0)
    elif check == "No":
        pdf.set_fill_color(255, 0, 0)
    elif check == "Flagged":
        pdf.set_fill_color(255, 165, 0)
    else:
        pdf.set_fill_color(0, 0, 0)
    pdf.cell(50, 5, check, border=1, align='C', fill=True, ln=1)
    pdf.cell(50, 5, "Electronics Enclosure: ", border=1, align='R')
    check = reportdata['Temperatures'][0]["StableElecTemp"]
    if check == "Yes":
        pdf.set_fill_color(0, 255, 0)
    elif check == "No":
        pdf.set_fill_color(255, 0, 0)
    elif check == "Flagged":
        pdf.set_fill_color(255, 165, 0)
    else:
        pdf.set_fill_color(0, 0, 0)
    pdf.cell(50, 5, check, border=1, align='C', fill=True, ln=1)
    pdf.ln(5)

    # Detector Stability Table
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Detector Stability (at the time the report was compiled)", border=0, align='L', ln=1)
    pdf.ln(2)

    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(25, 5, "", border=0, align='C')
    for i in range(0, 16):
        detl= "Det "+ str(i + 1)
        pdf.cell(10, 5, detl, border=1, align='C')
    pdf.ln(5)
    # Enabled Data
    pdf.cell(25, 5, "Enabled?", border=1, align='C')
    pdf.set_font('Helvetica', '', 8)
    for i in range(0, 16):
        det = "Detector" + str(i + 1)
        check = reportdata['DetectorStability'][0][det][0]['Enabled']

        if check == "Yes":
            pdf.set_fill_color(0, 255, 0)
        elif check == "No":
            pdf.set_fill_color(255, 0, 0)
        elif check == "Flagged":
            pdf.set_fill_color(255, 165, 0)
        else:
            pdf.set_fill_color(160, 160, 160)
        pdf.cell(10, 5, check, border=1, align='C', fill=True)
    pdf.ln(5)
    # Stable Data
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(25, 5, "Stable?", border=1, align='C')
    pdf.set_font('Helvetica', '', 8)
    for i in range(0, 16):
        det = "Detector" + str(i + 1)
        check = reportdata['DetectorStability'][0][det][0]['Stable']

        if check == "Yes":
            pdf.set_fill_color(0, 255, 0)
        elif check == "No":
            pdf.set_fill_color(255, 0, 0)
        elif check == "Flagged":
            pdf.set_fill_color(255, 165, 0)
        else:
            pdf.set_fill_color(160, 160, 160)
        pdf.cell(10, 5, check, border=1, align='C', fill=True)
    pdf.ln(10)

    pdf.image(fname + "\\Detector_Stability_output.png", x=20, w=170)
    pdf.ln(10)


def create_page_3(pdf, TFS, SFS, title, sitename, analyser, fname):
    # Add main title
    pdf.set_font('Helvetica', 'b', TFS)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')

    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SFS)
    pdf.multi_cell(0, 10, analyser + " at " + sitename, border=0, align='C')
    pdf.image(fname + "\\Temperatures_output.png", x=5, w=200)
    pdf.image(fname + "\\Daily_Tonnes_output.png", x=5, w=200, h=110)
    pdf.ln(1)


def create_page_4(pdf, TFS, SFS, title, sitename, analyser, fname):
    # Add main title
    pdf.set_font('Helvetica', 'b', TFS)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SFS)
    # Results 1 tables image
    pdf.multi_cell(0, 10, analyser + " at " + sitename, border=0, align='C')
    pdf.image(fname + "\\Results1_output.png", x=20, w=170, h=210)


def create_page_5(pdf, TFS, SFS, title, sitename, analyser, fname):
    # Add main title
    pdf.set_font('Helvetica', 'b', TFS)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SFS)
    pdf.multi_cell(0, 10, analyser + " at " + sitename, border=0, align='C')
    # Results 2 tables image
    pdf.image(fname + "\\Results2_output.png", x=20, w=170, h=210)
    pdf.ln(1)


def create_page_6(pdf, TFS, SFS, reportdata, title, sitename, analyser):
    # Add main title
    pdf.set_font('Helvetica', 'b', TFS)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SFS)
    pdf.multi_cell(0, 10, analyser + " at " + sitename, border=0, align='C')
    # PLC Plant Status Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Plant PLC Status", border=0, align='L', ln=1)
    pdf.ln(2)

    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "Belt Running", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['BeltRunning'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['BeltRunning'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['BeltRunning'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCStatus'][0]['BeltRunning'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Force Analyse", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['ForceAnalyse'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['ForceAnalyse'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCStatus'][0]['ForceAnalyse'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Force Standardise", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['ForceStandardise'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['ForceStandardise'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCStatus'][0]['ForceStandardise'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCStatus'][0]['ForceStandardise'][0]['Comment'], border=1, align='C', ln=1)
    pdf.ln(2)
    # Analyser Status Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Analyser Status", border=0, align='L', ln=1)
    pdf.ln(2)
    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "Analyser OK", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserStatus'][0]['AnalyserOK'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Standards OK", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['StandardsOK'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['StandardsOK'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserStatus'][0]['StandardsOK'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "IO Control OK", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['IOControlOK'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['IOControlOK'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserStatus'][0]['IOControlOK'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Spectra Stable", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['SpectraStable'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserStatus'][0]['SpectraStable'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserStatus'][0]['SpectraStable'][0]['Comment'], border=1, align='C', ln=1)
    pdf.ln(2)

    # PLC Analyser Results Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "PLC Analyser Results", border=0, align='L', ln=1)
    pdf.ln(2)

    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "System OK", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SystemOK'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SystemOK'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SystemOK'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCResults'][0]['SystemOK'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Source Control Fault", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceControlFault'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceControlFault'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceControlFault'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCResults'][0]['SourceControlFault'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Source Off", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceOff'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceOff'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceOff'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCResults'][0]['SourceOff'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Source On", border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceOn'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceOn'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['PLCResults'][0]['SourceOn'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['PLCResults'][0]['SourceOn'][0]['Comment'], border=1, align='C', ln=1)
    pdf.ln(2)
    # Analyser Configuration Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Analyser Configuration", border=0, align='L', ln=1)
    pdf.ln(2)
    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "Analysis Period", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserConfiguration'][0]['AnalysisPeriod'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Analysis Min Load Limit", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserConfiguration'][0]['AnalMinLoadLimit'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Standardise Period", border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['AnalyserConfiguration'][0]['StandardisePeriod'][0]['Comment'], border=1, align='C', ln=1)
    pdf.ln(2)
    # Standardisation Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Standardisation", border=0, align='L', ln=1)
    pdf.ln(2)
    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "System OK", border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['FirstStandardTime'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['FirstStandardTime'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['FirstStandardTime'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['Standardisation'][0]['FirstStandardTime'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Source Control Fault", border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['MostRecentStandard'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['MostRecentStandard'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['MostRecentStandard'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['Standardisation'][0]['MostRecentStandard'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Source Off", border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['Standardisation'][0]['NumStdPeriodsSinceClear'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "Source On", border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['Standardisation'][0]['NumStdPeriodsThisMnth'][0]['Comment'], border=1, align='C', ln=1)
    pdf.ln(2)
    # Software Versions Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Software Versions", border=0, align='L', ln=1)
    pdf.ln(2)
    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "Product", border=1, align='C')
    pdf.cell(30, 5, reportdata['SoftwareVersions'][0]['Product'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['SoftwareVersions'][0]['Product'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['SoftwareVersions'][0]['Product'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['SoftwareVersions'][0]['Product'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "CsSchedule", border=1, align='C')
    pdf.cell(30, 5, reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['SoftwareVersions'][0]['CsSchedule'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['SoftwareVersions'][0]['CsSchedule'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['SoftwareVersions'][0]['CsSchedule'][0]['Comment'], border=1, align='C', ln=1)
    pdf.ln(2)
    # Disk Space & Memory Remaining Table
    # Title
    pdf.set_font('Helvetica', 'bu', SFS)
    pdf.cell(95, 5, "Disk Space & Mem Rem", border=0, align='L', ln=1)
    pdf.ln(2)
    # Populate table
    # headings
    pdf.set_font('Helvetica', 'b', 8)
    pdf.cell(35, 5, "", border=0, align='C')
    pdf.cell(30, 5, "Current", border=1, align='C')
    pdf.cell(30, 5, "1 Report Ago", border=1, align='C')
    pdf.cell(30, 5, "2 Reports Ago", border=1, align='C')
    pdf.cell(65, 5, "Comment", border=1, align='C')
    pdf.ln(5)
    # Data
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(35, 5, "Disk Space", border=1, align='C')
    pdf.cell(30, 5, reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['DiskSpaceMem'][0]['DiskSpace'][0]['Comment'], border=1, align='C', ln=1)
    pdf.cell(35, 5, "% Disk Space", border=1, align='C')
    pdf.cell(30, 5, reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Current'], border=1, align='C')
    pdf.cell(30, 5, reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['1RepAgo'], border=1, align='C')
    pdf.cell(30, 5, reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['2RepAgo'], border=1, align='C')
    pdf.cell(65, 5, reportdata['DiskSpaceMem'][0]['PercDiskSpace'][0]['Comment'], border=1, align='C', ln=1)


def write_to_pdf(pdf, words):
    # Set text colour, font size, and font type
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font('Helvetica', '', 12)

    pdf.write(5, words)


class PDF(FPDF):

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


class gen_pdf():

    def generate_pdf(self, fname, root):
        print(fname)
        fname2 = fname + "\\ReportData.json"
        print(fname2)
        with open(fname2, "r") as f:
            reportdata = json.load(f)

        # Global Variables
        TITLEFONTSIZE = 20
        SUBTITLEFONTSIZE = 14
        GENERALFONTSIZE = 10
        TITLE = "PSA Report"
        SITENAME = reportdata['Summary'][0]['SiteName']
        WIDTH = 210
        HEIGHT = 297
        DATE = reportdata['Summary'][0]['ReportDate']
        ANALYSER = reportdata['Summary'][0]['AnalyserNo']
        SERVENG = reportdata['Summary'][0]['ServEng']
        APPLICATION = reportdata['Summary'][0]['Application']
        PERIOD = reportdata['Summary'][0]['Period']
        EMAIL = reportdata['Summary'][0]['Email']
        NEXTPSA = reportdata['Summary'][0]['NextPSA']
        TOPUP = reportdata['Summary'][0]['TopUpDue']

        # Create PDF
        pdf = PDF()  # A4 (210 by 297 mm)

        '''
        First Page of PDF
        '''
        # Add Page
        pdf.add_page()

        # Add lettterhead and title
        create_letterhead(pdf, WIDTH, root)
        create_title(TITLE, SITENAME, pdf, DATE, ANALYSER, SERVENG, APPLICATION, PERIOD, EMAIL, NEXTPSA, TOPUP, TITLEFONTSIZE, SUBTITLEFONTSIZE, GENERALFONTSIZE)
        # Populate report page 1
        create_summary(pdf, SUBTITLEFONTSIZE, GENERALFONTSIZE, reportdata)
        create_action_taken(pdf, SUBTITLEFONTSIZE, GENERALFONTSIZE, reportdata)
        create_action_required(pdf, SUBTITLEFONTSIZE, GENERALFONTSIZE, reportdata)
        print("Completed creation of page 1")
        '''
        Second Page of PDF
        '''
        # Add Page
        pdf.add_page()
        # Add lettterhead
        create_letterhead(pdf, WIDTH, root)
        # Populate Page 2
        create_page_2(pdf, TITLEFONTSIZE, SUBTITLEFONTSIZE, GENERALFONTSIZE, reportdata, TITLE, SITENAME, ANALYSER, root)
        print("Completed creation of page 2")
        '''
        Third Page of PDF
        '''
        # Add Page
        pdf.add_page()
        # Add lettterhead
        create_letterhead(pdf, WIDTH, root)
        # Populate Page 3
        create_page_3(pdf, TITLEFONTSIZE, SUBTITLEFONTSIZE, TITLE, SITENAME, ANALYSER, root)
        print("Completed creation of page 3")
        '''
        Fourth Page of PDF
        '''
        # Add Page
        pdf.add_page()
        # Add lettterhead
        create_letterhead(pdf, WIDTH, root)
        # Populate Page 4
        create_page_4(pdf, TITLEFONTSIZE, SUBTITLEFONTSIZE, TITLE, SITENAME, ANALYSER, root)
        print("Completed creation of page 4")
        '''
        Fifth Page of PDF
        '''
        # Add Page
        pdf.add_page()
        # Add lettterhead
        create_letterhead(pdf, WIDTH, root)
        # Populate Page 5
        create_page_5(pdf, TITLEFONTSIZE, SUBTITLEFONTSIZE, TITLE, SITENAME, ANALYSER, root)
        print("Completed creation of page 5")
        '''
        Sixth Page of PDF
        '''
        # Add Page
        pdf.add_page()
        # Add lettterhead
        create_letterhead(pdf, WIDTH, root)
        # Populate Page 6
        create_page_6(pdf, TITLEFONTSIZE, SUBTITLEFONTSIZE, reportdata, TITLE, SITENAME, ANALYSER)
        print("Completed creation of page 6")

        # Generate the PDF
        print(fname)
        pdfname = fname + "\\" + ANALYSER + " PSA Report " + reportdata['Summary'][0]['Period'] + ".pdf"
        pdf.output(pdfname, 'F')


