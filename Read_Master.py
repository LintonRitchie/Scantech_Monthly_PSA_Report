import matplotlib.style
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
from PyQt5.QtCore import QDir


def Read_Master(PSAMaster):
    data_required = ["Analyser Number", "Customer Name", "Service Engineer", "Application", "PSA Expiry Date", "Region",
                     "PSA Report Required?", "Calibrator"]
    data = pd.read_excel(open(PSAMaster,'rb'), sheet_name="AnalyserDetails")
    df = pd.DataFrame(data, columns= data_required)
    return df

def Read_AnalyserStatus(folder):
    fname = glob.glob(folder + "\\*Report.xls")
    fname=fname[0]
    StatusColumns = ["Result Name", "Value"]
    AnalyserStatus = pd.read_excel(open(fname,'rb'), sheet_name="Analyser Status")
    AnalyserStatusdf = pd.DataFrame(AnalyserStatus, columns= StatusColumns)
    return AnalyserStatusdf

def Read_AnalyserIO(folder):
    fname = folder + "\\PSAReport.xls"
    StatusColumns = ["Parameter Name", "Value"]
    AnalyserIO = pd.read_excel(open(fname,'rb'), sheet_name="Analyser I_O")
    AnalyserIOdf = pd.DataFrame(AnalyserIO, columns= StatusColumns)
    return AnalyserIOdf

def Read_VersionNumbers(folder):
    fname = folder + "\\PSAReport.xls"
    StatusColumns = ["Module", "Version"]
    VersionNumbers = pd.read_excel(open(fname,'rb'), sheet_name="Version Numbers")
    VersionNumbersdf = pd.DataFrame(VersionNumbers, columns= StatusColumns)
    return VersionNumbersdf

def Read_PeakControl(folder):
    fname = glob.glob(folder + "\\*Report.xls")
    fname=fname[0]
    PeakControl = pd.read_excel(open(fname,'rb'), sheet_name="Peak Control")
    PeakControldf = pd.DataFrame(PeakControl)
    return PeakControldf

def Read_PeakExtract(folder):     #extracting the peak control data for determining detector stability

    fname = folder + "\PeakExtract.csv"

    # read the csv containing the data. Since the 1st row is stupidly setup with tab & comma seperators as well as incomplete headings, we have to ignore it.
    PeakExtract = pd.read_csv(open(fname,'rb'), skiprows=1,header=None)

    # determine how many detectors are present
    ndets = (PeakExtract.shape[1]-2)/7

    # simplify dataframe with only detector stability data for the relevant number of detectors

    if ndets == 1:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 2:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 3:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 4:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25]])     # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4"]            # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 5:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 6:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 7:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 8:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 9:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 10:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 11:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10", "Det11"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 12:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10", "Det11", "Det12"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 13:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10", "Det11", "Det12", "Det13"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 14:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10", "Det11", "Det12", "Det13", "Det14"]  # renaming the columns of the new dataframe created for detector stability values only.

    elif ndets == 15:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95, 102]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10", "Det11", "Det12", "Det13", "Det14", "Det15"]  # renaming the columns of the new dataframe created for detector stability values only.

    else:
        PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95, 102, 109]])  # extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
        PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4", "Det5", "Det6", "Det7", "Det8", "Det9", "Det10", "Det11", "Det12", "Det13", "Det14", "Det15", "Det16"]  # renaming the columns of the new dataframe created for detector stability values only.

    DetStab = PeakExtractdf.plot().get_figure()                         # plot the data
    plt.title("Detector Stability")                                     # add a title
    plt.xticks(rotation=90)                                             # rotate the X axis titles
    DetStab.savefig("C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Detector_Stability.png")     # save the plot to file

    return PeakExtractdf

def Read_TempExtract(folder):                                                 # extracting the temperature staibility data for the month
    fname = folder + "\TempExtract.csv"
    TempExtract = pd.read_csv(open(fname,'rb'), index_col=0)                              # read the csv containing the data
    # print(TempExtract)
    TempExtractdf = pd.DataFrame(TempExtract.iloc[:, [1,2,3]])          # extract the 3 columns of Temperature data.
    TempExtractdf.columns = ["Detector", "Cabinet", "Ambient"]          # renaming the columns of the new dataframe created for detector stability values only.
    # print(TempExtractdf)
    TempStab = TempExtractdf.plot(figsize=(10,5)).get_figure()          # plot the data
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=3, mode="expand", borderaxespad=0)                  # places the legend above the plot
    plt.title("Temperature Stability", pad=30)                          # add a title
    plt.ylim(0,50)                                                      # extend the y axis limits
    plt.yticks(np.arange(0, 50, step=5))                                # setup the y axis ticks correctly
    plt.grid(which='both', axis="y")                                    # display the axis ticks
    # plt.xticks(rotation=90)                                           # rotate the X axis titles
    #plt.show()                                                          # show the plot
    TempStab.savefig("C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Temperatures.png")                      # save the plot to file
    return TempExtractdf

