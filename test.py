import win32print
import array

printer = win32print.EnumPrinters(2)
printerPiston = win32print.OpenPrinter('Canon E500 series Printer')
print(win32print.GetPrinter(printerPiston))
print(printerPiston)
with open('SE front.prn', 'r') as file:
    line = file.read()

# print(type(line))
# line = bytearray(line.encode())
print(len(line))
id = win32print.StartDocPrinter(printerPiston, 1, ("1549471928476", None, "RAW"))
length = win32print.WritePrinter(printerPiston, line)
win32print.EndDocPrinter(printerPiston)
print(id, length)
# print(printer)
# ./gswin64c.exe  -dPrinted -dBATCH -dNOPAUSE -dNOSAFER -q -dNumCopies=1 -sDEVICE=mswinpr2  "G:\python-gui-printer/1549471928476.ps"
import win32print, win32api


# name = win32print.GetDefaultPrinterW()
# print(name)
# printDefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
# level = 2
# handle = win32print.OpenPrinter(name)
# attributes = win32print.GetPrinter(handle, level)
# attributes['pDevMode'].Duplex = 1
# # win32print.SetPrinter(handle, level, attributes, 0)
# win32print.GetPrinter(handle, level)['pDevMode'].Duplex
# win32api.ShellExecute(0, 'print', 'test.pdf', '.', '/manualstoprint', 0)
# print(name)
