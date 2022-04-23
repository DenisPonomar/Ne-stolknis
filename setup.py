#!/usr/bin/python
import sys
from PyQt4 import QtGui

class Absolute(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('Communication')

        label = QtGui.QLabel('Couldn\'t', self)
        label.move(185, 10)

        self.resize(250, 150)

app = QtGui.QApplication(sys.argv)
qb = Absolute()
qb.show()
sys.exit(app.exec_())
