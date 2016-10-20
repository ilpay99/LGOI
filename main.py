from PyQt5 import QtWidgets
from login import *
from PyQt5.QtWidgets import QApplication , QMainWindow
class Glob(object):
    "This is a place to save some message"
class mywindow(QMainWindow,Ui_MainWindow):
    _UserNameHaveChanged=0
    _PassWordHaveChanged=0
    def showtext(self):
        Glob.Username=self.lineEdit.text()
        Glob.Password=self.lineEdit_2.text()
        print(Glob.Username,Glob.Password)
    def cleanTheUserNameText(self, event):
        if not (self._UserNameHaveChanged) and (event.button()==QtCore.Qt.LeftButton):
            self.lineEdit.setText("")
            self.lineEdit.setStyleSheet("color:black")
            self._UserNameHaveChanged=1

    def cleanThePassWordText(self, event):
        if not (self._PassWordHaveChanged) and (event.button()==QtCore.Qt.LeftButton):
            self.lineEdit_2.setText("")
            self.lineEdit_2.setStyleSheet("color:black")
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self._PassWordHaveChanged=1
        if (event.button()==QtCore.Qt.RightButton):
            pass
    def __init__(self):
        self._UserNameHaveChanged=0
        self._PassWordHaveChanged=0
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showtext)
#       self.lineEdit.mousePressEvent=self.cleanTheUserNameText
#       self.lineEdit_2.mousePressEvent=self.cleanThePassWordText

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
