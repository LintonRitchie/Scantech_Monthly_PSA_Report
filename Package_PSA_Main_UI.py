import PyInstaller.__main__

PyInstaller.__main__.run([
    "PSA_Main_UI.py",
    '-p C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\',
    '-p C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes\\',
    '-p C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32ctypes\\pywin32\\',
    '-p C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32\\lib\\',
    '-p C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\venv\\Lib\\site-packages\\win32com\\',
    '--debug=all',
    '--windowed',
    '--hiddenimport pywin32',
    '--hiddenimport pywintypes',
    '--hiddenimport pkg_resources',
    '--hiddenimport win32com',
    '--hiddenimport pythoncom'
])