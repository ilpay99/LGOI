from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys
class lineEdit(QtWidgets.QLineEdit):
    def mousePressEvent(self, event):
        if (event.button()==QtCore.Qt.LeftButton):
            print("OK")
    def __init__(self):
        super(lineEdit,self).__init__()

app=QtWidgets.QApplication(sys.argv)
a=lineEdit()
a.show()
sys.exit(app.exec_())
