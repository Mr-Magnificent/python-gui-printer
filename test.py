import os
import subprocess
import winreg

import win32print
import printergui

# Show all the printers
def getAllPrinters():
    printers = win32print.EnumPrinters(2)
    output = tuple(zip(*printers))[2]
    return output

def generatePrint(filename):
    # get printerName from the list
    printerName = printergui.Ui_MainWindow.getPrinterName()
    if (printerName == None):
        return
    print(printerName)
    baseGS = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\GPL Ghostscript")
    version = winreg.EnumKey(baseGS, 0)
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\GPL Ghostscript\\{0}".format(version))
    gsFolder, _ = winreg.QueryValueEx(key, "GS_DLL")

    gspath = os.path.dirname(gsFolder)

    args = '"{0}\gswin64c" ' \
            '-sDEVICE=mswinpr2 ' \
            '-dBATCH ' \
            '-dNOPAUSE ' \
            '-dFitPage ' \
            '-sOutputFile="%printer%{1}" '.format(gspath ,printerName)

    ghostscript = args + os.path.join(os.getcwd(), '{0}.ps'.format(filename))
    ghostscript = ghostscript.replace('\\', '\\\\')

    p = subprocess.Popen(ghostscript, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout, stderr, sep="\n")
