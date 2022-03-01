import win32com.client # this code works well. Please use
import os
import codecs

signature_path = os.path.join((os.environ['USERPROFILE']),'AppData\Roaming\Microsoft\Signatures\Ext L Ritchie - Scantech Aus_python\\')  # Finds the path to Outlook signature files with signature name "Work"
html_doc = os.path.join((os.environ['USERPROFILE']),'AppData\Roaming\Microsoft\Signatures\Ext L Ritchie - Scantech Aus_python.htm')  # Specifies the name of the HTML version of the stored signature
html_doc = html_doc.replace('\\\\', '\\')  # Removes escape backslashes from path string

html_file = codecs.open(html_doc, 'r', 'utf-8', errors='ignore')  # Opens HTML file and ignores errors
signature_code = html_file.read()  # Writes contents of HTML signature file to a string
signature_code = signature_code.replace('Work_files/', signature_path)  # Replaces local directory with full directory path
html_file.close()


outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0) #This creates the email object. The 0 refers to the item type from the office documentation OlItemType. This can be others eg 1 for appointments, 2 for contacts etc.
mail.To = 'l.ritchie@scantech.com.au'
mail.CC = 'l.balzan@scantech.com.au'
mail.CC = 'l.biggins@scantech.com.au'
mail.Subject = 'This is a Test. dont freak out yet'
mail.BodyFormat = 2
mail.HTMLBody = "<html><body style=font-family:Calibri;> Hi Lucas <br><br> I hope this comes through. I am testing a few automated emailing options. Please let me know if you get this email. <br> There should be an attachment called sales report.pdf </body></html>" + signature_code

mail.Attachments.Add('C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\SalesReport4.pdf')
mail.Display()