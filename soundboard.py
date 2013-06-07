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
        
    def position(self, posx, posy):
        self.posx = posx
        self.posy = posy

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Tooltips')    
        
        self.btns = []
        for y in range(5):
            for x in range(5):
                btn = SBButton('Button', self)
                btn.position(x, y)
                btn.setToolTip('This is a <b>QPushButton</b> widget')
                self.btns.append(btn)
        
    def resizeEvent(self, resize_event):
        super(Example, self).resizeEvent(resize_event)
        print "I got resized"
        w = self.width()/5
        h = self.height()/5
        for b in self.btns:
            b.move(w*b.posx, h*b.posy)
            b.resize(w, h)
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()