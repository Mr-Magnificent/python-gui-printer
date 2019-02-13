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
