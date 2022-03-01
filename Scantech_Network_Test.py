import requests
import subprocess
import os.path
url = "http://www.scantech.com.au"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")


filename = "my_file.txt"
if(os.path.isfile('J:\\Client Analysers\\Analyser PSA Report\\Development\\00-Forms\\PSA_Master_List.xlsx')):
  print("File Exists!!")
else:
  print("File does not exists!!")