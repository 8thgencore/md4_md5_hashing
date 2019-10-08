# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 61))
        self.groupBox.setObjectName("groupBox")
        self.pbOpenFile = QtWidgets.QPushButton(self.groupBox)
        self.pbOpenFile.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.pbOpenFile.setObjectName("pbOpenFile")
        self.pbHashFile = QtWidgets.QPushButton(self.groupBox)
        self.pbHashFile.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.pbHashFile.setObjectName("pbHashFile")
        self.label_CheckFile = QtWidgets.QLabel(self.groupBox)
        self.label_CheckFile.setGeometry(QtCore.QRect(130, 20, 121, 31))
        self.label_CheckFile.setObjectName("label_CheckFile")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 431, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pbHashString = QtWidgets.QPushButton(self.groupBox_2)
        self.pbHashString.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.pbHashString.setObjectName("pbHashString")
        self.leString = QtWidgets.QLineEdit(self.groupBox_2)
        self.leString.setGeometry(QtCore.QRect(10, 19, 321, 31))
        self.leString.setObjectName("leString")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 431, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.leMD4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.leMD4.setGeometry(QtCore.QRect(70, 20, 351, 31))
        self.leMD4.setObjectName("leMD4")
        self.leMD5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.leMD5.setGeometry(QtCore.QRect(70, 60, 351, 31))
        self.leMD5.setObjectName("leMD5")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 54, 31))
        self.label_2.setObjectName("label_2")
        self.label_for_image = QtWidgets.QLabel(self.centralwidget)
        self.label_for_image.setGeometry(QtCore.QRect(450, 20, 171, 201))
        self.label_for_image.setText("")
        self.label_for_image.setObjectName("label_for_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 23))
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
        self.groupBox.setTitle(_translate("MainWindow", "Хэш-сумма файла"))
        self.pbOpenFile.setText(_translate("MainWindow", "Выбрать файл"))
        self.pbHashFile.setText(_translate("MainWindow", "Расчитать"))
        self.label_CheckFile.setText(_translate("MainWindow", "файл не выбран"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Хэш-сумма строки"))
        self.pbHashString.setText(_translate("MainWindow", "Расчитать"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Результат"))
        self.label.setText(_translate("MainWindow", "MD4"))
        self.label_2.setText(_translate("MainWindow", "MD5"))

