# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PythonApplication_UseQtDesigner01_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(270, 60, 104, 71))
        self.price_box.setObjectName("price_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(270, 180, 42, 22))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Calc_Tax_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Calc_Tax_Button.setGeometry(QtCore.QRect(270, 280, 91, 21))
        self.Calc_Tax_Button.setObjectName("Calc_Tax_Button")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(260, 350, 181, 51))
        self.results_window.setObjectName("results_window")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 331, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.label.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "Tax Rate"))
        self.Calc_Tax_Button.setText(_translate("MainWindow", "Calculate Tax"))
        self.label_3.setText(_translate("MainWindow", "Sale Price Calculate"))

