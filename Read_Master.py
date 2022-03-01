import matplotlib.style
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Read_Master():
    data_required = ["Analyser Number", "Customer Name", "Service Engineer", "Application", "PSA Expiry Date", "Region",
                     "PSA Report Required?", "Calibrator"]
    data = pd.read_excel(r"C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSA_Master_List.xlsx", sheet_name="AnalyserDetails")
    df = pd.DataFrame(data, columns= data_required)
    return df

def Read_AnalyserStatus():
    StatusColumns = ["Result Name", "Value"]
    AnalyserStatus = pd.read_excel(r"C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSAReport.xls", sheet_name="Analyser Status")
    AnalyserStatusdf = pd.DataFrame(AnalyserStatus, columns= StatusColumns)
    return AnalyserStatusdf

def Read_AnalyserIO():
    StatusColumns = ["Parameter Name", "Value"]
    AnalyserIO = pd.read_excel(r"C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSAReport.xls", sheet_name="Analyser I_O")
    AnalyserIOdf = pd.DataFrame(AnalyserIO, columns= StatusColumns)
    return AnalyserIOdf

def Read_VersionNumbers():
    StatusColumns = ["Module", "Version"]
    VersionNumbers = pd.read_excel(r"C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSAReport.xls", sheet_name="Version Numbers")
    VersionNumbersdf = pd.DataFrame(VersionNumbers, columns= StatusColumns)
    return VersionNumbersdf

def Read_PeakControl():
    PeakControl = pd.read_excel(r"C:\\Users\\l.ritchie\\PycharmProjects\\Scantech_Monthly_PSA_Report\\PSAReport.xls", sheet_name="Peak Control")
    PeakControldf = pd.DataFrame(PeakControl)
    return PeakControldf

def Read_PeakExtract():     #extracting the peak control data for determining detector stability
    PeakExtract = pd.read_csv(r"C:\Users\l.ritchie\PycharmProjects\Scantech_Monthly_PSA_Report\PeakExtract.csv", index_col=0) #read the csv containing the data
    PeakExtractdf = pd.DataFrame(PeakExtract.iloc[:, [3,10,17,24]]) #extract the 4 columns of dector data. This is only applicable to 4 detector analysers. This will need to be updated to do a selection to allow for any number of detecotrs
    PeakExtractdf.columns = ["Det1", "Det2", "Det3", "Det4"]    # renaming the columns of the new dataframe created for detector stability values only.
    DetStab = PeakExtractdf.plot().get_figure()             #plot the data
    plt.title("Detector Stability")                         # add a title
    plt.xticks(rotation=90)                                 # rotate the X axis titles
    plt.show()                                                 # show the plot
    DetStab.savefig("Resources\Detector_Stability.png")     # save the plot to file
    return PeakExtractdf

def Read_TempExtract():                                                 #extracting the peak control data for determining detector stability
    TempExtract = pd.read_csv(r"C:\Users\l.ritchie\PycharmProjects\Scantech_Monthly_PSA_Report\TempExtract.csv",
                              index_col=0)                              # read the csv containing the data
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
    TempStab.savefig("Resources\Temperatures.png")                      # save the plot to file
    return TempExtractdf

def Read_A_08_Analyse():                                                 #extracting the peak control data for determining detector stability
    # this code is pretty rough and can be optimised dramatically but this does work.
    AllExtract = pd.read_csv(r"C:\Users\l.ritchie\PycharmProjects\Scantech_Monthly_PSA_Report\A_08__Analyse.csv",
                              index_col=1)                              # read the csv containing the data
    TonsAnalysed = AllExtract.groupby('Date')[['S034','S029']].sum()

    # Plot Daily tonns as a stacked histograme of Tons Analsyed and TOns not analysed
    plt.figure(figsize=(10,6))
    plt.tick_params(axis='x', which='both',labelsize=5,labelrotation=45,grid_color='grey', grid_alpha=0.8)
    plt.title("Total Daily Tonnes", pad=30)
    plt.grid(which='both', axis='y')
    plt.bar(TonsAnalysed.index, TonsAnalysed["S029"], 0.4, color = 'red', label='Tons not Analysed',zorder=1)
    plt.bar(TonsAnalysed.index,TonsAnalysed["S034"],0.4,bottom=TonsAnalysed["S029"],color = 'green', label='Tons Analysed',zorder=2)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0)                  # places the legend above the plot
    plt.savefig("Resources\Daily_Tonnes.png")
    plt.close()
    # Parameters for controlling Results plots
    lsize = 8
    lrot = 90
    gcol = 'grey'
    galpha = 0.1
    tpad = 5
    figw = 10
    figh = 15
    # Plot First 3 results for report as a single figure with 3 subplots
    Results = AllExtract.groupby('Date')[['R040','R030','R031','R032','R033', 'R034', 'R035']].mean()
    fig = plt.figure(figsize=(figw,figh))

    # Plot First Result
    ax1 = fig.add_subplot(311)
    ax1.plot(Results.index,Results["R030"])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title("R030", pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Second Result
    ax2 = fig.add_subplot(312)
    ax2.plot(Results.index, Results["R031"])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title("R031", pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Third Result
    ax3 = fig.add_subplot(313)
    ax3.plot(Results.index, Results["R032"])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title("R032", pad=tpad)
    plt.grid(which='both', axis='y')

    plt.subplots_adjust(bottom=0.07,top=0.97, hspace=0.5)

    plt.savefig("Resources\Results1.png")
    plt.close()

    fig = plt.figure(figsize=(figw,figh))

    # Plot First Result
    ax1 = fig.add_subplot(311)
    ax1.plot(Results.index,Results["R033"])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title("R033", pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Second Result
    ax2 = fig.add_subplot(312)
    ax2.plot(Results.index, Results["R034"])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title("R034", pad=tpad)
    plt.grid(which='both', axis='y')

    # Plot Third Result
    ax3 = fig.add_subplot(313)
    ax3.plot(Results.index, Results["R035"])
    plt.tick_params(axis='x', which='both', labelsize=lsize, labelrotation=lrot, grid_color=gcol, grid_alpha=galpha)
    plt.title("R035", pad=tpad)
    plt.grid(which='both', axis='y')

    plt.subplots_adjust(bottom=0.07,top=0.97, hspace=0.5)

    plt.savefig("Resources\Results2.png")
    plt.close()


#Read_A_08_Analyse()