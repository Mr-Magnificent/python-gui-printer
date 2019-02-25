# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ayush\Desktop\printergui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# from socketpy import sio
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QAction, qApp, QMenu
from fileHandling import add
import os.path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tray_icon = QSystemTrayIcon(MainWindow)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 130, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton.clicked.connect(self.sendFieldDetails)
        self.label.setText(_translate("MainWindow", "Enter UUID"))
        self.label_2.setText(_translate("MainWindow", "Select Default Printer"))
        self.label_3.setText(_translate("MainWindow", "Enter Printer Alias"))

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        scriptDir = scriptDir + os.path.sep + 'icons' + os.path.sep + 'printer.ico'
        print(scriptDir)
        show_action = QAction("Show", MainWindow)
        quit_action = QAction("Exit", MainWindow)
        hide_action = QAction("Hide", MainWindow)
        show_action.triggered.connect(MainWindow.show)
        hide_action.triggered.connect(MainWindow.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        print("hello")
        self.hide()
        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

    def insertPrinterList(self, printerNames):
        print(printerNames)
        self.comboBox.addItems(printerNames)

    def sendFieldDetails(self, data):
        # print(data, self.lineEdit.text(), self.lineEdit_2.text())
        # sio.emit('add user', {"uuid": self.lineEdit.text(), "alias": self.lineEdit_2.text()})
        print (data, self.comboBox.currentText(), self.lineEdit.text(), self.lineEdit_2.text())
        global PRINTER_NAME = self.comboBox.currentText()
        seq = [self.lineEdit.text() + '\n', self.lineEdit_2.text() + '\n']
        with open('credentials.txt', 'w') as file:
            file.writelines(seq)
        dirpath = os.path.dirname(os.path.abspath(__file__))
        add("Piston Print", dirpath + "socketpy.py")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setFixedSize(MainWindow.size())
    sys.exit(app.exec_())

