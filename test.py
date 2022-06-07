from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Dimensions
#Start position of window when opening up
xstart = ystart = 50
# Dimensions of the window
width = 1200; height = 800
xcenter = width/2
ycenter = width/2


def window():
   app = QApplication(sys.argv)
   win = QMainWindow()
   win.setGeometry(xstart, ystart, width, height)
   win.setWindowTitle('Substrate Database - NXPS')

   label = QtWidgets.QLabel(win)
   label.setText("My first label")
   label.move(xcenter-50, 50)

   win.show()
   sys.exit(app.exec_())

window()