from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime,QThread,QEventLoop

import PyQt5
import icon
import ctypes
import time
from login import *
from PyQt5.QtWidgets import QApplication , QMainWindow
import Globvar
class loadingGif(QtWidgets.QWidget):
    def quit(self):
        self.hide()
    def __init__(self,parent=None):
        super(loadingGif, self).__init__(parent)
        self.label = QtWidgets.QLabel('', self)
        self.setFixedSize(180,220)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.movie = QtGui.QMovie(":/Picture/World.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

class AccessTheServer(QThread):
    def __init__(self):
        super(AccessTheServer,self).__init__()  
    def run(self):
        loading=loadingGif()
        loading.show()  
        t=QtCore.QTime()
        t.start()
        _Glob.sendAccessResult(-1)
        while (t.elapsed()<60000):
            QtCore.QCoreApplication.processEvents()
            _Glob.sendAccessResult(0)
            if (_Glob.getAccessResult()==1):
                break;
            if (not _Glob.getAccessResult() and t.elapsed()>3000 ):
                break;
class mywindow(QMainWindow,Ui_MainWindow):

    def DealWithAccessResult(self):
        AccessResult=_Glob.getAccessResult()
        if (AccessResult== -1):
            self.show()
        if (AccessResult== 0):
            self.show()
        if (AccessResult== 1):
            pass
            self.close()
    def TryAccess(self):
        loading=loadingGif()
        loading.show()  
        t=QtCore.QTime()
        t.start()
        _Glob.sendAccessResult(-1)
        while (t.elapsed()<60000):
            QtCore.QCoreApplication.processEvents()
            _Glob.sendAccessResult(0)
            if (_Glob.getAccessResult()==1):
                break;
            if (not _Glob.getAccessResult() and t.elapsed()>3000 ):
                break;        
    def Login(self):
        self.hide()  
        self.TryAccess()
        self.DealWithAccessResult()
    def GetUserName(self):
        Username=self.lineEdit.text()
        Password=self.lineEdit_2.text()
        _Glob.sendUserMessage(Username,Password)
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
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    _Glob=Globvar.Glob()
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
