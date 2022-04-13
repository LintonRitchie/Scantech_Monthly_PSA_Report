@echo off
cd C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Scripts
pyrcc5 -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSAReportResources_rc.py C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSAReportResources.qrc
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Home_Cal.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Home_Cal.py
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page1.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page1.py
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page2.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page2.py
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page3.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page3.py
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page4.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page4.py
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page5.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page5.py
pyuic5 -x C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page6.ui -o C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Page6.py