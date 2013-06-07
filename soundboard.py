#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
"""

import sys
from PyQt4 import QtGui

class SBButton(QtGui.QPushButton):
    def __init__(self, name, parent):
        super(SBButton, self).__init__(name, parent)
        print "Width: " + str(parent.width()) + " height: " + str(parent.height())
        
    def resizeEvent(self, resize_event):
        print "SBButton: I got resized"

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Tooltips')    
        
        self.btn = SBButton('Button', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        
    def resizeEvent(self, resize_event):
        super(Example, self).resizeEvent(resize_event)
        print "I got resized"
        self.btn.resize(self.width()/5, self.height()/5)
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()