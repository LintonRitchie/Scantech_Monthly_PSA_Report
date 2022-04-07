import fpdf
from fpdf import FPDF
import time
import json
import pandas as pd
import matplotlib.pyplot as plt


def create_letterhead(pdf, WIDTH):
    pdf.image(".\\ResourcesEng\\ScantechReportHeader.png", 0, 0, WIDTH)


def create_title(title, sitename, pdf, date, analyser, serveng, application, period, email, nextpsa, topup):
    # Add main title
    pdf.set_font('Helvetica', 'b', TITLEFONTSIZE)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    pdf.ln(1)
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SUBTITLEFONTSIZE)
    pdf.ln(1)
    pdf.multi_cell(0, 10, sitename, border=0, align='C')
    pdf.ln(1)
    # Date of report from Data File
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(95, 5, "Date: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,date,border=0,align='L',ln=1)
    # Analyser of report from Data File
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(95, 5, "Analyser: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,analyser,border=0,align='L',ln=1)
    # Service Engineer of report from Data File
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(95, 5, "Service Engineer: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,serveng,border=0,align='L',ln=1)
    # Application of report from Data File
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(95, 5, "Application: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,application,border=0,align='L',ln=1)
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    # Period covered of report from Data File
    pdf.cell(95, 5, "Period Covered: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,period,border=0,align='L',ln=1)
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    # Email of report from Data File
    pdf.cell(95, 5, "Email: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,email,border=0,align='L',ln=1)
    # Next PSA Visit Date of report from Data File
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(95, 5, "Next PSA Visit: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,nextpsa,border=0,align='L',ln=1)
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    # Source Top-Up Due Date of report from Data File
    pdf.cell(95, 5, "Source Top-Up Due: ", border=0, align='R')
    # switch off bold for displaying Data
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
    pdf.cell(40,5,topup,border=0,align='L',ln=1)
    pdf.ln(1)

def create_summary():
    pdf.ln(2)
    pdf.set_font('Helvetica', 'bu', SUBTITLEFONTSIZE)
    pdf.cell(95, 5, "Summary ", border=0, align='L', ln=1)
    pdf.ln(2)
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
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

def create_action_taken():
    # Section Title
    pdf.ln(2)
    pdf.set_font('Helvetica', 'bu', SUBTITLEFONTSIZE)
    pdf.cell(95, 5, "Action Taken ", border=0, align='L', ln=1)
    pdf.ln(2)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(25, 5, "Date", border=1, align='C')
    pdf.cell(25, 5, "Time", border=1, align='C')
    pdf.cell(35, 5, "Action", border=1, align='C')
    pdf.cell(105, 5, "Description", border=1, align='C', ln=1)
    # Table row 1
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
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

def create_action_required():
    # Section Title
    pdf.ln(2)
    pdf.set_font('Helvetica', 'bu', SUBTITLEFONTSIZE)
    pdf.cell(95, 5, "Action Required ", border=0, align='L', ln=1)
    pdf.ln(2)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(50, 5, "By Whom", border=1, align='C')
    pdf.cell(35, 5, "By When", border=1, align='C')
    pdf.cell(105, 5, "Description", border=1, align='C', ln=1)
    # Table row 1
    pdf.set_font('Helvetica', '', GENERALFONTSIZE)
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

def create_page_2(title, sitename, analyser):
    # Add main title
    pdf.set_font('Helvetica', 'b', TITLEFONTSIZE)
    pdf.ln(35)
    pdf.multi_cell(0, 10, title, border=0, align='C')
    pdf.ln(1)
    # Add Subtitle
    pdf.set_font('Helvetica', 'b', SUBTITLEFONTSIZE)
    pdf.ln(1)
    pdf.multi_cell(0, 10, analyser + " at " + sitename, border=0, align='C')
    pdf.ln(1)

    # Generate Legend Table
    # Section Title
    pdf.set_font('Helvetica', 'bu', SUBTITLEFONTSIZE)
    pdf.cell(95, 5, "Legend ", border=0, align='L', ln=1)
    pdf.ln(1)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
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
    pdf.set_font('Helvetica', 'bu', SUBTITLEFONTSIZE)
    pdf.cell(95, 5, "Temperature Control ", border=0, align='L', ln=1)
    pdf.ln(2)
    # Table Headers
    pdf.set_font('Helvetica', 'b', GENERALFONTSIZE)
    pdf.cell(50, 5, "", border=1, align='C')
    pdf.cell(50, 5, "Stable?", border=1, align='C', ln=1)
    pdf.cell(50, 5, "Detector Enclosure: ", border=1, align='R')
    if reportdata['Temperatures'][0]["StableDetTemp"] == "Yes":
        pdf.set_fill_color(0, 255, 0)
    elif reportdata['Temperatures'][0]["StableDetTemp"] == "No":
        pdf.set_fill_color(255, 0, 0)
    elif reportdata['Temperatures'][0]["StableDetTemp"] == "Flagged":
        pdf.set_fill_color(255, 165, 0)
    else:
        pdf.set_fill_color(0, 0, 0)
    pdf.cell(50, 5, reportdata['Temperatures'][0]["StableDetTemp"], border=1, align='C', fill=True, ln=1)
    pdf.cell(50, 5, "Electronics Enclosure: ", border=1, align='R')
    if reportdata['Temperatures'][0]["StableElecTemp"] == "Yes":
        pdf.set_fill_color(0, 255, 0)
    elif reportdata['Temperatures'][0]["StableElecTemp"] == "No":
        pdf.set_fill_color(255, 0, 0)
    elif reportdata['Temperatures'][0]["StableElecTemp"] == "Flagged":
        pdf.set_fill_color(255, 165, 0)
    else:
        pdf.set_fill_color(0, 0, 0)
    pdf.cell(50, 5, reportdata['Temperatures'][0]["StableElecTemp"], border=1, align='C', fill=True, ln=1)
    pdf.ln(5)

    # Detector Stability Table
    pdf.set_font('Helvetica', 'bu', SUBTITLEFONTSIZE)
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
        print(check)
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
        print(check)
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

    pdf.image(".\\ResourcesEng\\Detector_Stability_output.png", x=20, w=170)
    pdf.ln(10)




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
with open(".\\ReportData.json","r") as f:
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
pdf = PDF() # A4 (210 by 297 mm)

'''
First Page of PDF
'''
# Add Page
pdf.add_page()

# Add lettterhead and title
create_letterhead(pdf, WIDTH)
create_title(TITLE, SITENAME, pdf, DATE, ANALYSER, SERVENG, APPLICATION, PERIOD, EMAIL, NEXTPSA, TOPUP)
# Populate report page 1
create_summary()
create_action_taken()
create_action_required()

'''
Second Page of PDF
'''
# Add Page
pdf.add_page()

# Add lettterhead
create_letterhead(pdf, WIDTH)

create_page_2(TITLE, SITENAME, ANALYSER)


# Add some words to PDF
write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")

# Add the generated visualisations to the PDF
# pdf.image("./resources/heicoders_annual_sales.png", 5, 200, WIDTH/2-10)
# pdf.image("resources/heicoders_2016_sales_breakdown.png", WIDTH/2, 200, WIDTH/2-10)
# pdf.ln(10)


'''
Second Page of PDF
'''

# Add Page
pdf.add_page()

# Add lettterhead
create_letterhead(pdf, WIDTH)

# Add some words to PDF
pdf.ln(40)
write_to_pdf(pdf, "3. In conclusion, the year-on-year sales of Heicoders Academy continue to show a healthy upward trend. Majority of the sales could be attributed to the global sales which accounts for 58.0% of sales in 2016.")
pdf.ln(15)

# Generate the PDF
pdf.output("annual_performance_report.pdf", 'F')
