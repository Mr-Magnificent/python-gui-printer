
import os.path
from printergui import *

def createGui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())




if not os.path.isfile('credentials.txt'):
    createGui()
