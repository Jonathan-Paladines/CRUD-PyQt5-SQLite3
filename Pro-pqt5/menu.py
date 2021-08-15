# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 506)
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(255, 185, 64);\n"
"background-color: rgb(4, 56, 25);\n"
"font: 8pt \"Castellar\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnTablaPersonas = QtWidgets.QPushButton(self.centralwidget)
        self.BtnTablaPersonas.setGeometry(QtCore.QRect(60, 290, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.BtnTablaPersonas.setFont(font)
        self.BtnTablaPersonas.setStyleSheet("color: rgb(255, 255, 30);\n"
"font: 11pt \"Lucida Calligraphy\";")
        self.BtnTablaPersonas.setObjectName("BtnTablaPersonas")
        self.BtnTablaProductos = QtWidgets.QPushButton(self.centralwidget)
        self.BtnTablaProductos.setGeometry(QtCore.QRect(300, 290, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.BtnTablaProductos.setFont(font)
        self.BtnTablaProductos.setStyleSheet("color: rgb(255, 255, 30);\n"
"font: 11pt \"Lucida Calligraphy\";")
        self.BtnTablaProductos.setObjectName("BtnTablaProductos")
        self.BtnGenerarArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.BtnGenerarArchivo.setGeometry(QtCore.QRect(140, 380, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.BtnGenerarArchivo.setFont(font)
        self.BtnGenerarArchivo.setStyleSheet("color: rgb(255, 255, 30);\n"
"font: 11pt \"Lucida Calligraphy\";")
        self.BtnGenerarArchivo.setObjectName("BtnGenerarArchivo")
        self.BtnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSalir.setGeometry(QtCore.QRect(454, 422, 71, 31))
        self.BtnSalir.setStyleSheet("color: rgb(131, 255, 247);")
        self.BtnSalir.setObjectName("BtnSalir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow_Menu"))
        self.BtnTablaPersonas.setText(_translate("MainWindow", "Tabla Personas"))
        self.BtnTablaProductos.setText(_translate("MainWindow", "Tabla Productos"))
        self.BtnGenerarArchivo.setText(_translate("MainWindow", "Generar Archivo Reporte"))
        self.BtnSalir.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Menu para ingreso </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">de información</span></p></body></html>"))
