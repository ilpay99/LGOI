from PyQt5 import QtWidgets
import PyQt5
import icon
from login import *
from PyQt5.QtWidgets import QApplication , QMainWindow
import Globvar
class mywindow(QMainWindow,Ui_MainWindow):
    def Login():
        pass
    def GetUserName(self):
        Username=self.lineEdit.text()
        Password=self.lineEdit_2.text()
        _Glob.receiveUsername(Username,Password)
        self.Login()
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Picture/LG.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.pushButton.clicked.connect(self.GetUserName)
        self.lineEdit.setAttribute(QtCore.Qt.WA_InputMethodEnabled, False)
        self.lineEdit_2.setAttribute(QtCore.Qt.WA_InputMethodEnabled, False)
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    _Glob=Globvar.Glob()
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
