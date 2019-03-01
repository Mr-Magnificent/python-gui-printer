
import os.path
import test
from printergui import *

def createGui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    printers = test.getAllPrinters()
    ui.insertPrinterList(printers)
    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())


# from ui.printergui import UI_Piston

# class Gui(UI_Piston):
    


if not os.path.isfile('credentials.txt'):
    createGui()
