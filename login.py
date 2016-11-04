# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\uipackage\Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Globvar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        screen=QtWidgets.QDesktopWidget().screenGeometry()
        Globvar._Glob.sendScreenSize(screen.width(),screen.height())
        Width=screen.width()/3.5
        Height=screen.height()/3.3
        MainWindow.setFixedSize(Width,Height)
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Picture/LG.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(Width/7.805, Height/1.293, Width/4.289, Height/7.507))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(Width/3.252, Height/2.909, Width/2.156, Height/7.507))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        validator=QtCore.QRegExp(r"[a-zA-Z0-9_]+")
        self.lineEdit.setValidator(QtGui.QRegExpValidator(validator,self.lineEdit))
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(Globvar._Glob.getdata("Username"))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(Width/3.252, Height/1.939, Width/2.156, Height/7.507))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setAttribute(QtCore.Qt.WA_InputMethodEnabled, False)
        self.lineEdit_2.setAttribute(QtCore.Qt.WA_InputMethodEnabled, False)
        self.lineEdit_2.setMaxLength(24)
        validator=QtCore.QRegExp(r"[a-zA-Z0-9_?,.;+-=~]+")
        self.lineEdit_2.setValidator(QtGui.QRegExpValidator(validator,self.lineEdit_2))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.lineEdit_2.setPlaceholderText("Password:")
        self.lineEdit.setPlaceholderText("Username:")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(Width/1.697, Height/1.293, Width/4.289, Height/7.507))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(Width/2.054, Height/1.455, Width/3.226, Height/11.636))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label.setOpenExternalLinks(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><a href='https://www.baidu.com/'><span style=\" text-decoration: underline; color:#0000ff;\">I forgot Password...</span></a></p></body></html>"))
