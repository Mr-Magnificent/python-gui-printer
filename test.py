import win32print, win32api


name = win32print.GetDefaultPrinterW()
print(name)
printDefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
level = 2
handle = win32print.OpenPrinter(name)
attributes = win32print.GetPrinter(handle, level)
attributes['pDevMode'].Duplex = 1
# win32print.SetPrinter(handle, level, attributes, 0)
win32print.GetPrinter(handle, level)['pDevMode'].Duplex
win32api.ShellExecute(0, 'print', 'test.pdf', '.', '/manualstoprint', 0)
print(name)