def Read_A_08_Analyse(folder):                                          # extracting the analysis results summary for the month
    # implments a wildcard search for analysis data. This can be A_01__Analyse or A_0X__Analyse or anything in between
    fname = glob.glob(folder + "\A*Analyse.csv")
    fname = QDir.toNativeSeparators(fname[0])           # esnure folder path in correct windows format

    AllExtract = pd.read_csv(open(fname,'r'),header=0, index_col=False)                              # read the csv containing the data. Index Col must = false to ensure the headings are not shifted

    # Columns Check for Tonnage data
    if "S034" in AllExtract.columns:            # check S034 in the array
        if "S029" in AllExtract.columns:        # Check S029 in the array
            TonsAnalysed = AllExtract.groupby('Date')[['S034','S029']].sum()    # perform the Tonnage total with S034 & S029
        else:
            TonsAnalysed = AllExtract.groupby('Date')[['S034']].sum()           # else perform with just S034
    else:
        TonsAnalysed = pd.DataFrame(columns=["S034","S029"])                    # else produce blank array

    # Plot Daily tonns as a stacked histograme of Tons Analsyed and TOns not analysed
    plt.figure(figsize=(10,6))
    plt.tick_params(axis='x', which='both',labelsize=5,labelrotation=45,grid_color='grey', grid_alpha=0.8)
    plt.title("Total Daily Tonnes", pad=30)
    plt.grid(which='both', axis='y')
    plt.bar(TonsAnalysed.index, TonsAnalysed["S029"], 0.4, color = 'red', label='Tons not Analysed',zorder=1)
    plt.bar(TonsAnalysed.index,TonsAnalysed["S034"],0.4,bottom=TonsAnalysed["S029"],color = 'green', label='Tons Analysed',zorder=2)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0)                  # places the legend above the plot
    plt.savefig("C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Daily_Tonnes.png")
    plt.close()

    # Parameters for controlling Results plots
    lsize = 8
    lrot = 90
    gcol = 'grey'
    galpha = 0.1
    tpad = 5
    figw = 10
    figh = 15

    # read in the correct results to plot

    columns1 = [1, 3, 4, 5, 6, 7, 8]
    df = AllExtract.iloc[:,columns1]

    # Plot First 3 results for report as a single figure with 3 subplots
    Results = df.groupby('Date').mean()

    # Setup the figure to be the size defined earlier
    fig = plt.figure(figsize=(figw,figh))

    # Plot First Result
    ax1 = fig.add_subplot(311)
    ax1.plot(Results.iloc[:,0])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title(str(Results.columns[0]), pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Second Result
    ax2 = fig.add_subplot(312)
    ax2.plot(Results.iloc[:,1])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title(str(Results.columns[1]), pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Third Result
    ax3 = fig.add_subplot(313)
    ax3.plot(Results.iloc[:,2])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title(str(Results.columns[2]), pad=tpad)
    plt.grid(which='both', axis='y')

    plt.subplots_adjust(bottom=0.07,top=0.97, hspace=0.5)

    plt.savefig("C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Results1.png")
    plt.close()

    fig = plt.figure(figsize=(figw,figh))

    # Plot First Result
    ax1 = fig.add_subplot(311)
    ax1.plot(Results.iloc[:,3])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title(str(Results.columns[3]), pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Second Result
    ax2 = fig.add_subplot(312)
    ax2.plot(Results.iloc[:,4])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title(str(Results.columns[4]), pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Third Result
    ax3 = fig.add_subplot(313)
    ax3.plot(Results.iloc[:,5])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title(str(Results.columns[5]), pad=tpad)
    plt.grid(which='both', axis='y')

    plt.subplots_adjust(bottom=0.07,top=0.97, hspace=0.5)

    plt.savefig("C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\Resources\\Results2.png")
    plt.close()
    print("Read Master Complete")


#Read_A_08_Analyse()