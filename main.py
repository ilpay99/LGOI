from PyQt5 import QtWidgets
from login import *
from PyQt5.QtWidgets import QApplication , QMainWindow
class Glob(object):
    "This is a place to save some message"
class mywindow(QMainWindow,Ui_MainWindow):
    def showtext(self):
        Glob.Username=self.lineEdit.text()
        Glob.Password=self.lineEdit_2.text()
        print(Glob.Username,Glob.Password)
    def __init__(self):
        self._UserNameHaveChanged=0
        self._PassWordHaveChanged=0
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showtext)
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
