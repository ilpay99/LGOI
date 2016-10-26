import Globvar
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QMessageBox
from GIF import loadingGif
class Access():
    def DealWithAccessResult(self,parent):
        AccessResult=Globvar._Glob.getAccessResult()
        if (AccessResult== -1):
            parent.show()
            self.PopMessageForConnectFailed(parent,"连接超时","Connect Timeout")
        if (AccessResult== 0):
            parent.show()
            self.PopMessageForConnectFailed(parent,"找不到服务器","Connect Failed")           
        if (AccessResult== 1):
            pass
            parent.close()

    def sendMessageToServer(self):
        pass

    def PopMessageForConnectFailed(self,parent,Text="",Title=""):
        reply=QMessageBox.information(parent,Title,Text)

    def TryAccess(self,parent):
        loading=loadingGif()
        loading.show()  
        t=QtCore.QTime()
        t.start()
        Globvar._Glob.sendAccessResult(-1)
        while (t.elapsed()<60000):
            QtCore.QCoreApplication.processEvents()
            self.sendMessageToServer()
            Globvar._Glob.sendAccessResult(0)
            if (Globvar._Glob.getAccessResult()==1):
                break;
            if (not Globvar._Glob.getAccessResult() and t.elapsed()>3000 ):
                break;      
