import json
import base64

with open("TestData.json") as f:
    reportdata = json.load(f)

inimgfile = "C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Temperatures.png"
outimgfile = "C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Temperatures_output.png"
print(outimgfile)

with open(inimgfile,"rb") as img:
    imgstr = base64.b64encode(img.read()).decode("utf-8")

reportdata["Test"] = imgstr
print(imgstr)

with open ('TestData.json',"w") as file:
    json.dump(reportdata,file)

imgstr2 = reportdata["Test"]
print(imgstr2)
imgplot = open(outimgfile, "wb")
imgplot.write(base64.b64decode(imgstr2))
imgplot.close()