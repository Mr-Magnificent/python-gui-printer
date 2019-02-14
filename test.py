import win32print
import subprocess
import os
import winreg

# Show all the printers
printer = win32print.EnumPrinters(2)

# get defprinter from the list
defprinter = win32print.GetDefaultPrinterW()

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\GPL Ghostscript\\9.26")
value, _ = winreg.QueryValueEx(key, "GS_DLL")

gspath = os.path.dirname(value)

args = '"{0}\gswin64c" ' \
           '-sDEVICE=mswinpr2 ' \
           '-dBATCH ' \
           '-dNOPAUSE ' \
           '-dFitPage ' \
           '-sOutputFile="%printer%{1}" '.format(gspath ,defprinter)

ghostscript = args + os.path.join(os.getcwd(), '1549471928476.ps')
ghostscript = ghostscript.replace('\\', '\\\\')

p = subprocess.Popen(ghostscript, shell=True,
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
print(stdout, stderr, sep="\n")