import PyQt5
from PyQt5 import QtWidgets,QtCore,QtGui
class loadingGif(QtWidgets.QWidget):
    """The Class to play loading gif , work at Logging"""
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
